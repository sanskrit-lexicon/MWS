MWS/mwsissues/issue137

Ref: https://github.com/sanskrit-lexicon/MWS/issues/137

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  07b58cbc6f7cd73ef34113d4f69a526d8ffb01ee

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  07b58cbc:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137/
 
*********************************************************************
BEGIN change_1
cp temp_mw_0.txt temp_mw_1.txt

# Will begin by changing temp_mw_1 manually.
# -------------------------------------------------------------
curly quotes
20724 matches in 18442 lines for "‘"
20723 matches in 18441 lines for "’"

'1 -> ‘  temporary editing convenience
'2 -> ’

NOTE:
1. (- - u u - -) to be changed as (- - ˘ ˘ - -)
  Instead change to (¯ ¯ ˘ ˘ ¯ ¯), as used 48 times elsewhere for meter

# -------------------------------------------------------------
’. 63 instances and .’ 207 instances

All but one of the 63 occurs in supplement, and each is changed as follows:
OLD: according to some ... ‘some text’.
NEW: (according to some ... ‘some text’).   which agrees with print.

the sole occurence outside of supplement is in 
<L>212369<pc>1051,1<k1>SatAvat

after changes ’. 0 instances.


A random small-sample check of print, shows that period precedes closing quote
 ".’" agrees with print.


# -------------------------------------------------------------
touch change_1.txt
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt temp_change_1.txt
217 changes written to temp_change_1.txt
# cp temp_change_1.txt change_1.txt
'first batch miscellaneous changes.'

# -------------------------------------------------------------
[1-3]\. <ab>sg 892 instances and [1-3] <ab>sg 12 instances

Print shows the period following (small random sample)
ADD periods in the 12 cases.
python make_change_regex.py 1 temp_mw_1.txt temp_change_regex_1.txt
11 cases written to temp_change_regex_1.txt
# insert temp_change_regex_1.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
228 change transactions from change_1.txt

# -------------------------------------------------------------
[1-3]\. <ab>du 139 instances and [1-3] <ab>du 1 instance
Add period to the instance
python make_change_regex.py 1a temp_mw_1.txt temp_change_regex_1a.txt
1 cases written to temp_change_regex_1a.txt
# insert temp_change_regex_1a.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
229 change transactions from change_1.txt

# -------------------------------------------------------------
[1-3]\. <ab>pl 839 instances and [1-3] <ab>pl 23 instances
Add period to the instance
python make_change_regex.py 1b temp_mw_1.txt temp_change_regex_1b.txt
23 cases written to temp_change_regex_1b.txt
# insert temp_change_regex_1b.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
252 change transactions from change_1.txt

# -------------------------------------------------------------
<ab>p\.</ab> [0-9]+ 102 instances and <ab>p\.</ab>[0-9]+ 1 instance
add space before page number in the one instance

python make_change_regex.py 1c temp_mw_1.txt temp_change_regex_1c.txt
1 cases written to temp_change_regex_1c.txt
# insert temp_change_regex_1c.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
253 change transactions from change_1.txt

# -------------------------------------------------------------
col\. [0-9]+ 1565 instances and col\.[0-9]+ 2 instances
insert space before column number

python make_change_regex.py 1d temp_mw_1.txt temp_change_regex_1d.txt
3 cases written to temp_change_regex_1d.txt
# insert temp_change_regex_1d.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
256 change transactions from change_1.txt

# -------------------------------------------------------------
missing space before '=': 7 instances
NOTE:  100 cases found by the regex "([^ ([])= ". This includes the
7 cases shown in issue 137 comment.
Note2:  Also, treated preceding open quote like open paren and bracket,
  e.g. "‘=", "(=", and "[="  are asserted 'correct'.
  
python make_change_regex.py 1e temp_mw_1.txt temp_change_regex_1e.txt
100 cases written to temp_change_regex_1e.txt
  Note: the 100 count includes about 20 false-positives for "‘="
# examine cases manually.
# insert temp_change_regex_1e.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
333 change transactions from change_1.txt

# -------------------------------------------------------------
7 matches for "\[[^]]*\["
mismatched square brackets, case 1

python make_change_regex.py 1f temp_mw_1.txt temp_change_regex_1f.txt
5 cases written to temp_change_regex_1f.txt
# examine cases manually.
# insert temp_change_regex_1f.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
338 change transactions from change_1.txt

Note: <L>61654.2<pc>338,2<k1>Kalu has nested brackets [X ... [Y] ...]

includes 3 cases from issues/137: (<L>23929<pc>137,2<k1>AdityaparRikA etc.)
(85683): [<ls>L.</ls> [<ls>L.</ls>]
(85686): [<ls>L.</ls> [<ls>L.</ls>]
(85689): [<ls>L.</ls> [<ls>L.</ls>]

# -------------------------------------------------------------
Line with closing square bracket preceded by no opening square bracket.

python make_change_regex.py 1g temp_mw_1.txt temp_change_regex_1g.txt
38 cases written to temp_change_regex_1g.txt
# examine cases manually. Generally can solve by merging previous line(s).
# insert temp_change_regex_1g.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
427 change transactions from change_1.txt

Note: there remains 1 'insoluble' cases.

216399 old <L>63278<pc>346,1<k1>ganDarva<k2>ganDarva/<e>1
<s>ganDarva/</s> ¦ <lex>m.</lex> a <s1 slp1="ganDarva">Gandharva</s1> [though in later times the <s1 slp1="ganDarva">Gandharva</s1>s are regarded as a class, yet in <ls>RV.</ls> rarely more than one is mentioned;   <<< beginning 

216450 old with <s1 slp1="jEna">Jaina</s1>s the <s1 slp1="ganDarva">Gandharva</s1>s constitute one of the eight classes of the <s1 slp1="vyantara">Vyantara</s1>s]<info lex="m"/>    <<< end of long bracketed section, 
;

# -------------------------------------------------------------
Line with opening square bracket followed by no closing square bracket.

python make_change_regex.py 1h temp_mw_1.txt temp_change_regex_1h.txt
3 cases written to temp_change_regex_1h.txt
# examine cases manually. Solve by merging line(s).
# insert temp_change_regex_1h.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
434 change transactions from change_1.txt

Note: there remains 1 'insoluble' case - the 216399 ganDarva mentioned above.

# -------------------------------------------------------------
NOTE ON FALSE TRAIL !
 I started revisions to have all parenthetical groups to be in ONE LINE.
 About half-way through, I decide this is should not be done now. Perhaps
 it should be done some other time, I'm not sure.
 The partial work is in file 'possible_change_regex_1i.txt'.

Line with closing paren preceded by no opening paren

python make_change_regex.py 1i temp_mw_1.txt temp_change_regex_1i.txt
283 cases written to temp_change_regex_1i.txt
# examine cases manually. Generally can solve by merging previous line(s).
# insert temp_change_regex_1i.txt into change_1
NEXT STEP NOT DONE, ON PURPOSE.
#python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
 change transactions from change_1.txt

Note: utility to print out range of lines for change transactions.
Used in the FALSE TRAIL. Possible useful elsewhere.
$ python make_oldnew_range.py 216872 216878 temp_mw_1.txt temp.txt
# -------------------------------------------------------------
mis-matched pairing of (...).
From https://github.com/sanskrit-lexicon/MWS/issues/137#issuecomment-1199862003
Many of these appear in 'possible_change_regex_1i.txt'
Labled 'temp_change_regex_1i_revised.txt' in change_1.txt

# insert temp_change_regex_1i_revised.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
456 change transactions from change_1.txt

Note: print change
<L>32084.1<pc>1321,3<k1>udaDinemi  Ragh.) : Ragh. : remove paren.

# -------------------------------------------------------------
Error in prior correction:
<L>59608<pc>329,2<k1>kzepaka<k2>kzepaka<e>2A
¦ inserted, interpolated, ; -------------------------------------------------------

This error introduced at
  mwauthorities/ls/issue135/change_2.txt at line 11399:
Correct to
¦ inserted, interpolated, <ls>R. ii, <ab>ch.</ab> 96</ls>, <ab>Sch.</ab>; <ls>Naiṣ. xxii, 48</ls>, <ab>Sch.</ab><info lex="inh"/>
See 'temp_prior_error' section of change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
459 change transactions from change_1.txt

# -------------------------------------------------------------
# Elisp program fragment used in modifying regex_1i.txt above.
(progn
(setq i 92336)
 (while (< i 92346)
  (insert (format "%s old \n" i))
  (insert (format ";\n"))
  (insert (format "%s new \n" i))  
  (insert (format ";\n"))
  (setq i (1+ i))
 )
)
---------------------------------------------------------------------------
# -------------------------------------------------------------
360 matches in 359 lines for "<s>√"
4630 matches in 4385 lines for "√ <s>"
"<s>√ " ->  "√ <s>"  For consistency 

python make_change_regex.py 1j temp_mw_1.txt temp_change_regex_1j.txt
359 cases written to temp_change_regex_1j.txt
# insert temp_change_regex_1j.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
818 change transactions from change_1.txt

# -------------------------------------------------------------
82 matches for "</hom> √"
2315 matches in 2249 lines for "√ <hom>"

Examine print for small sample: "√ <hom>" is found.
Change "</hom> √" to "√ <hom>" for consistency.

python make_change_regex.py 1k temp_mw_1.txt temp_change_regex_1k.txt
82 cases written to temp_change_regex_1k.txt
# insert temp_change_regex_1k.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
900 change transactions from change_1.txt

# -------------------------------------------------------------
'Capital letter following a small letter in a tagged entry'
list of corrections at https://github.com/sanskrit-lexicon/MWS/issues/137#issuecomment-1207244219
Manually enter into change_1.txt at 'temp_change_caplet'
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
911 change transactions from change_1.txt

# -------------------------------------------------------------
Number before <s>
29 matches in 24 lines for "[0-9] <s>"

python make_change_regex.py 1l temp_mw_1.txt temp_change_regex_1l.txt
24 cases written to temp_change_regex_1l.txt
# examine temp_change_regex_1l.txt manually, adjust as needed.
# many false positives.
# insert temp_change_regex_1l.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
916 change transactions from change_1.txt

# -------------------------------------------------------------
14 matches for "[0-9], <s>"

python make_change_regex.py 1m temp_mw_1.txt temp_change_regex_1m.txt
14 cases written to temp_change_regex_1m.txt
# examine temp_change_regex_1m.txt manually, adjust as needed.
# many false positives.
# insert temp_change_regex_1m.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
927 change transactions from change_1.txt
# -------------------------------------------------------------
---------------------------------------------------------------------------
install  temp_mw_1.txt to check xml
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137

# -------------------------------------------------------------
# orphan_broken_bar (3)
Ref: https://github.com/sanskrit-lexicon/MWS/issues/132#issuecomment-1223999614
# added section to change_1.
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
930 change transactions from change_1.txt

# -------------------------------------------------------------
 133 matches in 132 lines for "</s>[0-9]"
   add hom markup.
   Example:
   OLD: <s>raha</s> ¦ <lex>m.</lex> = <s>rahas</s>2 <ls>L.</ls><info lex="m"/>
   NEW: <s>raha</s> ¦ <lex>m.</lex> = <hom>2.</hom> <s>rahas</s>, <ls>L.</ls><info lex="m"/>

python make_change_regex.py 1n temp_mw_1.txt temp_change_regex_1n.txt
130 cases written to temp_change_regex_1n.txt
# examine temp_change_regex_1n.txt manually, adjust as needed.
# insert temp_change_regex_1n.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1060 change transactions from change_1.txt


# -------------------------------------------------------------
   Similarly 15 matches in 14 lines for "</s> [0-9]"

python make_change_regex.py 1o temp_mw_1.txt temp_change_regex_1o.txt
12 cases written to temp_change_regex_1o.txt
# examine temp_change_regex_1o.txt manually, adjust as needed.
# insert temp_change_regex_1o.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1070 change transactions from change_1.txt


# -------------------------------------------------------------
67 matches in 66 lines for "</s> <ls>"
   Normally expect "</s>, <ls>"

python make_change_regex.py 1p temp_mw_1.txt temp_change_regex_1p.txt
68 cases written to temp_change_regex_1p.txt
# examine temp_change_regex_1p.txt manually, adjust as needed.
# insert temp_change_regex_1p.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1140 change transactions from change_1.txt

# -------------------------------------------------------------
4 matches for "</ls><ab>"
expect comma separator

python make_change_regex.py 1q temp_mw_1.txt temp_change_regex_1q.txt
4 cases written to temp_change_regex_1q.txt
# examine temp_change_regex_1q.txt manually, adjust as needed.
# insert temp_change_regex_1q.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1144 change transactions from change_1.txt

# -------------------------------------------------------------
24 matches for "=<s>" in buffer
normally insert space

python make_change_regex.py 1r temp_mw_1.txt temp_change_regex_1r.txt
23 cases written to temp_change_regex_1r.txt
# examine temp_change_regex_1r.txt manually, adjust as needed.
# insert temp_change_regex_1r.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1167 change transactions from change_1.txt

# -------------------------------------------------------------
23 matches for "</s>[a-zA-Z]"
insert space

python make_change_regex.py 1s temp_mw_1.txt temp_change_regex_1s.txt
22 cases written to temp_change_regex_1s.txt
# examine temp_change_regex_1s.txt manually, adjust as needed.
# insert temp_change_regex_1s.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1189 change transactions from change_1.txt

# -------------------------------------------------------------
placement of <info> tags on last line (except for <info or/and=>)
Except for <info or/and.../>, put <info x="y"/> on last line of entry.

python make_change_info.py temp_mw_1.txt temp_change_info.txt
226 records written to temp_change_info.txt
# manual edit of temp_change_info.txt
# insert temp_change_info.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1642 change transactions from change_1.txt

# rerun
python make_change_info.py temp_mw_1.txt temp_change_info_redo.txt
0 entries have exactly 2 line with <info

# -------------------------------------------------------------
13 matches for "[ ][ ]"
Replace with single space. Thought we got rid of these recently.

python make_change_regex.py 1t temp_mw_1.txt temp_change_regex_1t.txt
12 cases written to temp_change_regex_1t.txt
# insert temp_change_regex_1t.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1654 change transactions from change_1.txt

# -------------------------------------------------------------
orsl anomaly <L>248495<pc>1231,3<k1>sumnAya<k2>sumnAya<e>2
orsl anomaly <L>248495.1<pc>1231,3<k1>sumnaya<k2>sumnaya<e>2
move <info orsl=X/> to 'headline' from 'lastline'
Manual addition to change_1 at 'temp_orsl_anomaly'

python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1658 change transactions from change_1.txt

---------------------------------------------------------------------------
install  temp_mw_1.txt to check xml
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137
END change_1

*********************************************************************
BEGIN change_2
cp temp_mw_1.txt temp_mw_2.txt
touch change_2.txt

# -------------------------------------------------------------
Remove space at end of line (1880 instances)

python make_change_regex.py 2a temp_mw_2.txt temp_change_regex_2a.txt
1806 cases written to temp_change_regex_2a.txt
# insert temp_change_regex_2a.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1806 change transactions from change_2.txt

# -------------------------------------------------------------
COMMA AFTER CLOSE-QUOTE
’, 13628 instances and ,’ 33 instances
Examine print for each of the 33 instances.  In all cases, the print
has the comma precede the closing quote !

Examine print for a very small sample of the 13628 cases -
  The print has ",’" COMMA BEFORE QUOTE.
  
Note either form is grammatically acceptable.

Put the comma AFTER the close quote character.

python make_change_regex.py 2b temp_mw_2.txt temp_change_regex_2b.txt
36 cases written to temp_change_regex_2b.txt
# insert temp_change_regex_2b.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1842 change transactions from change_2.txt

NOTE: print change

---------------------------------------------------------------
 semicolon AFTER closing quote  
    Print examined for small random sample - always print shows
    semicolon BEFORE closing quote.

python make_change_regex.py 2c temp_mw_2.txt temp_change_regex_2c.txt
2 cases written to temp_change_regex_2c.txt
# insert temp_change_regex_2c.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1844 change transactions from change_2.txt

NOTE: print change

# -------------------------------------------------------------
446 matches for "p\.[0-9]" in buffer
add space after p.

First, some also need <ab> markup.
 " p.980" -> " <ab>p.</ab> 980"
 
python make_change_regex.py 2d temp_mw_2.txt temp_change_regex_2d.txt
443 cases written to temp_change_regex_2d.txt
# insert temp_change_regex_2d.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
2287 change transactions from change_2.txt

There is one additional (p.488) to change
under <L>93630<pc>484,2<k1>dur
Manually add to change_2.
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
2288 change transactions from change_2.txt

# -------------------------------------------------------------
72 matches for "<ab>col.</ab> [0-9]"
598 matches in 597 lines for "<ab>col.</ab>[0-9]"

Add a space after <ab>col.</ab> in those 598 matches.

python make_change_regex.py 2e temp_mw_2.txt temp_change_regex_2e.txt
598 cases written to temp_change_regex_2e.txt
# insert temp_change_regex_2e.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
2885 change transactions from change_2.txt

# -------------------------------------------------------------
10 matches for [^Lcehm"]>[0-9]
add space after ">" where needed

python make_change_regex.py 2f temp_mw_2.txt temp_change_regex_2f.txt
10 cases written to temp_change_regex_2f.txt
# manually adjust temp_change_regex_2f.txt as needed.
# insert temp_change_regex_2f.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
2895 change transactions from change_2.txt


# -------------------------------------------------------------
4 matches for "[^0-9]\.[0-9]"

python make_change_regex.py 2g temp_mw_2.txt temp_change_regex_2g.txt
4 cases written to temp_change_regex_2g.txt
# manually adjust temp_change_regex_2g.txt as needed.
# insert temp_change_regex_2g.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
2899 change transactions from change_2.txt

---------------------------------------------------------------------------
install  temp_mw_2.txt to check xml
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137

END change_2

*********************************************************************
BEGIN change_3
cp temp_mw_2.txt temp_mw_3.txt
touch change_3.txt

# -------------------------------------------------------------
4622 matches in 4556 lines for "</ls> <ab>Sch.</ab>"
259 matches in 257 lines for "</ls>, <ab>Sch.</ab>"

136 cases  "<ls>Pāṇ.</ls> <ab>Sch.</ab>"
  print without comma:  (not comprehensive)
    <L>180<pc>1,3<k1>akarRya
    <L>2909<pc>13,2<k1>atyUDnI
    <L>4538<pc>22,3<k1>aDIzwa
    <L>8147<pc>43,3<k1>antarvaRam
    <L>9664<pc>52,1<k1>apavAda
    <L>9668<pc>52,1<k1>apavAdasTala
    <L>10969<pc>60,1<k1>abahvac
    <L>13315<pc>76,3<k1>aByavahArya
    <L>17388<pc>99,2<k1>avadAta
    <L>69885<pc>378,1<k1>Gozavat
  print with comma:  (not comprehensive)
    <L>12581<pc>71,1<k1>aBizic
    <L>12849<pc>73,2<k1>aBisambanDa
    <L>109676.1<pc>555,3<k1>nirDAraRa
    <L>126044<pc>635,1<k1>purogantf
    <L>141950<pc>717,2<k1>Palotpatti
    <L>209102.1<pc>1034,1<k1>vyavasTitaviBAzA
    <L>255473.1<pc>1263,2<k1>sTAnivattva

changes to insert the comma.

python make_change_regex.py 3a temp_mw_3.txt temp_change_regex_3a.txt
4556 cases written to temp_change_regex_3a.txt
# insert temp_change_regex_3a.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4556 change transactions from change_3.txt

# -------------------------------------------------------------
2463 matches in 2448 lines for "</s> <ab>q\.v\.</ab>"
195 matches for "</s>, <ab>q.v.</ab>"

  print has "</s>, <ab>q.v.</ab>"  (comma)
NOTE: so far, have found no print examples where the comma is absent.
Add the comma:

python make_change_regex.py 3b temp_mw_3.txt temp_change_regex_3b.txt
2446 cases written to temp_change_regex_3b.txt
# insert temp_change_regex_3b.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
7002 change transactions from change_3.txt

-# -------------------------------------------------------------
<L>65073<pc>355,1<k1>gira
  new entry 65073.1 girA hom 1, and remove from 65073

Add item to change_3.txt under 'temp_65073' section
Note: this is an 'ins' (insert) transaction -- 
  temp_mw_3.txt has 3 more lines than temp_mw_2.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
7006 change transactions from change_3.txt
7003 of type new, 3 of type ins

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
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137

END change_3

*********************************************************************
BEGIN temp_mw_4.txt
119 matches for "^ *$" 
Remove empty lines.

cp temp_mw_3.txt temp_mw_4.txt

# temporary copy of local mw.xml based on temp_mw_3.txt
cp /c/xampp/htdocs/cologne/mw/pywork/mw.xml temp_mw_3.xml
# manually delete the empty lines
  (Emacs delete-matching-lines command)

install  temp_mw_4.txt to check xml
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137

# compare mw.xml made from temp_mw_4
diff temp_mw_3.xml /c/xampp/htdocs/cologne/mw/pywork/mw.xml
92   ##  so 92 lines are different.
But now compare while ignoring white space

diff -w temp_mw_3.xml /c/xampp/htdocs/cologne/mw/pywork/mw.xml
0   NO DIFFERENCE.

END temp_mw_4.txt

*********************************************************************
BEGIN temp_mw_5.txt
cp temp_mw_4.txt temp_mw_5.txt
touch change_5.txt

# -------------------------------------------------------------
204 matches in 203 lines for "\.’"
In at least some of these, the period should be changed to comma.
Example: <L>8937<pc>47,3<k1>aponaptf
OLD: <lex>m.</lex> ‘grandson of the waters.’ <ab>N.</ab> of
NEW: <lex>m.</lex> ‘grandson of the waters’, <ab>N.</ab> of 

Provisionally change to "’." -- will examine individually.
Some will change to "’,".

python make_change_regex.py 5a temp_mw_5.txt temp_change_regex_5a.txt
203 cases written to temp_change_regex_5a.txt
# manually adjust temp_change_regex_5a.txt as needed.
# insert temp_change_regex_5a.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
204 change transactions from change_5.txt

NOTE: exceptions (.’)
1. <L>22937<pc>131,3<k1>AcAryA
 The title <s>AcArya</s> affixed to names of learned men is rather like our ‘Dr.’;
2. <L>60521.1<pc>1325,3<k1>kzoRI, and several more 
 <ab>accord.</ab> to others, ‘flood, stream of water or <s1 slp1="soma">Soma</s1> &c.’

---------------------------------------------------------------
69 matches for " or, "
Often, the comma should be removed (a typo)

python make_change_regex.py 5b temp_mw_5.txt temp_change_regex_5b.txt
69 cases written to temp_change_regex_5b.txt
# manually adjust temp_change_regex_5b.txt as needed. START HERE
# insert temp_change_regex_5b.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
258 change transactions from change_5.txt

---------------------------------------------------------------
Remove ** from 3 lines (correction error correction)

python make_change_regex.py 5c temp_mw_5.txt temp_change_regex_5c.txt
3 cases written to temp_change_regex_5c.txt
# insert temp_change_regex_5c.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
261 change transactions from change_5.txt



# -------------------------------------------------------------
and,  normally there is no comma after 'and'

python make_change_regex.py 5d temp_mw_5.txt temp_change_regex_5d.txt
379 cases written to temp_change_regex_5d.txt
# edit and make manual adjustments.
# insert temp_change_regex_5d.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
626 change transactions from change_5.txt

# -------------------------------------------------------------

"’ <ls>" -> "’, <ls>"

python make_change_regex.py 5e temp_mw_5.txt temp_change_regex_5e.txt
1062 cases written to temp_change_regex_5e.txt
# Confirm comma in a small sample
# insert temp_change_regex_5e.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
1688 change transactions from change_5.txt

# -------------------------------------------------------------
91 matches in 90 lines for "\bin, <ls"
Remove the comma.

python make_change_regex.py 5f temp_mw_5.txt temp_change_regex_5f.txt
88 cases written to temp_change_regex_5f.txt
# Examine a small sample to confirm agreement with print.
# insert temp_change_regex_5f.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
1776 change transactions from change_5.txt

# -------------------------------------------------------------
72 matches for "</s> <ab>Sch.</ab>"
5 matches for "</s>, <ab>Sch.</ab>"

"</s> <ab>Sch.</ab>" -> "</s>, <ab>Sch.</ab>"

python make_change_regex.py 5g temp_mw_5.txt temp_change_regex_5g.txt
72 cases written to temp_change_regex_5g.txt
# Examine a small sample to confirm agreement with print.
# insert temp_change_regex_5g.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
1849 change transactions from change_5.txt

# -------------------------------------------------------------
TODO
"> <ab>e.g.</ab>" => ">, <ab>e.g.</ab>"

python make_change_regex.py 5h temp_mw_5.txt temp_change_regex_5h.txt
255 cases written to temp_change_regex_5h.txt
# Examine a small sample to confirm agreement with print.
# There are a small number of false positives like <ab>ifc.</ab> <ab>e.g.</ab>;
#  I caught a few of these, but did not examine print for all instances.
# insert temp_change_regex_5h.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
2101 change transactions from change_5.txt

# -------------------------------------------------------------
240 matches in 228 lines for "[a-z] <ab>e.g.</ab>
Generally need a comma X, <ab>e.g.</ab>
Insert the comma

python make_change_regex.py 5i temp_mw_5.txt temp_change_regex_5i.txt
228 cases written to temp_change_regex_5i.txt
# Examine a small sample to confirm agreement with print.
# There are a small number of false positives like <ab>ifc.</ab> <ab>e.g.</ab>;
#  I caught a few of these, but did not examine print for all instances.
# insert temp_change_regex_5i.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
2329 change transactions from change_5.txt

# -------------------------------------------------------------
4 matches for "Â" (this character is an occasional Emacs artifact.
  it occurs when Emacs does not auto-detect UTF-8 encoding of unicode.)

Noticed during creation of iast version (see below)

python make_change_regex.py 5j temp_mw_5.txt temp_change_regex_5j.txt
4 cases written to temp_change_regex_5j.txt
# manually correct.
# insert temp_change_regex_5j.txt into change_5
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
2333 change transactions from change_5.txt

# -------------------------------------------------------------

END change_5

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
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137

# -------------------------------------------------------------
# iast version of mw.txt for AB
cd ../../mwtranscode
python mw_transcode.py slp1 roman ../mwsissues/issue137/temp_mw_5.txt ../mwsissues/issue137/temp_mw_5_iast.txt

#confirm invertibility:
python mw_transcode.py roman slp1 ../mwsissues/issue137/temp_mw_5_iast.txt ../mwsissues/issue137/temp_mw_5_slp1.txt

diff ../mwsissues/issue137/temp_mw_5.txt ../mwsissues/issue137/temp_mw_5_slp1.txt
# no difference

cd ../mwsissues/issue137/

--------------------------------------------------------- ---------
Push repositories to Github.
 csl-orig  commit dc533ea2d59092faae2536f23b3da23fb960e43e


and update the correspondents at Cologne web site.

DONE with this batch of corrections.

*********************************************************************
 correct two errors. modify change_5.txt
  see '<ls n="x"> *<ab>y</ab> ...</ls>' section in change_5.
1. Careless mistake: delete '**' characters used in manual changes. 200+ lines
2. A subtle mistake:  'diS' did not display (empty output).
   Cause:  a form '<ls n="Ratn."> <ab>Introd.</ab> 6</ls>'
   Similar form in 'tAqakA': '<ls n="R."><ab>G</ab> 27, 25 ff.</ls>'
   No other similar forms found.

python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
2335 change transactions from change_5.txt

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
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue137

# -------------------------------------------------------------
# iast version of mw.txt for AB
cd ../../mwtranscode
python mw_transcode.py slp1 roman ../mwsissues/issue137/temp_mw_5.txt ../mwsissues/issue137/temp_mw_5_iast.txt

#confirm invertibility:
python mw_transcode.py roman slp1 ../mwsissues/issue137/temp_mw_5_iast.txt ../mwsissues/issue137/temp_mw_5_slp1.txt

diff ../mwsissues/issue137/temp_mw_5.txt ../mwsissues/issue137/temp_mw_5_slp1.txt
# no difference

cd ../mwsissues/issue137/
rm temp_mw_5_slp1.txt

--------------------------------------------------------- ---------
Push repositories to Github.
 csl-orig  commit c85945ddd95e26718a5cc21653943c48f3150ed1


and update the correspondents at Cologne web site.

DONE with corrections to temp_mw_5.txt in change_5.txt.

*************************************************************************

---------------------------------------------------------------
OPEN QUESTIONS, FOR POSSIBLE FUTURE EXAMINATION
-----
# -------------------------------------------------------------
27480 matches in 24359 lines for "A<srs/>"
There are cases where A<srs/>  should be a^
 One instance of this error was noticed under
 <L>293<pc>2,2<k1>akuDryaYc where
 <s>A<srs/>k</s> is now changed to <s>a^k</s>.
 How to find others?
 
--
examine this revision   NO ACTION AT THIS TIME
<L>52328<pc>292,2<k1>kumAradezRa<k2>kumAra—dezRa<e>3
<s>kumAra—dezRa</s> ¦ <lex>mfn.</lex> granting perishable gifts [‘whose gifts are like those of children,’ <ab>i.e.</ab> ‘who gives and takes back’ <ls>Sāy.</ls>], <ls>RV. x, 34, 7.</ls> <info n="rev" pc="1325,1"/><info lex="m:f:n"/>
<LEND>
-----
examine this revision  NO ACTION AT THIS TIME
<L>100080<pc>511,2<k1>DarmaDft<k2>Darma—Df/t<e>3
<s>Darma—Df/t</s> ¦ <lex>mfn.</lex> ‘upholding order,’ applied to the gods, <ls>AV.</ls> <info n="rev" pc="1329,2"/><info lex="m:f:n"/>
<LEND>


# -------------------------------------------------------------
2489 matches in 2427 lines for "</ab> <ls>"
Should some categories have "</ab>, <ls>" ?

