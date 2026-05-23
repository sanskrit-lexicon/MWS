# Decisions — csl-atlas interactive microsite

Covers decisions **2**, **7**, **10**, **20**, **24**, **27**. See [decisions/README.md](README.md) for the full index.

---

## Decision 2 — Build both static (paper) and interactive (microsite)

**Both deliverables.** Static SVG figures (embeddable in the IJL paper) plus an interactive microsite (HTML, linked from the paper as supplementary materials).

The microsite lets reviewers:
- Explore the 18×14 matrix interactively (hover for percentages + counts).
- Filter the treemap by article type.
- Trace any `<ls>` source to the entries citing it.
- Compare two article types side-by-side.

Tier 1 figures (heatmap, Sankey, timeline, treemap) are produced **twice**: once as static SVG with embedded palette, once as interactive HTML/JS.

Data binding: JSON files in `papers/microanalysis/figures/data/` consumed by both the static renderer (Python) and the interactive renderer (D3 / Plot / Vega-Lite).

## Decision 7 — Hosting: new repo `csl-atlas`

The microsite lives in a new repo, **`csl-atlas`** under the `sanskrit-lexicon` org, rather than embedded in MWS. Rationale:

- Covers multiple CDSL dictionaries (9 in Phase 4) — natural to give it its own home.
- Hosted on GitHub Pages: `https://sanskrit-lexicon.github.io/csl-atlas/`.
- Pulls JSON data from per-dict `mw_block_matrix.py`-equivalent scripts.
- Versioned independently from any single dict's docs-pass.
- Clean separation: **MWS holds the static paper + data scripts; csl-atlas holds the live web app.**

## Decision 10 — Stack: Observable Framework

[Observable Framework](https://observablehq.com/framework). Rationale:
- Built-in i18n routing (matches per-locale-file strategy from [I18N.md](I18N.md)).
- Reactive data + D3 + Markdown pages out of the box.
- Static output (HTML/JS) deployable to GitHub Pages.
- First-class declarative data files (JSON/CSV) → matches our JSON-data architecture.
- Polished research-microsite aesthetic.

**[DOUBTS.md D8](../DOUBTS.md#d8--observable-framework-is-heavy-infrastructure-for-a-research-microsite--blocking) — RESOLVED 2026-05-23: keep Observable Framework.** The lock-in / build-pipeline trade-offs are accepted in exchange for built-in i18n routing, reactive D3/Plot, and Markdown pages. The vanilla-HTML+D3 alternative is *not* adopted. Mitigations become implementation notes: pin the Framework version, keep the static SVG/PNG figures independent of the framework (the paper does not depend on it), and reserve Observable for the interactive tools.

## Decision 20 — Navigation: hybrid (paper-tours + standalone tools)

Observable Framework `src/` structure:

```
csl-atlas/
  src/
    index.md                         landing page
    paper/                           paper-tour section (single consolidated paper)
      grounded.md                    body: five constructs + block economy
      triangulation.md               §7 — three frameworks converge
      appendices.md                  A Wiegand · B Atkins-Rundell · C Hausmann
    tools/                           standalone visualisation tools
      matrix-explorer.md             18×14 heatmap, interactive
      lineage-sankey.md              PWG→MW Sankey
      typology-treemap.md            article-type treemap
      timeline.md                    lexicographic timeline
      type-comparator.md             Tier 3 — side-by-side type compare
      citation-tracer.md             Tier 3 — click-source-see-entries
    dicts/                           Phase 4 per-dictionary chapters
      mw.md / pwg.md / pwk.md / ap.md / wil.md / skd.md / vcp.md
      armh.md / abch.md
    data/                            JSON data shared across pages
    locales/
      en/                            English locale routes
      ru/                            Russian locale routes
```

Reader paths:
- **Paper tour:** "I want to follow the argument of the paper — grounded body, then the triangulation, then the framework appendices."
- **Tools:** "I want to explore the data interactively without paper context."
- **Dictionary chapter:** "I'm here for one specific dict's microstructure."

Both share the same underlying data + palette + locale strings.

## Decision 24 — Name: `csl-atlas`

Full name: **"Atlas of the Cologne Digital Sanskrit Lexicons."** Tagline options (TBD):
- "A comparative microstructural atlas of the CDSL corpus"
- "Mapping nine Sanskrit dictionaries from microstructure to lineage"
- "An interactive companion to the CDSL"

The "atlas" framing signals Phase-4 ambition beyond MW. Each dictionary gets a chapter; each Tier-1 figure has per-dictionary and cross-dictionary variants.

## Decision 27 — CI/CD: GitHub Actions on push to `main`

`.github/workflows/build-and-deploy.yml` in `csl-atlas`:
1. Trigger on push to `main` (or manual dispatch).
2. Set up Node 20 + npm cache.
3. Run `npm ci && npm run build`.
4. Deploy `dist/` to GitHub Pages via `actions/deploy-pages@v4`.

A separate workflow (planned, not yet implemented) handles data refreshes:
- `data-refresh.yml` — manual trigger or cron monthly.
- Re-downloads `mw.txt` (and other dict data), re-runs `mw_block_matrix.py`, regenerates JSON in `data/`, commits to `main`; regular build-and-deploy then picks it up.

---

## Implementation status (2026-05-23)

- [x] Local scaffold complete at `D:/claude/csl-atlas/`
- [x] `package.json` + `observablehq.config.js` + `README.md` + `LICENSE` written
- [x] `src/index.md` landing page with paper-tour + tools + dicts grid
- [x] `src/tools/matrix-explorer.md` with working Plot.cell heatmap
- [x] `src/tools/lineage-sankey.md` with working D3-Sankey
- [x] `src/tools/typology-treemap.md` with Plot.cell treemap
- [x] `src/tools/timeline.md` Mermaid timeline reference
- [x] `data/` copied from MWS (5 JSON files + palette tokens)
- [x] `src/palette.css` copied from MWS
- [x] `.github/workflows/build-and-deploy.yml` GitHub Actions config
- [ ] Local Git initialised; **NOT yet pushed** to `sanskrit-lexicon/csl-atlas` — awaiting [@gasyoun](https://github.com/gasyoun)'s approval per Decision 7
- [ ] `npm install` not run; no dependency lock-file yet
- [ ] Paper-tour pages (4) not written — placeholder only
- [ ] Tier-3 tools (type-comparator, citation-tracer) not implemented
- [ ] Per-dictionary chapters (9) not written — Phase 4 work
- [ ] RU locale routes not yet wired

## Cross-links

- [VISUALISATIONS.md](../VISUALISATIONS.md) — catalogue
- [I18N.md](I18N.md) — locale routing
- [FIGURES.md](FIGURES.md) — what the microsite renders
- [DOUBTS.md D8, D10](../DOUBTS.md) — known doubts about stack choice and premature naming
- [csl-atlas local scaffold](file:///D:/claude/csl-atlas/) — current local state
- Future: `https://github.com/sanskrit-lexicon/csl-atlas` — pending push
