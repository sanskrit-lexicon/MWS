MWS/mwsissues/issue15x

Ref: https://github.com/sanskrit-lexicon/MWS/issues/15x

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
 278c0dbe8e8c45bd1c1622ba6250a267658531dd

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  278c0dbe:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue15x/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue15x/

# -------------------------------------------------------------
File lang.string.changes.txt
See: https://github.com/sanskrit-lexicon/mw-dev/issues/7#issue-1576531888

Manually remove Windows line-ending character (Emacs ^M)
File is structured in groups of 5 lines.
line 1 (N): MSG
  N is line number in mw-dev line number. Currently same as in mw.txt
  MSG is a 'filter' codes assigned by Andhrabharati
line 2 OLD\tX
  X is IAST form (from mw_AB.txt ?)
line 3 blank line
line 4 NEW\tX
line 5 ============================

1094 matches for "^=" in buffer: lang.string.changes.txt
 584 matches for ": NO Error" in buffer: lang.string.changes.txt

So 510 sections marked as changed in some way.

line 641 changed:
(102418-9): Misc. [New Tag; Change Tag]
(102418): Misc. [New Tag; Change Tag]
merged the two lines

line 2414 commented out multiline. no error

line 2597

line 3748 ff (531443-4): NO Error   delete section
line 4658 insert blank between OLD and NEW
# -------------------------------------------------------------
Count of groups based on MSG.
python groupcount.py lang.string.changes.txt groupcount.txt

There are 4 major categories:
582 NO Error
280 Misc.
142 Others
88 Greek

# -------------------------------------------------------------
make corrections to Greek text
python change_1.py temp_mw_0.txt lang.string.changes.txt change_1.txt
# manually update change_1.txt.
# then, install the changes into temp_mw_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt

# check work. Use minor variant of change_1.py
python change_1chk.py temp_mw_1.txt lang.string.changes.txt  temp_change_1chk.txt

# -------------------------------------------------------------
Greek character anomaly

;  QUESTION: There are two visually identical characters
; (1) ό  in σϕαδασμός  Greek Small Letter Omicron With Oxia (U+1F79) [3 times in mw]
; (2) ό in σϕεδανός and σϕοδρός.  [171 times in mw]
;  In Emacs, these show as different, but they show as
;  same when I paste into browser.  What is going on?

python unicode_test.py unicode_gk_o_in.txt unicode_gk_o_out.txt

# -------------------------------------------------------------
tonos to oxia accents for other (not omicron) characters
618 matches in 469 lines for "[άέήίύώ]"  (tonos)
# derive frequencies of other Greek chars with tonos accents
python tonos_oxia.py temp_mw_1.txt tonos_oxia.txt
# -------------------------------------------------------------
change tonos to oxio
See comments in issue/153
python change_2_oxio.py temp_mw_1.txt change_2.txt
880519 lines read from temp_mw_1.txt
287605 entries found
select: 151 lines to change
151 records written to change_2.txt

# install change_2 into temp_mw_2.
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
510 change transactions from change_2.txt

# check all oxia are gone
python tonos_oxia.py temp_mw_2.txt tonos_oxia_after.txt
# -------------------------------------------------------------
# -------------------------------------------------------------
make corrections to etym spelling
'Others' Spelling Error
based on lang.string.changes.txt
touch change_3.txt

# Automated change possible (same number of etym elements)
python change_3a.py temp_mw_2.txt lang.string.changes.txt temp_change_3a.txt
# insert temp_change_3a.txt into change_3.txt

# then, install the changes into temp_mw_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
124 change transactions from change_3.txt

------------------------------------
# Manual changes (different number of etym elements)
python change_3b.py temp_mw_3.txt lang.string.changes.txt temp_change_3b.txt
# manual changes to temp_change_3b
# insert temp_change_3b.txt into change_3.txt

# then, install the changes into temp_mw_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
135 change transactions from change_3.txt

Open Questions:
; QUESTION mw_ab  Mark acupedius as 'etym', not 'i'.
line # 97989
;NEW	<s>āśu</s>, ¦ [<ab>cf.</ab> <lang>Gk.</lang> <gk>ὠκύς</gk>, <gk>ὤκιστος</gk>; <lang>Lat.</lang> <etym>acu</etym> in <i>acupedius</i>, <etym>ôcissimus</etym> : of the same origin may be the <lang>Lat.</lang> <etym>aquila</etym> and <etym>accipiter</etym>.]

; QUESTION mw_ab  nose-hole also etym [Note print Not italics?]
line # 352922 
; NEW	 ¦ [<ab>Cf.</ab> <s>nāsā</s>, <s>nāsikā</s>; <lang>Lat.</lang> <etym>nas-turcium</etym>, <etym>nāres</etym>; <lang>Lith.</lang> <etym>nósis</etym>; <lang>Slav.</lang> <etym>nosǔ</etym>; <lang>Germ.</lang> <etym>Nase</etym>; <lang>Angl.Sax.</lang> <etym>nosu</etym>; <lang>Eng.</lang> <etym>nose</etym>, <etym>nostril</etym> = <etym>nose-thrill</etym>, nose-hole.]

*********************************************************************
Misc corrections
touch change_4.txt
cp temp_mw_3.txt temp_mw_4.txt

----------------------
option 1 <lang>Beng.</lang>
  
2 <ns>Bengāli</ns> -> <lang>Bengālī</lang>
3 matches for "Bengālī" in buffer: temp_mw_3.txt
2 <ab>Beng.</ab> -> <lang>Bengālī</lang>
7 matches for "<lang>Beng" temp_mw_AB.txt
7 matches for "<lang>Beng" in buffer: lang.string.changes.txt


python change_4a.py 1 temp_mw_4.txt lang.string.changes.txt temp_change_4a1.txt
7 langgroup NEW instances of <lang>Beng
# insert temp_change_4a1.txt into change_4.txt

# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
7 change transactions from change_4.txt

NOTE: require change to dtd for <lang>x</lang> (with no n attribute)
Also need to revise mw-dev/pywork/mw.dtd (This has been done)

----------------------
option 2 <lang>Prākṛt</lang>
  60 matches for "^NEW	.*Prākṛt" in buffer: lang.string.changes.txt
  244 matches in 238 lines for "Prākṛt" in buffer: temp_mw_AB.txt
  231 matches in 227 lines for "<lang>Prākṛt</lang>" in buffer: temp_mw_AB.txt
  240 matches in 236 lines for "<ns>Prākṛt</ns>" in buffer: temp_mw_4.txt

Note not all the <lang>Prākṛt</lang> instances in mw_AB are not
  mentioned in lang.string.changes.txt.
option 2 will change ALL to <lang>Prākṛt</lang>, ignoring lang.string.changes.
  

python change_4a.py 2 temp_mw_4.txt lang.string.changes.txt temp_change_4a2.txt

write_recs outputs 237 records to temp_change_4a2.txt

# insert temp_change_4a2.txt into change_4.txt

# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
243 change transactions from change_4.txt

# shrink the groups -- exclude cases
# exclude 'NO Error', and 'Greek'
python groupshrink.py 1 lang.string.changes.txt lang.string.changes.1.txt
422 records written to lang.string.changes.1.txt

# Also, exclude Others Spelling Error
python groupshrink.py 2 lang.string.changes.txt lang.string.changes.2.txt
287 records written to lang.string.changes.2.txt

# Also, exclude
  <lang>Prākṛt</lang> and
  <lang>Bengālī</lang> and
  <lang>Beng.</lang>
python groupshrink.py 3 lang.string.changes.txt lang.string.changes.3.txt
221 records written to lang.string.changes.3.txt

--------------------
option 3
'<s1 slp1="pAli">Pāli</s1>'  ->   '<lang>Pāli</lang>'

python change_4a.py 3 temp_mw_4.txt lang.string.changes.txt temp_change_4a3.txt
# 33 records to temp_change_4a3.txt
# insert temp_change_4a3.txt into change_4.txt
 
# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
275 change transactions from change_4.txt

# Also, exclude
  <lang>Pāli</lang>
  
python groupshrink.py 4 lang.string.changes.txt lang.string.changes.4.txt
197 records written to lang.string.changes.4.txt

--------------------
option 4
Persian <lang script="Arabic" n="Persian"> ->
<lang>Persian</lang> <lang script="Arabic" n="Persian">

python change_4a.py 4 temp_mw_4.txt lang.string.changes.txt temp_change_4a4.txt
# 8 records to temp_change_4a4.txt
# insert temp_change_4a4.txt into change_4.txt
 
# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
282 change transactions from change_4.txt

# Also, exclude
  <lang>Persian</lang>
  
python groupshrink.py 5 lang.string.changes.txt lang.string.changes.5.txt
189 records written to lang.string.changes.5.txt

--------------------
option 5
English -> <lang>English</lang>  
12 matches for "<lang>English</lang>" in buffer: temp_mw_AB.txt
16 matches in 15 lines for "English" in buffer: temp_mw_4.txt

python change_4a.py 5 temp_mw_4.txt lang.string.changes.txt temp_change_4a5.txt
# 16 records to temp_change_4a5.txt
# edit temp_change_4a5 and exclude changes not in mw_AB
# insert temp_change_4a5.txt into change_4.txt
 
# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
294 change transactions from change_4.txt



------------------
option 6
<ab>Eng.</ab> <etym>  ->  <lang>Eng.</lang> <etym>
198 matches for "<ab>Eng.</ab> <etym" in buffer: temp_mw_4.txt

190 matches for "<lang>Eng.</lang> <cog>" in buffer: temp_mw_AB.txt
  In mw_AB, use '<cog>' tag
  Example: <lang>Eng.</lang> <cog>coal</cog>

python change_4a.py 6 temp_mw_4.txt lang.string.changes.txt temp_change_4a6.txt
199 records to temp_change_4a6.txt

# insert temp_change_4a6 into change_4.
# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
480 change transactions from change_4.txt

# Also, exclude
  <lang>English</lang>, <lang>Eng.</lang>
  
python groupshrink.py 6 lang.string.changes.txt lang.string.changes.6.txt
145 records written to lang.string.changes.6.txt

------------------
option 7  Misc. Tag

Change many <ab>X</ab> to <lang>X</ab>

python change_4a.py 7 temp_mw_4.txt lang.string.changes.6.txt temp_change_4a7.txt
#988 records to temp_change_4a7
# insert temp_change_4a7 into change_4.
# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
1467 change transactions from change_4.txt


Modified csl-pywork ... make_xml.py and one.dtd
NOTE: This UNDONE at temp_mw_5 below.

# Also, exclude Misc. Tag

python groupshrink.py 7 lang.string.changes.txt lang.string.changes.7.txt
48 records written to lang.string.changes.7.txt

------------------
option 8 The remaining items in lang.string.changes.7.txt

python change_4a.py 8 temp_mw_4.txt lang.string.changes.7.txt temp_change_4a8.txt
#988 records to temp_change_4a8
# manually adjust temp_mw_change_48a
Notes:
1. <div n="cf"/>  is used instead of <div n="vp"?> in <L>28635<pc>164,1<k1>iK
2. <L>42914<pc>248,2<k1>kaDapriya
 150954 <s>adha-priya</s>. -> ? <s>adhapriya</s>.  (end-of-line hyphenation)
3. mw_ab has changed 'v.l.' to 'v. l.' (abbreviation)
4. mw_ab: <L>91851<pc>476,3<k1>dAS  @<div n="cf"/>  why @?
5. mw_ab: *⒉ <s>du</s>,¦ [<ab>cf.</ab> ...  Why *2. ?
  cf.  <L>93282<pc>482,3<k1>du<k2>du<h>2<e>1

# insert temp_change_4a8 into change_4.
# install the changes into temp_mw_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
1515 change transactions from change_4.txt

Add abbreviation for 'Thema'
; <L>8197.05<pc>43,3<k1>antara Theme -> Thema print error
# -------------------------------------------------------------
---------------------------------------------------------------------------
temp_mw_5.txt
Decide to undo the <lang>X</lang> markup.

python change_5_undolang.py temp_mw_4.txt change_5_undolang.txt
1265 records to change_5.txt

python updateByLine.py temp_mw_4.txt change_5_undolang.txt temp_mw_5.txt
1264 change transactions from change_5.txt

python diff_to_changes_dict.py temp_mw_3.txt temp_mw_5.txt change_3_5.txt
90 changes written to change_3_5.txt

python diff
ALSO, revert make_xml.py  and one.dtd

---------------------------------------------------------------------------
summary of all changes  changes.txt

python diff_to_changes_dict.py temp_mw_0.txt temp_mw_5.txt changes.txt
711 changes written to changes.txt
---------------------------------------------------------------------------
---------------------------------------------------------------------------
install  temp_mw_5.txt 
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue153
---------------------------------------------------------------------------
# update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/mw/mw.txt
git commit -m "MW:  Greek and other changes from mw-dev.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/153"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue153
--------------------------------
update mw at at Colgone.
--------------------------------
update this MWS repository
--------------------------------
Revise issue/153  comments
---------------------------------------------------------------------------
changes regarding 'phi' Greek character
---------------------------------------------------------------------------
touch change_6.txt
python change_6_phi.py temp_mw_5.txt temp_change_6.txt
select: 14 lines to change
SMALL LETTER PHI 03C6 changed 15 times
PHI SYMBOL unchanged 72 times
14 records written to change_6.txt

#insert temp_change_6.txt into change_6.txt
# add additional item(s) to change_6
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
15 change transactions from change_6.txt

---------------------------------------------------------------------------
---------------------------------------------------------------------------
In Windows 11,
Consolas represents two phi forms incorrectly.
Cascadia Code font  incorrect
Cascadia mono font  incorrect
Microsoft Sans Serif represents the two phi forms correctly.
  Note:  This font is not monospace.

---------------------------------------------------------------------------
---------------------------------------------------------------------------
install  temp_mw_6.txt 
cp temp_mw_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue153
---------------------------------------------------------------------------
# update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/mw/mw.txt
git commit -m "MW:  Correct 'small phi' to 'phi symbol'.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/153"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue153
--------------------------------
update mw at at Colgone.
--------------------------------
update this MWS repository
--------------------------------
Revise issue/153  comments

---------------------------------------------------------------------------
change_7:  more greek corrections
Based on AB.vs.CDSL.greek.text.differences.txt
cp temp_mw_6.txt temp_mw_7_work.txt
# manually edit temp_mw_7_work.txt
# construct change file for documentation
python diff_to_changes_dict.py temp_mw_6.txt temp_mw_7_work.txt change_7.txt
# 25 changes written to change_7.txt

# construct temp_mw_7.txt from change_7
python updateByLine.py temp_mw_6.txt change_7.txt temp_mw_7.txt
25 change transactions from change_7.txt

# check temp_mw_7.txt = temp_mw_7_work.txt
diff temp_mw_7_work.txt temp_mw_7.txt
# no difference, as expected
# temp_mw_7_work.txt no longer needed.
rm temp_mw_7_work.txt

---------------------------------------------------------------------------
install  temp_mw_7.txt 
cp temp_mw_7.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue153
---------------------------------------------------------------------------
# update csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull
git add v02/mw/mw.txt
git commit -m "MW: corrections from AB.vs.CDSL.greek.text.differences.txt.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/153"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue153
--------------------------------
update mw at at Colgone.
--------------------------------
update this MWS repository
--------------------------------
Revise issue/153  comments

