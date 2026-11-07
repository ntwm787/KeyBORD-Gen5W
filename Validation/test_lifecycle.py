from pathlib import Path
import subprocess,tempfile,json,importlib.util,hashlib,os
root=Path(__file__).resolve().parents[1]
work=root/'Validation'
bash='C:/Program Files/Git/usr/bin/bash.exe'
def unix(p):return '/'+p.drive[0].lower()+p.as_posix()[2:]
H='org.pocketworkstation.pckeyboard/.LatinIME'
O='com.android.inputmethod.diopen/.DioInputMethodService'
X='example.other/.IME'
mock=r"""
id() { echo 'uid=0(root) gid=0(root)'; }
getprop() { case "$1" in sys.boot_completed) echo 1 ;; ro.build.version.sdk) echo 19 ;; ro.build.product) echo "$MOCK_PRODUCT" ;; esac; }
settings() {
 _mock_file="$MOCK_ROOT/$3"
 case "$1" in
 get) if [ -f "$_mock_file" ]; then cat "$_mock_file"; else echo null; fi ;;
 put) echo "$4" > "$_mock_file" ;;
 delete) [ ! -f "$_mock_file" ] || rm "$_mock_file" ;;
 esac
}
ime() {
 case "$1" in
 list) cat "$MOCK_ROOT/available" ;;
 enable)
  _mock_value=$(settings get secure enabled_input_methods)
  case ":$_mock_value:" in *":$2:"*) ;; *) echo "$_mock_value:$2" > "$MOCK_ROOT/enabled_input_methods" ;; esac
  ;;
 set)
  if [ "$2" = "$MOCK_FAIL_SET" ]; then return 1; fi
  echo "$2" > "$MOCK_ROOT/default_input_method"
  echo -1 > "$MOCK_ROOT/selected_input_method_subtype"
  ;;
 esac
}
"""
def setup(default=O):
 p=Path(tempfile.mkdtemp(prefix='lifecycle-',dir=work))
 vals={'default_input_method':default,'enabled_input_methods':O,'selected_input_method_subtype':'7','available':O+'\n'+H+'\n'+X}
 for k,v in vals.items():(p/k).write_text(v+'\n',newline='\n')
 return p,{k:v for k,v in vals.items() if k!='available'}
def run(p,pid,hook,failset='',product='NEEV23.USA.S5W_M.V015.012.260507',legacy=False):
 # Use exact production hook and common code with filesystem targets redirected.
 def source(name):
  if legacy:
   return subprocess.check_output(['git','show','v2.0.1:Source/'+pid+'/scripts/'+name],cwd=root,text=True)
  return (root/'Source'/pid/'scripts'/name).read_text()
 common=source('common.sh').replace('export PATH=/sbin:/vendor/bin:/system/sbin:/system/bin:/system/xbin','export PATH=/usr/bin:/bin')
 body=source(hook).replace('. ./scripts/common.sh',common+'\n'+mock)
 body=body.replace('export PATH=/sbin:/vendor/bin:/system/sbin:/system/bin:/system/xbin','export PATH=/usr/bin:/bin')
 body=body.replace('/data/nemesis/backup/',unix(p)+'/backup/')
 f=p/'runner.sh';f.write_text('MOCK_PRODUCT="'+product+'"\nMOCK_ROOT="'+unix(p)+'"\nMOCK_FAIL_SET="'+failset+'"\n'+body,newline='\n')
 r=subprocess.run([bash,unix(f)],capture_output=True,text=True,cwd=p)
 return r

def state(p):return {k:(p/k).read_text().strip() if (p/k).exists() else 'null' for k in ['default_input_method','enabled_input_methods','selected_input_method_subtype']}
def ok(r):assert r.returncode==0,(r.stdout,r.stderr)
checks=[]
# Exact install/apply -> uninstall selection round trip, for both packages.
for pid,start in [('keyboard.activate',O),('keyboard.restore',H)]:
 p,before=setup(start);ok(run(p,pid,'pre.sh'));ok(run(p,pid,'post.sh'))
 expected=H if pid.endswith('activate') else O
 assert state(p)['default_input_method']==expected
 ok(run(p,pid,'select.sh'));ok(run(p,pid,'preun.sh'));assert state(p)==before
 ok(run(p,pid,'cleanup.sh'));assert not (p/'backup'/pid).exists()
checks.append('activation and restore round trips, repeat launch, verified cleanup')
# Both packages installed; uninstall in reverse order.
p,before=setup();ok(run(p,'keyboard.activate','post.sh'));ok(run(p,'keyboard.restore','post.sh'))
ok(run(p,'keyboard.restore','preun.sh'));ok(run(p,'keyboard.restore','cleanup.sh'))
assert state(p)['default_input_method']==H
ok(run(p,'keyboard.activate','preun.sh'));assert state(p)==before
checks.append('stacked KeyBridge / factory restore, reverse-order uninstall')
# Keep later user selection.
p,before=setup();ok(run(p,'keyboard.activate','post.sh'));(p/'default_input_method').write_text(X+'\n',newline='\n')
ok(run(p,'keyboard.activate','preun.sh'));assert state(p)['default_input_method']==X
checks.append('later user keyboard selection preserved')
# Missing original IME prevents destructive removal and retains backup.
p,before=setup(H);ok(run(p,'keyboard.restore','post.sh'));(p/'available').write_text(O+'\n',newline='\n')
r=run(p,'keyboard.restore','preun.sh');assert r.returncode!=0;assert (p/'backup/keyboard.restore/before.ready').exists()
checks.append('missing original IME refuses uninstall and retains snapshot')
# Failed selection rolls back previous enabled list / subtype / default.
p,before=setup();r=run(p,'keyboard.activate','post.sh',H);assert r.returncode!=0;assert state(p)==before
checks.append('selection failure rolls back original settings')
# Legacy helper packages without snapshots can be removed without guessing.
p,before=setup();ok(run(p,'keyboard.activate','preun.sh'));assert state(p)==before
checks.append('legacy no-snapshot removal leaves settings unchanged')
# Before removing the APK, a currently selected Hacker IME is replaced by OEM.
p,before=setup(H);ok(run(p,'keyboard.hackers','preun.sh'));assert state(p)['default_input_method']==O
checks.append('APK removal pre-hook selects factory keyboard first')
# Cross-model software-family gates; no hard-coded year, region or firmware revision.
for product in ['NEEV23.USA.S5W_M.V015.012.260507', 'TEST.EUR.S5W_M.V001.001.230101', 'OTHER.KOR.S5W_M.V999.999.991231']:
 p,before=setup();ok(run(p,'keyboard.activate','post.sh',product=product))
for product in ['TEST.USA.S5W_L.V001', 'TEST.USA.ccNC.V001', '']:
 p,before=setup();r=run(p,'keyboard.activate','post.sh',product=product)
 assert r.returncode!=0;assert state(p)==before;assert not (p/'backup').exists()
checks.append('Gen5W family accepts different model/region/revision identifiers; S5W_L, ccNC and missing identity rejected before changes')
# Exact old 2.01 hooks -> manager APK removal -> new keyboard verification ->
# exact old KeyBridge uninstall/cleanup -> new KeyBridge install and uninstall.
p,before=setup();ok(run(p,'keyboard.activate','post.sh',legacy=True))
ok(run(p,'keyboard.hackers','preun.sh',legacy=True))
assert state(p)['default_input_method']==O
# APK replacement is simulated by the available IME list; real pm remains on-unit.
ok(run(p,'keyboard.hackers','post.sh'))
ok(run(p,'keyboard.activate','preun.sh',legacy=True));ok(run(p,'keyboard.activate','cleanup.sh',legacy=True))
ok(run(p,'keyboard.activate','pre.sh'));ok(run(p,'keyboard.activate','post.sh'))
assert state(p)['default_input_method']==H
ok(run(p,'keyboard.activate','preun.sh'));assert state(p)['default_input_method']==O
checks.append('2.01 keyboard then KeyBridge update lifecycle using exact previous release hooks; activation and factory fallback retained')
# Direct helper update restores and recaptures the same baseline.
p,before=setup();ok(run(p,'keyboard.activate','post.sh',legacy=True))
ok(run(p,'keyboard.activate','preun.sh',legacy=True));ok(run(p,'keyboard.activate','cleanup.sh',legacy=True))
ok(run(p,'keyboard.activate','post.sh'));ok(run(p,'keyboard.activate','preun.sh'));assert state(p)==before
checks.append('2.01 KeyBridge direct update preserves original baseline through uninstall/reinstall')

for f in (root/'Source').glob('*/scripts/*.sh'):
 r=subprocess.run([bash,'-n',unix(f)],capture_output=True,text=True);assert r.returncode==0,(f,r.stderr)
checks.append('all production hooks pass shell syntax checks; copied cleanup runs without package cwd or siblings')
result={'result':'PASS','checks':checks,'limit':'Local simulation of IME selection, settings restoration and hook behavior.'}
(root/'Validation/lifecycle-tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
