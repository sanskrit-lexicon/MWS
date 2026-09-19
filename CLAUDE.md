# CLAUDE.md

_Created: 06-05-2026 · Last updated: 12-09-2026_

This repo is **MWS**, the correction, enhancement, and tooling layer for the
Cologne digitisation of Monier-Williams, *A Sanskrit-English Dictionary* (1899).
Canonical digitised source is
`csl-orig/v02/mw/mw.txt`
(SLP1), a sibling checkout on this machine (`../csl-orig/v02/mw/mw.txt`).
Generated XML (`mw.xml` / `monier.xml`) is a
[csl-pywork](https://github.com/sanskrit-lexicon/csl-pywork) build product of
`generate_dict.sh mw`, not a committed sibling `mwsxml` repo (that path does
not exist).

Operator manual:
[docs/PIPELINE_MANUAL.md](https://github.com/sanskrit-lexicon/MWS/blob/master/docs/PIPELINE_MANUAL.md).
Tag reference: [DATA_DICTIONARY.md](https://github.com/sanskrit-lexicon/MWS/blob/master/DATA_DICTIONARY.md).

**Projects 5–8** (not 1–4) — 1–4 were already taken when MWS was onboarded.
Taxonomy itself is the org standard.

## How to run

Transcode (`mwtranscode/`):

```sh
python mw_transcode.py slp1 roman mw.txt mw_iast.txt
python mw_transcode.py slp1 deva  mw.txt mw_deva.txt
```

Rebuild + validate after a correction (from `csl-pywork/v02/`; do **not**
write the result back to csl-orig):

```sh
sh generate_dict.sh mw ../../mw
sh xmlchk_xampp.sh mw
```

On Windows without `xmllint`, the build's assembled
`<outdir>/pywork/make_xml.py` printing
`All records parsed by ET` is the validate signal.

Issue folders under `mwsissues/issueNNN/` snapshot `mw.txt` to
`temp_mw_0.txt`, apply change files incrementally, then validate. Commit
documentation back **here**. Park a validated source change with
[`/cologne-correction-queue`](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-correction-queue.md);
do not push csl-orig. Full sequence:
[csl-corrections/docs/correction-workflow.md](https://github.com/sanskrit-lexicon/csl-corrections/blob/main/docs/correction-workflow.md).

`updateByLine.py` change-file format: paired `NNN old` / `NNN new` lines,
UTF-8, no BOM. Canonical copies travel with issue dirs (for example
[mwsissues/issue182/updateByLine.py](https://github.com/sanskrit-lexicon/MWS/blob/master/mwsissues/issue182/updateByLine.py))
and [mwtranscode/revdoc/updateByLine.py](https://github.com/sanskrit-lexicon/MWS/blob/master/mwtranscode/revdoc/updateByLine.py).

Homophone `extract_keys*.py` live in
[homophone/pywork/pykeysxml/](https://github.com/sanskrit-lexicon/MWS/tree/master/homophone/pywork/pykeysxml);
that workspace is frozen (see the operator manual).

## Do not

- Commit or push [csl-orig](https://github.com/sanskrit-lexicon/csl-orig).
- Invent a sibling `../mwsxml/mws.xml` checkout — generated XML comes from
  csl-pywork.
- Assign MWS issues to projects 1–4.
- Recopy the org label/milestone tables into this file.

## Primer

[SANSKRIT_CONTEXT_PRIMER.md](https://github.com/gasyoun/github-spine/blob/main/SANSKRIT_CONTEXT_PRIMER.md).

Issues use the Cologne taxonomy — see
[`/cologne-issue-runbook`](https://github.com/gasyoun/claude-config/blob/main/commands/cologne-issue-runbook.md).

_Dr. Mārcis Gasūns_
