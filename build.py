from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root=Path(__file__).resolve().parent
labels={'keyboard.hackers':'Hacker Keyboard','keyboard.activate':'KeyBridge','keyboard.restore':'Hyundai Keyboard Restore'}
for pid,label in labels.items():
    source=root/'Source'/pid
    store=root/'Store'/(pid+'.zip')
    with ZipFile(store,'w',ZIP_DEFLATED) as z:
        for f in sorted(source.rglob('*')):
            if f.is_file():z.write(f,f.relative_to(source).as_posix())
    wrapper=root/'USB'/(label+' USB v2.zip')
    with ZipFile(wrapper) as z:items={n:z.read(n) for n in z.namelist()}
    items['packages/'+pid+'.zip']=store.read_bytes()
    with ZipFile(wrapper,'w',ZIP_DEFLATED) as z:
        for n,b in items.items():z.writestr(n,b)
print('Rebuilt three store packages and their existing USB wrappers.')
