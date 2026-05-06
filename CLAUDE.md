# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MWS is a corrections and enhancements repository for the Cologne digitization of Monier Monier-Williams' *A Sanskrit-English Dictionary* (1899). The canonical source data lives in the companion repository `csl-orig/v02/mw/mw.txt`. This repo holds tooling, issue-specific correction workflows, and derived files.

The assumed local directory layout:
```
/c/xampp/htdocs/sanskrit-lexicon/
  MWS/          ← this repo
cologne/
  csl-orig/     ← source data repo (mw.txt lives here)
  csl-pywork/   ← build tools (generate_dict.sh, xmlchk_xampp.sh)
```

## Data Format

The primary data file (`mw.txt`) uses **SLP1 encoding** for Sanskrit, wrapped in custom XML-like tags:

```
<L>103697<pc>527,2<k1>napAtka<k2>napAtka<e>2
<s>napAtka</s> ¦ <lex>mfn.</lex> ...<info lex="m:f:n"/>
<LEND>
```

- `<L>` — record number (can be decimal like `116525.7`)
- `<pc>` — page,column in the 1899 print edition
- `<k1>` — headword key1 in SLP1
- `<k2>` — headword key2 in SLP1 (may include accent marks)
- `<e>` — hierarchy code
- `<s>...</s>` — Sanskrit text spans (transcoded by tooling)
- `<LEND>` — end of record

## Common Commands

### Transcoding (`mwtranscode/`)

Convert `mw.txt` (SLP1) to IAST or Devanagari:
```bash
python mw_transcode.py slp1 roman mw.txt mw_iast.txt
python mw_transcode.py slp1 deva  mw.txt mw_deva.txt
```

Verify invertibility (round-trip back to SLP1):
```bash
python mw_transcode.py roman slp1 mw_iast.txt temp_mw_slp1.txt
diff mw.txt temp_mw_slp1.txt
```

### Homophone pipeline (`homophone/pywork/`)

Sequential steps starting from a local copy of `monier.xml`:
```bash
python removeHom.py monier.xml monier_pg2.xml
python hierMod.py   monier_pg2.xml monier_pg2a.xml
python extract_keys.py   monier.xml extract_keys.txt
python extract_keys_a.py extract_keys.txt extract_keys_a.txt
python extract_keys_b.py extract_keys_a.txt extract_keys_b.txt
python newHom.py extract_keys_b.txt monier_pg2a.xml mod_hom.txt monier_pg3.xml > newHom_log.txt
```

### Rebuild & validate XML (run from `csl-pywork/v02/`)

After editing `mw.txt`, copy it into place, regenerate, and check:
```bash
cp temp_mw_N.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
```

### Auxiliary extraction tools

```bash
# Bot/bio tag extraction (from botbio/)
python tagunique.py bot ../../../cologne/csl-orig/v02/mw/mw.txt mw_bot.txt
python tagunique.py bio ../../../cologne/csl-orig/v02/mw/mw.txt mw_bio.txt

# Verb parsing pipeline (from mwverbs/)
python mwverb.py mw ../../../../cologne/csl-orig/v02/mw/mw.txt mwverbs.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
python mwverbs2.py mwverbs1.txt mwverbs2.txt
```

### History — cp1252 to UTF-8 conversion (`history/`)

```bash
python cp1252-to-utf8.py MONIER.ALL mw_orig_utf8.txt
```

## Issue Correction Workflow

Each `mwsissues/issueNNN/` directory follows this pattern:

1. Copy the current `mw.txt` to a local `temp_mw_0.txt` (not tracked by git)
2. Apply corrections incrementally as `temp_mw_1.txt`, `temp_mw_2.txt`, etc.
3. Rebuild XML and validate with `generate_dict.sh` + `xmlchk_xampp.sh`
4. Commit the corrected file to `csl-orig`, then sync to Cologne
5. Commit the issue documentation files back to this repo

The `readme.txt` / `readme2.txt` / `readme3.txt` files in each issue folder record the exact diff/correction steps and the case-by-case rationale.

## Transcoder

Transcoding rules are XML files in `mwtranscode/transcoder/`:
- `slp1_roman.xml` — SLP1 → IAST
- `roman_slp1.xml` — IAST → SLP1
- `slp1_deva.xml` / `deva_slp1.xml` — SLP1 ↔ Devanagari
- Also: `hk`, `itrans`, `wx`, `as` variants

Three known non-invertible words exist in the SLP1→IAST→SLP1 round-trip (documented in `mwtranscode/readme.txt`).

## Related Repositories

- **csl-orig** — canonical source data (`mw.txt` and other dict sources)
- **csl-pywork** — build system (`generate_dict.sh`, `xmlchk_xampp.sh`, display generation)
- **csl-corrections** — cross-dictionary corrections tracker (GitHub issues referenced from MWS issues)
