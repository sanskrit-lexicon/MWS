"""Docs-integrity check — validate relative file links and #anchors.

The link-everything rule means a broken link is a real defect. This scans the
microanalysis markdown (and the docs-pass root docs they link into), and for
every markdown link `[text](target)`:
  - external (http/https/mailto) -> skipped
  - relative file path           -> the file must exist
  - #anchor (same file or target) -> the heading slug must exist (GitHub rules)

Exit code 1 if any broken link is found, else 0.

Run:  python check_docs.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MICRO = os.path.normpath(os.path.join(HERE, '..'))        # papers/microanalysis
ROOT = os.path.normpath(os.path.join(MICRO, '..', '..'))  # repo root

LINK_RE = re.compile(r'\[(?:[^\]]*)\]\(([^)]+)\)')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*#*$')
# GitHub keeps underscores in slugs; only backticks/asterisks are stripped here.
INLINE_FMT = re.compile(r'[`*]')


def slug(text):
    s = text.strip().lower()
    s = INLINE_FMT.sub('', s)
    # drop link markup inside a heading: [t](u) -> t
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[^\w\s-]', '', s, flags=re.UNICODE)
    return s.replace(' ', '-')


_anchor_cache = {}


def anchors_of(path):
    if path in _anchor_cache:
        return _anchor_cache[path]
    anchors = set()
    counts = {}
    try:
        with open(path, encoding='utf-8') as f:
            in_code = False
            for line in f:
                if line.lstrip().startswith('```'):
                    in_code = not in_code
                    continue
                if in_code:
                    continue
                m = HEADING_RE.match(line)
                if not m:
                    continue
                base = slug(m.group(2))
                if base in counts:
                    counts[base] += 1
                    anchors.add(f'{base}-{counts[base]}')
                else:
                    counts[base] = 0
                    anchors.add(base)
    except OSError:
        pass
    _anchor_cache[path] = anchors
    return anchors


def md_files():
    files = []
    for dirpath, _dirs, names in os.walk(MICRO):
        for nm in names:
            if nm.endswith('.md'):
                files.append(os.path.join(dirpath, nm))
    # docs-pass root docs the microanalysis links into
    for nm in ('DICT_PROFILE.md', 'ENTRY_GUIDE.md', 'DATA_DICTIONARY.md',
               'CONTRIBUTING.md', 'ROADMAP.md', 'README.md', 'CITATION.cff'):
        p = os.path.join(ROOT, nm)
        if os.path.exists(p):
            files.append(p)
    return files


def main():
    broken = []
    checked = 0
    for src in md_files():
        srcdir = os.path.dirname(src)
        with open(src, encoding='utf-8') as f:
            text = f.read()
        for m in LINK_RE.finditer(text):
            s, e = m.start(), m.end()
            # skip a link wrapped wholly in backticks (`[text](target)`) — an example, not a live link
            if s > 0 and text[s - 1] == '`' and e < len(text) and text[e] == '`':
                continue
            target = m.group(1).strip()
            if target.startswith(('http://', 'https://', 'mailto:', 'file:')):
                continue
            checked += 1
            path_part, _, anchor = target.partition('#')
            if path_part == '':
                # same-file anchor
                if anchor and slug_decode(anchor) not in anchors_of(src):
                    broken.append((src, target, 'missing same-file anchor'))
                continue
            tgt = os.path.normpath(os.path.join(srcdir, path_part))
            if not os.path.exists(tgt):
                broken.append((src, target, 'missing file'))
                continue
            if anchor and tgt.endswith('.md'):
                if slug_decode(anchor) not in anchors_of(tgt):
                    broken.append((src, target, 'missing anchor'))

    print(f'Checked {checked} local links across {len(md_files())} markdown files.')
    if not broken:
        print('OK - no broken file links or anchors.')
        return 0
    print(f'\nBROKEN ({len(broken)}):')
    for src, target, why in broken:
        print(f'  {os.path.relpath(src, ROOT)}  ->  {target}   [{why}]')
    return 1


def slug_decode(anchor):
    # anchors in links are already slug-form; lowercase to be safe
    return anchor.strip().lower()


if __name__ == '__main__':
    sys.exit(main())
