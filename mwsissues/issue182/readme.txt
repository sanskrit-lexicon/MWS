12-09-2024. 

Ref: https://github.com/sanskrit-lexicon/MWS/mwsissues/182
   BHĀGAVATAPURĀṆA link target

   standardization of sch links for 'BhP.'
BHĀG. P. akarAla

this directory:
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue182

----
Start with mw.txt from csl-orig at latest commit
   8ddb1f0ef6e320fbc5d545ee33ee29649400d402
cd /c/xampp/htdocs/cologne/csl-orig
git show 8ddb1f0ef:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue182/temp_mw_0.txt

-----------------------------------------------
There are numerous non-standard aspects of <ls>
 e.g. '<ls>Suśr.</ls> 1, 27, 14.' -> '<ls>Suśr. 1,27,14.</ls>'
This applies to all ls with parameters, not only "Bhāg\. P\."

This change only within <lsX</ls>
# insert spaces.  This is so related programs will work more readily.
python link_prepare.py 1 temp_mw_0.txt temp_mw_1.txt
877279 read from temp_mw_0.txt
40894 lines changed
877279 lines written to temp_mw_1_ls.txt

# Because this change affects so many lines,
# temp_mw_1.txt is installed in csl-orig.

----
# local install and check
sh redo_mw.sh 1
# ok

# sync csl-orig to github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # mw.txt
git commit -m "MW: ', N' -> ',N' in <lsX</ls> (where N is a digit sequence)' 
Ref: https://github.com/sanskrit-lexicon/MWS/issues/182"
# 40894 lines changed. 
git push

-----------------------------------------------
-----------------------------------------------
baseline: all links
8803 matches in 8558 lines for "BhP\." in mw.txt
6967 matches in 6953 lines for "<ls>BhP\.</ls>"
1496 matches in 1487 lines for "<ls>BhP\. [ivx]" 

-----------------------------------------------

python link_prelim2.py temp_mw_1.txt link_prelim2_1.txt
 8483 <ls>BhP..*?</ls>
  320 <ls n="BhP..*?</ls>
 8803 Total

python summary.py 1 temp_mw_1.txt bhagp_standard_1.txt bhagp_nonstandard_1.txt
8803 instances of ls
8408 cases written to bhagp_standard_1.txt
395 cases written to bhagp_nonstandard_1.txt


python check_bur.py link_prelim2_1.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index

216 matches for "<ls>BhP. [ivx]+\.?</ls>"
94 matches for "<ls n="BhP.">[ivx]+\.?</ls>"
19 matches for "<ls>BhP. [ivx]+ [f]+\.?</ls>
5 matches for "<ls>BhP., <ab>Introd.</ab></ls>"
7 matches for "<ls n="BhP.">[ivx]+ f.</ls>"
25 matches for "<ls>BhP. [ivx]+,[0-9]+\.?</ls>"
2 matches for "<ls>BhP.*?[()]"
3 matches for "<ls n="BhP. [ixv]+,">[0-9]+\.?</ls>"
4 matches for "<ls n="BhP.">[ixv]+,[0-9]+\.?</ls>"
2 matches for "<ls>BhP. [ivx]+,[0-9]+ f.</ls>"

-----------------
readme_change_2.txt

-------------------------------
implement above changes
cp temp_mw_1.txt temp_mw_2.txt
 Manual edit of temp_mw_2.txt

python diff_to_changes_dict.py temp_mw_1.txt temp_mw_2.txt change_2.txt
59 changes written to change_2.txt
------
python link_prelim2.py temp_mw_2.txt link_prelim2_2.txt
 8482 <ls>BhP..*?</ls>
  322 <ls n="BhP..*?</ls>
 8804 Total

python summary.py 1 temp_mw_2.txt bhagp_standard_2.txt bhagp_nonstandard_2.txt
8804 instances of ls
findall_ls_entries: number of lines with duplicates= 0
8423 cases written to bhagp_standard_2.txt
381 cases written to bhagp_nonstandard_2.txt

# sort standard. Display parameters (with skandha roman numeral), and frequency.
python summary.py 2 temp_mw_2.txt  bhagp_verse_2.txt
8804 instances of ls
1260 cases written to bhagp_verse_2.txt

python check_bur.py link_prelim2_2.txt Burnouf.BhP.index.txt temp_check_bur.txt
0 links incompatible with index

--------------------------------------------
Install version 2 and sync csl-orig to github

sh redo_mw.sh 2

-------------------
# sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # mw.txt
git commit -m "MW: standardization of links for 'BhP.'
Ref: https://github.com/sanskrit-lexicon/MWS/mwsissues/issue182"
#  
git push

--------------------------------------------
--------------------------------------------

--------------------------------------------
Installation version 2
--------------------------------------------
# local installation
sh redo_mw.sh 2
# ok
-----------------------------------
# sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # mw.txt
git commit -m "MW: standardization of links for 'BhP.'
Ref: https://github.com/sanskrit-lexicon/MWS/mwsissues/issue182"
# 59  lines changed.
git push

-----------------------------------
# update csl-corrections/dictionaries/mw/mw_printchange.txt
  (refer readme_change_2.txt)

# sync csl-corrections to Github
cd /c/xampp/htdocs/cologne/csl-corrections

git add . # mw.txt
git commit -m "MW: standardization of links for 'BhP.'
Ref: https://github.com/sanskrit-lexicon/MWS/mwsissues/issue182"

git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue182

---------------------------------------------------------
version 3.  This undoes the format change of version 1,

python link_prepare.py 2 temp_mw_2.txt temp_mw_3.txt

Also, manual edit of temp_mw_3.txt to remove 3 blank lines introduced in version 2

--------------------------------------------
Installation version 3
--------------------------------------------
# local installation
sh redo_mw.sh 3
# ok
-----------------------------------
# sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # mw.txt
git commit -m "MW: restore spaces in <ls>: ',N' -> ', N' (N a digit)
Ref: https://github.com/sanskrit-lexicon/MWS/mwsissues/issue182"
# 40894 insertions(+), 40897 deletions
git push

-----------------------------------
Sync Cologne server to github
1. csl-orig repo pull
2. csl-corrections pull
3. csl-pywork/v02  remake displays for mw

-----------------------------------
sync this MW repo to github.
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue182
git add .
git commit -m "standardize links for 'BhP.' #182"

git push
============================================================
12-10-2024
version 4
Ref: https://github.com/sanskrit-lexicon/mws/issues/182#issuecomment-2530678105

L-27712.2 data should not be "deleted",
but is to be "relocated" as L-27713.2
   (it being a different HW "ā-śrāva", from "2. ā-śrava")!
 Note: 
-------

cp temp_mw_3.txt temp_mw_4.txt
Manual edit of temp_mw_4.txt 
OLD:
<L>27713.1<pc>1320,2<k1>ASravaRam<k2>A-SravaRam<e>2B
<s>A-SravaRam</s> ¦ <lex>ind.</lex> up to the ear, <ls>Naiṣ.</ls><info n="sup"/><info lex="ind"/>
<LEND>
<L>27713.2<pc>1320,2<k1>ASrAvitapratyASrAvita<k2>ASrAvita-pratyASrAvita<e>2
<s>ASrAvita-pratyASrAvita</s> ¦ <lex>n.</lex> <ab>du.</ab> address and response, <ls>JaimUp.</ls><info n="sup"/><info lex="n"/>
<LEND>
NEW:
<L>27713.1<pc>1320,2<k1>ASravaRam<k2>A-SravaRam<e>2B
<s>A-SravaRam</s> ¦ <lex>ind.</lex> up to the ear, <ls>Naiṣ.</ls><info n="sup"/><info lex="ind"/>
<LEND>
<L>27713.2<pc>1320,2<k1>ASrAva<k2>A-SrAva<e>2  
<s>A-SrAva</s> ¦ <ab>w.r.</ab> for <s>A-srAva</s>.<info n="sup"/>
<LEND>
<L>27713.3<pc>1320,2<k1>ASrAvitapratyASrAvita<k2>ASrAvita-pratyASrAvita<e>2
<s>ASrAvita-pratyASrAvita</s> ¦ <lex>n.</lex> <ab>du.</ab> address and response, <ls>JaimUp.</ls><info n="sup"/><info lex="n"/>
<LEND>

--------------------------------------------
Installation version 4
--------------------------------------------
# local installation
sh redo_mw.sh 4
# ok
-----------------------------------
# sync csl-orig to Github
cd /c/xampp/htdocs/cologne/csl-orig

git add . # mw.txt
git commit -m "MW: correction
Ref: https://github.com/sanskrit-lexicon/mws/issues/182#issuecomment-2530678105"
# 4 lines changed
git push
xxx
-----------------------------------
Sync Cologne server to github
1. csl-orig repo pull
2. csl-pywork/v02  remake displays for mw

-----------------------------------
sync this MW repo to github.
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue182
git add .
git commit -m "Ref: https://github.com/sanskrit-lexicon/mws/issues/182#issuecomment-2530678105"

git push
============================================================

