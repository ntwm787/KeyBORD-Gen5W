"""Build Store, USB and source downloads from editable package trees."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import hashlib

root = Path(__file__).resolve().parent
VERSION = '2.0.2'
SOURCE_NAME = 'KeyBORD 2.02 Source.zip'
labels = {'keyboard.hackers': 'Hacker Keyboard', 'keyboard.activate': 'KeyBridge',
          'keyboard.restore': 'Hyundai Keyboard Restore'}

def archive(path, items):
    path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(path, 'w', ZIP_DEFLATED) as z:
        for name, data in sorted(items.items()):
            info = ZipInfo(name, (2026, 11, 6, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = (0o100755 if name.endswith('.sh') else 0o100644) << 16
            z.writestr(info, data)

apk = root/'Source/keyboard.hackers/app/HackersKeyboard.apk'
expected = '641ab8a614f496765bb841665aa894fdb9d1f908c22ffb01af2059c7600ed0d3'
if not apk.exists() or hashlib.sha256(apk.read_bytes()).hexdigest() != expected:
    raise SystemExit("Supply the unchanged Hacker's Keyboard 1.41.1 APK in Source/keyboard.hackers/app/. See README for upstream source.")

for pid, label in labels.items():
    source = root/'Source'/pid
    store = root/'Store'/(pid+'.zip')
    archive(store, {f.relative_to(source).as_posix(): f.read_bytes()
                    for f in source.rglob('*') if f.is_file()})
    readme = (f'{label} USB v2 / package {VERSION}\n'
              'Android Gen5W across vehicle makes/models; no firmware-revision/year/region lock.\n'
              'Extract this outer ZIP to USB root. Keep the inner ZIP intact in packages/.\n'
              'Install with NEMESIS 1.16+ while parked, after Android has fully started.\n'
              'Existing 2.01 installation: confirm Update; keyboard first, KeyBridge second.\n'
              'Restore install/update selects the factory keyboard.\n'
              'The inner Store ZIP is the portal upload. See the repository README.\n'
              'NEMESIS is required separately and is not bundled.\n')
    archive(root/'USB'/(label+' USB v2.zip'), {
        'NEMESIS.data': f'[nemesis]\nversion=1.1\ntype=install\npath=packages/{pid}.zip\n'.encode(),
        'packages/'+pid+'.zip': store.read_bytes(),
        'READ-ME-FIRST.txt': readme.encode(),
        'LICENSES-AND-CREDITS.txt': (source/'LICENSES-AND-CREDITS.txt').read_bytes()})

items = {f.relative_to(root).as_posix(): f.read_bytes()
         for f in (root/'Source').rglob('*') if f.is_file() and f.suffix != '.apk'}
for name in ['build.py', 'README.md', 'CHANGELOG.md', 'LICENSE', 'Testing and Submission.md']:
    items[name] = (root/name).read_bytes()
for f in (root/'Validation').glob('*'):
    if f.is_file() and f.suffix in ('.py', '.json'):
        items[f.relative_to(root).as_posix()] = f.read_bytes()
archive(root/SOURCE_NAME, items)
downloads = sorted((root/'Store').glob('*.zip')) + sorted((root/'USB').glob('*.zip')) + [root/SOURCE_NAME]
(root/'SHA256SUMS.txt').write_text(''.join(
    hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.relative_to(root).as_posix()+'\n'
    for f in downloads), newline='\n')
print('Built three Store packages, three USB wrappers, source archive and checksums.')
