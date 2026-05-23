r"""Shared helpers for the microanalysis audit scripts.

These scripts audit the *published* block-detection algorithm — so we import
`classify_type` and `detect_blocks` verbatim from the figure pipeline
(`figures/scripts/export_data.py`) rather than re-implementing them. The
record regex is copied from the same source.

Data lives in the MSYS `/tmp` == Windows `%LOCALAPPDATA%\Temp`.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.normpath(os.path.join(HERE, '..', 'figures', 'scripts'))
sys.path.insert(0, SCRIPTS)

from export_data import classify_type, detect_blocks  # noqa: E402  (the real algorithm)

TMP = r'C:/Users/user/AppData/Local/Temp'
BLOCK_ORDER = [f'F{i:02d}' for i in range(1, 19)]
TYPE_ORDER = ['root', 'noun-m', 'noun-f', 'noun-n', 'noun-mn', 'adjective-mfn',
              'indeclinable', 'compound', 'derived', 'continuation',
              'lexicographer-only', 'etymological-ie', 'botanical',
              'biographical', 'vedic-accented', 'other']

# MW record header carries <e>; this is the exact pattern export_data uses.
MW_RECORD_RE = re.compile(
    r'<L>([0-9.]+)<pc>([^<]*)<k1>([^<\r\n]*?)<k2>([^<\r\n]*?)(?:<h>([^<]*))?<e>([^\r\n]+?)\r?\n(.*?)\r?\n<LEND>',
    re.DOTALL,
)


def datapath(name):
    return os.path.join(TMP, name)


def iter_mw(path=None):
    """Yield dicts for every MW record: lnum, pc, k1, k2, h, ecode, body."""
    path = path or datapath('mw.txt')
    with open(path, encoding='utf-8') as f:
        text = f.read()
    for m in MW_RECORD_RE.finditer(text):
        lnum, pc, k1, k2, h, ecode, body = m.groups()
        yield {
            'lnum': lnum, 'pc': pc, 'k1': k1, 'k2': k2,
            'h': h, 'ecode': ecode.strip(), 'body': body,
        }
