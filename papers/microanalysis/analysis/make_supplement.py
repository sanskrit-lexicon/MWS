"""Decision 16 — assemble the reproducibility supplement ZIP.

Bundles the paper, working notes, audit scripts + reports, and figures (with
their derived JSON data) into a single self-contained archive that backs the
paper's reproducibility claim. The raw dictionary .txt files are NOT included
(they live in CDSL csl-orig); the committed scripts regenerate every derived
artefact from them.

The .zip is a build artefact (gitignored); SUPPLEMENT_MANIFEST.md (committed)
records its contents and how to rebuild it.

Run:  python make_supplement.py
"""
import glob
import os
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
MICRO = os.path.normpath(os.path.join(HERE, '..'))
ARCNAME_ROOT = 'mw-microanalysis-supplementary'
ZIP_PATH = os.path.join(HERE, f'{ARCNAME_ROOT}.zip')

# Curated include patterns, relative to the microanalysis dir.
INCLUDE = [
    'PAPER.md', 'README.md', 'MICROANALYSIS.md', 'DOUBTS.md', 'VISUALISATIONS.md',
    'paper-grounded.md', 'paper-wiegand.md', 'paper-atkins-rundell.md', 'paper-hausmann.md',
    'decisions/*.md',
    'analysis/*.py', 'analysis/*.md', 'analysis/SPOTCHECK_SAMPLE.txt',
    'figures/*.svg', 'figures/*.png', 'figures/*.alt.txt', 'figures/*.desc.txt',
    'figures/*.md', 'figures/*.json', 'figures/*.css', 'figures/*.py',
    'figures/data/*.json', 'figures/scripts/*.py', 'figures/locales/*.json',
]
# Never bundle the zip itself or caches.
EXCLUDE_SUFFIX = ('.zip', '.pyc')


def collect():
    seen = set()
    files = []
    for pat in INCLUDE:
        for p in sorted(glob.glob(os.path.join(MICRO, pat))):
            rel = os.path.relpath(p, MICRO).replace('\\', '/')
            if rel in seen or p.endswith(EXCLUDE_SUFFIX) or not os.path.isfile(p):
                continue
            seen.add(rel)
            files.append((p, rel))
    return files


def main():
    files = collect()
    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as z:
        for path, rel in files:
            z.write(path, f'{ARCNAME_ROOT}/{rel}')
    total = sum(os.path.getsize(p) for p, _ in files)
    zsize = os.path.getsize(ZIP_PATH)
    print(f'wrote {ZIP_PATH}')
    print(f'  {len(files)} files, {total/1024:.0f} kB uncompressed -> {zsize/1024:.0f} kB zip')

    # Manifest (committed)
    by_dir = {}
    for _p, rel in files:
        d = rel.split('/')[0] if '/' in rel else '(root)'
        by_dir.setdefault(d, []).append(rel)
    manifest = os.path.join(HERE, 'SUPPLEMENT_MANIFEST.md')
    with open(manifest, 'w', encoding='utf-8') as f:
        f.write('# Reproducibility supplement — manifest (Decision 16)\n\n')
        f.write('Built by [`make_supplement.py`](make_supplement.py) into '
                '`mw-microanalysis-supplementary.zip` (a gitignored build artefact). '
                'The raw dictionary `.txt` files are not bundled — they live in '
                '[csl-orig](https://github.com/sanskrit-lexicon/csl-orig); the included '
                'scripts regenerate every derived artefact from them.\n\n')
        f.write(f'**{len(files)} files**, {total/1024:.0f} kB uncompressed.\n\n')
        f.write('## To rebuild\n\n```\ncd papers/microanalysis/analysis\npython make_supplement.py\n```\n\n')
        f.write('## Contents\n\n')
        for d in sorted(by_dir):
            f.write(f'- **{d}/** — {len(by_dir[d])} files\n')
        f.write('\n<details><summary>Full file list</summary>\n\n')
        for _p, rel in files:
            f.write(f'- `{rel}`\n')
        f.write('\n</details>\n')
    print(f'  wrote {manifest}')


if __name__ == '__main__':
    main()
