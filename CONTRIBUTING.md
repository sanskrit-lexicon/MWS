# Contributing

Thank you for considering a contribution to a Cologne Digital Sanskrit Dictionaries (CDSL) repository. This file is templated across all CDSL dictionary repositories; project-specific guidance is in `CLAUDE.md`.

## How to contribute

### Reporting an error or improvement (issues)

Use one of the issue templates in `.github/ISSUE_TEMPLATE/` when opening a new issue. Templates exist for:

- **`text-correction`** — typo, missing word, wrong gloss
- **`markup`** — XML tag content or structure
- **`link-target`** — citation that should link to a scanned PDF
- **`encoding`** — SLP1/IAST transcoding, character rendering
- **`bug`** — broken link, malformed XML, broken download
- **`question`** — scholarly or editorial question

The issue tracker uses the unified taxonomy described at the org level (see [`csl-observatory`](https://github.com/sanskrit-lexicon/csl-observatory)). A maintainer will assign one **type label**, one **severity label**, and one **milestone** when triaging.

### Submitting a correction (pull request)

For text or markup corrections to dictionary data, use the `change_*.txt` + `updateByLine.py` pattern documented in `CLAUDE.md`:

```sh
python updateByLine.py <input.txt> <change_NNN.txt> <output.txt>
```

The `change_NNN.txt` file is paired-line format:

```
1234 old original text here
1234 new corrected text here
```

Please attach the change file to your pull request and describe the **why** of the correction (which print edition, which page, which authority).

### Identifying yourself

If you have a GitHub account, your commits will be attributed automatically. We track real names, ORCIDs, and roles in [`csl-observatory/scripts/contributors_map.json`](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/scripts/contributors_map.json) — please open a PR there with your real name, affiliation, and (optionally) ORCID once you have made a non-trivial contribution.

## Style

- All source files are **UTF-8 NFC**.
- Sanskrit text in entries is **SLP1** (in `{#…#}` blocks); display layer uses IAST.
- Commit messages: imperative mood, reference an issue number in the form `#NNN`.
- Keep changes small and focused; one issue per pull request where practical.

## Code of Conduct

By contributing you agree to abide by the [Contributor Covenant 2.1](CODE_OF_CONDUCT.md).

## Licence

By contributing you agree your contributions will be licensed under the same terms as the repository: **CC BY-SA 4.0** for dictionary data, **GPL-3.0** for code.
