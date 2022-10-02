MWS/mwsissues/issue141

Ref: https://github.com/sanskrit-lexicon/MWS/issues/141

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  0e5c12526e769cda439a5fb29e1ea05fcfbd36bd
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0.txt in this directory
  git show  0e5c1252:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141/temp_mw_0.txt
# Also, get copies of pw.txt and pwg.txt
# generate temp_pwg_0.txt in this directory
  git show  0e5c1252:v02/pwg/pwg.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141/temp_pwg_0.txt
# generate temp_pw_0.txt in this directory
  git show  0e5c1252:v02/pw/pw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141/temp_pw_0.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141/
 
*********************************************************************
headword svarita accents in pwg and mw
470 matches for "<k2>.*\^" in buffer: temp_pwg_0.txt
114 matches for "<k2>.*\^" in buffer: temp_mw_0.txt
Note: vast majority are words with 'ya' suffix.
90 matches for "<k2>.*ya\^<" in buffer: temp_mw_0.txt

*********************************************************************
svarita_mw_0.txt
A list of the 114 metalines with a svarita accent.
These examined individually in mw scan.
Those with agreement marked with '+'
Those with disagreement marked with '-'
# cp temp_mw_0.txt temp_mw_0_work.txt
# make changes in temp_mw_0_work.txt manually, based on svarita_mw_0.txt.
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_0_work.txt temp_change_mw_1.txt
32 changes written to temp_change_mw_1.txt
# check
python updateByLine.py temp_mw_0.txt temp_change_mw_1.txt temp_mw_1.txt
32 change transactions from temp_change_mw_1.txt
diff temp_mw_0_work.txt temp_mw_1.txt
# no diff, as expected.
# annotate change_mw_1.txt a bit
cp temp_change_mw_1.txt change_mw_1.txt
change_mw_1.txt change transactions for those marked with '-'
python updateByLine.py temp_mw_0.txt change_mw_1.txt temp_mw_1.txt
*********************************************************************
find_accent_diff is minor rewrite of
Dhaval's MWS/accent_diff/find_accent_diff.py.
Only operational difference is that two different dictionary filenames
are provided, rather than dictionary codes.
python find_accent_diff.py temp_mw_0.txt temp_pwg_0.txt find_accent_diff_pwg.txt
diff find_accent_diff_pwg.txt ../../accent_diff/log.tsv
# no difference.
# NOTE: I have not done anything further with find_accent_diff_pwg.txt

*********************************************************************
find_accent_diff1 option 0,0 considers cases where
1. each  dictionary has any accent
python find_accent_diff1.py 0,0 temp_mw_0.txt temp_pwg_0.txt tempad_mw_0_pwg_0.txt
2. removes k2 hyphens (i.e., allow hyphens in k2).
3. Also print a 4th field, the 'pc' values for the k1 of dict1.
3169 differences written to tempad_mw_0_pwg_0.txt

*********************************************************************
find_accent_diff1 option 0,1 considers cases where
1a. 1st dictionary has any accent
1b. 2nd dictionary has svarita accent
2. removes k2 hyphens (i.e., allow hyphens in k2).

python find_accent_diff1.py 0,1 temp_mw_1.txt temp_pwg_0.txt tempad_mw_0_pwg_1.txt
343 differences written to tempad_mw_0_pwg_1.txt
This file edited and renamed to ad1.txt
It serves as a guide to the next set of corrections to MW.

*********************************************************************
Options are X  ?  +.  (refer ad1.txt)
; X means MW typo, need to change / to ^
; ? means not simple in some way
; + means MW confirmed to use / in print. no change to be made.

# first, the 'X' option
python ad_change2.py 'X' ad1.txt temp_mw_1.txt temp_change_mw_2a.txt
528 changes written to temp_change_mw_2a.txt
# edit temp_change_mw_2a.txt.
# insert temp_change_mw_2a.txt into change_mw_2.txt

python updateByLine.py temp_mw_1.txt change_mw_2.txt temp_mw_2.txt
1038 change transactions from change_mw_2.txt
---------------------------------------------------------------------
# next, the '?' cases
START: write make_changes_2 function
python ad_change2.py '?' ad1.txt temp_mw_2.txt temp_change_mw_2b.txt
191 potential changes written to temp_change_mw_2b.txt
# edit temp_change_mw_2b.txt.
# insert temp_change_mw_2b.txt into change_mw_2.txt

python updateByLine.py temp_mw_1.txt change_mw_2.txt temp_mw_2.txt
1292 change transactions from change_mw_2.txt
*********************************************************************

Additional (not with ^ accent in pwg) but with MW print accent ^
<L>112737<pc>572,1<k1>nyarRRa<k2>ny-a/rRRa<e>1  mw print nya^rRRa
<L>120783<pc>612,3<k1>pastyA<k2>pastyA/<h>a<e>1B 
<L>150112<pc>754,1<k1>BAryA<k2>BAryA/<h>a<e>1B
<L>150114<pc>754,1<k1>BAryA<k2>BAryA/<h>b<e>2

<L>208301<pc>1029,1<k1>vyenas<k2>vy—e/nas<e>3
<L>210265<pc>1040,3<k1>vyupta<k2>vy-u/pta<h>1<e>
<L>210278<pc>1040,3<k1>vyuzwa<k2>vy-u/zwa<h>2<e>2

<L>230570<pc>1138,3<k1>sadanya<k2>sadanya/<e>2
<L>235784<pc>1170,3<k1>samuhya<k2>sam-uhya/<h>c<e>2
<L>239659<pc>1191,2<k1>savatya<k2>savatya<e>1   ya^
<L>112723.35<pc>571,3<k1>nyak<k2>ny-a/k<h>c<e>2C (and other ny-a^k following)
<L>235800<pc>1170,3<k1>samUhya<k2>sam-Uhya/<h>1<e>2

python change_hwlist.py nyarRRa,pastyA,BAryA temp_mw_2.txt temp_change_mw_2c1.txt
python change_hwlist.py vyodana,vyupta,vyuzwa temp_mw_2.txt temp_change_mw_2c2.txt
python change_hwlist.py sadanya,samuhya,savatya,nyak temp_mw_2.txt temp_change_mw_2c3.txt
python change_hwlist.py samUhya temp_mw_2.txt temp_change_mw_2c4.txt

python 
$ cat temp_change_mw_2c1.txt temp_change_mw_2c2.txt temp_change_mw_2c3.txt temp_change_mw_2c4.txt > temp_change_mw_2c.txt
# edit temp_change_mw_2c.txt manually
# insert temp_change_mw_2c.txt into change_mw_2.txt
python updateByLine.py temp_mw_1.txt change_mw_2.txt temp_mw_2.txt
1339 change transactions from change_mw_2.txt
#
# misc addition to change_mw_2.txt:
<L>84495<pc>444,3<k1>tArpya  (<s>°pya/</s>)  -> (<s>°pya^</s>)
python updateByLine.py temp_mw_1.txt change_mw_2.txt temp_mw_2.txt
1340 change transactions from change_mw_2.txt

*********************************************************************
# ad1_rev.txt
## rerun find_accent_diff1 0,1 with temp_mw_2.txt

find_accent_diff1 option 0,1 considers cases where
1a. 1st dictionary has any accent
1b. 2nd dictionary has svarita accent
2. removes k2 hyphens (i.e., allow hyphens in k2).

python find_accent_diff1.py 0,1 temp_mw_2.txt temp_pwg_0.txt ad1_rev.txt
44 differences written to ad1_rev.txt
  (compare to the 343 differences when using temp_mw_1.txt).
# rechecked all of these.
These 44 are cases where there is a confirmed difference in accent between mw and pwg.
Only MW scan was examined for these.  pwg scan not examined
ad1_rev.txt also notes where an accent (udAtta invariably) was 'inherited' in
a compound in mw (11 such cases).

--------------------------------------------------------------
ad2.txt  words where pwg has a svarita accent, but mw has no accent.
python find_accent_diff2.py temp_mw_2.txt temp_pwg_0.txt ad2.txt
102 records printed, 28 not found in mw

ad2.txt edited to classify as X or +.
ad2.txt also has NF
From analysis of ad2.txt, changes in mw required for:

talIdya,pastyAvat,pastyAvat
yAjyavat,puronuvAkyAvat,pravargyavat
anuvAkyavat,avarArDya,asmadryaYc
udApyAm,dakziRArDya,dASvaDvara
droRyaSva,dvyakzara,nyakna
paricAyya,yAjyavat,yAdrADyam
rAjanyavat,vyoman,vyoza
yAdrADyam,rAjanyavat,vayasyA,vIryavat
vIryAvat,SaravyA,SvanvatI,saMgrAhagrAhya
samBArya,svarvat,samAhArya,svizwi

python change_hwlist.py talIdya,pastyAvat,pastyAvat temp_mw_2.txt temp_change_mw_2d1.txt
python change_hwlist.py yAjyavat,puronuvAkyAvat,pravargyavat temp_mw_2.txt temp_change_mw_2d2.txt
python change_hwlist.py anuvAkyavat,avarArDya,asmadryaYc temp_mw_2.txt temp_change_mw_2d3.txt
python change_hwlist.py udApyAm,dakziRArDya,dASvaDvara temp_mw_2.txt temp_change_mw_2d4.txt
python change_hwlist.py droRyaSva,dvyakzara,nyakna temp_mw_2.txt temp_change_mw_2d5.txt
python change_hwlist.py paricAyya,yAjyavat,yAdrADyam temp_mw_2.txt temp_change_mw_2d6.txt
python change_hwlist.py rAjanyavat,vyoman,vyoza temp_mw_2.txt temp_change_mw_2d7.txt
python change_hwlist.py yAdrADyam,rAjanyavat,vayasyA,vIryavat temp_mw_2.txt temp_change_mw_2d8.txt
python change_hwlist.py vIryAvat,SaravyA,SvanvatI,saMgrAhagrAhya temp_mw_2.txt temp_change_mw_2d9.txt
python change_hwlist.py samBArya,svarvat,samAhArya,svizwi temp_mw_2.txt temp_change_mw_2d10.txt

cat temp_change_mw_2d*.txt > temp_change_mw_2d.txt

# edit temp_change_mw_2d.txt
# insert temp_change_mw_2d.txt into change_mw_2.txt
python updateByLine.py temp_mw_1.txt change_mw_2.txt temp_mw_2.txt
1455 change transactions from change_mw_2.txt

---------------------------------------------------------------------------
849 matches for "<L>.*<k2>.*\^" in buffer: temp_mw_2.txt
Compare with where we started.
114 matches for "<k2>.*\^" in buffer: temp_mw_0.txt

---------------------------------------------------------------------------
correction to pwg:  aRvya -> aRavya (typo)
change_pwg_1.txt
python updateByLine.py temp_pwg_0.txt change_pwg_1.txt temp_pwg_1.txt
2 change transactions from change_pwg_1.txt

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
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141

---------------------------------------------------------------------------
install  temp_pwg_1.txt to check xml
cp temp_pwg_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'pwg ' redo_xampp_all.sh
sh generate_dict.sh pwg  ../../pwg
sh xmlchk_xampp.sh pwg
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141

---------------------------------------------------------------------------
ad2arev.txt
diff2a program takes into account some spelling differences between
mw and pwg:  Notably pwg uses 'vant' suffix while mw uses 'vat' suffix.

python find_accent_diff2a.py temp_mw_2.txt temp_pwg_1.txt ad2arev.txt
81 records printed, 17 not found in mw
For the 64 (81 - 17) headwords matched in both mw and pwg,
 pwg has a svarita accent while mw shows no accent.

svarita_mw_2.txt
A list of the 849 metalines in temp_mw_2.txt with a svarita accent.

svarita_pwg_1.txt
A list of the 470 metalines in temp_pwg_1.txt with a svarita accent.

---------------------------------------------------------------------------
#  'iast' version of mw
# transcoding to iast, using the revised transcoder files.
cd ../../mwtranscode
python mw_transcode1.py slp1 roman ../mwsissues/issue141/temp_mw_2.txt ../mwsissues/issue141/temp1_mw_2_iast.txt

#confirm invertibility:
python mw_transcode1.py roman slp1 ../mwsissues/issue141/temp1_mw_2_iast.txt ../mwsissues/issue141/temp1_mw_2_slp1.txt

diff ../mwsissues/issue141/temp_mw_2.txt ../mwsissues/issue141/temp1_mw_2_slp1.txt
# no difference
# remove checking file
rm ../mwsissues/issue141/temp1_mw_2_slp1.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141/
--------------------------------------------------------
zip revised iast version
zip temp1_mw_2_iast.zip temp1_mw_2_iast.txt

*********************************************************************
NOTE: this not used.
examine mw headwords X which
(a) have no svarita accent
(b) have a correspondent Y in PWG and Y has a svarita accent.
python mw_svarita_missed.py temp_mw_1.txt temp_pwg_0.txt temp_mw_svarita_missed.txt
*********************************************************************
installing to github and cologne
in csl-orig:
pwg.txt  commit 211328d0333b20a55b5c84426067a7aeef5c5409
mw.txt   commit d23735163f17509f7afeeecdd745fa8c604fecd2
push to github.
At cologne:
 pull csl-orig
 in csl-pywork/v02,  install pwg and mw
*********************************************************************
PHASE 2
Presumably, the corrections are done for cases where PWG shows a
svarita accent.
We now investigate the remaining cases from find_accend_diff_pwg.txt.
In particular, these cases do not have 'compound' markup ('-') in k2.
First, it is convenient to redo this so that the mw 'pc' (page-column)
information is included.
python find_accent_diff3.py temp_mw_2.txt temp_pwg_1.txt ad3.txt
-----------------------------------------------------------------
details:
 For mw, exclude when k2 contains '-' or '—'.
 For either, require k2 contains an accent
 For pwg, change 'ant' suffix to 'at' suffix (the mw spelling)

325 differences written to ad3.txt
# edit ad3.txt.  Confer mw print. Add '+' or 'x' status markup
# '+' (193) k2-mw agrees with print. No additional changes.
# 'x' (132) k2-mw may need some change. Various reasons.

NOTE: This will be revised
-----------------------------------------------------------------
change_mw_3.txt and change_pwg_2.txt for further corrections
cp temp_mw_2.txt temp_mw_3.txt
cp temp_pwg_1.txt temp_pwg_2.txt

-----------------------------------------------------------------
misc1 changes added to change_mw_3.txt
k1 change
<L>42901<pc> - 42902  <k1>kadru -> <k1>kadrU

page number changes d
<L>24082<pc>138,2<k1>Adya<k2>Adya^<e>1B  <pc>138,1
<L>70105<pc>379,2 pc 379,1
<L>81582<pc>431,3 pc 431,2
<L>149876<pc>753,1 752,3

python updateByLine.py temp_mw_2.txt change_mw_3.txt temp_mw_3.txt
6 change transactions from change_mw_3.txt

; *********************************************************

-----------------------------------------------------------------
misc1 added to change_pwg_2.txt
yamunA,yamya,
 python updateByLine.py temp_pwg_1.txt change_pwg_2.txt temp_pwg_2.txt
5 change transactions from change_pwg_2.txt

-----------------------------------------------------------------
observation on akra.  Not sure how common this is.
The very first example (akra) exposes a problem in the construction
of ad3.txt.  
There are two accented versions in mw: <k2>a/-kra  and <k2>akra/.
However ad3.txt shows just one form:  akra/.  Why?
The reason is the '-' in 'a/-kra', which causes this to be excluded,
as we are wanting to restrict to non-compounds.


-----------------------------------------------------------------
singletons in mw.  These are cases where two accented versions
appear. But only the first is present in <k2>.
This could generates 'false positives' when comparing to pwg.
python singleton_or_and.py 1 temp_mw_3.txt temp_singleton.txt
115 singleton or/and entries

singleton corrections added to change_mw_3.txt (12 lines changed)

python updateByLine.py temp_mw_2.txt change_mw_3.txt temp_mw_3.txt
18 change transactions from change_mw_3.txt

# rerun
python singleton_or_and.py 1 temp_mw_3.txt temp_singleton.txt
112 entries written to temp_singleton.txt
0 Problems parsing headline

Now, change metalines for these
# this introduces another markup convention:
# k2 in metaline can have multiple 'comma-separated' variants.
# currently, these 112 are the only such instances.
python singleton_or_and.py 2 temp_mw_3.txt temp_singleton_k2changes.txt
112 changes written to temp_singleton_k2changes.txt
# edit temp_singleton_k2changes.txt and resolve the 'TODO' cases to 'DONE'
# There are a handful that are further annotated 'NO CHANGE',
# generally involving '<srs/>' (simple-vowel sandhi); these have only
# one k2 variant, as the <srs/> markup is is avoided in the metaline syntax.
# insert temp_singleton_k2changes.txt into chchange_mw_3.txt

python updateByLine.py temp_mw_2.txt change_mw_3.txt temp_mw_3.txt
132 change transactions from change_mw_3.txt

-----------------------------------------------------------------
ad3_rev.txt
Revise ad3, taking into account the new k2 syntax for mw.
# temp_ad3_a.txt  got by rerunning diff3 version
python find_accent_diff3.py temp_mw_3.txt temp_pwg_2.txt temp_ad3_orig.txt
# write: n=5157, nf = 25, neq=4784, nout=348

cp find_accent_diff3.py find_accent_diff3a.py
python find_accent_diff3a.py temp_mw_3.txt temp_pwg_2.txt temp_ad3a.txt
# write: n=5158, nf = 25, neq=4787, nout=346
-----------------------------------------------------------------
cp find_accent_diff3a.py find_accent_diff3b.py
python find_accent_diff3b.py temp_mw_3.txt temp_pwg_2.txt temp_ad3b.txt
# write: n=5158, nf = 25, neq=4767, nout=366

ad3_rev.txt is a merger of ad3.txt and temp_ad3b.txt.
216 matches for "[+]" in buffer ad3_rev.txt
  - mw k2 markup confirmed by print
  - mw k2 different from computed pwg k2.
  - no further changes expected for these
162 matches for "[x]" in buffer ad3_rev.txt
  - mw to be changed for conformity with mw print

-----------------------------------------------------------------
python ad_change3b.py 'x' ad3_rev.txt temp_mw_3.txt temp_change_mw_3b.txt

# manually finish changes in temp_change_mw_3b.txt
# insert temp_change_mw_3.txt into change_mw_3b.txt

python updateByLine.py temp_mw_2.txt change_mw_3.txt temp_mw_3.txt
605 change transactions from change_mw_3.txt

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
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141

-----------------------------------------------------------------
mw print changes: noted in csl-corrections.
<L>83693.1<pc>441,2<k1>tAjadBaNga tAja/d-Ba/Nga -> tAja/d-BaNga (agree PWG)
-----------------------------------------------------------------
rerun:
python find_accent_diff3b.py temp_mw_3.txt temp_pwg_2.txt temp_ad3b_rev.txt
write: n=5149, nf = 25, neq=4848, nout=276
compare to previous:
# write: n=5158, nf = 25, neq=4767, nout=366

# ad3b_rev.txt
Apply the '+' markup from ad3_rev.txt to temp_ad3b_rev.txt
python ad_markplus.py ad3_rev.txt temp_ad3b_rev.txt ad3b_rev.txt
281 records in ad3b_rev.txt
67 of these not marked as '+'.
# edit ad3b_rev.txt
# For all the '_' items, recheck the print of mw and
# mark as '+' if the k2mw agrees with print

-----------------------------------------------------------------
# push to github   START
 csl-orig/v02  commit:
 csl-corrections
 mws (this directory)
*********************************************************************

*********************************************************************
-----------------------------------------------------------------
-----------------------------------------------------------------

mw page 87 3rd col. truncated
https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=mw&page=0087
mw page 648 3rd col. problem
