
Begin 08-12-2024

Ref: https://github.com/sanskrit-lexicon/MWS/issues/176

This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  f677a655c4876c7adf668df631317b449d5c2100

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  f677a655c:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue176/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue176

--------------------------------------------------------
Identify the headwords 'lost' in grouping.
First, get a list of the groups which have a '<div n="P"/>' markup.
  The 'lost' headwords will be among these
Dump the 'and/or' groups to a file.For documentation.

python dumpgroups_div.py temp_mw_0.txt dumpgroups_div.txt

278 records written to dumpgroups_div.txt

cp dumpgroups_div.txt dumpgroups_div_missinghw.txt
  edit dumpgroups_div_missinghw.txt and add lines for
  headwords that were (probably) lost (missing) as part of the 
  and-or group standardization.
  ;** hw  
------------------------------

typos:
---
 213583,SarezIkA;213583.1,SarEzIkA
old: div n="P"/> (<s>Sare/zikA</s>) an <ab n="arrow">ar°</ab>
new: div n="P"/> (<s>Sare/zIkA</s>) an <ab n="arrow">ar°</ab>
---
The <L>37448.1 metaline has the <e> within <k2> field as <k2>ulapya^<e>,ulapya/<e>2B
old: <L>37448.1<pc>218,2<k1>ulapya<k2>ulapya^<e>,ulapya/<e>2B
new: <L>37448.1<pc>218,2<k1>ulapya<k2>ulapya^,ulapya/<e>2B

****************************************************************
old notes from issue175
# -------------------------------------------------------------
Step 1:  identify non-sequential or groups.
# Check for internal inconsistencies, and make corrections
cp temp_mw_0.txt temp_mw_1.txt

python nonseq.py or temp_mw_0.txt temp_nonseq_or_0.txt
880411 lines read from temp_mw_0.txt
287570 entries found
6472 entries matching <info or="(.*?)"/>
3198 groups
13 or problems -- see changes_1_readme.txt

---------------------------------------------
python nonseq.py or temp_mw_1.txt nonseq_or_1.txt
0 or problems

python nonseq.py and temp_mw_0.txt temp_nonseq_and_0.txt
2 and problems -- see changes_1_readme.txt

python nonseq.py and temp_mw_1.txt temp.txt
check_groups_2 finds 53 problems

make changes to temp_mw_1.txt and rerun
python nonseq.py and temp_mw_1.txt temp_mw_2a.txt

--------------------------------------------------------
# local install temp_mw_1.txt

cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

---------------------------------------------

temp_mw_2a.txt
; BEGIN case 001: 693,akzIba;693.3,akziba
...
; END case 001: 693,akzIba;693.3,akziba  -- this is estimated.

cp temp_mw_2a.txt temp_mw_2b.txt
 This will allow editing of the ; END ... placement
 NOTE: temp_mw_2b.txt not edited much --  can ignore I think
 
cp temp_mw_2b.txt temp_mw_2c.txt
 temp_mw_2c.txt will rewrite the groups manually
--------------------------------------------------------
# local install temp_mw_2c.txt

cp temp_mw_2c.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

------------------------
Check local install temp_mw_2f.txt

cp temp_mw_2f.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

--------------------------------------------------------

# see if any other 'and' groups that are problematic in 2c
python nonseq.py or temp_mw_2c.txt temp_mw_2d.txt

check_groups_3 finds 326 problems

cp temp_mw_2d.txt temp_mw_2e.txt
manual edit of temp_mw_2e.txt to resolve the 326 problems

... days pass ...  done 2024-08-09

Manual edit done

## rerun to find errors remaining
python nonseq.py or temp_mw_2e.txt temp_mw_2f.txt

879569 lines read from temp_mw_2e.txt
286492 entries found
6493 entries matching <info or="(.*?)"/>
3202 groups
check_groups_1 finds 0 problems
check_groups_2 finds 0 problems
check_groups_3 finds 0 problems
286492 records written to temp_mw_2f.txt

------------------------
Check local install temp_mw_2f.txt

cp temp_mw_2f.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176


python nonseq.py and temp_mw_2e.txt temp_mw_2e_and.txt
1764 entries matching <info and="(.*?)"/>
840 groups
check_groups_1 finds 0 problems
check_groups_2 finds 0 problems
check_groups_3 finds 0 problems

rm temp_mw_2e_and.txt

---------------------------------------------------
Check both 'or' and 'and' groups 
python nonseq1.py 1 temp_mw_2e.txt temp_mw_3a.txt
879569 lines read from temp_mw_2e.txt
286492 entries found
8257 entries matching ['<info or="(.*?)"/>', '<info and="(.*?)"/>']
4042 groups
check_groups_1 finds 0 problems
check_groups_2 finds 0 problems
check_groups_3 finds 0 problems
286492 records written to temp_mw_3a.txt

# note temp_mw_3a.txt is same as temp_mw_2e.txt except for 'case' lines in temp_mw_2e.

python nonseq1.py 2 temp_mw_3a.txt temp_mw_3b_work.txt
878259 lines read from temp_mw_3a.txt
286492 entries found
8257 entries matching ['<info or="(.*?)"/>', '<info and="(.*?)"/>']
4042 groups
check_groups_1 finds 0 problems
check_groups_2 finds 0 problems
check_groups_3 finds 0 problems
check_groups_4 finds 480 problems
286492 records written to temp_mw_3b_work.txt

------------------------------------
# most of these 'problems' are that '<info lex="x"/>` occur differently in the body.
# e.g. the group has mixed genders.  We just remove such 
python change_3b.py temp_mw_3a.txt temp_mw_3b.txt

# rerun nonseq1 with temp_mw_3b.txt
python nonseq1.py 2 temp_mw_3b.txt temp_mw_3b_work.txt
check_groups_4 finds 104 problems

cp temp_mw_3b_work.txt temp_mw_3c.txt
# manual edit 3c to 'correct' the 104 problems

#  rerun nonseq1 with temp_mw_3c.txt
python nonseq1.py 2 temp_mw_3c.txt temp_mw_3c_work.txt
# further edit 3c
# rerun nonseq1 with temp_mw_3c.txt
python nonseq1.py 2 temp_mw_3c.txt temp_mw_3c_work.txt
# no problems identified
# 3c may be the final version!

-------------------------------------------
Check local installation for temp_mw_3c.txt

cp temp_mw_3c.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

-------------------------------------------------------
temp_mw_3d.txt  remove alphabetic homs that occur in the or/and group metalines

10584 matches for "<h>[^0-9<]+<" in buffer:  most of these are <h>[a-z].
These are 'artificial' homs that allow 're-centering' in the list displays.

However, these cannot be kept in the 'and/or' groups

python nonseq1.py 3 temp_mw_3c.txt temp_mw_3c_work.txt
# 326 cases found
rm temp_mw_3c_work.txt  # don't need this -- changes done by change_3d.py program

# auto-correct these 326 (remove the <h>X from matching metaline, when X is non-numeric
python change_3d.py temp_mw_3c.txt temp_mw_3d.txt
327 cases altered by change_3b

rm temp_mw_3c_work.txt  # no further need for this
-------------------------------------------
Check local installation for temp_mw_3d.txt

cp temp_mw_3d.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

-------------------------------------------------------
temp_mw_3e.txt  require a single '<e>' code for all metalines in a group

10584 matches for "<h>[^0-9<]+<" in buffer:  most of these are <h>[a-z].
These are 'artificial' homs that allow 're-centering' in the list displays.

However, these cannot be kept in the 'and/or' groups

python nonseq1.py 4 temp_mw_3d.txt temp_mw_3d_work.txt
check_groups_6 finds 80 problems

cp temp_mw_3d_work.txt temp_mw_3e.txt
#Correct manually in version 3e
#Also, remove '<info lex="inh"/>' from a few groups
rm temp_mw_3e_work.txt  # no longer needed

-------------------------------------------
Check local installation for temp_mw_3e.txt

cp temp_mw_3e.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

--------------------------------------------------------
temp_mw_3f.txt
In 3e there are comments between entries (for purpose of
 review).  These comments are removed for the csl-orig

python cleanup.py temp_mw_3e.txt temp_mw_3f.txt

-------------------------------------------
Check local installation for temp_mw_3f.txt

cp temp_mw_3f.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176
8257 entries matching ['<info or="(.*?)"/>', '<info and="(.*?)"/>']
4042 groups

--------------------------------------------------------
Dump the 'and/or' groups to a file.
For documentation.

python dumpgroups.py temp_mw_3f.txt groups_3f.txt

--------------------------------------------------------
sync csl-orig to github, using version 3f.
sync this MWS repository to github
update cologne server for mw (csl-orig and displays)
***************************************************************
