# Security policy

This repository contains scholarly text data and tooling, not user-facing services with authentication. The principal security concerns are:

1. **Supply-chain risk** in the Python and Node.js tooling we run during corrections.
2. **Integrity of the dictionary data** — unauthorised commits introducing falsified entries.
3. **Credential leakage** in committed files (API tokens, SSH keys).

## Reporting a vulnerability

Please do **not** open a public GitHub issue for security-sensitive reports. Instead:

- Email the maintainers via the address listed in the project README, or
- Contact `@gasyoun`, `@funderburkjim`, or `@drdhaval2785` directly via GitHub.

We will acknowledge within five working days and triage privately.

## Out of scope

- Bug reports about display rendering, broken links, or character-encoding glitches in dictionary entries — please use the regular issue tracker with the appropriate type label.
- Concerns about dictionary content (typos, mistranslations, scholarly disagreement) — these are *editorial* matters, not security; please open a normal `text-correction` or `question` issue.

## Licence

This security policy itself is licensed CC BY 4.0.
