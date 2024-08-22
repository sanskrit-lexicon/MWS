
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

typos:  These changes made in temp_mw_2.txt (see below)
---
 213583,SarezIkA;213583.1,SarEzIkA
old: div n="P"/> (<s>Sare/zikA</s>) an <ab n="arrow">ar°</ab>
new: div n="P"/> (<s>Sare/zIkA</s>) an <ab n="arrow">ar°</ab>
---
The <L>37448.1 metaline has the <e> within <k2> field as <k2>ulapya^<e>,ulapya/<e>2B
old: <L>37448.1<pc>218,2<k1>ulapya<k2>ulapya^<e>,ulapya/<e>2B
new: <L>37448.1<pc>218,2<k1>ulapya<k2>ulapya^,ulapya/<e>2B

---------------------------------------------------------------
08-13-2024
Sample rewrite of groups:
OLD:
<L>37661<pc>219,3<k1>uSat<k2>uSat<h>1<e>1
<hom>1.</hom> <s>uSat</s>, <s>an</s>, or <s>uSata</s>, <s>as</s>, ¦ <lex>m.</lex> <ab>N.</ab> of a king, <ls>Hariv.</ls><info or="37661,uSat;37661.1,uSata"/><info lex="m"/>
<LEND>
<L>37661.1<pc>219,3<k1>uSata<k2>uSata<h>1<e>1
<hom>1.</hom> <s>uSat</s>, <s>an</s>, or <s>uSata</s>, <s>as</s>, ¦ <lex>m.</lex> <ab>N.</ab> of a king, <ls>Hariv.</ls><info or="37661,uSat;37661.1,uSata"/><info lex="m"/>
<LEND>

NEW:
<L>37661<pc>219,3<k1>uSat<k2>uSat<h>1<e>1
<hom>1.</hom> <s>uSat</s>, <s>an</s>, or <s>uSata</s>, <s>as</s>, ¦ <lex>m.</lex> <ab>N.</ab> of a king, <ls>Hariv.</ls><info or="37661,uSat;37661.1,uSata"/><info lex="m"/>
<LEND>
<L>37661.1<pc>219,3<k1>uSata<k2>uSata<h>1<e>1
 {{Lbody=37661}}
<LEND>

Revisions to hw.py program will use the body lines of 37661
as the body lines of 37661.1.

---------------------------------------------------------------
temp_mw_1.txt Lbody in groups

python convert_lbody.py temp_mw_0.txt temp_mw_1.txt
878258 lines read from temp_mw_0.txt
286491 entries found
8257 entries matching ['<info or="(.*?)"/>', '<info and="(.*?)"/>']
4042 groups
286491 records written to temp_mw_1.txt

jimfu@DESKTOP-6PTUC6R MINGW64 /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue176 (master)
$ wc -l temp_mw_?.txt
   878258 temp_mw_0.txt
   877131 temp_mw_1.txt

-------------------------------------------
Check local installation for temp_mw_1.txt

cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

# -------------------------------------------------------------
revise hw.py in csl-pywork repo to
 make use of the pattern {{Lbody=X}}
redo local install as above with version temp_mw_1.txt

It seems to work!
# -------------------------------------------------------------
temp_mw_2.txt
1. add entries for the 'lost' headwords
2. correct the typos noted above
cp temp_mw_1.txt temp_mw_2.txt
# manual edits of temp_mw_2.txt

-------------------------------------------
Check local installation for temp_mw_2.txt

cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

----------------------
upload version of displays to cologne for examination.
cp /c/xampp/htdocs/cologne/mw/downloads/mwweb1.zip temp_mwweb1_2.zip

****************************************************************
08-16-2024
Conversion between k2 form and Lbody form for alternates.
cdsl prefers the Lbody form.
Andhrabharati prefers the k2 form.

cp temp_mw_2.txt temp_mw_3.txt
# edit temp_mw_3.txt:
- Remove space at the end of metalines 16582 and 46547
- Remove blank line
- OLD: <L>5412.04<pc>27,2<k1>anasTika<k2>anasTi/ka,an-a/sTika<e>1
- NEW: <L>5412.04<pc>27,2<k1>anasTika<k2>anasTi/ka;an-a/sTika<e>1
    Only example of a group alternate with two accent-forms. 
-----------------------
temp_mw_4.txt

463 matches for "<k2>[^<]*," in buffer: temp_mw_3.txt

These are NON-groups. We plan to generate an AB form where
  alternate groups appear in k2 field separated by ','.
  These 463 cases already have a comma in k2 (indicating alternate accents).
  We don't want to treat them as groups.  Thus we need to change
  the comma in these 463 k2s to some other character not in any k2 field for any entry.
  One choice is ';', which is not currently in any 'k2' field.

python k2_comma_semi.py temp_mw_3.txt temp_mw_4.txt
877272 from temp_mw_3.txt
change_line: 463 lines changed
877272 lines written to temp_mw_4.txt
NOTE: I made a mistake here, and did not catch until temp_mw_7.txt !
   The 463 lines were NOT CHANGED.  See temp_mw_8.txt below for correction
   (/ 1848 4) = 462
-------------------------------------------
temp_mw_5.txt
artificial homonyms. There are about 10,000 of these.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/176#issuecomment-2294916790

In temp_mw_4:
5765 matches for "<h>[0-9]+<"          :  real hom in metaline
10220 matches for "<h>[<]*[^0-9]"      :  artificial hom in metaline
10305 matches for "<hom>[^<.]*[^0-9.]" :  artificial hom in text
11562 matches in 9452 lines for "<hom>[0-9]+\.</hom>" : real hom in text

1) From <h>X in metaline, add <info halt="X"/> to last line of entry
2) if X is artificial (non-numeric), then remove <h>X from metaline
3) remove <hom>X</hom> from body of entry when X is artificial

# program constructs temp_mw_5.txt
python artificial.py temp_mw_4.txt temp_mw_5.txt
nmeta= 10284  # metalines changed (remove artificial <h>a, etc.)
nhui= 16049   # <info hui="X"/>  (real AND artificial
nhomui= 10305 # remove <hom>X</hom> when X is artificial.

In temp_mw_5:
5765 matches for "<h>[0-9]+<"          :  real hom in metaline
0     matches for "<h>[<]*[^0-9]"      :  artificial hom in metaline
0     matches for "<hom>[^<.]*[^0-9.]" :  artificial hom in text
11562 matches in 9452 lines for "<hom>[0-9]+\.</hom>" : real hom in text

-------------------------------------------
temp_mw_6
Remove the <info or="X"/> and <info and="X"/>.  These are no longer needed, as
replaced by the {{Lbody=Z}} coding

python remove_and_or.py temp_mw_5.txt temp_mw_6.txt
877272 from temp_mw_5.txt
remove 3202 instances of <info or=".*?"/>
remove 840 instances of <info and=".*?"/>
877272 lines written to temp_mw_6.txt

4311
-------------------------------------------
temp_mw_7.txt
86 matches for "<info orsl=".*?"/>" in buffer: temp_mw_6.txt
14 matches for "orwr" in buffer:

These are also alternates, and thus can be coded with the Lbody method.
cp temp_mw_6.txt temp_mw_7.txt
Manual edit of temp_mw_7.txt as per this example:
{{Lbody=}}
4311 matches for "{{Lbody=[0-9.]+}}" in buffer: temp_mw_7.txt
----
Example:
OLD:
<L>13034<pc>74,3<k1>aBIpAda<k2>aBI-pAda<e>1
<s>aBI-pAda</s> or <s>aBI-pada</s> ¦ See <hom>1.</hom> <s>a-BI</s>.<info orsl="13034,aBIpAda;13034.1,aBIpada"/>
<LEND>
<L>13034.1<pc>74,3<k1>aBIpada<k2>aBI-pada<e>1
<s>aBI-pAda</s> or <s>aBI-pada</s> ¦ See <hom>1.</hom> <s>a-BI</s>.<info orsl="13034,aBIpAda;13034.1,aBIpada"/><info hui="b"/>
<LEND>
NEW:
<L>13034<pc>74,3<k1>aBIpAda<k2>aBI-pAda<e>1
<s>aBI-pAda</s> or <s>aBI-pada</s> ¦ See <hom>1.</hom> <s>a-BI</s>.
<LEND>
<L>13034.1<pc>74,3<k1>aBIpada<k2>aBI-pada<e>1
{{Lbody=13934}}
<LEND>

-------------------------------------------

-------------------------------------------
Changes to display programs:
csl-pywork
1. one.dtd  '<info hui="X"/>

csl-websanlexicon - the following files modified
webtc/dispitem.php
webtc/getwordClass.php
webtc/getword_data.php
webtc1/listhiermodel.php
webtc1/listhierview.php
webtc1/listparm.php
webtc1/main.js


-------------------------------------------
temp_mw_8.txt

Correct the mistake in temp_mw_4 construction.
cp k2_comma_semi.py k2_comma_semi_rev.py
python k2_comma_semi_rev.py temp_mw_7.txt temp_mw_8.txt
877265 from temp_mw_7.txt
change_line: 462 lines changed
877265 lines written to temp_mw_8.txt

diff temp_mw_7.txt temp_mw_8.txt | wc -l
# 1848
Note (/ 1848 4) == 462, as expected.


-------------------------------------------
temp_mw_9.txt 
41 matches for "}}<info hui" in buffer: temp_mw_8.txt

Some of these are 'right' and some are 'wrong.
How to 'handle' cases where we have a group with alternates X and Y
And the 'hom' status of X and Y should be different?


cp temp_mw_8.txt temp_mw_9.txt
Manual edit of temp_mw_9.txt
First, examine all the 41 cases in light of print.
1. Remove the <info hui="n"/> text as above
   e.g. '{{Lbody=3500}}<info hui="1"/>' -> '{{Lbody=3500}}'
2. Correct the <h> attribute of metalines as needed for the 41 cases

-----
Remove <h>n  in :
--- 
<L>3500.1<pc>17,2<k1>atrA<k2>a/-trA<h>1<e>1
---
<L>13324.5<pc>76,3<k1>aByAsam<k2>aBy-Asam<h>1<e>2
<L>13324.6<pc>76,3<k1>aByAse<k2>aBy-Ase<h>1<e>2
<L>13324.7<pc>76,3<k1>aByAsAt<k2>aBy-AsAt<h>1<e>2
<L>13766.1<pc>80,1<k1>Anta<k2>Anta<h>1<e>2
<L>29788.1<pc>170,3<k1>IrmA<k2>IrmA/<h>1<e>1
<L>37661.1<pc>219,3<k1>uSata<k2>uSata<h>1<e>1
<L>97463<pc>500,2<k1>dyotana<k2>dyotana<h>2<e>2
<L>102809.1<pc>524,1<k1>nakla<k2>nakla<h>2<e>1
<L>122887.1<pc>621,3<k1>pArTona<k2>pArTona<h>4<e>1
<L>149877.1<pc>753,1<k1>BAmaka<k2>BAmaka<h>3<e>1
<L>178179.1<pc>881,2<k1>ri<k2>ri<e>1
<L>194790.1<pc>958,3<k1>vicI<k2>vicI<h>1<e>1
<L>224193.1<pc>1104,3<k1>SvaRW<k2>SvaRW<h>2<e>1
<L>229217.1<pc>1132,3<k1>sajj<k2>sajj<h>1<e>1
<L>254842.1<pc>1260,1<k1>stF<k2>stF<h>1<e>1
<L>255336.1<pc>1262,3<k1>zWA<k2>zWA/<h>2<e>2
<L>263654.1<pc>1302,2<k1>hF<k2>hF<h>2<e>1


-------------------------------------------
temp_mw_10.txt
remove all <info hui="[0-9]+"/> from temp_mw_9.txt
These will be inserted in mw.xml (from <h>HOM) in make_xml.py
Note: The <info hui="X"/> where X is not a digit sequence
   remain in temp_mw_10.txt as 'artificial homs'.

python remove_true_hui.py temp_mw_9.txt temp_mw_10.txt
877265 from temp_mw_9.txt
change_line: 5764 lines changed
877265 lines written to temp_mw_10.txt

10277 matches for "<info hui="[a-z0-9]+"/>" in buffer: temp_mw_10.txt
    0 matches for "<info hui="[0-9]+"/>" in temp_mw_10.txt

-------------------------------------------
temp_mw_11.txt
20 or so miscodings in version 10

cp temp_mw_10.txt temp_mw_11.txt
Manual edit

-------------------------------------------
Check local installation for temp_mw_11.txt

cp temp_mw_11.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

-------------------------------------------
Transformation to ab form.
We develop an alternate form (temp_mw_X_ab2.txt) of temp_mw_X.txt for Andhrabharati.
This form is invertible (i.e. programatically equivalent) to temp_mw_X.txt
We do this in two steps

temp_mw_11_ab1.txt
# convert metalines from cdsl form to AB form w.r.t. <h> and <k2>
1. no <h> field in metaline, but put into k2 field
# 
python convert_ab1.py cdsl,ab temp_mw_11.txt temp_mw_11_ab1.txt

# check invertibility
# convert metalines from ab form back to cdsl form
python convert_ab1.py ab,cdsl temp_mw_11_ab1.txt temp_mw_11_ab1_chk.txt
# Is computed form same as original?
diff temp_mw_11.txt temp_mw_11_ab1_chk.txt | wc -l
#0  Yes ---  the process is invertible!

rm temp_mw_11_ab1_chk.txt  # unneeded

-----------------------
temp_mw_11_ab2.txt
Convert groups to AB form
alternate entries indicated by comma-separated fields in k2 field of metaline
The {{Lbody=X}} entries dropped and their k2s are comma-separated and put into k2 of of L=X
Also, the Ls of a group are added as {{X,L1,L2,...}} field of the parent X.

python convert_ab2.py cdsl,ab temp_mw_11_ab1.txt temp_mw_11_ab2.txt
286534 entries found
init_groups_cdsl finds 4311 Lbody entries
282223 records written to temp_mw_11_ab2.txt
282223 new entries written to temp_mw_11_ab2.txt

286538 entries found
282276 new entries written to temp_mw_11_ab2.txt
init_groups_cdsl finds 4311 Lbody entries
-------------------
check invertibility

python convert_ab2.py ab,cdsl temp_mw_11_ab2.txt temp_mw_11_ab2_chk.txt

282223 entries found
init_groups_ab finds 3885 Lgroup entries
286534 records written to temp_mw_11_ab2_chk.txt
286534 entry records written to temp_mw_11_ab2_chk.txt

(- 286534 282223) 4311


diff temp_mw_11_ab1.txt  temp_mw_11_ab2_chk.txt | wc -l
# 0  Confirms invertibility.
----------------------------------------------------------

upload version 11 of displays to cologne for examination.
cp /c/xampp/htdocs/cologne/mw/downloads/mwweb1.zip temp_mwweb1_11.zip

---
08-20-2024
zip temp_mw_11.zip temp_mw_11.txt  # cdsl version
zip temp_mw_11_ab2.zip temp_mw_11_ab2.txt  # ab2 version

-------------------------------------------------------------------------
08-21-2024
temp_mw_12.txt
From issue#174, AB noticed this change
'<ab>Ā.</ab> <ab>P.</ab>' -> '<ab>P.</ab> <ab>Ā.</ab>'

cp temp_mw_11.txt temp_mw_12.txt
Use Emacs to make above change in temp_mw_12.txt
203 occurrences changed.

---------------
Check local installation for temp_mw_12.txt

cp temp_mw_12.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

-------------------------------------------
Transformation to ab form.

python convert_ab1.py cdsl,ab temp_mw_12.txt temp_mw_12_ab1.txt
python convert_ab2.py cdsl,ab temp_mw_12_ab1.txt temp_mw_12_ab2.txt
-------------------
zip temp_mw_12_ab2.zip temp_mw_12_ab2.txt  # ab2 version

***************************************************************
08-21-2024
temp_mw_13.txt
minor correction
cp temp_mw_12.txt temp_mw_13.txt
Manual correction:

L-130326 and L-132942
'<ab>P.</ab> <ab>Ā.</ab>' -> '<ab>Ā.</ab> <ab>P.</ab>'
 correction to my mistake in temp_mw_12.txt
L-91601
 dADikA ¦ -> <s>dADikA</s> ¦
--------------------------------------------------------------
temp_mw_14.txt
removal of slp1 attribute.  This occurs mostly in the <s1> tag
and occasionally in the <ab> tag.

Original purpose of this tag:
 Example: <s1 slp1="vizRu">Viṣṇu</s1>
 Displays could display this as if <s>vizRu</s> which would be,
 with choice of Devanagari output, विष्णु. 
However, this 'feature' no longer seems useful, so the slp1 markup can
be dropped.
I'll generate a list of the altered tags.

python remove_slp1.py temp_mw_13.txt temp_mw_14.txt remove_slp1_s1.txt remove_slp1_ab.txt
877264 from temp_mw_13.txt
change_line_s1: 38300 lines changed
change_line_ab_slp1: 2462 lines changed
877264 lines written to temp_mw_14.txt
52208 lines written to remove_slp1_s1.txt
2627 lines written to remove_slp1_ab.txt

old: <ab n="Terminalia">T°</ab> and <ab n="Puṣa" slp1="puza">P°</ab>
new: <ab n="Terminalia">T°</ab> and <s1>Punar-vasu</s1>
---------------------------------------------------
display changes
csl-pywork:  declare n attribute of s1; remove slp1 attribute
csl-websanlexicon
 basicadjust.php change
  <s1 n="X">Y</s1> -> <ab n="X">Y</ab>
  This allows tooltip X for Y in displays.
csl-apidev

---------------
Check local installation for temp_mw_14.txt

cp temp_mw_14.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

-------------------------------------------
Transformation to ab form.

python convert_ab1.py cdsl,ab temp_mw_14.txt temp_mw_14_ab1.txt
python convert_ab2.py cdsl,ab temp_mw_14_ab1.txt temp_mw_14_ab2.txt
# check
python convert_ab2.py ab,cdsl temp_mw_14_ab2.txt temp_mw_14_ab1_chk.txt
diff temp_mw_14_ab1_chk.txt temp_mw_14_ab1.txt | wc -l
#0 ok
python convert_ab1.py ab,cdsl temp_mw_14_ab1.txt temp_mw_14_chk.txt
diff temp_mw_14.txt temp_mw_14_chk.txt | wc -l
# 0

# remove the chk files
rm temp_mw_14_ab1_chk.txt temp_mw_14_chk.txt
-------------------
zip temp_mw_14_ab2.zip temp_mw_14_ab2.txt  # ab2 version

********************************************************************
08-22-2024
------------------------------------------
comments from AB:
----
L=450  <info lex="m"/>  problem: not at end of entry
L=693  <info lex="m:f:n"/>  similar problem to AB
L=85374 amd 85375 error in tooltip --
   let AB make this and other such correction

------------------------------------------
temp_mw_15.txt
8 corrections in preparation of temp_mw_16.txt
cp temp_mw_14.txt temp_mw_15.txt
manual edit temp_mw_15.txt
 8 cases failed to have all <info/>  AT END of last line
 4 blank lines removed.

Moving info tags to the end of entry
python infotag.py temp_mw_15.txt temp_mw_16.txt
13 lines written to infotag_attr.txt
325 lines written to infotag_notend.txt
0 lines written to infotag_extralast.txt


# chk infotag does nothing on temp_mw_16
mv infotag_attr.txt tempprev_infotag_attr.txt
mv infotag_notend.txt tempprev_infotag_notend.txt

python infotag.py temp_mw_16.txt temp_mw_16_chk.txt
diff temp_mw_16.txt temp_mw_16_chk.txt | wc -l
# 0
rm temp_mw_16_chk.txt # unneeded


--------------------------------------------------

Check local installation for temp_mw_16.txt

cp temp_mw_16.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
# grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue176

-------------------------------------------
Transformation to ab form.

python convert_ab1.py cdsl,ab temp_mw_16.txt temp_mw_16_ab1.txt
python convert_ab2.py cdsl,ab temp_mw_16_ab1.txt temp_mw_16_ab2.txt
# check
python convert_ab2.py ab,cdsl temp_mw_16_ab2.txt temp_mw_16_ab1_chk.txt
diff temp_mw_16_ab1_chk.txt temp_mw_16_ab1.txt | wc -l
#0 ok
python convert_ab1.py ab,cdsl temp_mw_16_ab1.txt temp_mw_16_chk.txt
diff temp_mw_16.txt temp_mw_16_chk.txt | wc -l
# 0

# remove the chk files
rm temp_mw_16_ab1_chk.txt temp_mw_16_chk.txt
-------------------
zip temp_mw_16_ab2.zip temp_mw_16_ab2.txt  # ab2 version
revise this MWS repo and sync to github.
upload temp_mw_16_ab2.zip to the issue176 comments

********************************************************************

