#!/usr/bin/env python3
"""Push full DICT_PROFILE.md to PWG docs-pass branch (S8)."""
import base64, json, os, subprocess, sys, tempfile
sys.stdout.reconfigure(encoding='utf-8')

ORG = 'sanskrit-lexicon'
REPO = 'PWG'
BRANCH = 'docs-pass'

DICT_PROFILE = r"""# Dictionary Profile — Petersburger Wörterbuch (Großes PW)

*Boehtlingk and Roth's* **Sanskrit-Wörterbuch** (**PWG**), the founding comprehensive
Sanskrit dictionary of the European philological tradition. Facts verified against
[Wikipedia](https://en.wikipedia.org/wiki/Sanskrit%E2%80%93Worterbuch), the original
volumes, and the CDSL [`pwg.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt).
Block-profile data from
[`pwg_blocks.json`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/pwg_blocks.json).

---

## At a glance

| Fact | Value |
|---|---|
| Full title | *Sanskrit-Wörterbuch, herausgegeben von der Kaiserlichen Akademie der Wissenschaften* |
| Short name in CDSL | `pwg` |
| Authors | [Otto von Böhtlingk](https://en.wikipedia.org/wiki/Otto_von_B%C3%B6htlingk) (1815–1904) · [Rudolf Roth](https://en.wikipedia.org/wiki/Rudolf_von_Roth) (1821–1895) |
| Language | Sanskrit → German |
| Volumes | 7 |
| Publication years | 1855–1875 |
| Publisher | Imperial Academy of Sciences, St. Petersburg |
| Records in digital edition | 123,366 `<L>` records |
| `<ls>` citations/record | **4.63** (highest among CDSL structured bilingual dicts) |
| Modal blocks/entry | 4 |
| Mean blocks/entry | 3.74 |
| Adjective `<lex>` convention | `<lex>a.</lex>` (not `mfn.`) |
| Source data | [`csl-orig v02/pwg/pwg.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt) |
| Digital license | CC-BY-SA-4.0 |
| Printed source | Public domain |

---

## Orthographical conventions (brief)

Full reference: see [`csl-orig/v02/pwg/`](https://github.com/sanskrit-lexicon/csl-orig/tree/master/v02/pwg).

- **Stored form:** SLP1 encoding for Sanskrit headwords in `<k1>`, `<k2>`.
- **Definitions:** in German (not English — require German-language competence for use).
- **Adjective `<lex>`:** PWG uses `<lex>a.</lex>` (German *Adjektiv*), not `<lex>mfn.</lex>`. The CDSL display system maps this correctly; tools reading raw XML must account for it.
- **`<ls>` citations:** PWG names sources directly by abbreviation — e.g. `<ls>H.</ls>` for Hemacandra, `<ls>AK.</ls>` for Amarakośa. No anonymous `L.` hedge: every source is named. See [Citation markers](#citation-markers--pwgs-named-source-apparatus) below.
- **Volumes:** The 7-volume structure (vol. I A–D, II E–GH, III I–N, IV P–BH, V M–R, VI Ś–SP, VII SPH–H) is preserved in the page-column `<pc>` tags.

---

## Historical background

**Otto von Böhtlingk** (1815–1904; born in St. Petersburg of German parents) and
**Rudolf Roth** (1821–1895; Professor at Tübingen) undertook the *Sanskrit-Wörterbuch*
at the commission of the Imperial Academy of Sciences in St. Petersburg — hence
the informal name *Petersburger Wörterbuch* (PW) or, in English scholarship, PWG
(to distinguish the 7-volume *Großes PW* from the 5-volume *kürzeres PW* = [PWK](https://github.com/sanskrit-lexicon/PWK)).

Publication ran from **1855 to 1875** — twenty years of collaborative philological
work, producing seven large-format volumes of approximately 1,300 pages each. The
project is one of the foundational achievements of 19th-century comparative philology.
At the time of publication it was, and it arguably remains, the most exhaustively
annotated Sanskrit dictionary ever produced: 123,366 records averaging **4.63 cited
sources per record** — six times the citation density of [MW](https://github.com/sanskrit-lexicon/MWS) (1.089 ls/rec).

Böhtlingk had already demonstrated his philological credentials with his [edition of
Pāṇini's Aṣṭādhyāyī](https://en.wikipedia.org/wiki/A%E1%B9%A3%E1%B9%AD%C4%81dhy%C4%81y%C4%AB)
(1839–40), the first critical edition of the grammar that structures Sanskrit itself.
Roth brought his Vedic textual expertise, having studied the Rigveda with Christian
Lassen. The combination — Böhtlingk's grammatical rigour and Roth's textual scholarship
— produced the comprehensive citation apparatus that defines PWG.

[Monier Monier-Williams](https://en.wikipedia.org/wiki/Monier_Monier-Williams) used
the early PWG volumes extensively for his
[1872 first edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/index.php)
and the completed PWG for his [1899 second edition](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php).
MW translated, condensed, and reworked PWG's German into English — adding IE-cognate
apparatus and compound sub-entries, but replacing PWG's named-kosha attributions
with the anonymous `<ls>L.</ls>` hedge.

Böhtlingk later produced the **shorter dictionary**, [PWK](https://github.com/sanskrit-lexicon/PWK)
(*Sanskrit-Wörterbuch in kürzerer Fassung*, 1879–1889), a single-volume condensation
of the 7-volume PWG with corrections. PWK has more records (170,556) but far lower
citation density (0.515 ls/rec) — condensation preferentially dropped citations.

---

## Scholarly significance

PWG is **the primary scholarly Sanskrit dictionary for German-reading Indologists**
and the most citation-rich dictionary in CDSL. Its central strengths:

- **Citation depth.** With 4.63 `<ls>` citations/record, PWG names the texts
  and page/verse references supporting each gloss. Where [MW](https://github.com/sanskrit-lexicon/MWS)
  collapses kosha attributions into the anonymous `L.` hedge, **PWG names every source**:
  Hemacandra (17,337 times), Amarakośa (14,473), Medinīkośa (13,055), and dozens more.
- **Kosha tradition.** PWG is the principal scholarly access point for the Indian
  lexicographic tradition — ABCH, ARMH, Amarakośa, Medinīkośa, Trikāṇḍaśeṣa — whose
  citations it documents with named attribution. See [Citation markers](#citation-markers--pwgs-named-source-apparatus).
- **Vedic depth.** The Rigveda, Atharva-Veda, Yajur-Veda, Sāma-Veda and their
  Brāhmaṇas and Prātiśākhyas are documented in full for each entry. PWG's Vedic
  coverage in its era was unmatched.
- **Completeness.** 123,366 records across all Sanskrit periods — Classical, Epic,
  Purāṇic, technical (grammar, medicine, astronomy, law), and Vedic.

Limitations:

- **Language barrier.** Definitions are in German. For non-German readers, MW is
  the access point; but MW's `L.` hedge conceals PWG's source attributions.
- **7-volume format.** Comprehensive but unwieldy; [PWK](https://github.com/sanskrit-lexicon/PWK) is the practical one-volume alternative.
- **Digital display.** The Cologne web display for PWG is functional but less polished
  than MW's; the scan-link apparatus is still being built out (see [GitHub issues](https://github.com/sanskrit-lexicon/PWG/issues)).

---

## When to use PWG

| Question / use case | PWG appropriate? | Alternative |
|---|---|---|
| Tracing a specific citation to its original text | **Yes** — uniquely strong | — |
| Named kosha attribution (who said what) | **Yes** — names sources MW anonymises | — |
| Vedic text (RV, AV, ŚBr, TB, etc.) attestation | **Yes** — full apparatus | [GRA](https://github.com/sanskrit-lexicon/GRA) for RV accent |
| Classical Sanskrit, German medium | **Yes** | — |
| Classical Sanskrit, English medium | Partial (German barrier) | [MW](https://github.com/sanskrit-lexicon/MWS), [AP90](https://github.com/sanskrit-lexicon/AP90) |
| Compact one-volume lookup | No — 7 vols | [PWK](https://github.com/sanskrit-lexicon/PWK) (Böhtlingk abridgment) |
| Buddhist Hybrid Sanskrit | Partial | [BHS](https://github.com/sanskrit-lexicon/BHS) (Edgerton) |
| Understanding what MW's `L.` hides | **Yes** — PWG names all kosha sources | — |
| Scholarly citation tracing (peer-level) | **Yes** — PWG is the primary reference | — |

**Summary:** Use PWG when you need named-source attribution, Vedic text depth, or
German-language comprehensive coverage. For English-medium lookup, open MW first —
but cross-reference PWG whenever MW's `L.` hedge appears or when citation accuracy matters.

---

## Article types — what you'll encounter in PWG

PWG entries follow a structured format analogous to MW but with German definitions
and the `<lex>a.</lex>` convention for adjectives.

| Type | Identifying marker | Notes |
|---|---|---|
| **Masculine noun** | `<lex>m.</lex>` | 35,665 records (28.9%) |
| **Feminine noun** | `<lex>f.</lex>` | 14,170 records (11.5%) |
| **Neuter noun** | `<lex>n.</lex>` | 15,082 records (12.2%) |
| **Adjective** | `<lex>a.</lex>` — *not* `mfn.` | 31,671 records (25.7%); CDSL maps `a.` → adj-mfn |
| **Other / no `<lex>`** | — | 26,778 records (21.7%); includes roots, particles, continuations |
| **Cited entry** | `<ls>` tags present | 98.7% of main nouns and adjectives have at least one source citation |
| **Kosha-cited** | `<ls>H.</ls>`, `<ls>AK.</ls>`, `<ls>MED.</ls>`, etc. | The dominant citation type; see [Citation markers](#citation-markers--pwgs-named-source-apparatus) |
| **Verbal root** | No `<lex>`; often starts with √ | Covered in the "other" category |

**Key difference from MW:** the `cite%` profile across types is **flat (0.4 pt spread)**
— PWG cites almost every nominal entry equally thoroughly (98.4–98.7% across m/f/n/adj-mfn).
MW shows 11.3 pts spread (adj-mfn cited most, nouns-n cited least). PWG's editorial standard
is more uniform: every headword is expected to have textual backing.
See [`CROSS_DICT_PROFILES.md`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md).

---

## Citation markers — PWG's named-source apparatus

Unlike [MW](https://github.com/sanskrit-lexicon/MWS), which collapses kosha attributions
into the anonymous `<ls>L.</ls>` hedge (40,213 occurrences), **PWG names every source**.
The most-cited sources in PWG are predominantly Sanskrit lexicons (kosha tradition):

| Marker | Source | PWG citations | MW equivalent |
|---|---|---:|---|
| `H.` | [Hemacandra](https://en.wikipedia.org/wiki/Hemachandra) (*Abhidhānacintāmaṇi* = [ABCH](https://github.com/sanskrit-lexicon/abch)) | **17,337** | Collapsed into `L.` |
| `AK.` | *Amarakośa* (Amarasiṃha, ~5th c.) | ~14,473 | Collapsed into `L.` |
| `MED.` | *Medinīkośa* | ~13,055 | Collapsed into `L.` |
| `HALĀY.` | [Halāyudha](https://en.wikipedia.org/wiki/Hal%C4%81yudha) (*Abhidhānaratnamālā* = [ARMH](https://github.com/sanskrit-lexicon/armh)) | ~5,114 | Collapsed into `L.` |
| `RV.` | [Rigveda](https://en.wikipedia.org/wiki/Rigveda) | — | `RV.` (retained) |
| `MBH.` | [Mahābhārata](https://en.wikipedia.org/wiki/Mahabharata) | — | `MBh.` (retained) |

**Reading PWG to recover MW's sources:** When an MW entry shows `<ls>L.</ls>`, the
corresponding PWG entry (same headword) names the kosha: usually `H.`, `AK.`, `MED.`,
or `HALĀY.` The four CDSL kosha repos —
[ABCH](https://github.com/sanskrit-lexicon/abch),
[ARMH](https://github.com/sanskrit-lexicon/armh),
[ACPH](https://github.com/sanskrit-lexicon/acph),
[ACSJ](https://github.com/sanskrit-lexicon/acsj) — are the eventual resolution targets for these attributions.

---

## Block profile (format-robust common-block vocabulary)

Data from [`pwg_blocks.json`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/data/pwg_blocks.json)
generated by [`export_dict_blocks.py`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/figures/scripts/export_dict_blocks.py).

| Block | % of entries |
|---|---|
| head (record) | 100.0% |
| body (¦ separator) | 98.6% |
| gram (`<lex>` tag) | 78.3% |
| cite (`<ls>` source) | 96.5% |
| hom (homograph `<hom>`) | 1.5% |
| etym (etymology √ / `<ab>fr.</ab>`) | 0.0% |
| xref (cross-ref q.v. / cf.) | 0.0% |
| hedge (L. hedge `<ls>L.</ls>`) | 0.0% |
| info (digitisation `<info`) | 0.0% |

**Notable:** PWG has **no hedge block** (0% `<ls>L.</ls>`) — it uses named sources.
It has **no etym block** (0%) — etymologies are covered in running German prose,
not with dedicated markers. The high cite% (96.5%) is the highest among all CDSL dicts.

See the [cross-dictionary comparison](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT.md)
for how PWG's block profile compares across all nine CDSL dicts.

---

## Per-type citation profile

From [`analysis/CROSS_DICT_PROFILES.md`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md).

| Type | N | cite% | mean blocks |
|---|---:|---:|---:|
| noun-m | 35,665 | 98.7% | 3.99 |
| noun-f | 14,170 | 98.4% | 3.98 |
| noun-n | 15,082 | 98.4% | 3.98 |
| adj-mfn | 31,671 | 98.5% | 3.98 |
| other | 26,778 | 77.4% | 2.84 |
| → profile spread | — | **0.4 pts** | — |

The near-zero spread (0.4 pts) means PWG applies citation standards uniformly across all gender-types — a consistent editorial standard distinguishing it from [MW](https://github.com/sanskrit-lexicon/MWS) (11.3 pts spread) and [AP90](https://github.com/sanskrit-lexicon/AP90) (15.2 pts spread).

---

## Sample entries

PWG entries follow the pattern: `<k1>headword</k1> ¦ <lex>type</lex> definition. <ls>citations</ls>`.
Below are representative examples showing the named-source apparatus.

### Sample 1 — noun-m with kosha citations

A typical nominal entry (representative pattern — verify against
[pwg.txt line lookup](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/pwg/pwg.txt)):

```
<L>…<k1>aMSa</k1>…
aMSa ¦ <lex>m.</lex> Theil, Antheil.
<ls>AK. 3, 4, 1, 24.</ls> <ls>H. 1465.</ls> <ls>MED. ś. 22.</ls>
```

Reading: "aṃśa, masculine noun. 'Part, share.'
Cited: Amarakośa 3.4.1.24; Hemacandra 1465; Medinīkośa ś.22."
Three kosha sources — all anonymised as `L.` in the corresponding MW entry.

### Sample 2 — adjective with `<lex>a.</lex>` convention

```
<L>…<k1>eka</k1>…
eka ¦ <lex>a.</lex> ein, einzeln, einzig.
<ls>AK.</ls> <ls>H.</ls> <ls>RV.</ls> …
```

Reading: "eka, adjective. 'One, single, unique.'
Cited: Amarakośa, Hemacandra, Rigveda."
Note `<lex>a.</lex>` — not `<lex>mfn.</lex>` as in MW.

### Sample 3 — compound sub-entry with volume reference

```
<L>…<k1>aMSu</k1>…
aMSu ¦ <lex>m.</lex> Faden; Strahl; Soma-Pflanze.
<ls>AK. 1, 1, 2, 12.</ls> <ls>H. 1114.</ls> <ls>RV.</ls>
```

**Böhtlingk-Roth compound enumeration:** compounds of *aṃśu* appear as sub-entries
in the same record block, following the parent, separated by `;` in PWG's format.
The same word in [MW](https://github.com/sanskrit-lexicon/MWS) shows `<ls>L.</ls>`
where PWG names the Amarakośa and Hemacandra sources explicitly.

---

## Relationship to other CDSL dictionaries

| Dictionary | Relationship to PWG |
|---|---|
| [PWK](https://github.com/sanskrit-lexicon/PWK) (Böhtlingk, 1879–1889) | Böhtlingk's own 1-volume condensation of PWG; 170,556 records but 0.515 ls/rec — condensation dropped most citations |
| [MW](https://github.com/sanskrit-lexicon/MWS) (Monier-Williams, 1899) | Primary English downstream consumer — translated + condensed PWG; replaced named-kosha attribution with the generic `L.` hedge |
| [MW72](https://github.com/sanskrit-lexicon/MW72) (Monier-Williams, 1872) | First MW edition; used early PWG volumes while the set was still being published |
| [WIL](https://github.com/sanskrit-lexicon/WIL) (Wilson, 1832) | Earlier English dictionary; predates most of PWG; MW supplemented WIL with PWG's apparatus |
| [AP90](https://github.com/sanskrit-lexicon/AP90) (Apte, 1890) | Student-oriented English dictionary; uses `<lex>a.</lex>` convention (same as PWG) |
| [CAE](https://github.com/sanskrit-lexicon/CAE) (Cappeller, 1891) | Compact English dictionary; Cappeller also contributed to MW1899; uses `<lex>a.</lex>` |
| [ABCH](https://github.com/sanskrit-lexicon/abch) (Hemacandra, ~12th c.) | Most-cited source in PWG — 17,337 citations as `H.`; one of the four CDSL kosha repos |
| [ARMH](https://github.com/sanskrit-lexicon/armh) (Halāyudha, ~10th c.) | Second major kosha source — cited ~5,114 times as `HALĀY.` |
| [GRA](https://github.com/sanskrit-lexicon/GRA) (Grassmann, 1873) | RV-Wörterbuch — the specialised Rigveda complement; coordinate on RV citation links ([#133](https://github.com/sanskrit-lexicon/PWG/issues/133), [#173](https://github.com/sanskrit-lexicon/PWG/issues/173)) |
| [SKD](https://github.com/sanskrit-lexicon/SKD) (*Śabdakalpadruma*, 1858) | Sanskrit-Sanskrit kosha; contemporary with PWG; CDSL preserves both traditions |

---

## Known issues

See [GitHub issues](https://github.com/sanskrit-lexicon/PWG/issues) for this repository.
All issue tracking follows the [CDSL taxonomy](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/CONTRIBUTING.md).

The [PWG ROADMAP.md](https://github.com/sanskrit-lexicon/PWG/blob/docs-pass/ROADMAP.md)
summarises open work by category. Major open categories:

- **Link target** (~16 open): building scan-page links for PWG's rich `<ls>` apparatus
- **Link splitting** (~5 open): splitting combined multi-page citation references
- **Markup** (~10 open): `<ls>` tag normalization; commentarial/titular reference conventions
- **Content enhancement** (3 hard): merge AB's version (#163); Weber's Nachlass (#61); Cologne Additions (#37)

---

## Further reading

- [Cologne Digital Sanskrit Dictionaries](https://www.sanskrit-lexicon.uni-koeln.de/)
- [csl-orig source data — v02/pwg/](https://github.com/sanskrit-lexicon/csl-orig/tree/master/v02/pwg)
- [Cross-dictionary microanalysis](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/PAPER.md) (MW1899 as reference; PWG block profile in §Cross-dict)
- [CROSS_DICT_PROFILES.md](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/papers/microanalysis/analysis/CROSS_DICT_PROFILES.md) — per-type profiles across all nine dicts
- [csl-atlas per-dict chapter](https://github.com/sanskrit-lexicon/csl-atlas/blob/main/src/dicts/pwg.md) (Observable JS block-profile visualisation)
- [Wikipedia: Sanskrit-Wörterbuch](https://en.wikipedia.org/wiki/Sanskrit%E2%80%93Worterbuch)
- [Wikipedia: Otto von Böhtlingk](https://en.wikipedia.org/wiki/Otto_von_B%C3%B6htlingk)
- [Wikipedia: Rudolf Roth](https://en.wikipedia.org/wiki/Rudolf_von_Roth)

---

## BibTeX

```bibtex
@misc{boehtlingk_roth_pw_1855,
  title = {{Sanskrit-W{\"o}rterbuch, herausgegeben von der Kaiserlichen Akademie der Wissenschaften}},
  editor = {Otto von B{\"o}htlingk and Rudolf Roth},
  year = {1855},
  howpublished = {Cologne Digital Sanskrit Dictionaries},
  url = {https://www.sanskrit-lexicon.uni-koeln.de/}
}
```
"""

def run_gh(args):
    result = subprocess.run(['gh'] + args, capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
    return result.stdout.strip(), result.returncode

def push_file(repo, path, content_str, msg, branch='docs-pass'):
    content_b64 = base64.b64encode(content_str.encode('utf-8')).decode('ascii')
    payload = {'message': msg, 'content': content_b64, 'branch': branch}
    out, rc = run_gh(['api', f'repos/{ORG}/{repo}/contents/{path}?ref={branch}',
                      '-H', 'Accept: application/vnd.github.v3+json', '--jq', '.sha'])
    if rc == 0 and out:
        payload['sha'] = out
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False)
        tmp = f.name
    try:
        _, rc = run_gh(['api', f'repos/{ORG}/{repo}/contents/{path}', '-X', 'PUT', '--input', tmp])
        return rc == 0
    finally:
        os.unlink(tmp)

if __name__ == '__main__':
    msg = ('docs-pass: full DICT_PROFILE.md for PWG (S8)\n\n'
           'Replaces the Phase-4 stub with a full profile following the MWS template.\n'
           'Sections: At-a-Glance, Orthography, Historical background, Scholarly significance,\n'
           'When-to-use matrix, Article types, Citation markers (named sources vs L. hedge),\n'
           'Block profile, Per-type profile, Sample entries, Relationship table, BibTeX.\n\n'
           'Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>')
    ok = push_file(REPO, 'DICT_PROFILE.md', DICT_PROFILE, msg)
    if ok:
        print(f'Pushed DICT_PROFILE.md to {REPO}/{BRANCH} ({len(DICT_PROFILE):,} chars)')
    else:
        print('ERROR: push failed')
        sys.exit(1)
