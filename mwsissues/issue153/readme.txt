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

*********************************************************************
Extract the references to '<s>[^<]*\.'

python make_change.py temp_mw_0.txt change_1.txt

880519 lines read from temp_mw_0.txt
287605 entries found
select 19 entries matching "<s>a.s°</s>"

# manually change 'new' lines in change_1.txt 
# apply changes, getting temp_mw_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt

18 change transactions from change_1.txt

# -------------------------------------------------------------
---------------------------------------------------------------------------
install  temp_mw_1.txt 
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue15x


 
