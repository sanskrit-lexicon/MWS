
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
