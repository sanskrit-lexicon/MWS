
11-10-2025 begun ejf

----------------------
@aumsanskrit describes the problem:

MW dictionary clearly includes the Headwords: "mīḍhu" and "mīḻhú".
However, both of these printed Headwords: "mīḍhu" and "mīḻhú" are missing from the online Hierarchy!
Andhrabharati has replied as follows:

BTW, the CDSL MW.txt (earlier version at my end) has the entry--

<L>164587<pc>818,2<k1>mīḍhu<k2>mīḍhu<e>2
<s>mīḍhu</s> or <s>mīḻhú</s>, ¦ <lex>m.</lex> = <s>dhana</s>, <ls>Naigh. ii, 10.</ls><info lex="m"/>
<LEND>{{164587, 164587.1}}

[This is missing in the present CDSL version!]
-------------------------

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190

-------------------------------------
# get temporary local copy of mw, current commit
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

# temp_mw_1.txt   has changes to solve the problem
cp temp_mw_0.txt temp_mw_1.txt
------------------------------------
from readme_follow.txt
temp_mw_lost.txt        oldest version of mw.txt which is missing <L>164587
temp_mw_lostparent.txt  parent mw.txt

diff_lost.txt:
  diff temp_mw_lostparent.txt temp_mw_lost.txt > diff_lost.txt
  
------------------------------------

python comphw.py diff_lost.txt comphw_diff_lost.txt
This is interesting, but not quite what we need!

------------------------------------
python comphw1.py temp_mw_lostparent.txt temp_mw_lost.txt comphw1.txt
temp_mw_lostparent.txt 194065 distinct headwords
temp_mw_lost.txt 194010 distinct headwords
60 lines written to comphw1.txt

python comphw1.py temp_mw_lost.txt temp_mw_lostparent.txt comphw1a.txt
temp_mw_lost.txt 194010 distinct headwords
temp_mw_lostparent.txt 194065 distinct headwords
5 lines written to comphw1a.txt

example from comphhw1.txt
abudDipUrvakam
 - not in lost, but in lost parent
 - in current mw

--------------------------------
python comphw2.py temp_mw_0.txt comphw1.txt comphw2.txt
temp_mw_0.txt 194071 distinct headwords
60 lines read from comphw1.txt
21 lines written to comphw2.txt

# headwords in comphw1.txt (so missing in temp_mw_lost.txt)
# And also whether headword in current mw

# check these 21 manually, correct temp_mw_1

--------------------------------
comphw2_edit.txt separates these 21 into 16 cases
each case adds:
 * other headwords related to the case
 * link to the page,column of MW scans 
 * The 'context' from temp_mw_lostparent.txt

-------------------------------
CASE 09 mIQu, mI|u  solved. see case_09.txt

======================================
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
-- end of 'remake xml ...'

* OLD

================================================
INSTALLATION
sync to github:

------------------
# csl-orig  
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "mw: mIQu
Ref: https://github.com/sanskrit-lexicon/mws/issues/190"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190

---------------------------------------------------
# sync to Cologne, pull changed repos

---------------
csl-orig #pull

---------------
# update displays for pwg, etc.
cd csl-pywork/v02
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue190 to github.
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
git pull
git add .
git commit -m "(case 01-16 )
Ref: https://github.com/sanskrit-lexicon/MWS/issues/190"
git push

------------------------------------------------------------
See readme2.txt for handling of the other cases

