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
Phase 3.  Accents on samAsas.
*********************************************************************
-----------------------------------------------------------------
ad_cpd_non.txt   combine ad2arev.txt and ad3b_rev.txt.
We will assume these are 'handled', and exclude from subsequent
difference analysis
python ad_cpd_non.py ad2arev.txt ad3b_rev.txt ad_cpd_non.txt 
84 read from ad2arev.txt
287 read from ad3b_rev.txt
371 lines written to ad_cpd_non.txt

-----------------------------------------------------------------
# make a 4th version of mw for changes to come
cp temp_mw_3.txt temp_mw_4.txt
touch change_mw_4.txt

-----------------------------------------------------------------
# accent diff 4.  Find additional differences. Primarily where
# mw has samAsa markup. Specifically, we exclude differences
# between mw and pwg which are already known (i.e., present in ad_cpd_non.txt)
python find_accent_diff4a.py ad_cpd_non.txt temp_mw_4.txt temp_pwg_2.txt temp_ad4a.txt
write: n=12970, nf = 328, neq=10094, nout=2548

The 2548 cases need to be examined and systematic errors in mw coding corrected.

-----------------------------------------------------------------
1899 matches in 1893 lines for "[\/^][^	 ]*[\/^]" in buffer: temp_ad4a.txt
aMsaDrI   	a/MsaDrI/      	aMsaDrI/       	1,2
Need to change mw k2 a/MsaDrI/ to aMsaDrI/

# option 4a0
# more than 2 accents OR comma in k2
python ad_change4a1.py 4a0 temp_ad4a.txt temp_mw_4.txt temp_change_mw_4a0.txt
14 changes
# manual edit of temp_change_mw_4a0.txt
# insert temp_change_mw_4a0.txt into change_mw_4.txt
python updateByLine.py temp_mw_3.txt change_mw_4.txt temp_mw_4.txt
25 change transactions from change_mw_4.txt

-----------------------------------------------------------------
# change_mw_4a1:  mw k2 has TWO accents (and no comma in k2)
# Program generates changes to metaline and headline.
# for some headlines, the program doesn't detect the change,
# and it must be done manually.

python ad_change4a1.py 4a1 temp_ad4a.txt temp_mw_4.txt temp_change_mw_4a1.txt
make_changes_4a1: 720 changes marked "**" - manual check required
changes for 2776 entries written to temp_change_mw_4a1.txt
# edit temp_change_mw_4a1.txt and consider the '**' cases.
# most of the '**' cases are where broken bar is first character.
# 81 headlines require attention.
# insert temp_change_mw_4a1.txt into change_mw_4.txt
python updateByLine.py temp_mw_3.txt change_mw_4.txt temp_mw_4.txt
4938 change transactions from change_mw_4.txt

-----------------------------------------------------------------
ad4a_rev1.txt
# rerun diff4a
python find_accent_diff4a.py ad_cpd_non.txt temp_mw_4.txt temp_pwg_2.txt temp_ad4a_rev1.txt
write: n=12970, nf = 328, neq=11909, nout=733
Examine the mw print of these and classify rev1 as + or x,
depending on whether print agrees with the mwk2 shown.
Those marked 'x' will require further changes.
# next so git will keep, done after editing
cp temp_ad4a_rev1.txt ad4a_rev1.txt

-----------------------------------------------------------------
temp_change_mw_4b_0.txt
# changes for lines in ad4a_rev1.txt with status code = 0.
# Remove accent in metaline k2 and in headline
python ad_change4b.py 0 ad4a_rev1.txt temp_mw_4.txt temp_change_mw_4b_0.txt
#changes for 387 entries written to temp_change_mw_4b_0.txt
#make_changes_4a1: 33 changes marked "**" - manual check required
# edit temp_change_mw_4b_0.txt and resolve the '**' cases manually.
# insert temp_change_mw_4b_0.txt into change_mw_4.txt
python updateByLine.py temp_mw_3.txt change_mw_4.txt temp_mw_4.txt
5630 change transactions from change_mw_4.txt

-----------------------------------------------------------------
temp_change_mw_4b_p.txt
# changes for lines in ad4a_rev1.txt with status code = p.
# Replace the mw accent with the pwg accent, in metaline and headline.
python ad_change4b.py p ad4a_rev1.txt temp_mw_4.txt temp_change_mw_4b_p.txt

# edit temp_change_mw_4b_p.txt and resolve the '**' cases manually.
# insert temp_change_mw_4b_p.txt into change_mw_4.txt
python updateByLine.py temp_mw_3.txt change_mw_4.txt temp_mw_4.txt
5918 change transactions from change_mw_4.txt

-----------------------------------------------------------------
temp_change_mw_4b_x.txt
# changes for lines in ad4a_rev1.txt with status code = x.
# correct the accents, in metaline and headline.
python ad_change4b.py x ad4a_rev1.txt temp_mw_4.txt temp_change_mw_4b_x.txt

# edit temp_change_mw_4b_x.txt and resolve all cases manually.
# insert temp_change_mw_4b_x.txt into change_mw_4.txt
python updateByLine.py temp_mw_3.txt change_mw_4.txt temp_mw_4.txt
change transactions from change_mw_4.txt
6491 change transactions from change_mw_4.txt

-----------------------------------------------------------------
python find_accent_diff4a.py ad_cpd_non.txt temp_mw_4.txt temp_pwg_2.txt temp_ad4a_rev2.txt
write: n=12639, nf = 328, neq=12126, nout=185
compare to previous run of diff4a
write: n=12970, nf = 328, neq=11909, nout=733

So we've gone down from 733 to 185 (548 more matches with pwg !)
To be conservative, let's review the mw print for these 185.
Best way is to mark all these as 'x', and
temp_ad4a_rev2x.txt has all the initial '_' changed to 'x'
python ad_change4b.py x temp_ad4a_rev2x.txt temp_mw_4.txt temp_change_mw_4b_x_rev1.txt

Reviewed through <L>13004<pc>74,2<k1>aBIruRa<k2>a-BI/ruRa,aBIru/Ra<e>2
and found no discrepancies with mw print. Will assume the rest are ok.

-----------------------------------------------------------------
find_accent_diff4b.py
find_accent_diff4a.py improvement to handle mw avagraha in k2.
example: 31859 old <L>8646<pc>45,3<k1>anyatoraRya<k2>anya/to-'raRya<e>3

python find_accent_diff4b.py ad_cpd_non.txt temp_mw_4.txt temp_pwg_2.txt temp_ad4b.txt
write: n=12639, nf = 328, neq=12130, nout=181
write: n=12639, nf = 328, neq=12134, nout=177
 We have mw-pwg matches for 8 additional items, since now avagraha ("'")
 is removed (in both mw and pwg) before comparison of k2mw and k2pwg.

-----------------------------------------------------------------
ad_cpd.txt is a copy of temp_ad4b.txt, with the status changed from
'_' to '+'.
This contains the remaining pwg headwords where
(a) there is an accent in pwg
(b) there is an accent in mw
(c) The set of accented mw k2 is NOT equal to the set of accented pwg k2.

-----------------------------------------------------------------
cat ad_cpd_non.txt ad_cpd.txt > ad4b.txt

ad4b.txt contains known disagreements between mw and pwg, for cases
where pwg has an accent, and mw has an accent.

--------------------------------------------------------------------------
install  temp_mw_4.txt to check xml
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141

-----------------------------------------------------------------
We might still have an accented pwg headword 
(a) which is also an mw headword, and 
(b) no mw entry for this headword has an accent.

python find_accent_diff4c.py ad4b.txt temp_mw_4.txt temp_pwg_2.txt temp_ad4c.txt
write: n=6293, nf = 32, neq=0, nout=6261

6261 is a huge number to examine, but there is no other way. Need
to classify as +,p,x. All the k2mw cases are unaccented currently in mw.txt.

Take 5 days to examine all the cases, and mark them as '+','p','x','c'.
# save our hard-won markup so git will track.
cp temp_ad4c.txt ad4c.txt 
-
'p' means mw needs an accent, and the accent is provided by pwg.
'c' means mw needs a change to metaline '<pc>' value;
      a few also require an accent and the accent may differ from pwg.
'x' mw needs an accent and the accent may differ from pwg.
'+' mw print shows no accent
5460 matches for "^[+]" in buffer: ad4c.txt
635 matches for "^p" in buffer: ad4c.txt
 95 matches for "^c" in buffer: ad4c.txt
 71 matches for "^[x]" in buffer: ad4c.txt
(+ 5460 635 95 71) = 6261
There will be some revisions to these counts after 4c_x below
---------------------------------------------------------------------------
touch change_mw_5.txt
cp temp_mw_4.txt temp_mw_5.txt

-----------------------------------------------------------------
# ad_change4c.py handles 'c' 
# Also adapts handling of 'p'
# handle the 'p' cases
python ad_change4c.py p ad4c.txt temp_mw_5.txt temp_change_mw_4c_p.txt
#changes for 927 entries written to temp_change_mw_4c_p.txt
#make_changes_4a1: 142 changes marked "**" - manual check required
# manual adjustments to temp_change_mw_4c_p.txt
# insert temp_change_mw_4c_p.txt into change_mw_5.txt

python updateByLine.py temp_mw_4.txt change_mw_5.txt temp_mw_5.txt
# 1626 change transactions from change_mw_5.txt

# rerun find_accent_diff4c.py with revised temp_mw_5.txt
python find_accent_diff4c.py ad4b.txt temp_mw_5.txt temp_pwg_2.txt temp_ad4c_rev1.txt
write: n=5658, nf = 32, neq=0, nout=5626
compare to prior:
write: n=6293, nf = 32, neq=0, nout=6261
(- 6261 5626) 635  so we have reduced the mw-pwg mismatches by 635,
  which is just the number expected  (the number of "p" cases)

-----------------------------------------------------------------
# handle the 'c' cases
python ad_change4c.py c ad4c.txt temp_mw_5.txt temp_change_mw_4c_c.txt
# 95 adrecs with status c
# changes for 267 entries written to temp_change_mw_4c_c.txt
# make_changes_4a1: 0 changes marked "**" - manual check required

# edit temp_change_mw_4c_c.txt and correct the 'pc' in metaline.
# In a few cases, there will be mw accent changes.
# insert temp_change_mw_4c_c.txt into change_mw_5.txt

python updateByLine.py temp_mw_4.txt change_mw_5.txt temp_mw_5.txt
1745 change transactions from change_mw_5.txt

# rerun find_accent_diff4c.py with revised temp_mw_5.txt
python find_accent_diff4c.py ad4b.txt temp_mw_5.txt temp_pwg_2.txt temp_ad4c_rev2.txt
write: n=5650, nf = 32, neq=0, nout=5618
previous: write: n=5658, nf = 32, neq=0, nout=5626
  so we solved 8 of the accent differences.

-----------------------------------------------------------------
# handle the 'x' cases
python ad_change4c.py x ad4c.txt temp_mw_5.txt temp_change_mw_4c_x.txt
#71 adrecs with status x
#changes for 219 entries written to temp_change_mw_4c_x.txt
# manual update of temp_change_mw_4c_x.txt
# insert temp_change_mw_4c_x.txt into change_mw_5.txt

python updateByLine.py temp_mw_4.txt change_mw_5.txt temp_mw_5.txt
1978 change transactions from change_mw_5.txt

Revised counts (some 'x' items moved to '+', my clerical error)
5467 matches for "^[+]" in buffer: ad4c_rev1.txt
636 matches for "^p" in buffer: ad4c_rev1.txt
 95 matches for "^c" in buffer: ad4c_rev1.txt
 63 matches for "^[x]" in buffer: ad4c_rev1.txt
(+ 5467 636 95 63) = 6261 check.


-----------------------------------------------------------------
cat ad4b.txt ad4c.txt > ad5a.txt
# then change all 'status' to '+' in the ad4c part.

ad5a.txt contains all examined disagreements between pwg and mw, where
pwg has an accent, and mw may or may not have an accent.


python find_accent_diff4c.py ad5a.txt temp_mw_5.txt temp_pwg_2.txt temp_ad4c_rev3.txt
# write: n=32, nf = 32, neq=0, nout=0

# now remove any restriction on
python find_accent_diff5a.py ad5a.txt temp_mw_5.txt temp_pwg_2.txt temp_ad5a_rev0.txt
# prepare_dict_mw: 194046
# prepare_dict_pw: 20657
# write: n=12494, nf = 360, neq=12134, nout=0
neq1 = 10721, neq2 = 1413 (+ 10721 1413) = 12134)

Explanation
1. start with all k1 of pwg where k2 has an accent. (20657 of these)
2. start with all k1 of mw, where k2 may or may not have accent (194046 of these)
3. With few exceptions ('ant'), ignore cases where k1-pwg not found in mw
   (360 of these)
4. Also, ignore all k1 appearing in ad5a.txt

There are 12494 k1 in total.
For each such k1, look at the set of k2 from pwg : set(k2pwg)
And, look at the set of k2 from mw: set(k2mw).
If set(k2mw) == set(k2pwg), count as ok, and increment neq1
if set(k2mw) == set(k2pwg).union(list[k1]), count as ok, and increment neq2.
Otherwise, count as NOT ok, and increment nout.

As expected, nout = 0. And neq1 and neq2 are as above.

THIS FINISHES THE STUDY OF CASES pwg headwords with an accent.

It remains to examine cases where mw has an accent, EXCLUDING
the cases thus far examined.
This will be the next step.

-----------------------------------------------------------------
install  temp_mw_5.txt to check xml
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue141
-----------------------------------------------------------------
# commit to csl-orig: 70b7392b59bad245492e6a06696e3b504dd2b0b6
# commit to mws repository: 


-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
TODO
NOTE: anya/to'raRya  ' in k2pwg   apuro'nuvAkya^ka
pwg: ftu\Sa/s   prA/cInayogIpu/tra  (also mw shows 2 accents!) va/naspa/ti
mw prA/SnI-putra/
<L>185990<pc>918,1<k1>vanaspati<k2>va/na-s-pa/ti<h>a<e>3
<L>189485<pc>934,3<k1>vAtajUta<k2>vA/ta—jUta^<e>3
=====
girijA in mw:  not a pwg headword. cdsl incorrectly shows 'inherited' accent
bahutiTa print change see page 626 -> see page 726  va/naspa/ti
<L>258981<pc>1280,3<k1>svapnanaMSana mw print shows only svapna-na
  page 1280 may is truncated in 3rd column.
  https://archive.org/details/in.ernet.dli.2015.31959/page/n1318/mode/1up
  page 160 truncated
Mismarked in k2, but NOT in pwg, so not yet caught.

<L>1321<pc>6,3<k1>agrepA<k2>agre—pA/<e>3
  headline pU/ not marked.  This is an OR with two words
<L>1405.1<pc>7,1<k1>aGnyA<k2>a/-GnyA<e>2B
<L>1405.2<pc>7,1<k1>aGnyA<k2>a/-GnyA<e>2B
<L>16138<pc>92,1<k1>arDaKArI<k2>arDa/—KArI<e>3 no accent - and others
<L>20166.6<pc>116,1<k1>azAQA<k2>a/-zAQA<e>1B
<L>126351<pc>636,3<k1>purunizWA<k2>puru/—nizWA<e>3
<L>162307<pc>807,2<k1>mAtfbanDU<k2>mAtf/—banDU<e>3B
<L>204122<pc>1008,1<k1>vfkatAti<k2>vf/ka—tAti<e>3
<L>113613<pc>576,1<k1>paYcacitIka<k2>paYca—citIka<e>3  pa/
<L>114548<pc>580,1<k1>paqvISa<k2>paq—vISa<e>3 pa/
<L>114549<pc>580,1<k1>paqviMSa<k2>pa/q—viMSa<e>3 pa/
<L>128466.1<pc>646,1<k1>pfTivizWA<k2>pfTivi—zWA<e>4
<L>140878<pc>711,3<k1>pruzvA<k2>pruzvA/<e>2B info or
<L>25998<pc>149,2<k1>Arti<k2>Arti<e>2  text refers to hom1 and 2, but no h2.

NEW or entries for L=5164  5164.1, 5164.2, 5164.3
-----------------------------------------------------------------
-----------------------------------------------------------------
2229 matches for "<k2>[^<]*[\/^][^<]*[\/^][^<]*<" in buffer: temp_mw_4.txt
example: <L>96<pc>1,2<k1>aMsadaGna<k2>a/Msa—daGna/<e>3
<L>126347<pc>636,3<k1>puruDa<k2>puru—Da/<e>3 headline
<L>126348<pc>636,3<k1>puruDA<k2>puru/—DA/<e>3 headline
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------

mw page 87 3rd col. truncated
https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=mw&page=0087
mw page 648 3rd col. problem
mw page 142 problems
mw page 728
page 796

