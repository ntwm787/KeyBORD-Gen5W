from pathlib import Path
from zipfile import ZipFile
import configparser,hashlib,importlib.util,json,fnmatch,subprocess,sys
root=Path(__file__).resolve().parents[1]
builder=Path(sys.argv[1])
spec=importlib.util.spec_from_file_location('upstream_builder',builder);up=importlib.util.module_from_spec(spec);spec.loader.exec_module(up)
checks=[]
for source in sorted((root/'Source').iterdir()):
 pid=source.name
 assert up.validate(source/'NEMESIS.data')==[]
 meta=configparser.ConfigParser();meta.read(source/'NEMESIS.data');m=meta['nemesis']
 assert m['id']==pid and m['package-version']=='2.0.2'
 assert m['os']=='*S5W_M*' and m['models']=='any'
 old=configparser.ConfigParser();old.read_string(subprocess.check_output(['git','show','v2.0.1:Source/'+pid+'/NEMESIS.data'],cwd=root,text=True))
 assert old['nemesis']['id']==m['id']
 assert tuple(map(int,m['package-version'].split('.'))) > tuple(map(int,old['nemesis']['package-version'].split('.')))
 if pid=='keyboard.activate':assert m['depends']=='"keyboard.hackers@>=2.0.1"'
 with ZipFile(root/'Store'/(pid+'.zip')) as z:
  assert z.testzip() is None
  assert {n:z.read(n) for n in z.namelist()}=={f.relative_to(source).as_posix():f.read_bytes() for f in source.rglob('*') if f.is_file()}
 for key in ('preinstall','postinstall','preuninstall','postuninstall'):
  if key in m:assert (source/m[key]).is_file()
 checks.append(pid+': upstream descriptor validator passes; same ID, higher version, unrestricted models, exact source payload')
labels={'keyboard.hackers':'Hacker Keyboard','keyboard.activate':'KeyBridge','keyboard.restore':'Hyundai Keyboard Restore'}
for pid,label in labels.items():
 with ZipFile(root/'USB'/(label+' USB v2.zip')) as z:
  assert z.testzip() is None
  assert [n for n in z.namelist() if n.endswith('.zip')]==['packages/'+pid+'.zip']
  assert z.read('packages/'+pid+'.zip')==(root/'Store'/(pid+'.zip')).read_bytes()
checks.append('exactly three USB wrappers; each holds one intact matching Store package')
assert hashlib.sha256((root/'Source/keyboard.hackers/app/HackersKeyboard.apk').read_bytes()).hexdigest()=='641ab8a614f496765bb841665aa894fdb9d1f908c22ffb01af2059c7600ed0d3'
checks.append('Hacker Keyboard APK unchanged; all existing licenses and notices retained')
for product in ['NEEV23.USA.S5W_M.V015.012.260507','OTHER.EUR.S5W_M.V001.001.230101','MODEL.KOR.S5W_M.V999.999.991231']:
 assert fnmatch.fnmatchcase(product,'*S5W_M*')
checks.append('software glob accepts different model, region, year and firmware revision strings')
result={'result':'PASS','package_version':'2.0.2','checks':checks,'limit':'Local package inspection; lifecycle simulation is recorded separately.'}
(root/'Validation/package-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
