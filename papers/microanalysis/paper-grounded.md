# The microstructure of *Monier-Williams 1899*: a data-grounded framework

> **Supplementary extended draft — superseded by [PAPER.md](PAPER.md).** One of four single-framework drafts consolidated into the single submission paper per [DOUBTS.md D4](DOUBTS.md#d4--4-framework-papers-from-the-same-data--is-this-honest--blocking). The data-grounded reading below is now the **body** of [PAPER.md](PAPER.md); this fuller draft is retained as supplementary material only. **For the canonical paper, read [PAPER.md](PAPER.md).**

**Draft for the [*International Journal of Lexicography*](https://academic.oup.com/ijl) (Oxford University Press).** ~8K words target.

**Theoretical framing:** *None* (deliberately). Builds the analytic apparatus from the data itself. One of four parallel framework analyses — see [README](README.md). Data source: [MICROANALYSIS.md](MICROANALYSIS.md).

---

## Abstract

The dominant frameworks in metalexicography — Wiegand (1989, 2002), Hausmann (1977, 1985), Atkins & Rundell (2008) — were built on European mid-20th- and late-20th-century dictionaries. Applying them to *Monier-Williams 1899* (henceforth MW) **risks imposing categories the lexicographer did not himself recognise**, however productively the exercise illuminates the artefact. This paper takes the opposite stance: we build a descriptive framework **from MW outward**, treating its 18 formal blocks and 14 article types as primary, and constructing a typology that respects the dictionary's own internal logic before any external theory is consulted. The framework that emerges has five core constructs — **block, slot, profile, hedge, infrastructure** — each operationalised against the live [`mw.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt) digital edition (286,561 records). We end by **comparing** this grounded framework against the three external theories applied in our companion papers, and argue that the grounded view captures one fact none of the external theories does: MW is a **block-economical** dictionary whose 286,561 entries reuse the same ~6-block kernel with type-driven variation. We propose this *block-economy* as a typological signature distinguishing 19th-century scholarly dictionaries from both modern learner-dictionaries (more pragmatic information, fewer formal blocks) and indigenous synonymies / koshas (different infrastructure entirely).

**Keywords:** grounded theory, microstructure, Monier-Williams, Sanskrit lexicography, CDSL, block economy, scholarly dictionary

---

## 1. Why ground the framework in the data?

Scholarly metalexicography is dominated by frameworks built between 1977 and 2008 on dictionaries from a narrow band of European traditions (French, German, English). They have produced powerful taxonomies — Wiegandian microstructure, Hausmann comment-classes, Atkins-Rundell production/retrieval typology — and we apply them to MW1899 in our companion papers. But each framework also **imposes categories**. Wiegand's "fully integrated microstructure" presupposes a sense-hierarchy that MW's `<e>1A` continuation-by-adjacency pattern does not quite realise. Hausmann's four comment-classes lacked a category for MW's lexicographer-hedge (we added one). Atkins-Rundell's typology of dictionary purposes assumes a 21st-century user.

We propose a complementary exercise. **What does MW1899 look like if we build the analytical apparatus from MW itself**, only consulting external frameworks at the end for comparison? The answer, we argue, is a *minimal* framework — five constructs — that captures MW's design with no superfluous categories, and lets us see what is **specific to MW** that the imported frameworks dilute or miss.

Our data is the [working notes file](MICROANALYSIS.md), built by parsing every `<L>...<LEND>` record in mw.txt and counting formal-block occurrences.

## 2. The five grounded constructs

### Construct 1 — *Block*

A **block** is a discriminable structural component of an MW entry. We identify 18 such blocks (see [MICROANALYSIS.md §1](MICROANALYSIS.md)). The block is the **atomic unit** of analysis. We make no a priori claim about what blocks *should* be present, and no a priori taxonomy of block-roles.

A block has:
- A **marker** — a tag, glyph, or stereotyped position that lets us detect it.
- A **population** — the number of entries containing it.
- An **occurrence profile** — the rate at which it co-occurs with each other block (the matrix in MICROANALYSIS.md §4).

### Construct 2 — *Slot*

A **slot** is an ordered position within an entry where blocks may occur. MW's slot order (from `<L>` to `<LEND>`) is fixed:

```
[F01 header] → [F02 display headword] [F03 hom] [F04 lex] [F05 cl./P./Ā.]
            → [F06 √] [F07 lang] [F08 inflection forms] [F09 commentary]
            → ¦ → [F10 gloss] [F11 sense divisions] → [F12 ls cites] [F13 L. hedge]
            → [F14 bot] [F15 bio] [F16 cross-ref] → [F17 info] → [F18 corrections]
            → <LEND>
```

Many slots are **optional**. The *grammatical category* slot exists; whether F04 fills it depends on the article type. The slot architecture is what distinguishes MW from a free-form dictionary (entries are not arbitrary prose) and from a purely tabular dictionary (entries are not key-value pairs).

The slot view is also the **renderer's view** — MW's [SQLite generation pipeline](https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/makotemplates/pywork/sqlite/sqlite.py) walks the slots in order and emits HTML.

### Construct 3 — *Profile*

A **profile** is the *block-set characteristic of an article type*. We identify 14 article types (see [MICROANALYSIS.md §3](MICROANALYSIS.md)). Each type has a characteristic profile:

- A **necessary-block set**: blocks present in ≥ 95% of entries of this type.
- An **enriched-block set**: blocks present at substantially higher rates than baseline (e.g. F09 commentary at 78% in roots vs ~10% baseline).
- An **omitted-block set**: blocks present at substantially lower rates than baseline (e.g. F02 display headword at 33.9% in continuations vs ~99% baseline).

The profile is the **lexicographer's strategic choice** for handling a type of lemma. Each of MW's 14 profiles is internally coherent — see the [Article-type matrix](MICROANALYSIS.md).

### Construct 4 — *Hedge*

A **hedge** is a block whose function is to modify the evidentiary status of the entire entry. MW has one explicit hedge: `<ls>L.</ls>` (F13). Its function is to signal that the entry's sole evidence is the indigenous lexicographer tradition.

Hedges are distinct from blocks-in-general because they:
- Operate at the **entry level**, not the slot level. An `L.`-hedge doesn't qualify the gloss it follows; it qualifies the whole entry's evidentiary basis.
- Have a **transverse distribution**: they appear across many article types, not concentrated in one (see MICROANALYSIS.md §4: F13 at 71.5% of botanicals, 64.7% of biographicals, 100% of lexicographer-only).
- Carry **reader-guidance**: they tell the user how to weight the entry's content.

MW has exactly one hedge. PWG had zero (a different design choice — see [Lineage section](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg)). The hedge is the **single most distinctive block** in MW's design.

### Construct 5 — *Infrastructure*

**Infrastructure** is the set of blocks that exist to support the dictionary's *processability* — not its *content*. MW has two infrastructure blocks: F17 `<info>` machine annotation (in 96% of entries) and F18 correction record (< 30 instances).

Infrastructure is not a Hausmann or Wiegand category. It is a **digital-era construct** — a block that has no analogue in the print dictionary. The print MW1899 has no `<info>` tag; the CDSL editors added it during digitisation to support the SQLite pipeline and the web display. Treating F17 as infrastructure (not as part of microstructure proper) preserves the original-vs-digital distinction.

## 3. The block-economy thesis

Our central empirical observation is this: **MW reuses a small core of blocks across an enormous number of entries**.

The modal entry has **6 blocks**, drawn from a kernel of 5–7 (F01, F02, F04, F10, F12, F17, and either F08 or F13). The remaining 11–12 blocks are *type-specific enrichments* that appear in a small fraction of entries.

We name this **block economy**. Quantitatively:

| Block | Population (% of entries) | Role |
|---|--:|---|
| **F01 Record header** | 100% | Kernel |
| **F17 Machine annotation** | 96% | Kernel (digital-era) |
| **F02 Display headword** | 99% | Kernel |
| **F10 Sense gloss** | ~100% | Kernel |
| **F12 Source citation** | ~80% | Kernel (high) |
| **F04 Grammatical category** | 65% | Kernel (medium) |
| F08 Inflection form | 21% | Type-enriched |
| F13 Hedge L. | 13% | Type-enriched |
| F09 Editorial commentary | 9% | Type-enriched |
| F06 Etymology root | 6% | Type-enriched |
| F03 Homophone marker | 5% | Type-enriched |
| F14 Botanical | 3% | Type-specific |
| F11 Sense division | < 1% | Type-specific (rare) |
| F07 IE cognate | 0.7% | Type-specific (rare) |
| F15 Biographical | < 0.1% | Type-specific (rare) |
| F05 Verb inflection class | < 1% | Type-specific (verbs only) |
| F16 Cross-reference | 9% | Distributed |
| F18 Correction record | < 0.01% | Vanishing |

**Six blocks (F01, F02, F04, F10, F12, F17) recur in 65–100% of entries**. These six **make MW MW**. The other twelve are deployed sparingly, in type-specific clusters.

This is **block economy** in the explicit sense: **a 19th-century printed dictionary cannot afford to elaborate every block in every entry**. Print space is finite; setting cost is real; the user must be able to scan. MW's design rationalises this by maintaining a 6-block kernel and adding to it only when the article-type demands.

The block-economy is **not** present in MW's source dictionary PWG, which we calculated has [571,152 `<ls>` citations against MW's 312,159](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) — PWG is roughly 1.8× more citation-dense per entry. PWG can afford this density because it's a multi-volume work. MW1899 is one volume; block-economy is the print-economic constraint made explicit.

## 4. Profiles as the unit of typology

Once block-economy is recognised, the article-type *profile* (Construct 3) becomes the natural unit of lexicographic typology. Each of MW's 14 profiles is a **specific deviation** from the 6-block kernel — adding some blocks, suppressing others. We illustrate three.

### 4.1 The verbal-root profile

**Kernel: present**: F01, F02, F10, F12, F17 (skipping F04 — verbs are not in `<lex>`).
**Enrichments**: F05 verb class (98.4%), F08 inflection forms (99.9%), F03 homophone (49.6%), F09 commentary (78.1%), F06 root marker (44.7%), F07 IE cognate (35.2%), F16 cross-reference (54.5%).

Result: average 9.73 of 18 blocks present. **The most elaborate profile in MW.** Roots are 0.26% of entries; they receive the largest share of editorial apparatus.

### 4.2 The compound-sub-entry profile

**Kernel: present**: F01, F02 (84.7%), F04 (80.7%), F10 (97.9%), F17 (96.3%).
**Enrichments**: F12 source citation (81.2%), F08 inflection (18.5%) — modest additions.
**Suppressions**: F03 (0.9%), F05 (0.3%), F06 (1.6%), F07 (0.1%), F09 (3.5%), F11 (0.0%), F14 (3.3%), F15 (14.7%), F16 (4.7%).

Result: average 6.02 blocks. **The kernel + a citation, almost nothing more.** Compounds are 44% of MW's entries; their economical treatment is what makes the dictionary printable.

### 4.3 The lexicographer-only profile

**Kernel: present**: F01, F02, F04 (65.2%), F10 (100%), F17 (99.2%) — slight `<lex>` suppression.
**Enrichments**: F12 source citation (100%) — definitional (the `L.` is itself an `<ls>`).
**Singular**: F13 hedge L. = 100%.

Result: average 6.89 blocks. **The kernel + the hedge.** The hedge IS the entry's distinctive content; the rest is standard.

## 5. The infrastructure layer and its meaning

Construct 5 — infrastructure — deserves a moment's attention because it does work no purely Wiegandian or Hausmannian analysis can do.

F17 (`<info>` machine annotation) is present in 96% of entries. It carries machine-readable encoding of information that the human-readable blocks already convey. **It is a redundancy**, but a deliberate one: the CDSL editors needed a tag set the SQLite pipeline could parse without ambiguity, and they added it to mw.txt during digitisation. From a 19th-century print perspective, F17 doesn't exist; from a 21st-century digital perspective, it's the most pervasive block.

This dual existence — present in the digital edition, absent from the print — is the **infrastructure layer**. Recognising it explicitly lets us:

- **Preserve the historical artefact** (when we talk about MW1899-as-print, F17 is not part of it).
- **Acknowledge the digital tooling** (when we talk about MW1899-as-data, F17 is essential).
- **Track digitisation choices as such** — what the CDSL editors added vs what was in the print.

The infrastructure construct is **specific to digital editions of historical dictionaries**. We propose it as a general analytical category.

## 6. Comparison to the three external frameworks

How does the grounded framework compare to Wiegand, Hausmann-Wiegand, and Atkins-Rundell? We summarise:

| Construct | Wiegand equivalent | Hausmann-Wiegand equivalent | Atkins-Rundell equivalent |
|---|---|---|---|
| **Block** | Item (*Angabe*) | Comment sub-element | Field |
| **Slot** | Position in microstructure | Comment sequence | Entry skeleton |
| **Profile** | Article-type (*Artikeltyp*) | Comment-class signature | Entry pattern |
| **Hedge** | (transverse structural indicator) | Provenance-comment (we added) | Register marker |
| **Infrastructure** | — (no equivalent) | — (no equivalent) | — (no equivalent) |

The grounded framework adds one construct — **infrastructure** — that none of the three external frameworks recognises. We claim this is a positive contribution. We also rename two constructs (item → block, article-type → profile) for clarity in a Sanskrit-lexicographic context where Wiegand's German terminology is unfamiliar.

The two constructs the external frameworks handle better than ours:

- **Wiegand** has a precise theory of **mediostructure** (cross-references between articles) that we treat only informally (F16). For MW's 4,401 `<ab>id.</ab>` ("the same as the immediately preceding") instances, a Wiegandian mediostructure analysis is more productive.
- **Atkins-Rundell** has a richer typology of **dictionary purpose** (production vs retrieval, learner vs scholar) that lets them position MW within a broader lexicographic landscape. Our grounded framework can describe MW but cannot place it in such a landscape without borrowing A&R's apparatus.

The construct unique to the grounded view — **block-economy** (§3) — is one we have not seen named elsewhere, and is the framework's strongest contribution.

## 7. What the grounded view reveals that the external frameworks dilute

Three findings emerge more sharply from the data-grounded view than from any external framework:

### 7.1 MW is *kernel-plus-enrichment*, not *full-microstructure*

Wiegand's "fully integrated microstructure" suggests every block is in principle available to every entry. MW's actual practice is the opposite: a small kernel (6 blocks) plus type-driven enrichments. The lexicographic *strategy* is to maintain the kernel rigorously and add only where the article-type demands. A "fully integrated" reading of MW obscures this constraint.

### 7.2 The L.-hedge is structurally singular

The `<ls>L.</ls>` block is the only **transverse hedge** in MW — the only block that operates entry-level rather than slot-level, across multiple article types. Hausmann's framework didn't anticipate it (we had to add a fifth comment-class); Atkins-Rundell treats it as one register-marker among many; the grounded view names it as a singular structural device. Our analysis suggests MW has exactly one explicit hedge; it is therefore worth naming and tracking it as such.

### 7.3 The infrastructure layer is the digitisation residue

F17 `<info>` is in 96% of entries but is **not part of the print MW1899**. It is the **trace of digitisation** in the data file. Recognising the infrastructure construct (as opposed to merging F17 into the microstructure) lets us tell the original-vs-digital story cleanly. Future analyses of CDSL dictionaries can use this construct to separate "what MW had" from "what CDSL added."

## 8. Application: a 14-row profile table

We can express the entire grounded analysis in one table — the **MW profile table** below — which collapses all 14 article types into one printable diagnostic:

| Profile | Kernel (F01-02-04-10-12-17) | Distinctive enrichments | Distinctive suppressions | Avg blocks | Hedge incidence |
|---|---|---|---|--:|--:|
| Root | F02+F10+F12+F17 (no F04) | F05 cl.,P.,Ā. (98%); F08 forms (100%); F09 (78%); F06 √ (45%); F07 IE (35%); F16 (55%); F03 hom (50%) | F04 (gram absent) | 9.73 | 7% |
| Noun_m | full kernel | F12 (78%); F08 (22%); F09 (7%); F06 (9%) | — | 6.43 | 19% |
| Noun_f | full kernel | F14 botanical (6%) elevated | — | 6.28 | 21% |
| Noun_n | full kernel | F08 (18%) | — | 6.05 | 12% |
| Adjective_mfn | full kernel | F06 (17%) | F14, F15 lowest | 6.25 | 4% |
| Indeclinable | full kernel | F08 (30%); F09 (12%) | F14 (0.1%) | 6.39 | 2% |
| Compound | F01,F02,F04 (81%),F10,F17 | F12 (81%); F08 (18%) | F03, F05, F06, F07, F09, F11, F14, F15 all suppressed | 6.02 | 13% |
| Derived | F01,F02 (69%),F04 (51%),F10,F17 | F12 (81%); F08 (23%) | most enrichments suppressed | 5.73 | 16% |
| Continuation | F01,F10,F17 only (F02, F04 inherited) | F12 (81%) | F02 (34%); F04 (0.3%); F08 (7%) | 4.76 | 21% |
| Lexicographer_only | full kernel | F13 hedge (100%); F14 (15%) | F09 (3%) | 6.89 | 100% |
| IE_etymological | F01, F02 (95%), F08 (53%), F10, F17 | F07 (100%); F09 (38%); F16 (55%); F08 (53%) | F04 (27%) | 7.70 | 3% |
| Botanical | F01, F02 (67%), F04 (69%), F10, F12, F14 (100%) | F13 hedge (72%); F08 (14%) | F02 lower (display by `<bot>`) | 7.28 | 72% |
| Biographical | F01, F02, F04 (75%), F10, F12 (94%), F15 (100%) | F13 hedge (65%); F08 (20%) | — | 7.58 | 65% |
| Vedic_accented | F01,F02 (70%),F04 (51%),F10,F12 (88%),F17 | F08 (28%); F09 (11%) | — | 5.93 | 11% |

This table is the **single most useful diagnostic** for the working CDSL editor: pick an article type, see which blocks are expected, see what's distinctive, see how much elaboration to budget. It is also the framework's single deliverable for downstream metalexicographic comparison — the same table can be produced for any CDSL dictionary, allowing direct comparison across the corpus.

## 9. What this framework would change about future CDSL work

Three concrete implications:

- **For dictionary editing**: the [ROADMAP](../../ROADMAP.md) currently lists 34 open issues + new strategic categories (authority records, Vedic accent expansion, `L.` verification). The block-profile view suggests that **the highest-leverage editorial work is filling Profile-specific gaps** — e.g. systematically reducing F13 hedge incidence in botanical entries (currently 72%, target: lower via better named-source citation; covered by [our Atkins-Rundell paper §10](paper-atkins-rundell.md#10-what-modern-lexicography-would-change)).
- **For cross-dictionary work**: each CDSL dict ([PWG](https://github.com/sanskrit-lexicon/PWG), [AP](https://github.com/sanskrit-lexicon/ap), [WIL](https://github.com/sanskrit-lexicon/WIL), [SKD](https://github.com/sanskrit-lexicon/SKD), [GRA](https://github.com/sanskrit-lexicon/GRA), [BHS](https://github.com/sanskrit-lexicon/BHS)) and the four koshas ([ARMH](https://github.com/sanskrit-lexicon/armh), [ABCH](https://github.com/sanskrit-lexicon/abch), [ACPH](https://github.com/sanskrit-lexicon/acph), [ACSJ](https://github.com/sanskrit-lexicon/acsj)) should be analysed with the same 18-block framework. A comparative table of profile-distributions would surface intellectual lineages and design contrasts that no single-dictionary study can. The [Lineage section in DICT_PROFILE.md](../../DICT_PROFILE.md#lineage-wil--koshas-mw--pwg) gives the qualitative version; a quantitative version would be a natural follow-up.
- **For digital-edition methodology**: the **infrastructure construct** (§5) is a transferable analytical tool. Any future digital edition of a historical dictionary needs to track what was added in digitisation vs what was in the original. The CDSL `<info>` system is one example; XML attributes like `@type="digital"` could formalise the distinction across the project.

## 10. Conclusion

A framework built **from MW1899 outward** identifies five core constructs — block, slot, profile, hedge, infrastructure — and yields one central empirical claim: **MW is a block-economical scholarly dictionary**, maintaining a 6-block kernel across 286,561 entries with type-driven enrichment. The single most distinctive structural feature is the *hedge* `<ls>L.</ls>` (Construct 4), realised by one block, deployed transversely across article types, and absent from MW's source PWG. The single most distinctive *meta*-feature is the **infrastructure layer** (Construct 5) — the 96% incidence of `<info>` machine annotations added during digitisation, a trace of the digital edition itself.

Compared to imported frameworks: Wiegand explains how MW *could be* described as integrated-microstructure but obscures the kernel-plus-enrichment design; Hausmann-Wiegand fits MW's source-comment apparatus but had to be extended with a fifth class for the hedge; Atkins-Rundell positions MW in a broader lexicographic landscape but treats blocks generically as "fields." The grounded view, as we have set it out, captures something each external framework dilutes or misses — and it gives the working CDSL editor a single diagnostic table (§8) for budgeting editorial work per article type.

Whether a grounded framework is *preferable* to an external one depends on the analytic purpose. For comparing MW to other 19th-century dictionaries, Atkins-Rundell wins. For situating MW in metalexicographic theory, Wiegand wins. For Sanskrit-specific work, we suggest the grounded view in this paper, supplemented by Hausmann-Wiegand for source-attribution analysis (paper-hausmann.md §5).

---

## References (selected)

- Apresjan, J. (2002). *Principles of Systematic Lexicography*. In M.-H. Corréard (ed.).
- Atkins, B. T. S. & Rundell, M. (2008). *The Oxford Guide to Practical Lexicography*. Oxford University Press.
- Glaser, B. G. & Strauss, A. L. (1967). *The Discovery of Grounded Theory*. Aldine. (For the grounded-theory methodology applied here.)
- Hausmann, F. J. (1985). *Lexikographie*. HSK.
- Monier-Williams, M. (1899). *A Sanskrit-English Dictionary*. 2nd edn. Oxford: Clarendon Press.
- Scharf, P. M. & Hyman, M. (2009–2011). *Encoding Sanskrit dictionaries: report from the Cologne project*. In *Sanskrit Computational Linguistics*.
- Wiegand, H. E. (1989). *Aspekte der Makrostruktur*. HSK 5.1.
- Wiegand, H. E. (2002). *Equivalence in Bilingual Lexicography*. Lexikos 12.

---

*Source data: [MICROANALYSIS.md](MICROANALYSIS.md). Companion framework papers: [Wiegand](paper-wiegand.md) · [Atkins-Rundell](paper-atkins-rundell.md) · [Hausmann-Wiegand](paper-hausmann.md). All four analyse the same MW1899 dataset through different theoretical lenses.*
