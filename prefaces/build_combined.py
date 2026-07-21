import sys, os, re, glob
sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.environ.get('DICT', 'mw')
# The source language of the MW front matter is English, so the base .md files
# ARE the English edition; we therefore emit an English consolidated file from
# the base .md and a Russian consolidated file from the .ru.md pages.
# (suffix, outfile, doc title, page-word, src-word)
LANGS = {
  'en':  ('.md',    f'{CODE}pref_all.en.md', 'Front matter — complete (English, source language)', 'Page',      'Source (scan)'),
  'ru':  ('.ru.md', f'{CODE}pref_all.ru.md', 'Предварительные материалы — полностью (русский)',    'Страница', 'Источник (скан)'),
}
def split(text):  # drop opening YAML block + first H1; return (meta, body)
    meta={}; L=text.splitlines(); i=0
    if L and L[0].strip()=='---':
        i=1
        while i<len(L) and L[i].strip()!='---':
            m=re.match(r'\s*([A-Za-z_]+):\s*(.*)$', L[i])
            if m: meta[m.group(1)]=m.group(2).strip().strip('"')
            i+=1
        i+=1
    while i<len(L) and not L[i].strip(): i+=1
    if i<len(L) and L[i].lstrip().startswith('# '): i+=1
    while i<len(L) and not L[i].strip(): i+=1
    return meta, '\n'.join(L[i:]).rstrip()
def slug(s):
    s=re.sub(r'[^\w\s-]','',s.lower(),flags=re.UNICODE); return re.sub(r'\s+','-',s.strip())
pages = sorted(glob.glob(os.path.join(HERE, f'{CODE}pref[0-9][0-9].md')))
for lang,(suf,outname,title,pw,srcw) in LANGS.items():
    out=[f'# {title}\n', f'Per-page files: `{CODE}prefNN{suf}`. Index: [README.md](README.md).\n', '## Contents\n']
    body=[]
    for de in pages:
        nn=re.search(r'(\d\d)\.md$', de).group(1)
        src=de[:-3]+suf if suf!='.md' else de
        if not os.path.exists(src): continue
        meta,txt=split(open(src,encoding='utf-8').read())
        h=f'{pw} {nn} — {meta.get("source_page","")} (vol. {meta.get("volume","?")})'
        out.append(f'- [{h}](#{slug(h)})')
        # demote in-body headings so the page heading stays the top level (H2)
        txt=re.sub(r'(?m)^(#{1,5})(\s)', r'#\1\2', txt)
        body.append(f'\n---\n\n## {h}\n\n<sub>{srcw}: [{meta.get("source_scan","")}]({meta.get("source_url","")})</sub>\n\n{txt}\n')
    open(os.path.join(HERE,outname),'w',encoding='utf-8').write('\n'.join(out+body).rstrip()+'\n')
    print('wrote', outname)
