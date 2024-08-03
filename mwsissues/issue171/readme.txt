mwsissues/issue171  hierarchy placement of MW supplement entries.
Begin 07-12-2024

Ref: https://github.com/sanskrit-lexicon/MWS/issues/171

This directory:

cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue171

In mw.txt, the material from the 1899 supplement section has been
integrated into the 'main' text.  However, recent corrections from
Scott Rhodes identified some supplement issues which have been misplaced.


First goal: identify  entries which have been misplaced,
  and move them in mw.txt to where they should be.

cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue171

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  45cad97424c2ab8c9a6bfb7cb8c14c7cc9a508cf  (07-12-2024)

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  45cad9742:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue171/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue171

# -------------------------------------------------------------
Alphabetical misplacements of 'sup' entries.
alphabetical ordering  may be one way to identify.
Hypothetical

python alphasup.py temp_mw_0.txt alphasup.txt
880450 lines read from temp_mw_0.txt
287582 entries found
nonalpha nsup =  6395
# misordered =  216
216 records written to alphasup.txt

# more information needed for correcting to new L
python alphasup1.py temp_mw_0.txt alphasup1.txt

880450 lines read from temp_mw_0.txt
287582 entries found
nonalpha nsup =  6395
# misordered =  216
216 records written to alphasup1.txt
216 lines written to alphasup1.txt

cp alphasup1.txt to alphasup1_edit.txt
# Examine each case, and mark those which can be 'solved'
  Markup example
  OLD: * bahirmAlA 3 144102.1 sup -> ?
  NEW: * bahirmAlA 3 144102.1 sup -> 144148.1
# 149 marked as above.

------------------
# manually construct L_change_01.txt from alphasup1_edit.txt
Format of each line is
LOLD LNEW

------------------
# construct 'standard' change file
python make_change_L.py temp_mw_0.txt L_change_01.txt change_01.txt
------------------
apply the standard change file
python updateByLine.py temp_mw_0.txt change_01.txt temp_mw_0a.txt

# temp_mw_0a.txt:  An implicit assumption of mw.txt is that the
  entries are ordered by L.
  Since our file temp_mw_0a does not fulfill this condition.
  So we must re-order the entries.

# temp_mw_01.txt  sorted by L
python L_order.py temp_mw_0a.txt temp_mw_01.txt
880450 lines read from temp_mw_0a.txt
287582 entries found
287582 records (880445 lines) written to temp_mw_01.txt

Note: Why 5 fewer lines in output?
   Because lines outside of <L>...<LEND> are discarded in output.
   In our example there are 5 such lines
 a) before first <L>
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mw SYSTEM "mw.dtd">
<!-- Copyright Universitat Koln and The Sanskrit Library 2012; for details see MWHeader.xml -->
<mw>
 b) after last <LEND>
</mw>

-------------------
# check validity of temp_mw_01.txt
cp temp_mw_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mwissue171

--------------------------------------------------------------
Review of changes in L_change_01.txt.
However we got these proposed changes, it is useful to review them in
context of the respective versions of mw.txt

Note first parm is option regarding input file L_change_01.txt
 option = 1:  Assume Lold Lnew and use Lold
 option = 2:  Assume Lold Lnew and use Lnew

# context for the OLD L
python L_context.py 1 temp_mw_0.txt L_change_01.txt L_context_01_old.txt

# context for the NEW L
python L_context.py 2 temp_mw_01.txt L_change_01.txt L_context_01_new.txt

# -------------------------------------------------------------

Misc. comments while editing alphasup1.txt
----
OLD: ?
<L>4052<pc>20,1<k1>aDokza<k2>aDo-'kza/<e>3
<s>aDo-'kza/</s> ¦ <lex>mfn.</lex> being below (or not coming up to) the axle, <ls>RV. iii, 33, 9.</ls><info lex="m:f:n"/>
NEW:
<L>4052<pc>20,1<k1>aDoakza<k2>aDo-akza/<e>3
<s>aDo-akza/</s> ¦ <lex>mfn.</lex> being below (or not coming up to) the axle, <ls>RV. iii, 33, 9.</ls><info lex="m:f:n"/>
---
hiving a face  (anyatomuKa)  -> having a face
--- duplicate in suppl
aparaSvas 3 9455 xxx
<L>9455<pc>50,3<k1>aparaSvas<k2>apara—Svas<h>a<e>3
<s>apara—Svas</s> <hom>a</hom> ¦ <lex>ind.</lex> the day after to-morrow, <ls>Gobh.</ls><info lex="ind"/>

<L>9458.1<pc>1314,1<k1>aparaSvas<k2>apara—Svas<h>b<e>3
<s>apara—Svas</s> <hom>b</hom> ¦ <lex>ind.</lex> the day after to-morrow, <ls>Gobh.</ls><info n="sup"/><info lex="ind"/>

---
<L>28744.1<pc>1320,3<k1>itaHpradAna<k2>itaH—pradAna<h>a<e>3
<s>itaH—pradAna</s> <hom>a</hom> ¦ (<s>ita/H</s> also) <lex>n.</lex> oblation from hence, <ls>TS.</ls><info n="sup"/><info lex="n"/>

<L>28745<pc>165,1<k1>itaHpradAna<k2>ita/H-pradAna<h>b<e>3
<s>ita/H-pradAna</s> <hom>b</hom> ¦ <lex>mfn.</lex> offering from hence <ab>i.e.</ab> from this world, <ls>TS.</ls>; <ls>ŚBr.</ls><info lex="m:f:n"/>

---
nizpezavat 3 111005.1 sup  should be 4

--------------------------------------------------------------
installation of temp_mw_01.txt

cp temp_mw_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
# sync csl-orig with github
cd /c/xampp/htdocs/cologne/csl-orig/v02
git add .
git commit -m "MW: sup-replacement.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/171"
git push

End of phase 1 work on issue171. 07-15-2024
*********************************************************************
07-17-2024  legacy directory.  Some files from Cologne server
  relating to additions (ca 2012).

# convert to the xxx.txt form (<L>...<LEND>).
python legacy1/make_add3a.py legacy/ADD3.xml legacy1/add3a.txt
7145 from legacy/ADD3.xml
4 non-standard lines
7141 records written to legacy1/add3a.txt

-------------------------------------------
## supplement entries whose k1 is unknown in current mw
python legacy1/match1.py temp_mw_01.txt legacy1/add3a.txt legacy1/match1.txt
237 records written to legacy1/temp_match1.txt

-------------------------------------------
## current mw-revsup whose k1 is unknown in add3a
python legacy1/match1a.py temp_mw_01.txt legacy1/add3a.txt legacy1/match1a.txt
7141 entries found from add3a
6921 distinct k1 from legacy1/add3a.txt
245 records written to legacy1/match1a.txt

# for correction of typos in headwords
cp legacy1/add3a.txt legacy1/add3b.txt
cp temp_mw_01.txt temp_mw_02.txt

corrections (add3b)
refer: add3b_changes.txt
--------------------
corrections temp_mw_02
refer changes_mw_02.txt
-------------------------------------------
Rerun using temp_mw_02 and add3b
## supplement entries whose k1 is unknown in current mw
python legacy1/match1.py temp_mw_02.txt legacy1/add3b.txt legacy1/match1_rev.txt
880445 lines read from temp_mw_02.txt
287582 entries found
194068 distinct k1 from temp_mw_02.txt
28560 lines read from legacy1/add3b.txt
7140 entries found
41 records written to legacy1/match1_rev.txt

-------------------------------------------
## current mw-revsup whose k1 is unknown in add3b
python legacy1/match1a.py temp_mw_02.txt legacy1/add3b.txt legacy1/match1a_rev.txt
880445 lines read from temp_mw_02.txt
287582 entries found
28560 lines read from legacy1/add3b.txt
7140 entries found
6920 distinct k1 from legacy1/add3b.txt
55 records written to legacy1/match1a_rev.txt

-------------------------------------------
07-19-2024  How to resolve the non-matches of
match1_rev.txt and match1a_rev.txt ?
forcematch.txt
 sample: mw,60622,kzmAvfzan sup,329560,kzmAvfza
  forces kzmAvfzan in mw to match with kzmAvfza in suppl.
 
## supplement entries whose k1 is unknown in current mw
python legacy1/match2.py temp_mw_02.txt legacy1/add3b.txt legacy1/forcematch.txt legacy1/match2.txt
29 from legacy1/forcematch.txt
16 records written to legacy1/match2.txt

-----
python legacy1/match2a.py temp_mw_02.txt legacy1/add3b.txt legacy1/forcematch.txt legacy1/match2a.txt
0 records written to legacy1/match2a.txt
------
add3b
7157 entries
 517 "(in <ab>comp.</ab>"
6640
----
temp_mw_02
6394 "<info n="sup"
 247 "<info n="rev"
6641 (+ 6394 247)

What is that extra one in temp_mw_02 ?

--------------------------------------
python legacy1/remov
cp legacy1/add3b.txt legacy1/add3c.txt
 remove need for forcematch.txt (27 cases)
   by changing the k1 to agree with temp_mw_02

python legacy1/match3.py 1 temp_mw_02.txt legacy1/add3c.txt legacy1/match3_1.txt

6642 suprev entries in mw body
6642 suprev entries in mw supplement
0 lines written to legacy1/match3.txt
mwkeys same as supkeys?: True
# of distinct sup keys= 6442

6642 lines written to legacy1/match3_1.txt

python legacy1/match3.py 2 temp_mw_02.txt legacy1/add3c.txt legacy1/match3_difflib_02.txt
7487 lines

python legacy1/match3.py 3 temp_mw_02.txt legacy1/add3c.txt legacy1/match3_3.txt
7487 lines in match3_3.txt
Output contains mw-suppl. meta-info, using difflib.

xxx = 845  yyy = 845
(- 7487 845) = 6642  Same as number of sup items

-----------------------------------
07-22-2024
--------------
1. install temp_mw_02.txt into csl-orig
cp temp_mw_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../
sh xmlchk_xampp.sh mw
ok
# sync csl-orig with github
cd /c/xampp/htdocs/cologne/csl-orig/v02
git add .
git commit -m "MW: revisions re supplement.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/171 (legacy1)"
git push

--------------
2. sync this repo to Github

End of phase 2 work on issue171. 07-22-2024
*********************************************************************

Begin phase 3 work on issue171. 08-01-2024
# some changes since 07-22-2024 made to csl-orig/mw, so
# temp_mw_02.txt slightly out of date.
Start with temp_mw_03.txt from csl-orig at commit
  b219da352a738c8ab12fd3e0af6d00b69114b72f

cd /c/xampp/htdocs/cologne/csl-orig/
git show  b219da35:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue171/temp_mw_03.txt

----------------------------
temp_mw_03a.txt: 
Add temporary 'org-mode' markup to temp_mw_03.txt:
  
python legacy1/match3_org.py temp_mw_03.txt temp_mw_03a.txt

manual edit temp_mw_03a.txt.
 primarily use the '<OR/>' markup of add3c.txt to reposition groups
   so that group entries are consecutive. Usually this is clear, but sometimes not clear
   due to existing main entries with a group headword
 Another source of reposition is with compounds of 'eka'

cp legacy1/match3_3.txt legacy1/match3_3_edit.txt
Some notes made in this file, but not systematic.

cp temp_mw_03a.txt temp_mw_03b.txt
Remove temporary markup ('*') in temp_mw_03b.txt
'* TODO S <L>' -> <L>
'* DONE S <L>' -> <L>
'* TODO R <L>' -> <L>
'* DONE R <L>' -> <L>
'* <LEND>' -> <LEND>

temp_mw_03b.txt has 7 fewer lines than temp_mw_03.txt
--------------
CHeck for errors.
1. install temp_mw_03b.txt into csl-orig
cp temp_mw_03b.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../
sh xmlchk_xampp.sh mw
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue171

----------------
# recreate the comparison of add3d.txt and the revsup entries of temp_mw_03b.txt
python legacy1/match3.py 3 temp_mw_03b.txt legacy1/add3d.txt legacy1/match3_3b.txt

I do not see how to make further use of match3_3b regarding revsup placement.
----------------
Summarize the metaline differences between temp_mw_0.txt to temp_mw_03b.txt

python legacy1/match4.py 1 temp_mw_0.txt temp_mw_03b.txt legacy1/match4_1_0_03b.txt
  These are the metalines (ignoring <k2>*$) differences whose position changes from
  version 0 of mw to version 03b.
  The lines starting with '+' (266 of them) indicate position changes from version 0 to version 03b.

python legacy1/match3.py 2 temp_mw_03b.txt legacy1/add3d.txt legacy1/match3_difflib_03b.txt
  792 lines start with '+' - These are k1 from version 3b that differ in order from
    the supplement order (as determined from add3d.txt)
    
----------------
The akzoDuka anomaly ...
----------------


*************************
sync with github:
---
  csl-orig
cd /c/xampp/htdocs/cologne/csl-orig/v02/
git add mw/mw.txt
git commit -m "MW: supplement placement.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/171"
git push
---
  csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git add .  # mwab_input.txt
git commit -m "mwab_input.txt correction"
git push
---
  this MWS repo
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue171
git add .
git commit -m "#171 - phase 3"
git push
---------------
sync with Cologne
  csl-orig
  csl-pywork  # a random correction
  remake mw displays

  
