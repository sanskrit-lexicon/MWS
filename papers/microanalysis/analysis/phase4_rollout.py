#!/usr/bin/env python3
"""S6 — Phase-4 wave-1 docs-pass rollout for 15 CDSL dict repos.

For each repo:
  1. Create docs-pass branch from master/main HEAD
  2. Push DICT_PROFILE.md (data-rich for Tier A; stub for Tier B/C)
  3. Open tracking issue with @funderburkjim @Andhrabharati

Run:  python phase4_rollout.py [REPO ...]
  e.g. python phase4_rollout.py PWG PWK     (single repos)
       python phase4_rollout.py              (all 15)
"""
import base64
import json
import os
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding='utf-8')

ORG = 'sanskrit-lexicon'
MWS_BRANCH = 'https://github.com/sanskrit-lexicon/MWS/blob/docs-pass'
PROFILES_URL = f'{MWS_BRANCH}/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md'
CROSS_URL = f'{MWS_BRANCH}/papers/microanalysis/analysis/CROSS_DICT.md'
ATLAS_URL = 'https://github.com/sanskrit-lexicon/csl-atlas'
CDSL_URL = 'https://www.sanskrit-lexicon.uni-koeln.de/'

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(HERE, '..', 'figures', 'data'))

# --- Repo metadata -------------------------------------------------------

REPOS = {
    'PWG': {
        'csl_code': 'pwg',
        'full_name': 'Petersburger Wörterbuch (Großes PW) 1855–1875',
        'author': 'Otto von Böhtlingk and Rudolf Roth',
        'author_url': 'https://en.wikipedia.org/wiki/Otto_von_B%C3%B6htlingk',
        'year': '1855–1875', 'lang': 'German', 'vols': 7,
        'records': 123366, 'ls_per_rec': 4.63, 'modal': 4, 'mean': 3.74,
        'genre': 'structured',
        'blocks_json': 'pwg_blocks.json',
        'relationship': (
            'PWG is MW\'s principal scholarly source. '
            'Monier-Williams used the 7-volume Großes PW throughout the 1899 revision, '
            'selectively incorporating its citation apparatus while condensing into one volume. '
            'See [DICT_PROFILE.md — Beyond PWG]'
            f'({MWS_BRANCH}/DICT_PROFILE.md#beyond-pwg--what-mw-contributes) '
            'for a quantified comparison.'
        ),
        'when_to_use': (
            'Use PWG when tracing **Vedic attestation** or following a citation chain '
            'to named sources. With 4.63 `<ls>` citations/record (vs MW\'s 1.089), '
            'PWG names the kosha and textual sources that MW collapses into the anonymous '
            '`L.` hedge. In German but structured similarly to MW.'
        ),
        'bibtex_key': 'boehtlingk_roth_pw_1855',
        'bibtex_extra': '  editor = {Otto von B{\\"o}htlingk and Rudolf Roth},\n',
    },
    'PWK': {
        'csl_code': 'pw',
        'full_name': 'Böhtlingk Sanskrit-Wörterbuch in kürzerer Fassung 1879–1889',
        'author': 'Otto von Böhtlingk',
        'author_url': 'https://en.wikipedia.org/wiki/Otto_von_B%C3%B6htlingk',
        'year': '1879–1889', 'lang': 'German', 'vols': 1,
        'records': 170556, 'ls_per_rec': 0.515, 'modal': 3, 'mean': 3.32,
        'genre': 'structured',
        'blocks_json': 'pwk_blocks.json',
        'relationship': (
            'PWK is Böhtlingk\'s condensed single-volume abridgment of [PWG](https://github.com/sanskrit-lexicon/PWG). '
            'With 170,556 records it is the largest CDSL dict by count; but citation density (0.515 ls/rec) '
            'is much lower than PWG (4.63) — condensation preferentially dropped citations. '
            'MW (1 vol, English) and PWK (1 vol, German) are useful counterparts for the same era.'
        ),
        'when_to_use': (
            'Use PWK as a compact German-language alternative to PWG for quick lookups, '
            'or when PWG\'s 7-volume format is unwieldy. '
            'PWK adds corrections to PWG while abridging. '
            'For citation tracing, prefer PWG.'
        ),
        'bibtex_key': 'boehtlingk_pwk_1879',
        'bibtex_extra': '  editor = {Otto von B{\\"o}htlingk},\n',
    },
    'AP90': {
        'csl_code': 'ap90',
        'full_name': "Apte's Practical Sanskrit-English Dictionary 1890",
        'author': 'Vaman Shivaram Apte',
        'author_url': 'https://en.wikipedia.org/wiki/Vaman_Shivaram_Apte',
        'year': '1890', 'lang': 'English', 'vols': 1,
        'records': 90654, 'ls_per_rec': 0.691, 'modal': 2, 'mean': 2.53,
        'genre': 'structured',
        'blocks_json': 'ap_blocks.json',
        'relationship': (
            'Apte (AP90) is a student-oriented single-volume English companion '
            'to MW. Where MW provides citation apparatus and etymological depth, '
            'Apte emphasises breadth of compound coverage with minimal philological overhead '
            '(modal blocks = 2 vs MW\'s 5). Its compound-heavy "other" category (63,841 of 90,654 records) '
            'makes it useful for practical lookup of derived forms.'
        ),
        'when_to_use': (
            'Use AP90 for **practical lookup of compounds and verb forms** where you need '
            'a quick English gloss without citation context. '
            'For scholarly citation tracing, use MW + PWG. '
            'AP90 and MW complement each other: AP90 for breadth, MW for depth.'
        ),
        'bibtex_key': 'apte_practical_1890',
        'bibtex_extra': '  author = {Vaman Shivaram Apte},\n',
    },
    'WIL': {
        'csl_code': 'wil',
        'full_name': "Wilson's Sanskrit-English Dictionary 1832",
        'author': 'Horace Hayman Wilson',
        'author_url': 'https://en.wikipedia.org/wiki/Horace_Hayman_Wilson',
        'year': '1832', 'lang': 'English', 'vols': 1,
        'records': 44577, 'ls_per_rec': 0.005, 'modal': 3, 'mean': 3.00,
        'genre': 'structured',
        'blocks_json': 'wil_blocks.json',
        'relationship': (
            'WIL is MW\'s direct English-language ancestor. '
            'Monier-Williams used the 1832 WIL as the base for both the '
            '[1872 first edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php) '
            'and the [1899 second edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php), '
            'supplementing it with PWG\'s philological apparatus. '
            'CDSL classifies WIL as a `koSa` (kosha), reflecting its origin at '
            '[Fort William College, Calcutta](https://en.wikipedia.org/wiki/Fort_William_College) '
            'with Indian pandits working from classical kosha sense-divisions.'
        ),
        'when_to_use': (
            'Use WIL for **historical comparison** with MW — to see the sense-divisions '
            'that MW inherited from the 1832 baseline. '
            'WIL has no source-citation apparatus (0.005 ls/rec) so is not useful for citation tracing. '
            'Its systematic grammatical tagging (99.8% gram block) is a strength for morphological lookup.'
        ),
        'bibtex_key': 'wilson_sanskrit_1832',
        'bibtex_extra': '  author = {Horace Hayman Wilson},\n',
    },
    'CAE': {
        'csl_code': 'cae',
        'full_name': "Cappeller's Sanskrit-English Dictionary 1891",
        'author': 'Carl Cappeller',
        'author_url': 'https://en.wikipedia.org/wiki/Carl_Cappeller',
        'year': '1891', 'lang': 'English', 'vols': 1,
        'records': 40069, 'ls_per_rec': 0.000, 'modal': 3, 'mean': 2.93,
        'genre': 'structured',
        'blocks_json': 'cae_blocks.json',
        'relationship': (
            '[Carl Cappeller](https://en.wikipedia.org/wiki/Carl_Cappeller) '
            'also contributed as an editor to MW (1899). '
            'CAE is a compact single-volume English dictionary contemporaneous with MW. '
            'It has no `<ls>` source-citation apparatus (0.000 ls/rec) and no hedge block. '
            'The [asterisk (*) and dagger (†) markers](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/LS_HEDGE_CHECK.md) '
            'in CAE are entry-level markers (similar to MW\'s `L.` hedge) — '
            'see DOUBTS D2 for the ongoing investigation.'
        ),
        'when_to_use': (
            'Use CAE as a compact English-language secondary check alongside MW. '
            'Cappeller\'s dictionary is well-regarded for its conciseness and accuracy. '
            'Not useful for citation tracing (no `<ls>` apparatus).'
        ),
        'bibtex_key': 'cappeller_sanskrit_1891',
        'bibtex_extra': '  author = {Carl Cappeller},\n',
    },
    'BEN': {
        'csl_code': 'ben',
        'full_name': 'Benfey Sanskrit-English Dictionary 1866',
        'author': 'Theodor Benfey',
        'author_url': 'https://en.wikipedia.org/wiki/Theodor_Benfey',
        'year': '1866', 'lang': 'English', 'vols': 1,
        'records': 5186, 'ls_per_rec': 2.836, 'modal': 3, 'mean': 2.93,
        'genre': 'structured',
        'blocks_json': 'ben_blocks.json',
        'relationship': (
            'Benfey (1866) predates MW\'s 1872 first edition by 6 years and PWG is still ongoing (1855–75). '
            'With 2.836 ls/rec, BEN has a surprisingly high citation density for its size (5,186 records) — '
            'but these records appear to be primarily root/verb entries, not full-coverage headwords. '
            'BEN has no `<lex>` grammatical tags.'
        ),
        'when_to_use': (
            'Use BEN for historical comparison and for checking root-level Sanskrit definitions '
            'from 1866 against MW (1872/1899). '
            'Small size (5,186 records) reflects its coverage of verbal roots rather than full lexicon.'
        ),
        'bibtex_key': 'benfey_sanskrit_1866',
        'bibtex_extra': '  author = {Theodor Benfey},\n',
    },
    'GRA': {
        'csl_code': 'gra',
        'full_name': "Grassmann's Wörterbuch zum Rig-Veda 1872–1875",
        'author': 'Hermann Grassmann',
        'author_url': 'https://en.wikipedia.org/wiki/Hermann_Grassmann',
        'year': '1872–1875', 'lang': 'German', 'vols': 1,
        'records': None, 'ls_per_rec': None, 'modal': None, 'mean': None,
        'genre': 'structured',
        'blocks_json': None,
        'relationship': (
            'GRA is the specialized Rig-Veda lexicon — the primary reference for Vedic Sanskrit '
            'in the CDSL collection. Where MW covers Classical and Vedic, GRA focuses exclusively '
            'on Rig-Veda attestation with extensive citation of RV hymns. '
            'It is the principal resource for scholars of early Vedic.'
        ),
        'when_to_use': (
            'Use GRA for **Rig-Veda attestation** — when you need the exact RV context '
            'for a Vedic word. MW cites the RV extensively via `<ls>RV.</ls>` but '
            'GRA provides the full entry in its Vedic context.'
        ),
        'bibtex_key': 'grassmann_rigveda_1872',
        'bibtex_extra': '  author = {Hermann Grassmann},\n',
    },
    'SKD': {
        'csl_code': 'skd',
        'full_name': 'Śabdakalpadrumaḥ 1822–1858',
        'author': 'Rādhākāntadeva',
        'author_url': 'https://en.wikipedia.org/wiki/Radha_Kanta_Dev',
        'year': '1822–1858', 'lang': 'Sanskrit', 'vols': 1,
        'records': 42531, 'ls_per_rec': 0.000, 'modal': 2, 'mean': 1.99,
        'genre': 'sanskrit',
        'blocks_json': 'skd_blocks.json',
        'relationship': (
            'SKD is a Sanskrit-Sanskrit kosha — a different genre from the structured '
            'bilingual dicts (MW, PWG, AP90). No `<lex>` or `<ls>` markup; '
            'gender is marked inline in Sanskrit prose; sources cited via inline *iti* quotation '
            '(72,176 instances = 1.70/record). '
            'Contemporary with [WIL](https://github.com/sanskrit-lexicon/WIL) (1832) and '
            'partially overlapping with [PWG](https://github.com/sanskrit-lexicon/PWG) (1855–75). '
            'SKD\'s sense-divisions are a source for the kosha tradition that influenced WIL → MW.'
        ),
        'when_to_use': (
            'Use SKD for **Sanskrit-to-Sanskrit lookup** when the bilingual glosses of MW/AP90 '
            'are insufficient. SKD provides Sanskrit definitions for scholars who read Sanskrit. '
            'The framework-robust block apparatus does not apply — SKD is a different genre.'
        ),
        'bibtex_key': 'radhaKanta_sabdakalpadruma_1822',
        'bibtex_extra': '  author = {R{\\=a}dh{\\=a}k{\\=a}ntadeva},\n',
    },
    'VCP': {
        'csl_code': 'vcp',
        'full_name': 'Vācaspatyam 1873–1884',
        'author': 'Tārānātha Tarkavācaspati',
        'author_url': 'https://en.wikipedia.org/wiki/Taranatha_Tarkavachaspati',
        'year': '1873–1884', 'lang': 'Sanskrit', 'vols': 1,
        'records': 50135, 'ls_per_rec': 0.000, 'modal': 2, 'mean': 1.96,
        'genre': 'sanskrit',
        'blocks_json': 'vcp_blocks.json',
        'relationship': (
            'VCP is an encyclopedic Sanskrit-Sanskrit lexicon — larger than '
            '[SKD](https://github.com/sanskrit-lexicon/SKD) (50,135 vs 42,531 records) '
            'and more encyclopedic in character. '
            'Contemporary with [PWG](https://github.com/sanskrit-lexicon/PWG) (1855–75); '
            'Tārānātha compiled VCP independently without using the German philological tradition. '
            'VCP demonstrates the **parallel development** of the indigenous Sanskrit-Sanskrit '
            'and European philological lexicographic traditions.'
        ),
        'when_to_use': (
            'Use VCP for **Sanskrit-to-Sanskrit encyclopedic lookup** — especially for '
            'philosophical, astronomical, grammatical, and poetic terminology where VCP\'s '
            'extensive textual quotations (Manu-Smṛti, Bhagavad-Gītā, Pāṇini) provide scholarly context. '
            'VCP is the richest source for Vedānta, Nyāya, and Jyotiṣa terminology in CDSL.'
        ),
        'bibtex_key': 'taranatha_vacaspatyam_1873',
        'bibtex_extra': '  author = {T{\\=a}r{\\=a}n{\\=a}tha Tarkav{\\=a}caspati},\n',
    },
    'MW72': {
        'csl_code': 'mw72',
        'full_name': 'Monier-Williams Sanskrit-English Dictionary 1872 (first edition)',
        'author': 'Monier Monier-Williams',
        'author_url': 'https://en.wikipedia.org/wiki/Monier_Monier-Williams',
        'year': '1872', 'lang': 'English', 'vols': 1,
        'records': 55388, 'ls_per_rec': 0.000, 'modal': None, 'mean': None,
        'genre': 'structured',
        'blocks_json': None,
        'relationship': (
            'MW72 is the **1872 first edition** of MW, preceding the canonical '
            '[1899 second edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php) '
            '(MWS in CDSL). MW72 is primarily useful for tracing the evolution of '
            'Monier-Williams\'s editorial choices over the 27 years between editions. '
            'The 1899 edition expanded significantly (55,388 → 286,561 records) by '
            'incorporating PWG\'s citation apparatus. '
            'See [Cologne MW72 scan](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php).'
        ),
        'when_to_use': (
            'Use MW72 for **historical comparison** with the 1899 edition (MWS). '
            'Useful for understanding which entries existed in 1872 vs were added later, '
            'and how sense-divisions evolved. Not recommended as a primary reference — '
            'prefer the [1899 MWS](https://github.com/sanskrit-lexicon/MWS) for scholarly use.'
        ),
        'bibtex_key': 'monierWilliams_1872',
        'bibtex_extra': '  author = {Monier Monier-Williams},\n',
    },
    'MD': {
        'csl_code': 'md',
        'full_name': "Macdonell's Sanskrit-English Dictionary 1893",
        'author': 'Arthur A. Macdonell',
        'author_url': 'https://en.wikipedia.org/wiki/Arthur_Anthony_Macdonell',
        'year': '1893', 'lang': 'English', 'vols': 1,
        'records': None, 'ls_per_rec': None, 'modal': None, 'mean': None,
        'genre': 'structured',
        'blocks_json': None,
        'relationship': (
            '[Macdonell](https://en.wikipedia.org/wiki/Arthur_Anthony_Macdonell) '
            'was Boden Professor of Sanskrit at Oxford, succeeding Monier-Williams. '
            'MD (1893) is a compact English-language dictionary primarily for Classical Sanskrit, '
            'contemporaneous with CAE (1891) and the later editions of AP90. '
            'It is not as exhaustive as MW but known for clarity of definition.'
        ),
        'when_to_use': (
            '[DRAFT — maintainers please fill in. Key questions: what is the record count? '
            'What is the coverage relative to MW and CAE? What is the target audience?]'
        ),
        'bibtex_key': 'macdonell_sanskrit_1893',
        'bibtex_extra': '  author = {Arthur A. Macdonell},\n',
    },
    'SHS': {
        'csl_code': 'shs',
        'full_name': 'Shabda-Sagara Sanskrit-English Dictionary',
        'author': 'Tara Natha Tarkavachaspati',
        'author_url': None,
        'year': '~1867', 'lang': 'English', 'vols': 1,
        'records': None, 'ls_per_rec': None, 'modal': None, 'mean': None,
        'genre': 'structured',
        'blocks_json': None,
        'relationship': (
            'SHS (Śabda-Sāgara) is an English-medium Sanskrit dictionary by '
            'Tara Natha Tarkavachaspati. '
            '[DRAFT — maintainers please verify author, year, and relationship to other dicts.]'
        ),
        'when_to_use': (
            '[DRAFT — maintainers please fill in.]'
        ),
        'bibtex_key': 'shabdaSagara',
        'bibtex_extra': '',
    },
    'BHS': {
        'csl_code': 'bhs',
        'full_name': 'Buddhist Hybrid Sanskrit Grammar and Dictionary 1953',
        'author': 'Franklin Edgerton',
        'author_url': 'https://en.wikipedia.org/wiki/Franklin_Edgerton',
        'year': '1953', 'lang': 'English', 'vols': 2,
        'records': None, 'ls_per_rec': None, 'modal': None, 'mean': None,
        'genre': 'structured',
        'blocks_json': None,
        'relationship': (
            'BHS (Buddhist Hybrid Sanskrit) is a specialized dictionary for the hybrid '
            'Sanskrit of Buddhist canonical texts. Unlike the pan-Sanskrit dicts (MW, AP90), '
            '[Edgerton](https://en.wikipedia.org/wiki/Franklin_Edgerton)\'s BHS focuses on '
            'vocabulary found in Buddhist Hybrid Sanskrit texts (Mahāvastu, Lalitavistara, etc.) '
            'that is not well-attested in Classical Sanskrit dictionaries. '
            'An essential supplement to MW for Buddhist scholars.'
        ),
        'when_to_use': (
            'Use BHS for **Buddhist Sanskrit** vocabulary — words found in Mahāyāna texts '
            'that MW marks as `[BHSkt.]` or that are absent from MW entirely. '
            'For Classical Sanskrit, prefer MW + PWG. '
            'BHS and MW are complementary, not competing, references.'
        ),
        'bibtex_key': 'edgerton_bhs_1953',
        'bibtex_extra': '  author = {Franklin Edgerton},\n',
    },
    'INM': {
        'csl_code': 'inm',
        'full_name': 'Index to Names in the Mahābhārata',
        'author': 'Sorensen / CDSL digitization',
        'author_url': None,
        'year': '1904', 'lang': 'English', 'vols': 1,
        'records': None, 'ls_per_rec': None, 'modal': None, 'mean': None,
        'genre': 'index',
        'blocks_json': None,
        'relationship': (
            'INM is a name index rather than a full dictionary. '
            'It indexes proper names occurring in the Mahābhārata, '
            'useful for tracing mythological figures and their appearances across the epic. '
            'Complements MW\'s biographical entries and the INM-specific `<bio>` block. '
            '[DRAFT — maintainers please verify the author (Sørensen 1904?) and scope.]'
        ),
        'when_to_use': (
            'Use INM for **proper name lookup** in the Mahābhārata context. '
            'For general Sanskrit vocabulary, prefer MW.'
        ),
        'bibtex_key': 'sorensen_inm_1904',
        'bibtex_extra': '',
    },
    'SCH': {
        'csl_code': 'sch',
        'full_name': "Schmidt's Nachträge zum Sanskrit-Wörterbuch (1928)",
        'author': 'Richard Schmidt',
        'author_url': 'https://de.wikipedia.org/wiki/Richard_Schmidt_(Indologe)',
        'year': '1928', 'lang': 'German', 'vols': 1,
        'records': None, 'ls_per_rec': None, 'modal': None, 'mean': None,
        'genre': 'structured',
        'blocks_json': None,
        'relationship': (
            'SCH (*Nachträge zum Sanskrit-Wörterbuch* = Supplements to the Sanskrit Dictionary) '
            'is a German-language supplement designed to extend/correct PWG/PWK. '
            'Published in 1928, it postdates MW (1899) and represents the German tradition\'s '
            'corrections to Böhtlingk-Roth. '
            '[DRAFT — maintainers please verify author, scope, and csl-orig path.]'
        ),
        'when_to_use': (
            'Use SCH when PWG/PWK coverage of a word is incomplete or erroneous, '
            'and you need the correction documented in Schmidt\'s 1928 supplement. '
            'German language.'
        ),
        'bibtex_key': 'schmidt_nachtraege_1928',
        'bibtex_extra': '  author = {Richard Schmidt},\n',
    },
}


# --- Helper functions -------------------------------------------------------

def run_gh(args, capture=True):
    result = subprocess.run(
        ['gh'] + args, capture_output=capture,
        text=True, encoding='utf-8', errors='replace'
    )
    if capture:
        return result.stdout.strip(), result.returncode
    return None, result.returncode


def get_default_branch_sha(repo):
    """Return the SHA of the master (or main) branch HEAD."""
    for branch in ('master', 'main'):
        out, rc = run_gh(['api', f'repos/{ORG}/{repo}/git/refs/heads/{branch}', '--jq', '.object.sha'])
        if rc == 0 and len(out) == 40:
            return branch, out
    return None, None


def create_docs_pass_branch(repo, sha):
    """Create the docs-pass branch from sha. Returns True on success."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump({'ref': 'refs/heads/docs-pass', 'sha': sha}, f)
        tmp = f.name
    try:
        _, rc = run_gh(['api', f'repos/{ORG}/{repo}/git/refs', '-X', 'POST', '--input', tmp])
        return rc == 0
    finally:
        os.unlink(tmp)


def push_file_to_branch(repo, path, content_str, commit_msg, branch='docs-pass'):
    """Create or update a file on a branch via GitHub API."""
    content_b64 = base64.b64encode(content_str.encode('utf-8')).decode('ascii')
    payload = {'message': commit_msg, 'content': content_b64, 'branch': branch}
    # Check if file exists on the target branch (get its SHA for update)
    out, rc = run_gh(['api', f'repos/{ORG}/{repo}/contents/{path}?ref={branch}',
                      '-H', 'Accept: application/vnd.github.v3+json',
                      '--jq', '.sha'])
    if rc == 0 and out:
        payload['sha'] = out  # required for update
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False)
        tmp = f.name
    try:
        _, rc = run_gh(['api', f'repos/{ORG}/{repo}/contents/{path}', '-X', 'PUT', '--input', tmp])
        return rc == 0
    finally:
        os.unlink(tmp)


def open_tracking_issue(repo, meta):
    """Open a docs-pass tracking issue. Returns the issue URL."""
    title = f'docs-pass: {repo} documentation review'
    body = build_issue_body(repo, meta)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(body)
        tmp = f.name
    try:
        out, rc = run_gh(['issue', 'create',
                          '--repo', f'{ORG}/{repo}',
                          '--title', title,
                          '--body-file', tmp])
        return out if rc == 0 else None
    finally:
        os.unlink(tmp)


# --- Content generators ----------------------------------------------------

def load_blocks_json(filename):
    """Load the per-dict blocks JSON by filename."""
    jfile = os.path.join(DATA_DIR, filename)
    if os.path.exists(jfile):
        with open(jfile, encoding='utf-8') as f:
            return json.load(f)
    return None


def build_block_table(data):
    """Build a markdown table from the blocks_pct dict."""
    if not data:
        return '*Block profile data not yet computed. Run `export_dict_blocks.py` against the source data.*\n'
    rows = ['| Block | % of entries |', '|---|---|']
    block_labels = {
        'head': 'head (record)', 'body': 'body (¦ separator)', 'gram': 'gram (`<lex>` tag)',
        'cite': 'cite (`<ls>` source)', 'hom': 'homograph (`<hom>`)',
        'etym': 'etymology (√ / `<ab>fr.</ab>`)', 'xref': 'cross-ref (q.v. / cf.)',
        'hedge': 'L. hedge (`<ls>L.</ls>`)', 'info': 'info (digitisation `<info`)',
    }
    for b in data.get('blocks', []):
        pct = data['blocks_pct'].get(b, 0)
        rows.append(f'| {block_labels.get(b, b)} | {pct:.1f}% |')
    return '\n'.join(rows) + '\n'


def build_per_type_table(data):
    """Build a per-type table from matrix data."""
    if not data or not data.get('matrix'):
        return '*Per-type profile not available (no `<lex>` tags, or data not computed).*\n'
    rows = ['| Type | N | cite% | mean blocks |', '|---|---:|---:|---:|']
    for row in data['matrix']:
        t = row['type']
        n = row['count']
        cite_pct = row.get('cite_pct', 0)
        cite_cnt = row.get('cite', 0)
        cite_pct2 = 100.0 * cite_cnt / n if n else 0
        # Compute mean blocks (sum all block counts / n)
        total_blocks = sum(row.get(b, 0) for b in data.get('blocks', []))
        mean_b = total_blocks / n if n else 0
        rows.append(f'| {t} | {n:,} | {cite_pct2:.1f}% | {mean_b:.2f} |')
    return '\n'.join(rows) + '\n'


def build_dict_profile(repo, meta):
    """Generate DICT_PROFILE.md content for a repo."""
    code = meta['csl_code']
    full_name = meta['full_name']
    author = meta['author']
    author_url = meta.get('author_url')
    author_link = f'[{author}]({author_url})' if author_url else author
    year = meta['year']
    lang = meta['lang']
    vols = meta['vols']
    records = meta.get('records')
    ls_per_rec = meta.get('ls_per_rec')
    modal = meta.get('modal')
    mean = meta.get('mean')
    genre = meta.get('genre', 'structured')

    src_url = f'https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/{code}/{code}.txt'
    repo_url = f'https://github.com/sanskrit-lexicon/{repo}'
    branch_url = f'{repo_url}/tree/docs-pass'
    issues_url = f'{repo_url}/issues'

    blocks_data = load_blocks_json(meta['blocks_json']) if meta.get('blocks_json') else None

    records_str = f'{records:,}' if records else '[DRAFT]'
    ls_str = f'{ls_per_rec:.3f}' if ls_per_rec is not None else '[DRAFT]'
    modal_str = str(modal) if modal is not None else '[DRAFT]'
    mean_str = f'{mean:.2f}' if mean is not None else '[DRAFT]'

    block_table = build_block_table(blocks_data)
    type_table = build_per_type_table(blocks_data) if genre == 'structured' else \
        '*Per-type profile not applicable (Sanskrit-Sanskrit kosha genre).*\n'

    block_ref = (
        f'Data from [`papers/microanalysis/figures/data/{code}_blocks.json`]'
        f'(https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/{code}_blocks.json) '
        f'generated by [`export_dict_blocks.py`]'
        f'(https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/scripts/export_dict_blocks.py).'
    ) if blocks_data else (
        'Block profile data not yet computed. '
        f'Run `export_dict_blocks.py` against [`csl-orig v02/{code}/{code}.txt`]({src_url}).'
    )

    bibtex_key = meta.get('bibtex_key', f'{code}_{year}')
    bibtex_extra = meta.get('bibtex_extra', '')
    bibtex_year = year.split('–')[0] if '–' in str(year) else str(year)

    content = f"""# DICT_PROFILE.md — {full_name}

A reader's guide to the [Cologne Digital Sanskrit Dictionaries]({CDSL_URL}) ({repo} repository) edition
of *{full_name}*. Part of the org-wide
[docs-pass](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/HANDOFF.md)
pilot, modelled on [MWS DICT_PROFILE.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md).

---

## At a Glance

| | |
|---|---|
| Full title | *{full_name}* |
| CDSL short name | `{code}` |
| Author(s) | {author_link} |
| Year | {year} |
| Language | {lang} |
| Volumes | {vols} |
| Record count | {records_str} |
| `<ls>` citations/record | {ls_str} |
| Modal blocks/entry | {modal_str} |
| Mean blocks/entry | {mean_str} |
| Source data | [`csl-orig v02/{code}/{code}.txt`]({src_url}) |

---

## Block profile (format-robust common-block vocabulary)

{block_ref}

{block_table}
See the [cross-dictionary comparison]({CROSS_URL}) for how {repo}'s block profile
compares across all nine CDSL dicts.

---

## Per-type citation profile

From [`analysis/CROSS_DICT_PROFILES.md`]({PROFILES_URL}).

{type_table}
---

## When to use {repo}

{meta.get('when_to_use', '[DRAFT — maintainers please fill in.]')}

---

## Relationship to MW

{meta.get('relationship', '[DRAFT — maintainers please fill in.]')}

---

## Orthographical conventions

[DRAFT — maintainers please document the encoding conventions specific to {repo}:
SLP1 vs IAST vs AS, headword format, compound markers, accent marks, etc.
Reference: [`csl-orig v02/{code}/{code}.txt`]({src_url})]

---

## Known issues

See [GitHub issues]({issues_url}) for this repository.
All issue tracking follows the [CDSL taxonomy](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/CONTRIBUTING.md).

---

## Further reading

- [Cologne Digital Sanskrit Dictionaries]({CDSL_URL})
- [csl-orig source data — v02/{code}/]({src_url})
- [Cross-dictionary microanalysis]({MWS_BRANCH}/papers/microanalysis/PAPER.md) (MW1899 as reference)
- [csl-atlas per-dict chapter]({ATLAS_URL}/blob/main/src/dicts/{code}.md)

---

## BibTeX

```bibtex
@misc{{{bibtex_key},
  title = {{{{{full_name}}}}},
{bibtex_extra}  year = {{{bibtex_year}}},
  howpublished = {{Cologne Digital Sanskrit Dictionaries}},
  url = {{{CDSL_URL}}}
}}
```
"""
    return content


def build_issue_body(repo, meta):
    """Generate the tracking issue body for a docs-pass branch."""
    code = meta['csl_code']
    full_name = meta['full_name']
    branch_url = f'https://github.com/sanskrit-lexicon/{repo}/tree/docs-pass'
    dict_profile_url = f'https://github.com/sanskrit-lexicon/{repo}/blob/docs-pass/DICT_PROFILE.md'
    records_str = f'{meta["records"]:,}' if meta.get('records') else '[DRAFT]'

    return f"""@funderburkjim @Andhrabharati — please review the `docs-pass` branch.

Branch: [`docs-pass`]({branch_url}) of `{repo}`.

Part of the org-wide docs-pass for ~76 sanskrit-lexicon repositories
(modelled on [MWS #195](https://github.com/sanskrit-lexicon/MWS/issues/195)).

---

## Docs-pass: {repo} ({full_name})

### Track A — added (verify facts, then merge)

| File | Status | What to verify |
|---|---|---|
| [`DICT_PROFILE.md`]({dict_profile_url}) | Stub | Historical facts; at-a-glance stats; when-to-use text; block profile data |

### Pending (Track B — not yet added)

| File | Notes |
|---|---|
| `ENTRY_GUIDE.md` | Reader's guide to encoding conventions; sample entries; tag counts |
| `DATA_DICTIONARY.md` | Tag inventory; markup conventions specific to {repo} |
| `CONTRIBUTING.md` | Correction workflow for {repo} |
| `CITATION.cff` | Bibliographic citation file |

### Known stats

- **Records:** {records_str}
- **Source data:** [`csl-orig v02/{code}/{code}.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/{code}/{code}.txt)
- **Block profile data:** [`figures/data/{code}_blocks.json`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/{code}_blocks.json)
- **Cross-dict comparison:** [`CROSS_DICT_PROFILES.md`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md)

### Reviewer checklist

- [ ] `DICT_PROFILE.md` at-a-glance stats correct (record count, year, author)
- [ ] `DICT_PROFILE.md` when-to-use section accurate
- [ ] `DICT_PROFILE.md` relationship to MW correct
- [ ] Block profile data verified (run `export_dict_blocks.py` if needed)
- [ ] Track B files added before merge
- [ ] Branch merged to master
"""


# --- Main ------------------------------------------------------------------

def process_repo(repo):
    meta = REPOS[repo]
    print(f'\n=== {repo} ===')

    # 1. Get default branch SHA
    default_branch, sha = get_default_branch_sha(repo)
    if not sha:
        print(f'  ERROR: could not get master/main SHA for {repo}')
        return False
    print(f'  default branch: {default_branch}, SHA: {sha[:8]}...')

    # 2. Create docs-pass branch
    ok = create_docs_pass_branch(repo, sha)
    if ok:
        print(f'  created docs-pass branch')
    else:
        # Branch might already exist
        out, rc = run_gh(['api', f'repos/{ORG}/{repo}/branches/docs-pass', '--jq', '.name'])
        if rc == 0 and out:
            print(f'  docs-pass branch already exists')
        else:
            print(f'  ERROR: could not create docs-pass branch')
            return False

    # 3. Generate DICT_PROFILE.md content
    profile_content = build_dict_profile(repo, meta)

    # 4. Push DICT_PROFILE.md
    commit_msg = f'docs-pass: add DICT_PROFILE.md stub (Phase-4 wave-1 rollout)\n\nCo-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>'
    ok = push_file_to_branch(repo, 'DICT_PROFILE.md', profile_content, commit_msg)
    if ok:
        print(f'  pushed DICT_PROFILE.md ({len(profile_content):,} chars)')
    else:
        print(f'  ERROR: could not push DICT_PROFILE.md')
        return False

    # 5. Open tracking issue
    issue_url = open_tracking_issue(repo, meta)
    if issue_url:
        print(f'  opened tracking issue: {issue_url}')
    else:
        print(f'  WARNING: could not open tracking issue')

    return True


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(REPOS.keys())
    # Validate
    for r in targets:
        if r not in REPOS:
            print(f'Unknown repo: {r}. Valid: {list(REPOS.keys())}')
            sys.exit(1)

    results = {}
    for repo in targets:
        ok = process_repo(repo)
        results[repo] = ok

    print('\n=== Summary ===')
    for repo, ok in results.items():
        status = 'OK' if ok else 'FAILED'
        print(f'  {repo}: {status}')

    failed = [r for r, ok in results.items() if not ok]
    if failed:
        print(f'\nFailed repos: {failed}')
        sys.exit(1)
    else:
        print(f'\nAll {len(targets)} repos processed successfully.')


if __name__ == '__main__':
    main()
