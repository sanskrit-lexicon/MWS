@funderburkjim @Andhrabharati — please review the `docs-pass` branch.
All Track B content has been researched and written (no `[DRAFT]` placeholders remain).

Branch: [`docs-pass`](https://github.com/sanskrit-lexicon/MWS/tree/docs-pass) of `MWS`.

Part of the org-wide docs-pass for ~73 sanskrit-lexicon repos.

---

## Docs-pass: MWS (Dictionary)

### Track A — added / extended (mechanical)

| File | Action | Notes |
|---|---|---|
| `DATA_DICTIONARY.md` | extended | Tag counts from 2026-05 markup-fix audit; `<INFER/>`/`<UNMARKED>` abbreviation taxonomy; `<lex>` vs `<ab>` list; `<ab n="…">` note |
| `CONTRIBUTING.md` | rewritten | Issue template guide; label taxonomy; multi-step correction workflow |
| `CITATION.cff` | rewritten | Full title; 1899/2020 dates; Leumann + Cappeller collaborators; entry count; abstract |
| `.github/ISSUE_TEMPLATE/` | skipped | Directory already populated (7 templates exist) |

### Track B — added (verify facts, then merge)

| File | Status | What to verify |
|---|---|---|
| [`DICT_PROFILE.md`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/DICT_PROFILE.md) | Complete | Historical facts (Boden chair, Leumann/Cappeller, 1872/1899 editions); when-to-use verdicts |
| [`ENTRY_GUIDE.md`](https://github.com/sanskrit-lexicon/MWS/blob/docs-pass/ENTRY_GUIDE.md) | Complete | Sample entry annotations (L9, L10, L57); tag counts (from markup-fix audit) |

### Research performed (Track B)

- **DICT_PROFILE.md:** Wikipedia on Monier-Williams biography + Boden chair + Müller
  controversy; 1872 vs 1899 edition details; Leumann + Cappeller collaboration;
  ~1,333-page folio; PWG origin story; when-to-use matrix (Classical/Vedic/BHS/IE);
  three sample entries annotated; BibTeX with collaborators.
- **ENTRY_GUIDE.md:** Verified sample entries L9/L10/L57 in `csl-orig/v02/mw/mw.txt`;
  confirmed L10's 9 sub-entries (L11–L19); confirmed L47 as parent of L57 compound;
  tag counts pulled from markup-fix audit; abbreviation taxonomy from `mwab_input.txt`;
  mwauthorities system documented.

### Reviewer checklist

- [ ] `DICT_PROFILE.md` historical facts correct
- [ ] `DICT_PROFILE.md` when-to-use verdicts accurate
- [ ] `ENTRY_GUIDE.md` sample entry annotations correct
- [ ] `ENTRY_GUIDE.md` mwauthorities section accurate
- [ ] `CITATION.cff` fields verified (entry count, date-released, editors)
- [ ] `CONTRIBUTING.md` correction workflow accurate for your local setup
- [ ] Branch merged to master
