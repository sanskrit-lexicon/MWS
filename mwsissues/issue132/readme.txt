MWS/mwsissues/issue132

Ref: https://github.com/sanskrit-lexicon/MWS/issues/132

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  a4b2854a2b8acca106f7cb6d08c5834e5417000d

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  a4b2854a:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue132/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue132/
 
*********************************************************************
BEGIN change_1
cp temp_mw_0.txt temp_mw_1.txt
touch change_1.txt

# -------------------------------------------------------------
The ¦ character is a (non-xml) markup. It is removed in the
transition from mw.txt to mw.xml.

# counts of broken bars
python bbar1.py temp_mw_0.txt
empty entry: <L>78878<pc>419,1<k1>jAbAlopanizad<k2>jAbAlopanizad<e>3A
287603 metalines
287602 headlines
280837 headlines with 1 ¦
0 headlines with > 1 ¦
6765 headlines with 0 ¦
0 non-headlines with 1 or more ¦

# -----------------------------
# 78878 jAbAlopanizad is empty.  
<L>78878<pc>419,1<k1>jAbAlopanizad<k2>jAbAlopanizad<e>3A

<LEND>
Add change in change_1 to make this <L> and <LEND> lines empty.
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
2 change transactions from change_1.txt
(
# -----------------------------
$ grep -E "^[^¦].*[^ ]¦" temp_mw_0.txt | wc -l   (12)
$ grep -E "^[^¦].*¦[^ ]" temp_mw_0.txt | wc -l   (67)
$ grep -E "^[^¦].* ¦ " temp_mw_0.txt | wc -l     (213595)

In almost all cases, the non-initial broken bar is preceded and followed by
a space character.

Make changes so that in these few cases, also a space precedes and follows ¦.

# --------------------------
 '([^ ])¦'  -> '\1 ¦'
python make_change_regex.py 1a temp_mw_1.txt temp_change_regex_1a.txt
12 cases written to temp_change_regex_1a.txt
# insert temp_change_regex_1a.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
 change transactions from change_1.txt

# --------------------------
 '¦([^ ])'  -> '¦ \1'
python make_change_regex.py 1b temp_mw_1.txt temp_change_regex_1b.txt
74 cases written to temp_change_regex_1b.txt
# insert temp_change_regex_1b.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
88 change transactions from change_1.txt

---------------------------------------------------------------------------
# temp_L-entries.to.fill.and-or.tags.txt
  This list provided by AB used for two purposes:
  1) To add missing broken bar
  2) To identify entry-groups which need markup
      <info and=.../>   or <info or=.../>.
Apply the markup (2)
# change_and_or_input.txt
  0. edit of temp_L-entries.to.fill.and-or.tags.txt
  1. add 'GROUP' markup separating the or/and groups
  2. Remove cases that are not Groups (see next section)
  
python change_and_or.py change_and_or_input.txt temp_mw_1.txt temp_change_and_or.txt
# insert temp_change_and_or.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
255 change transactions from change_1.txt

---------------------------------------------------------------------------
# Miscelaneous corrections from L-entries.to.fill.and-or.tags.txt
 Note no change at <L<77315
1. corrected add ¦
 <L>135782<pc>685,3<k1>pramanT
1a. Correct info number
 <L>135670.1<pc>685,1<k1>pramanT
 OLD: <info or="135670,pramaT;135782,pramanT"/>
 NEW: <info or="135670,pramaT;135670.1,pramanT"/>

 
2. correct info number
<info or="108451,nid;108659,nind"/>  
<L>108451<pc>547,3<k1>nid<k2>nid<h>1<e>1
3. no change needed
<L>102543<pc>522,3<k1>Dvas<k2>Dvas<h>1<e>1
<hom>1.</hom> <s>Dvas</s>.¦ See <s>DvaMs</s>.
NOTE: 
<L>102398.2<pc>522,1<k1>Dvas
<info or="102398,DvaMs;102398.2,Dvas"/>
<L>102398<pc>522,1<k1>DvaMs
<info or="102398,DvaMs;102398.2,Dvas"/>

4. corrected. Add ¦
<L>72600.1<pc>391,1<k1>cala<k2>cala<e>2E
(<ab>cf.</ab> <s>a-</s>, <s>niS-</s>, <s>puMScalI</s>, <s>cAla</s>.)

5. No change  <<<<
<L>77315<pc>412,3<k1>jamB<k2>jamB<h>1<e>1
<hom>1.</hom> and <hom>2.</hom> <s>jamB</s>. ¦ See √ <hom>1.</hom> and √ <hom>2.</hom> <s>jaB</s>.<info and
 Note:
   <info or="77183,jaB;77183.05,jamB"/> for hom=1
   <info or="77248,jaB;77248.1,jamB"/>  for hom=2

6. corrected. Add ¦
<L>56162<pc>1325,2<k1>kesarin<k2>kesarin<e>2B
¦ <ab>N.</ab> of a <s1 slp1="taTAgata">Tathāgata</s1>, <ls>Sukh. i</ls>.<info n="sup"/><info lex="inh"/>

7. corrected. Add ¦
<L>59840<pc>330,2<k1>kzIv
<s>kzIv</s>, <s>kzIva</s>¦ See √ <s>kzIb</s>.<info verb="root" cp="0"/> <info and

8. corrected Add ¦
<L>40093<pc>231,3<k1>ema
<s>e/ma</s>, <s>am</s>, <s>e/man</s>, <s>a</s>,¦ <lex>n.</lex> course, way, <ls>RV.</ls>; <ls>VS.</ls>; <info lex="n"/><info or="40093,ema;40094,eman"/>
<LEND>

9. corrected Add ¦
<L>40094<pc>231,3<k1>eman
<s>e/ma</s>, <s>am</s>, <s>e/man</s>, <s>a</s>,¦ <lex>n.</lex> course, way, <ls>RV.</ls>; <ls>VS.</ls>; <info lex="n"/><info or="40093,ema;40094,eman"/>
<LEND>
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
263 change transactions from change_1.txt

---------------------------------------------------------------------------
Start with file provided by AB.
cp ~/Downloads/tagged.and-group.entries.split.with.vertical.bar.txt temp_bbar2_input.txt
Use this file to generate changes which add vertical bars.
python bbar2.py temp_bbar2_input.txt temp_mw_1.txt temp_change_bbar2.txt
# manual adjust temp_change_bbar2.txt for
#  those where needed (due to changes not yet in AB version)
# insert temp_change_bbar2.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1669 change transactions from change_1.txt

---------------------------------------------------------------------------
START HERE
There remain some 'and' groups without broken bar
65 matches for "^[^¦]*<info and="" in buffer: temp_mw_1.txt

python make_change_regex.py 1c temp_mw_1.txt temp_change_regex_1c.txt
128 cases written to temp_change_regex_1c.txt
# not sure why the Elisp match shows only 65 cases.
#   maybe the Elisp match spans lines.
# insert temp_change_regex_1c.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1798 change transactions from change_1.txt

Note 1: L= 151238 and 151239 are odd.
Note 2: in L=38955, 38955.1 the <info and> is not in headline, but on next line.

---------------------------------------------------------------------------
 "^<s>X</s> ¦ and <s>Y</s> " -> <s>X</s> and <s>Y</s> ¦ "

python make_change_regex.py 1d temp_mw_1.txt temp_change_regex_1d.txt
27 cases written to temp_change_regex_1d.txt
# insert temp_change_regex_1d.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1825 change transactions from change_1.txt

---------------------------------------------------------------------------

 "^<s>X</s> ¦ and <s>Y</s>," -> <s>X</s> and <s>Y</s>, ¦"
python make_change_regex.py 1e temp_mw_1.txt temp_change_regex_1e.txt
87 cases written to temp_change_regex_1e.txt
# insert temp_change_regex_1e.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1921 change transactions from change_1.txt

---------------------------------------------------------------------------
9 matches for "</s> ¦ and <s>" in buffer: temp_mw_1.txt
These few stragglers done by hand
python make_change_regex.py 1f temp_mw_1.txt temp_change_regex_1f.txt
9 cases written to temp_change_regex_1f.txt
# manually change temp_change_regex_1f.txt
# insert temp_change_regex_1f.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1921 change transactions from change_1.txt

---------------------------------------------------------------------------
---------------------------------------------------------------------------
Now begin changes for 'or' groups
cp temp_mw_1.txt temp_mw_2.txt
touch change_2.txt
---------------------------------------------------------------------------
---------------------------------------------------------------------------

---------------------------------------------------------------------------
6336 matches for "<info or="" in buffer: temp_mw_1.txt
592 matches for "</s> ¦ or <s>" in buffer: temp_mw_1.txt

 "^<s>X</s> ¦ or <s>Y</s>," -> <s>X</s> or <s>Y</s>, ¦"
python make_change_regex.py 2a temp_mw_2.txt temp_change_regex_2a.txt
472 cases written to temp_change_regex_2a.txt
# insert temp_change_regex_2a.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
472 change transactions from change_2.txt

---------------------------------------------------------------------------
49 matches for "<hom>[^<]*</hom> <s>.*?</s> ¦ or <s>.*?</s> " in buffer: temp_mw_2.txt
python make_change_regex.py 2b temp_mw_2.txt temp_change_regex_2b.txt
49 cases written to temp_change_regex_2b.txt
# insert temp_change_regex_2b.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
521 change transactions from change_2.txt

---------------------------------------------------------------------------
7 matches for "<hom>[^<]*</hom> <s>.*?</s> ¦ or <s>[^<]*?</s>,"
NOTE ending comma in above regex
python make_change_regex.py 2c temp_mw_2.txt temp_change_regex_2c.txt
7 cases written to temp_change_regex_2c.txt
# insert temp_change_regex_2c.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
528 change transactions from change_2.txt

---------------------------------------------------------------------------
71 matches for "</s> ¦ or <s>" in buffer: temp_mw_2.txt

python make_change_regex.py 2d temp_mw_2.txt temp_change_regex_2d.txt
71 cases written to temp_change_regex_2d.txt
# manual changes to temp_change_regex_2d.txt
# insert temp_change_regex_2d.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
599 change transactions from change_2.txt

---------------------------------------------------------------------------
"^<s>[^<]*?</s> or <s>[^<]*?</s>, [^¦]*<info or=" 

python make_change_regex.py 2e temp_mw_2.txt temp_change_regex_2e.txt
2464 cases written to temp_change_regex_2e.txt
# insert temp_change_regex_2e.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
3063 change transactions from change_2.txt

---------------------------------------------------------------------------
"^<s>[^<]*?</s> or <s>[^<]*?</s> or <s>[^<]*?</s>, [^¦]*<info or=" 

python make_change_regex.py 2f temp_mw_2.txt temp_change_regex_2f.txt
111 cases written to temp_change_regex_2f.txt
# insert temp_change_regex_2f.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
3174 change transactions from change_2.txt

---------------------------------------------------------------------------
grep -E "^<s>[^¦]*?</s> or <s>[^¦]*?</s> [^¦]*<info or=" temp_mw_2.txt | wc -l
292

python make_change_regex.py 2g temp_mw_2.txt temp_change_regex_2g.txt
292 cases written to temp_change_regex_2g.txt
# manually correct  temp_change_regex_2g.txt
# insert temp_change_regex_2g.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
3466 change transactions from change_2.txt


---------------------------------------------------------------------------
"^<s>[^<]*?</s> or <s>[^<]*?</s>, [^¦]*<info or=" 
Also, allow <srs/>
python make_change_regex.py 2h temp_mw_2.txt temp_change_regex_2h.txt
314 cases written to temp_change_regex_2h.txt
# insert temp_change_regex_2h.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
3780 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>a/MSa—kalpanA</s>, <lex>f.</lex> or <s>a/MSa—prakalpanA</s>, <lex>f.</lex> or <s>a/MSa—pradAna</s>, <lex>n.</lex> allotment of a portion.
'S1, L1 or S2, L2 or S3, L3 '->
'S1, L1 or S2, L2 or S3, L3 ¦ '
python make_change_regex.py 3a temp_mw_2.txt temp_change_regex_3a.txt
15 cases written to temp_change_regex_3a.txt
# insert temp_change_regex_3a.txt into change_2
3795 python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt


---------------------------------------------------------------------------
<s>a/MSa—kalpanA</s>, <lex>f.</lex> or <s>a/MSa—prakalpanA</s>, <lex>f.</lex> or <s>a/MSa—pradAna</s>, <lex>n.</lex> allotment of a portion.
'S1, L1 or S2, L2 '->
'S1, L1 or S2, L2 ¦ '
python make_change_regex.py 3b temp_mw_2.txt temp_change_regex_3b.txt
380 cases written to temp_change_regex_3b.txt
# insert temp_change_regex_3b.txt into change_2
4175 python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt

<s>X</s>, <lex>
---------------------------------------------------------------------------
<s>vanIka</s> (<ls>L.</ls>) or <s>vanIpaka</s> (<ls>L.</ls> and, <ls>Siṃhās.</ls> <ab>v.l.</ab>), <lex>m.</lex> a beggar
'S1 (X1) or S2 (X2), <lex>' ->
'S1 (X1) or S2 (X2), ¦ <lex>'
python make_change_regex.py 3c temp_mw_2.txt temp_change_regex_3c.txt
314 cases written to temp_change_regex_3c.txt
# insert temp_change_regex_3c.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4489 change transactions from change_2.txt

---------------------------------------------------------------------------

'S1 [X1] or S2 [X2], <lex>' ->
'S1 [X1] or S2 [X2], ¦ <lex>'
python make_change_regex.py 3d temp_mw_2.txt temp_change_regex_3d.txt
75 cases written to temp_change_regex_3d.txt
# insert temp_change_regex_3d.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4564 change transactions from change_2.txt

---------------------------------------------------------------------------
'S1 (X1) or S2 (X2), Y' ->
'S1 (X1) or S2 (X2), ¦ Y'
python make_change_regex.py 3c1 temp_mw_2.txt temp_change_regex_3c1.txt
12 cases written to temp_change_regex_3c1.txt
# insert temp_change_regex_3c1.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4576 change transactions from change_2.txt

---------------------------------------------------------------------------

cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
# 
python make_change_regex.py 3e temp_mw_2a.txt temp_change_regex_3e.txt
21 cases written to temp_change_regex_3e.txt
# change _ to <srs/> in temp_change_regex_3e.txt
# insert temp_change_regex_3e.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4597 change transactions from change_2.txt


---------------------------------------------------------------------------
python make_change_regex.py 3f temp_mw_2a.txt temp_change_regex_3f.txt
6 cases written to temp_change_regex_3f.txt
# change _ to <srs/> in temp_change_regex_3f.txt
# insert temp_change_regex_3f.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4603 change transactions from change_2.txt

---------------------------------------------------------------------------

s>tuRi</s>, <s>tu°Rika</s>, <lex>m.</lex>
python make_change_regex.py 3g temp_mw_2a.txt temp_change_regex_3g.txt
131 cases written to temp_change_regex_3g.txt
# change _ to <srs/> in temp_change_regex_3g.txt
# insert temp_change_regex_3g.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4734 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>aMsa-BArika</s>, <lex>mf(<s>I</s>)n.</lex> or <s>aMse-BArika</s>, <lex>mf(<s>I</s>)n.</lex> bearing a burden

python make_change_regex.py 3h temp_mw_2a.txt temp_change_regex_3h.txt
46 cases written to temp_change_regex_3h.txt
# change _ to <srs/> in temp_change_regex_3h.txt
# a few other changes.
# Also, commented out several duplications of prior changes.
# insert temp_change_regex_3h.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4763 change transactions from change_2.txt


---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>u/ttara—prozWapadA</s>, <s>u/ttara—PalgunI</s> or <s>u/ttara—PAlgunI</s>, <lex>f.</lex>

python make_change_regex.py 3i temp_mw_2a.txt temp_change_regex_3i.txt
83 cases written to temp_change_regex_3i.txt
# change _ to <srs/> in temp_change_regex_3i.txt
# a few other changes.
# Also, commented out several duplications of prior changes.
# insert temp_change_regex_3i.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4843 change transactions from change_2.txt
---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>i/zu—Danva/</s> (<ls>TĀr.</ls>) or <s>i/zu—Danvan</s>, <lex>n.</lex>

python make_change_regex.py 3j temp_mw_2a.txt temp_change_regex_3j.txt
55 cases written to temp_change_regex_3j.txt
# change _ to <srs/> in temp_change_regex_3j.txt
# a few other changes.
# insert temp_change_regex_3j.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
4898 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>mahA/—paTa—gama</s>, <lex>m.</lex> (<ls>L.</ls>) or <s>mahA/—paTa—gamana</s>, <lex>n.</lex> (<ls>MW.</ls>) 

python make_change_regex.py 3k temp_mw_2a.txt temp_change_regex_3k.txt
167 cases written to temp_change_regex_3k.txt
# change _ to <srs/> in temp_change_regex_3k.txt
# a few other changes.
# Note some <info lex=".."/> corrections  ARE THERE MORE?
# insert temp_change_regex_3k.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5065 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
17 matches for "^<s>[^<]*</s> and <s>"
# these also require change '<info or=' -> '<info and='

python make_change_regex.py 3l temp_mw_2a.txt temp_change_regex_3l.txt
15 cases written to temp_change_regex_3l.txt
# change _ to <srs/> in temp_change_regex_3l.txt
# insert temp_change_regex_3l.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5080 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>arjunA<srs/>rcana-kalpalatA</s>, <lex>f.</lex> or <s>arjunA<srs/>rcA-pArijAta</s>, <lex>m.</lex>

python make_change_regex.py 3m temp_mw_2a.txt temp_change_regex_3m.txt
52 cases written to temp_change_regex_3m.txt
# change _ to <srs/> in temp_change_regex_3m.txt
# edit . Some corrections to info lex.
# insert temp_change_regex_3m.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5132 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>hitA<srs/>rTam</s> (<ls>R.</ls>) or <s>hitA<srs/>r°TAya</s> (<ls>MBh.</ls>; <ls>R.</ls>), <lex>ind.</lex>

python make_change_regex.py 3n temp_mw_2a.txt temp_change_regex_3n.txt
64 cases written to temp_change_regex_3n.txt
# change _ to <srs/> in temp_change_regex_3n.txt
# insert temp_change_regex_3n.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5196 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>a-ganDi</s> (or <s>a-gan°Din</s>), <lex>mfn.</lex> without smell

python make_change_regex.py 3o temp_mw_2a.txt temp_change_regex_3o.txt
26 cases written to temp_change_regex_3o.txt
# change _ to <srs/> in temp_change_regex_3o.txt
# insert temp_change_regex_3o.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5222 change transactions from change_2.txt
---------------------------------------------------------------------------
<s>A/-gata—nandin</s> [or <s>A/-gata-nardin</s>, <ls>Kāś.</ls>], <lex>mfn.</lex>

python make_change_regex.py 3p temp_mw_2a.txt temp_change_regex_3p.txt
2 cases written to temp_change_regex_3p.txt
# change _ to <srs/> in temp_change_regex_3p.txt
# insert temp_change_regex_3p.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5224 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>kalya—pAla</s>, <lex>mf(<s>I</s>)</lex> or <s>kalya—pAlaka</s>, <lex>mf.</lex>, a distiller

python make_change_regex.py 3q temp_mw_2a.txt temp_change_regex_3q.txt
12 cases written to temp_change_regex_3q.txt
# change _ to <srs/> in temp_change_regex_3q.txt
# some manual changes. 2 false-positives commented out (already marked)
# insert temp_change_regex_3q.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5231 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>gfhIta—cApa</s>, <s>gfhIta—Danus</s>, or <s>gfhIta—Danvan</s>, <lex>mfn.</lex> 
python make_change_regex.py 3r temp_mw_2a.txt temp_change_regex_3r.txt
16 cases written to temp_change_regex_3r.txt
# change _ to <srs/> in temp_change_regex_3r.txt
# insert temp_change_regex_3r.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5247 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>a/-martya—tA</s> [<ls>MBh.</ls>], <lex>f.</lex> or <s>a/-martya—tva</s> [<ls>L.</ls>], <lex>n.</lex>

python make_change_regex.py 3s temp_mw_2a.txt temp_change_regex_3s.txt
10 cases written to temp_change_regex_3s.txt
# change _ to <srs/> in temp_change_regex_3s.txt
# some lex corrections
# insert temp_change_regex_3s.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5257 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>a/rTa—kftya</s>, <lex>n.</lex> [<ls>R.</ls>] or <s>a/rTa—kftyA</s>, <lex>f.</lex> [<ls>Megh.</ls>]

python make_change_regex.py 3t temp_mw_2a.txt temp_change_regex_3t.txt
10 cases written to temp_change_regex_3t.txt
# change _ to <srs/> in temp_change_regex_3t.txt
# some lex corrections
# insert temp_change_regex_3t.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5267 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>nir—ASa—tA</s>, <lex>f.</lex> (<ls>Bhām.</ls>), <s>nir—ASa—tva</s>, <lex>n.</lex> (<ls>Pañc. B.</ls>)

python make_change_regex.py 3u temp_mw_2a.txt temp_change_regex_3u.txt
11 cases written to temp_change_regex_3u.txt
# change _ to <srs/> in temp_change_regex_3u.txt
# some lex corrections
# insert temp_change_regex_3u.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5278 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>ni-Bartsana</s>, <s>ni-Bar°tsayat</s>, <ab>w.r.</ab> for
<s>wowa</s>, <s>wo°wI</s>, <ab>v.l.</ab> for

python make_change_regex.py 3v temp_mw_2a.txt temp_change_regex_3v.txt
47 cases written to temp_change_regex_3v.txt
# change _ to <srs/> in temp_change_regex_3v.txt
# insert temp_change_regex_3v.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5325 change transactions from change_2.txt

---------------------------------------------------------------------------
refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>vEjala-deva</s> or <s>°la-BUpati</s>. See <s>

python make_change_regex.py 3w temp_mw_2a.txt temp_change_regex_3w.txt
18 cases written to temp_change_regex_3w.txt
# change _ to <srs/> in temp_change_regex_3w.txt
# insert temp_change_regex_3w.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5343 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>a-kutra</s> or (<ab>Ved.</ab>) <s>a-kutrA</s>, <lex>ind.</lex>

python make_change_regex.py 3x temp_mw_2a.txt temp_change_regex_3x.txt
2 cases written to temp_change_regex_3x.txt
# change _ to <srs/> in temp_change_regex_3x.txt
# insert temp_change_regex_3x.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5345 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>akza/—nEpuRa</s> or <s>akza/—nEpuRya</s>. <lex>n.</lex>

python make_change_regex.py 3y temp_mw_2a.txt temp_change_regex_3y.txt
12 cases written to temp_change_regex_3y.txt
# change _ to <srs/> in temp_change_regex_3y.txt
# insert temp_change_regex_3y.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5357 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>zarAjima</s>, <s>zarAYjima</s> and <s>zArija</s>, <ab>

python make_change_regex.py 3z temp_mw_2a.txt temp_change_regex_3z.txt
14 cases written to temp_change_regex_3z.txt
# change _ to <srs/> in temp_change_regex_3z.txt
# insert temp_change_regex_3z.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5371 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>agni/—hu/t</s> [<ls>VS.</ls>] or <s>agni/—huta</s>, <lex>mfn.</lex> sacrificed by fire

python make_change_regex.py 4a temp_mw_2a.txt temp_change_regex_4a.txt
12 cases written to temp_change_regex_4a.txt
# change _ to <srs/> in temp_change_regex_4a.txt
# insert temp_change_regex_4a.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5383 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>ISvara—kAraRika</s> (<ls>Jātakam.</ls>), <s>ISvara—kAraRin</s> (<ls>Śaṃk.</ls>), or <s>ISvara—kArin</s> (<ls>Hcar.</ls>), <lex>m.</lex> atheist 

python make_change_regex.py 4b temp_mw_2a.txt temp_change_regex_4b.txt
34 cases written to temp_change_regex_4b.txt
# change _ to <srs/> in temp_change_regex_4b.txt
# insert temp_change_regex_4b.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5417 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>Aptor-yAma</s>, <s>Aptor-yAman</s> = <s>apt°</s>,

python make_change_regex.py 4c temp_mw_2a.txt temp_change_regex_4c.txt
34 cases written to temp_change_regex_4c.txt
# change _ to <srs/> in temp_change_regex_4c.txt
# insert temp_change_regex_4c.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5449 change transactions from change_2.txt

---------------------------------------------------------------------------
#refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>awavi</s>, <s>is</s>, or usually <s>awavI</s>, <lex>f.</lex> ‘place to roam in’

python make_change_regex.py 4d temp_mw_2a.txt temp_change_regex_4d.txt
52 cases written to temp_change_regex_4d.txt
# change _ to <srs/> in temp_change_regex_4d.txt
# manual placement of vertical bar. one 'info or' to 'info and'.
# insert temp_change_regex_4d.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5501 change transactions from change_2.txt

---------------------------------------------------------------------------
#refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt
---------------------------------------------------------------------------
<s>taRqA—pracara</s>, or <s>taRqA—pratara</s>, <lex>m.</lex>

python make_change_regex.py 4e temp_mw_2a.txt temp_change_regex_4e.txt
52 cases written to temp_change_regex_4e.txt
# change _ to <srs/> in temp_change_regex_4e.txt
# manual placement of vertical bar; etc.
# insert temp_change_regex_4e.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5553 change transactions from change_2.txt

---------------------------------------------------------------------------
</s> \[.*?\], <lex

python make_change_regex.py 4f temp_mw_2a.txt temp_change_regex_4f.txt
42 cases written to temp_change_regex_4f.txt
# change _ to <srs/> in temp_change_regex_4f.txt
# manual placement of vertical bar; etc.
# insert temp_change_regex_4f.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5595 change transactions from change_2.txt

---------------------------------------------------------------------------
<s>aja/—loman</s>, <lex>n.</lex>

python make_change_regex.py 4g temp_mw_2a.txt temp_change_regex_4g.txt
87 cases written to temp_change_regex_4g.txt
# change _ to <srs/> in temp_change_regex_4g.txt
# manual placement of vertical bar; etc.
# insert temp_change_regex_4g.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5562 change transactions from change_2.txt

---------------------------------------------------------------------------
#refresh temp_mw_2a.txt
cp temp_mw_2.txt temp_mw_2a.txt
# change <srs/> to _ in temp_mw_2a.txt

---------------------------------------------------------------------------
Most of the rest containing <lex>
python make_change_regex.py 4h temp_mw_2a.txt temp_change_regex_4h.txt
255 cases written to temp_change_regex_4h.txt
# change _ to <srs/> in temp_change_regex_4h.txt
# manual placement of vertical bar; etc.
# insert temp_change_regex_4h.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5835 change transactions from change_2.txt

---------------------------------------------------------------------------
Lines (a) starting with <hom> (b) without ¦ and (c) with <info or=
grep -E "^<hom>[^¦]*<info or=" temp_mw_2.txt | wc -l
9 cases

python make_change_regex.py 4i temp_mw_2.txt temp_change_regex_4i.txt
9 cases written to temp_change_regex_4i.txt
# manual placement of vertical bar; etc.
# insert temp_change_regex_4i.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
 change transactions from change_2.txt

---------------------------------------------------------------------------
# counts of broken bars in headlines
Every entry should have a headline, which should have exactly 1 ¦
Write change transactions for cases failing this.

python bbar1a.py temp_mw_2.txt temp_change_bbar1a_2.txt
287602 metalines
287602 headlines
287593 headlines with 1 ¦
5 headlines with > 1 ¦
4 headlines with 0 ¦
0 non-headlines with 1 or more ¦
9 cases written to temp_change_bbar1a_2.txt

# manual adjust temp_change_bbar1a_2.txt
# insert temp_change_bbar1a_2.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5844 change transactions from change_2.txt


---------------------------------------------------------------------------
# rerun bbar1a
python bbar1a.py temp_mw_2.txt temp_change_bbar1a_2.txt

287602 metalines
287602 headlines
287602 headlines with 1 ¦
0 headlines with > 1 ¦
0 headlines with 0 ¦
0 non-headlines with 1 or more ¦
0 cases written to temp_change_bbar1a_2.txt

now 
a) every headline has exactly 1 ¦,
b) every non-headline has 0 ¦.

This is as it should be.
So we can go on to other aspects.

---------------------------------------------------------------------------
There are still several instances where an 'or' or 'and' group is
not preceded ON THE SAME LINE by ¦.
These are expected to be cases where '<info or/and=' is on a non-headline.
This is known to happen for some common verbs.
We can identify cases with a regex.

grep -E "^[^¦]*<info or=" temp_mw_2.txt | wc -l
213

grep -E "^[^¦]*<info and=" temp_mw_2.txt | wc -l
2

---------------------------------------------------------------------------
cp temp_mw_2.txt temp_mw_3.txt
touch change_3.txt

---------------------------------------------------------------------------
Generate changes to move '<info or="X"/>' markup from a non-headline
to the corresponding headline.
The displays should be unaffected by this.

python bbar3.py temp_mw_3.txt temp_change_bbar3.txt
# insert temp_change_bbar3.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
430 change transactions from change_3.txt

# one xml error correction added to change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
431 change transactions from change_3.txt

# verify all cases accounted for in temp_mw_3.txt
grep -E "^[^¦]*<info or=" temp_mw_3.txt | wc -l
0

grep -E "^[^¦]*<info and=" temp_mw_3.txt | wc -l
0

# verify bbar1 for version 3
python bbar1a.py temp_mw_3.txt temp_change_bbar1a_3.txt
287602 metalines
287602 headlines
287602 headlines with 1 ¦
0 headlines with > 1 ¦
0 headlines with 0 ¦
0 non-headlines with 1 or more ¦
0 cases written to temp_change_bbar1a_3.txt


grep -E "<info or=" temp_mw_3.txt | wc -l
6301
grep -E "<info and=" temp_mw_3.txt | wc -l
1737
---------------------------------------------------------------------------
bbar4 program another consistency check for <info or/and>.
Namely, that each L in and info-or/and has the SAME <info or/and>

python bbar4.py temp_mw_3.txt temp_change_bbar4.txt

---------------------------------------------------------------------------
<info or="104599,navyaDarmitAvacCedakavAdArTa;104600,navyanirmARa;104601,navyamatarahasya;104602,navyamatavAda;104603,navyamatavicAra,104604,navyamatavAdArTa;104605,navyamuktivAdawippanI"/>
# 1. '104603,navyamatavicAra,104604' -> '104603,navyamatavicAra;104604' in
#    7 entries, L=104599-104605.  Add these changes to change_3.txt.
# 2. 11 changes due to typos in the numbers of info or elements.
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
449 change transactions from change_3.txt

---------------------------------------------------------------------------
Some more corrections re broken bar:
Example:
OLD <s>sTA/</s> ¦ (or <s>zWA/</s>), <lex>mfn.</lex>
NEW <s>sTA/</s> (or <s>zWA/</s>), ¦ <lex>mfn.</lex>

python make_change_regex.py 5a temp_mw_3.txt temp_change_regex_5a.txt
27 cases written to temp_change_regex_5a.txt
# insert temp_change_regex_5a.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
476 change transactions from change_3.txt

---------------------------------------------------------------------------
 <s>a/gra—BAga</s> ¦ (or <s>agrA<srs/>MSa</s>), <lex>m.</lex>
   Note the <srs/> in 2nd spelling

python make_change_regex.py 5b temp_mw_3.txt temp_change_regex_5b.txt
5 cases written to temp_change_regex_5b.txt
# insert temp_change_regex_5b.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
481 change transactions from change_3.txt

---------------------------------------------------------------------------
<s>zaq—aha/</s> ¦ (or <s>zaLaha/</s>) <lex>m.</lex>
  Note: no comma after right-paren

python make_change_regex.py 5c temp_mw_3.txt temp_change_regex_5c.txt
88 cases written to temp_change_regex_5c.txt
# insert temp_change_regex_5c.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
569 change transactions from change_3.txt

---------------------------------------------------------------------------
<s>vi-√ maT</s> ¦ (or <s>manT</s>) <ab>P.</ab>
 Note: no lex after right paren.

python make_change_regex.py 5d temp_mw_3.txt temp_change_regex_5d.txt
81 cases written to temp_change_regex_5d.txt
# many manual adjustments.
# markup for some verbs is uncertain
# insert temp_change_regex_5d.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
659 change transactions from change_3.txt

---------------------------------------------------------------------------
<s>a/Ta</s> or <s>a/TA</s> ¦ (or <ab>Ved.</ab> <s>a/TA</s>),
  As previous, but with comma after right paren

python make_change_regex.py 5e temp_mw_3.txt temp_change_regex_5e.txt
50 cases written to temp_change_regex_5e.txt
# many manual adjustments.
# markup for some verbs is uncertain
# insert temp_change_regex_5e.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
711 change transactions from change_3.txt

---------------------------------------------------------------------------
79 matches for "¦ (or "
62 matches for "¦ (or .*<info or="

python make_change_regex.py 5f temp_mw_3.txt temp_change_regex_5f.txt
59 cases written to temp_change_regex_5f.txt
# many manual adjustments.
# markup for some verbs is uncertain
# insert temp_change_regex_5f.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
770 change transactions from change_3.txt

START HERE
---------------------------------------------------------------------------
20 matches for "¦ (or "

Some of these need <info or=""/> markup added

python make_change_regex.py 5g temp_mw_3.txt temp_change_regex_5g.txt
13 cases written to temp_change_regex_5g.txt
# expected 20 cases.
# manual adjustments.
# insert temp_change_regex_5g.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
784 change transactions from change_3.txt

NOTE: 7 matches for "¦ (or "
These don't need to change. They are not part of '<info or' groups.
---------------------------------------------------------------------------
Happened to notice one pattern for missing hom markup.
Might as well change these now, though unrelated to '<info or'.

55 matches for " √ [1-9]\."  missing hom markup

python make_change_regex.py 5h temp_mw_3.txt temp_change_regex_5h.txt
48 cases written to temp_change_regex_5h.txt
# manual adjustments.
# insert temp_change_regex_5h.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
832 change transactions from change_3.txt

---------------------------------------------------------------------------
7 matches for " √ [1-9]"  (no period after hom number

python make_change_regex.py 5i temp_mw_3.txt temp_change_regex_5i.txt
7 cases written to temp_change_regex_5i.txt
# manual adjustments.
# insert temp_change_regex_5i.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
839 change transactions from change_3.txt

---------------------------------------------------------------------------
27 matches for " ¦ [0-9]\. [0-9]\."
OLD: <s>parI-tta</s> <hom>a</hom> ¦ 1. 2. <s>parI-tta</s>.
NEW: <hom>1.</hom> <hom>2.</hom> <s>parI-tta</s> <hom>a</hom> ¦ 

python make_change_regex.py 5j temp_mw_3.txt temp_change_regex_5j.txt
26 cases written to temp_change_regex_5j.txt
# manual adjustments.
# insert temp_change_regex_5j.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
865 change transactions from change_3.txt

---------------------------------------------------------------------------
174 matches for "See under [1-9]+\. <s>"
add hom markup

python make_change_regex.py 5k temp_mw_3.txt temp_change_regex_5k.txt
174 cases written to temp_change_regex_5k.txt
# insert temp_change_regex_5k.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1039 change transactions from change_3.txt

---------------------------------------------------------------------------
33 matches for "under [1-9]\. <s>"
add hom markup

python make_change_regex.py 5l temp_mw_3.txt temp_change_regex_5l.txt
33 cases written to temp_change_regex_5l.txt
# insert temp_change_regex_5l.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1072 change transactions from change_3.txt

---------------------------------------------------------------------------
8 matches for "also [1-9]\. <s>"
add hom markup

python make_change_regex.py 5m temp_mw_3.txt temp_change_regex_5m.txt
8 cases written to temp_change_regex_5m.txt
# insert temp_change_regex_5m.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1080 change transactions from change_3.txt

---------------------------------------------------------------------------
62 matches in 59 lines for "and [1-9]\. <s>"
add hom markup

python make_change_regex.py 5n temp_mw_3.txt temp_change_regex_5n.txt
59 cases written to temp_change_regex_5n.txt
# insert temp_change_regex_5n.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1140 change transactions from change_3.txt

---------------------------------------------------------------------------
14 matches for " or [1-9]\. <s>"

python make_change_regex.py 5o temp_mw_3.txt temp_change_regex_5o.txt
14 cases written to temp_change_regex_5o.txt
# insert temp_change_regex_5o.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1154 change transactions from change_3.txt

---------------------------------------------------------------------------
to, for, with <ab>cf.</ab>
add hom markup
python make_change_regex.py 5p temp_mw_3.txt temp_change_regex_5p.txt
13 cases written to temp_change_regex_5p.txt
# a couple of false-positives
# insert temp_change_regex_5p.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1165 change transactions from change_3.txt

---------------------------------------------------------------------------
<ab>g.</ab> 1. <s>naqA<srs/>di</s>
add hom markup
python make_change_regex.py 5q temp_mw_3.txt temp_change_regex_5q.txt
47 cases written to temp_change_regex_5q.txt
# a couple of false-positives
# insert temp_change_regex_5q.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1212 change transactions from change_3.txt

---------------------------------------------------------------------------
54 matches for "= [0-9]\. <s>"
add hom markup
python make_change_regex.py 5r temp_mw_3.txt temp_change_regex_5r.txt
54 cases written to temp_change_regex_5r.txt
# insert temp_change_regex_5r.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1266 change transactions from change_3.txt

---------------------------------------------------------------------------
449 matches in 380 lines for " [0-9]\. <s>"
but 212 matches in 206 lines for "<ab>cl.</ab> [0-9]\. <s>"

Make temporary version
cp temp_mw_3.txt temp_mw_3a.txt
manually edit it to change
OLD: <ab>cl.</ab> [0-9]\. <s>
NEW: <ab>cl.</ab>_[0-9]\. <s>

python make_change_regex.py 5s temp_mw_3a.txt temp_change_regex_5s.txt
175 cases written to temp_change_regex_5s.txt
# change _ to ' ' in temp_change_regex_5s.txt
# examine  temp_change_regex_5s.txt for changes (and remove false positives)
# insert temp_change_regex_5s.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1410 change transactions from change_3.txt

---------------------------------------------------------------------------
22 matches for "([0-9]\. <s>"
add hom markup
python make_change_regex.py 5t temp_mw_3.txt temp_change_regex_5t.txt
22 cases written to temp_change_regex_5t.txt
# examine  temp_change_regex_5t.txt for changes (and remove false positives)
# insert temp_change_regex_5t.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1432 change transactions from change_3.txt

---------------------------------------------------------------------------
install  temp_mw_3.txt to check xml
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue132
---------------------------------------------------------------------------

---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
Add missed entries
cp temp_mw_3.txt temp_mw_4.txt
# manual changes
-----
<L>146246.1<pc>736,2<k1>bfhadAraRya
 <L>146247<pc>736,2<k1>bfhadAraRyaka
 need new entry bfhadAraRyakopanizad
-----
<L>224188<pc>1104,3<k1>SvaNk
 <L>224188.1<pc>1104,3<k1>SraNk
 need new entry
 <L>224188.2<pc>1104,3<k1>svaNk
-----
<L>224189<pc>1104,3<k1>SvaNg
 <L>224189.1<pc>1104,3<k1>SraNg
 need new entry
 <L>224189.2<pc>1104,3<k1>svaNg
-----
<L>219450<pc>1082,2<k1>SudDasADyavasAnA
 <L>219451<pc>1082,2<k1>SudDasAropA
 Add 3rd alternate 219451.1, SudDasAropalakzaRA
-----
<L>3043<pc>14,2<k1>atinicft
 add <L>3043.1<pc>14,2<k1>atinivft  and <info or
-----
<L>10935<pc>60,1<k1>abandDra
 add <L>10935.1<pc>60,1<k1>abanDra
-----
<L>55568<pc>308,2<k1>kF
  add <L>55568.1<pc>308,2<k1>kf and <info or
-----
<L>58916<pc>325,3<k1>kzan
  add <L>58916.5<pc>325,3<k1>kzaR  and <info or
-----
<L>60633<pc>334,1<k1>kzviq
 add <L>60633.5<pc>334,1<k1>kzvid  (hom 1) and <info or
-----
<L>60652<pc>334,1<k1>kzviq (hom 2) and <info or
 add <L>60652.1<pc>334,1<k1>kzvid
-----
<L>108540<pc>548,2<k1>nidrA
 add <L>108540.1<pc>548,2<k1>nidrE and <info or
-----
<L>219616<pc>1083,1<k1>SuB  
 add <L>219616.1<pc>1083,1<k1>SumB  hom 1 and <info or
-----
<L>233817<pc>1157,2<k1>samavado
 add  <L>233817.1<pc>1157,2<k1>samavadA and <info or
-----
<L>101325<pc>517,1<k1>DItA
 add <L>101325.1<pc>517,1<k1>DIdA  and <info and
-----
<L>75556<pc>404,3<k1>Cad  add <info or
 add ; <L>75556.X<pc>404,3<k1>Cand  hom <info or>
-----

---------------------------------------------------------------------------
# return to topic of consistency in info or/and markup.
# make corrections in temp_mw_5.txt, change_5.txt

cp temp_mw_4.txt temp_mw_5.txt
touch change_5.txt

bbar4 program another consistency check for <info or/and>.

Namely, that each L in and info-or/and has the SAME <info or/and>
Run it now with latest temp_mw_4 - objective to look for inconsitencies

python bbar4.py temp_mw_5.txt temp_change_bbar4_5.txt
3 cases
# manual adjust temp_change_bbar4_5.txt
# insert temp_change_bbar4_5.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
1 change transactions from change_5.txt

python bbar4.py temp_mw_5.txt temp_change_bbar4_5.txt
0 cases

------------------------------
final tally for number of groups
6319 matches for "<info or="
1736 matches for "<info and="
---------------------------------------------------------------------------
install  temp_mw_5.txt to check xml
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue132

---------------------------------------------------------------------------
TODO:
1. 241846 headword spelling? sADAraRAsADAraRAnupasaMhAriviroDin
 (regex_3m)
2. <L>252713<pc>1249,3<k1>soBari
  <L>252713.1<pc>1249,3<k1>soBarI
  soBarI declined as masculine?  or is headword soBarin ?
3. <L>3801.1<pc>1310,1<k1>adButakfzRarAja
  markup of Kṛ° confusing
4. ? <L>48375<pc>273,3<k1>kAmukAyana
<s>kAmukAyana</s> ¦ <lex>m.</lex> (<ab>g.</ab> 1. <s>naqA<srs/>di</s>)
Can find 2 homonyms for 'naq', but no homonyms for 'naqa'
Thus (<ab>g.</ab> <hom>1.</hom> <s>naqA<srs/>di</s>) may be wrong.


-------------------------------------------------------------------------
Push repositories to Github.
 csl-orig  commit 

 mws 
and update the correspondents at Cologne web site.
DONE with this batch of corrections.

End change_5
*************************************************************************
