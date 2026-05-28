{% raw %}
# Contributing to MWS

MWS is a corrections and enhancements repository for the Cologne digitisation of
Monier-Williams' *Sanskrit-English Dictionary* (1899 edition). Contributions
fall into two tracks: **reporting issues** and **submitting corrections** (PRs).

---

## Before opening an issue

1. **Search existing issues** — many patterns recur (abbreviation inconsistencies,
   `<ls>` tag pairs, compound-entry hierarchy). Check closed issues too.
2. **Check the print** — confirm the digitised text diverges from the 1899 Clarendon
   print before reporting. The [Internet Archive facsimile](https://archive.org/details/sanskritenglish00moniuoft) is the canonical reference.
3. **Check the markup-fix-audit** — `mwissues/markup_fix/markup_audit.txt` lists
   known systematic issues and their dispositions (auto-fixed, intentional, etc.).
4. **Check the web display** — the [CDSL browser](https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/index.php)
   renders the current `mw.txt`; some apparent errors are display-time artefacts,
   not data-file errors.

---

## Issue templates

Use the GitHub issue form — it selects the right template and labels automatically.

| Template | Use when | Labels applied |
|---|---|---|
| **Bug** | Broken link, malformed XML, broken download | `bug` + severity |
| **Encoding issue** | SLP1 / IAST / Devanagari transcoding error; character corruption; round-trip loss | `encoding` + severity |
| **Link target** | A `<ls>` literary-source citation that should link to a scanned PDF of the cited edition | `link-target` + `medium` |
| **Markup issue** | Wrong or missing XML tag (`<ls>`, `<lex>`, `<ab>`, etc.); structural correction | `markup` + severity |
| **Scholarly question** | Editorial question requiring research before any code change; print-edition ambiguity | `question` + `minor` |
| **Text correction** | Typo, wrong gloss, or other text-level error in an entry | `text-correction` + severity |

### Severity labels

| Label | Scope |
|---|---|
| `minor` | Single entry or character |
| `medium` | Batch of similar errors; one tag class across a section |
| `hard` | Structural change spanning many entries or multiple dictionaries |

### Cross-repo questions

For project-wide questions that span multiple dictionaries, open an issue in
[COLOGNE](https://github.com/sanskrit-lexicon/COLOGNE/issues) instead of here.

---

## Submitting a correction (pull request)

MWS corrections follow a multi-step validation workflow — the dictionary rebuilds
and XML-checks on every round of edits.

### Local setup

```bash
export BASE=/c/xampp/htdocs   # adjust to your installation
# Expected layout:
# $BASE/sanskrit-lexicon/MWS/       ← this repo
# $BASE/cologne/csl-orig/           ← canonical source (mw.txt lives here)
# $BASE/cologne/csl-pywork/         ← build tools
```

### Correction workflow (per issue)

Each `mwissues/issueNNN/` (or `mwsissues/issueNNN/`) directory follows this pattern:

1. **Copy** current `mw.txt` to a local `temp_mw_0.txt` (not tracked by git — add to `.gitignore` if needed).
2. **Apply** corrections incrementally: `temp_mw_1.txt`, `temp_mw_2.txt`, etc. `N` increments with each round.
3. **Rebuild and validate XML** after each round:

   ```bash
   cp temp_mw_N.txt $BASE/cologne/csl-orig/v02/mw/mw.txt
   cd $BASE/cologne/csl-pywork/v02
   sh generate_dict.sh mw  ../../mw
   sh xmlchk_xampp.sh mw
   ```

4. **Document** the rationale for each correction in `readme.txt` / `readme2.txt`
   within the issue folder. Reference the print page and column.
5. **Commit** the corrected file to `csl-orig`, then sync to the Cologne server.
6. **Commit** the issue documentation files back to this repo and close the tracking
   issue with a link to the `csl-orig` commit.

### In-file correction records

If the source file (`mw.txt`) itself records the correction history, the format is:

```
{{old text -> new text || YYYY-MM-DD | author | URL |}}
```

These records are preserved verbatim and processed by the `updateByLine.py`
toolchain — never edit them by hand.

### GitHub Pages / Jekyll Liquid gotcha

GitHub Pages renders this repo's Markdown through Jekyll. Jekyll's Liquid
templating engine treats two CDSL markup conventions as template syntax:

- `{%…%}` — the italic-span marker; collides with Liquid tag syntax.
- `{{…}}` — the correction-record format above; collides with Liquid
  variable interpolation.

A page containing either marker outside an escape block breaks the Pages
build. The fix applied across this repo is to wrap the entire affected
file in `{% raw %}` and the matching closing tag. See
[DATA_DICTIONARY.md](DATA_DICTIONARY.md), [ENTRY_GUIDE.md](ENTRY_GUIDE.md),
[DICT_PROFILE.md](DICT_PROFILE.md) and the `papers/microanalysis/` notes
for working examples (PRs [#198](https://github.com/sanskrit-lexicon/MWS/pull/198), [#200](https://github.com/sanskrit-lexicon/MWS/pull/200), [#201](https://github.com/sanskrit-lexicon/MWS/pull/201)).

When adding a new `.md` documenting `<L>` records, markup conventions, or
sample entry text — wrap it.

### Pull request checklist

- [ ] Correction verified against the 1899 print facsimile
- [ ] `generate_dict.sh` + `xmlchk_xampp.sh` pass with no new errors
- [ ] `readme.txt` in the issue folder documents the rationale
- [ ] No unrelated changes mixed into the PR
- [ ] Issue number referenced in the PR title or body

---

## Project organisation

MWS uses GitHub **Projects 5–8** (not 1–4 — those were taken when MWS was
onboarded). The label + milestone taxonomy is otherwise identical to the CDSL
org standard — see [COLOGNE/CLAUDE.md](https://github.com/sanskrit-lexicon/COLOGNE)
for the org-wide taxonomy.

---

## Code of conduct

All contributors are expected to follow the
[CDSL Code of Conduct](CODE_OF_CONDUCT.md).
{% endraw %}
