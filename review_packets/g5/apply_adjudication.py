#!/usr/bin/env python
"""Apply the Fable 5 adjudication rulings to the G5 disagreement set.

The RULINGS table below is the adjudication data itself: one entry per
(sample_id, block) disagreement row, each decided by reading the full
<L>...<LEND> record in csl-orig/v02/mw/mw.txt @ 392ed6b (the pinned commit).
Adjudicator: Fable 5 (`claude-fable-5`), session H070, 2026-07-03.

Outputs:
  - disagreements.csv rewritten with `adjudicated` + `adjudication_note` filled
  - G5_gold_adjudicated.csv: the 200-record gold table with adjudicated_blocks
    = (A intersect B) + rows adjudicated yes, minus rows adjudicated no.

Usage: python apply_adjudication.py   (from review_packets/g5/)
"""
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8')

Y, N = 'yes', 'no'

# Shared rationales for recurring patterns — every record was still read
# individually; the pattern label records WHY each call went the way it did.
L_ONLY = ("record's only citation is <ls>L.</ls> hedging the entry -> F13, "
          "not F12 (spec reviewer rule 4: 'other <ls> references remain F12')")
INFO_VERB = ("no print conjugation-class marker (cl./P./A.); Pass A fired on "
             "<info verb=>, which is F17 machine annotation per reviewer rule 3")
DIV_VP = ("<div n=\"vp\"/> introduces the Caus./Desid./Intens. paradigm "
          "section - grammatical structure, not editorial commentary")
CF_F16 = "cf./see is a cross-reference marker (F16 per paper SS1), not editorial commentary"
PHW_F17 = ("only <info phwparent/phwchild=> machine relation present -> F17 per "
           "reviewer rule 3; no textual cross-ref marker (q.v./cf./id./See)")
PHW_SUB = ("inline (-X <lex type=\"phw\">) is a sub-headword display, not a "
           "cross-reference; the phw graph attr is F17")
FEM_STEM = ("feminine-stem <s> display inside <lex> (mf(I/A)n. / ifc. f(A).) is "
            "genuine inflectional-form info of the headword")
INFL = "additional <s> span(s) are genuine inflected/conjugated forms of the headword"

RULINGS = {
    # ---- F05: all 10 adjudicated NO (Pass B) --------------------------------
    ('G5-001', 'F05'): (N, "only <ab>Caus.</ab> (derived-stem morphology, F08 territory) + <info verb=>; " + INFO_VERB),
    ('G5-034', 'F05'): (N, INFO_VERB),
    ('G5-038', 'F05'): (N, "aor./Subj./Imper. labels mark inflected FORMS (F08), not a conjugation class; " + INFO_VERB),
    ('G5-061', 'F05'): (N, "Imper. 2 sg. labels an inflected form, not a class; " + INFO_VERB),
    ('G5-089', 'F05'): (N, "bare -rajyate form, no class marker at all; " + INFO_VERB),
    ('G5-140', 'F05'): (N, INFO_VERB),
    ('G5-185', 'F05'): (N, "pure See-reference record with no conjugation content; " + INFO_VERB),
    ('G5-186', 'F05'): (N, "Pass./Caus. stem labels only, no primary class marker; " + INFO_VERB),
    ('G5-190', 'F05'): (N, INFO_VERB),
    ('G5-194', 'F05'): (N, INFO_VERB),
    # ---- F12: 48 NO (L.-only hedge records, Pass A) + 1 YES ----------------
    **{(sid, 'F12'): (N, L_ONLY) for sid in [
        'G5-003', 'G5-004', 'G5-005', 'G5-007', 'G5-011', 'G5-012', 'G5-013',
        'G5-020', 'G5-024', 'G5-030', 'G5-032', 'G5-035', 'G5-036', 'G5-039',
        'G5-044', 'G5-047', 'G5-062', 'G5-064', 'G5-065', 'G5-070', 'G5-071',
        'G5-076', 'G5-079', 'G5-087', 'G5-090', 'G5-099', 'G5-100', 'G5-101',
        'G5-102', 'G5-104', 'G5-112', 'G5-125', 'G5-127', 'G5-132', 'G5-133',
        'G5-137', 'G5-144', 'G5-149', 'G5-150', 'G5-161', 'G5-163', 'G5-173',
        'G5-178', 'G5-179', 'G5-184', 'G5-189', 'G5-192', 'G5-200']},
    ('G5-191', 'F12'): (Y, "<ls n=\"RV.\">iv, 13, 2</ls> is a genuine RV source citation (work name in the n= attribute); Pass A's content-only check missed it"),
    # ---- F08: 34 YES (Pass B) + 1 NO ---------------------------------------
    ('G5-008', 'F08'): (Y, "a/pvA (Naigh.), voc. apve, acc. apvA/m - " + INFL),
    ('G5-011', 'F08'): (Y, "(<s>A</s>) " + FEM_STEM),
    ('G5-016', 'F08'): (Y, "(in <s>a-v0</s>) gives the attested compound shape of the lemma - borderline, ruled a form block"),
    ('G5-023', 'F08'): (Y, "-Bavati: " + INFL),
    ('G5-029', 'F08'): (Y, "svAH nom. pl. quoted with its own gloss - " + INFL),
    ('G5-030', 'F08'): (Y, "(<s>ikA</s>) " + FEM_STEM),
    ('G5-033', 'F08'): (Y, "ci/kiti is the SV variant form of the headword"),
    ('G5-035', 'F08'): (Y, "(iBam-Acala) sandhi-resolved full form of the headword - a form display"),
    ('G5-038', 'F08'): (Y, "-spa/rat, -spar, -spfDi, -spftam: " + INFL),
    ('G5-040', 'F08'): (Y, "0yati Nom. present: " + INFL),
    ('G5-049', 'F08'): (Y, "-Ikzate (0ti): " + INFL),
    ('G5-051', 'F08'): (Y, "mf(<s>I</s>)n.: " + FEM_STEM),
    ('G5-056', 'F08'): (Y, "-Bajati, 0te: " + INFL),
    ('G5-061', 'F08'): (Y, "-myakza Imper.: " + INFL),
    ('G5-068', 'F08'): (Y, "0yati Nom. present: " + INFL),
    ('G5-071', 'F08'): (Y, "mf(<s>I</s>)n.: " + FEM_STEM),
    ('G5-073', 'F08'): (Y, "-karoti: " + INFL),
    ('G5-078', 'F08'): (Y, "(<s>am</s>) phw adverb form + lavam api inflected usage phrase"),
    ('G5-089', 'F08'): (Y, "-rajyate: " + INFL),
    ('G5-103', 'F08'): (Y, "-Bavati: " + INFL),
    ('G5-113', 'F08'): (Y, "(ifc. f(A).): " + FEM_STEM),
    ('G5-114', 'F08'): (Y, "-siYcate: " + INFL),
    ('G5-116', 'F08'): (Y, "(<s>A</s>) " + FEM_STEM),
    ('G5-120', 'F08'): (Y, "izaRyati + participle izaRya/t: " + INFL),
    ('G5-124', 'F08'): (Y, "mf(<s>I/</s>)n. (accented): " + FEM_STEM),
    ('G5-129', 'F08'): (Y, "(ifc. f(A).): " + FEM_STEM),
    ('G5-130', 'F08'): (Y, "0yati Nom. present: " + INFL),
    ('G5-139', 'F08'): (Y, "-sIdati: " + INFL),
    ('G5-146', 'F08'): (Y, "-karoti: " + INFL),
    ('G5-148', 'F08'): (Y, "(ifc. f(A).): " + FEM_STEM),
    ('G5-160', 'F08'): (Y, "(<s>am</s>) adverbial-form display of the phw headword"),
    ('G5-168', 'F08'): (Y, "mf(<s>A</s>)n.: " + FEM_STEM),
    ('G5-170', 'F08'): (Y, "mf(<s>I</s>)n.: " + FEM_STEM),
    ('G5-196', 'F08'): (Y, "(also <s>0ska</s>) variant stem: " + INFL),
    ('G5-194', 'F08'): (N, "extra <s> spans are the segmented headword itself (aBy-upA- root kf), not additional inflected forms"),
    # ---- F09: 16 NO + 4 YES -------------------------------------------------
    ('G5-004', 'F09'): (N, CF_F16),
    ('G5-013', 'F09'): (N, "parenthetical identifies the referent (encyclopedic gloss); the cf. inside it is F16"),
    ('G5-051', 'F09'): (N, "(fr. vi-Seza) is an etymology marker (F06), not commentary"),
    ('G5-074', 'F09'): (N, DIV_VP),
    ('G5-078', 'F09'): (N, CF_F16),
    ('G5-087', 'F09'): (N, CF_F16),
    ('G5-095', 'F09'): (N, DIV_VP),
    ('G5-098', 'F09'): (N, "cf. root lup is F16; " + DIV_VP),
    ('G5-118', 'F09'): (N, "'cf. below' is a cross-pointer; the parenthetical is a form inventory, not editorial prose"),
    ('G5-140', 'F09'): (N, DIV_VP),
    ('G5-156', 'F09'): (N, "the whole entry is a cross-reference (cf. a-, su-) - F16, no commentary"),
    ('G5-170', 'F09'): (N, "cf. Pan. Sch. is a comparative cross-ref (F16), not commentary"),
    ('G5-181', 'F09'): (N, CF_F16),
    ('G5-183', 'F09'): (N, DIV_VP),
    ('G5-186', 'F09'): (N, DIV_VP),
    ('G5-188', 'F09'): (N, "see-also is F16; the paradigm parentheses are grammar, not commentary"),
    ('G5-014', 'F09'): (Y, "(accord. to L. ...) reports an attributed, uncertain identification - editorial commentary"),
    ('G5-059', 'F09'): (Y, "(said to consist in ...) hedged attributed description - editorial commentary"),
    ('G5-079', 'F09'): (Y, "(for dogDf?) uncertain derivation flagged with a literal ? - editorial commentary"),
    ('G5-158', 'F09'): (Y, "(said to be brought from ...) hedged report - editorial commentary"),
    # ---- F16: 11 NO (phw-infrastructure) + 13 YES (textual markers) --------
    ('G5-010', 'F16'): (N, PHW_F17),
    ('G5-026', 'F16'): (N, PHW_F17),
    ('G5-050', 'F16'): (N, PHW_SUB),
    ('G5-103', 'F16'): (N, "(0rTI-BAva <lex type=\"phw\">) " + PHW_SUB),
    ('G5-110', 'F16'): (N, PHW_F17),
    ('G5-155', 'F16'): (N, "'= X' equivalence gloss is not in F16's marker set (q.v./cf./id./see); phwchild attr is F17"),
    ('G5-159', 'F16'): (N, PHW_SUB),
    ('G5-160', 'F16'): (N, PHW_F17),
    ('G5-166', 'F16'): (N, PHW_F17),
    ('G5-169', 'F16'): (N, PHW_SUB),
    ('G5-172', 'F16'): (N, PHW_F17),
    ('G5-004', 'F16'): (Y, "(cf. <s>Jampa</s>) textual cross-reference"),
    ('G5-013', 'F16'): (Y, "(cf. <s>padma-priyA</s>) textual cross-reference"),
    ('G5-042', 'F16'): (Y, "'see sanizyada/ under root syand' explicit see-reference"),
    ('G5-063', 'F16'): (Y, "[For cognates See under varzA and 1. vfza] + cf. - textual cross-references"),
    ('G5-069', 'F16'): (Y, "'see under <s>sarga</s>' textual cross-reference"),
    ('G5-087', 'F16'): (Y, "(cf. 3. <s>sUta</s>) textual cross-reference"),
    ('G5-094', 'F16'): (Y, "(q.v.) after Acamana - listed F16 marker"),
    ('G5-098', 'F16'): (Y, "(cf. root <s>lup</s>) textual cross-reference"),
    ('G5-141', 'F16'): (Y, "(q.v.) after Upa-vasatha - listed F16 marker"),
    ('G5-156', 'F16'): (Y, "entry consists of 'cf. a-, su-' - pure cross-reference"),
    ('G5-181', 'F16'): (Y, "(cf. <s>arDa-praharikA</s>) textual cross-reference"),
    ('G5-188', 'F16'): (Y, "(see also <s>kruDyamAna</s>) textual see-reference"),
    ('G5-194', 'F16'): (Y, "'See upA- root 1. kf' explicit see-reference"),
    # ---- F15: 4, all YES (formal-marker line: <bio>/<s1> proper name) ------
    ('G5-063', 'F15'): (Y, "<s1>Parjanya/Indra</s1> proper-name markup present; F15's formal marker is <bio>/<s1> - kept consistent with G5-084/138/143 (B's semantic narrowing rejected for marker consistency)"),
    ('G5-084', 'F15'): (Y, "<s1 n=\"Veda\">V0</s1> proper-name marker; Pass A's regex missed the n= attribute form"),
    ('G5-138', 'F15'): (Y, "<s1>Buddha</s1> + genuinely encyclopedic content; Pass A's '<s1> without <bot>' rule wrongly excluded records that also carry <bot>"),
    ('G5-143', 'F15'): (Y, "<s1 n=\"Zastra\">S0</s1> proper-name marker; Pass A regex artifact on the n= attribute"),
    # ---- F02 / F06 / F07 ----------------------------------------------------
    ('G5-171', 'F02'): (Y, "(kanI/naka) re-displays the accented headword; in continuation records the display form structurally follows the initial separator"),
    ('G5-051', 'F06'): (Y, "<ab>fr.</ab> vi-Seza is the paper's own listed F06 marker; Pass A's rule omitted fr."),
    ('G5-118', 'F07'): (N, "<lang>Ved.</lang> is a register label on Vedic forms, not IE-cognate content (no <etym>/<gk>)"),
    ('G5-188', 'F07'): (N, "<lang>ep.</lang> is a register label (epic), not IE-cognate content (no <etym>/<gk>)"),
}


def read_disagreements(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    comments = [ln for ln in lines if ln.startswith(';')]
    rows = list(csv.DictReader([ln for ln in lines if not ln.startswith(';')]))
    return comments, rows


def main():
    comments, rows = read_disagreements('disagreements.csv')
    used = set()
    for r in rows:
        key = (r['sample_id'], r['block'])
        if key not in RULINGS:
            raise SystemExit(f'UNADJUDICATED ROW: {key}')
        verdict, note = RULINGS[key]
        r['adjudicated'] = verdict
        agrees = 'A' if (verdict == Y) == (r['in_A'] == 'yes') else 'B'
        r['adjudication_note'] = f'[->{agrees}] {note}'
        used.add(key)
    unused = set(RULINGS) - used
    if unused:
        raise SystemExit(f'RULINGS with no matching row: {sorted(unused)}')

    with open('disagreements.csv', 'w', encoding='utf-8', newline='') as f:
        f.writelines(comments)
        f.write('; adjudicated by Fable 5 (claude-fable-5), session H070, 2026-07-03, '
                'reading each record in csl-orig/v02/mw/mw.txt @ 392ed6b\n')
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # build the adjudicated gold table
    def load(path, col):
        with open(path, encoding='utf-8', newline='') as f:
            return {r['sample_id']: r for r in csv.DictReader(f)}

    pa = load('pass_a/annotations.csv', 'gold_blocks_A')
    pb = load('pass_b/annotations.csv', 'gold_blocks_B')
    decided = {}
    notes = {}
    for r in rows:
        decided.setdefault(r['sample_id'], {})[r['block']] = r['adjudicated']
        notes.setdefault(r['sample_id'], []).append(
            f"{r['block']}={r['adjudicated']} {r['adjudication_note']}")

    n_adj = 0
    out = []
    for sid in sorted(pa):
        ra, rb = pa[sid], pb[sid]
        sa = set(x for x in ra['gold_blocks_A'].split(';') if x)
        sb = set(x for x in rb['gold_blocks_B'].split(';') if x)
        final = sa & sb
        for blk, verdict in decided.get(sid, {}).items():
            if verdict == Y:
                final.add(blk)
            else:
                final.discard(blk)
        row = dict(ra)
        row['gold_blocks_B'] = rb['gold_blocks_B']
        row['adjudicated_blocks'] = ';'.join(sorted(final))
        row['notes'] = ' | '.join(notes.get(sid, []))
        if sid in decided:
            n_adj += 1
        out.append(row)

    with open('G5_gold_adjudicated.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    print(f'adjudicated rows: {len(rows)}; records touched: {n_adj}; gold table: {len(out)} records')


if __name__ == '__main__':
    main()
