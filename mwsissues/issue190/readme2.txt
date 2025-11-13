
11-12-2025 readme2.txt

readme.txt ends with solution to case 09.
This readme2.txt begins with other cases, following
Andhrabharati analyses in in issue comments

The revised mw.txt is temp_mw_2.txt: 
cp temp_mw_1.txt temp_mw_2.txt

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190

case 01 agnyADAna 
case 02 ajaloma
case 03 atiCattra
case 04 boDAyanIya
case 05 durgAQa -- minor corrections not in AB ref.
        Note  durgAQatva was a headword in error
case 06 ekASraya -- Jim adds ekASrayaguRa
case 07 karvara
case 08 no change  'lost' krIli is wrong and was previously changed to krILi
case 09 mIQu 
case 10 napAt [group by gender, following AB]
case 11 rAjayakzma [remove rAjayakzmannAman replaced by rAjayakzmanAman
case 12 sAmaga  [group by gender, following AB; add cpd sAmagAnAMCandas
case 13 sma  [add variant spellings zma, zmA; smottara remains lost]
case 14 tulApragraha [missing hw added]
case 15 vinDyAvali  [remove duplicate 197389.1 vinDyAvalIsuta]
case 16 yamalArjuna [no cpds with yamalArjunaka]
======================================
# remake xml from temp_mw_2.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
-- end of 'remake xml ...'

================================================
INSTALLATION
sync to github:

------------------
# csl-orig  
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
diff temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "16 cases re lost headwords
Ref: https://github.com/sanskrit-lexicon/mws/issues/190"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190

---------------------------------------------------
# sync to Cologne, pull changed repos

---------------
csl-orig #pull

---------------
# update displays for mw
cd csl-pywork/v02
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue190 to github.
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
git pull
git add .
git commit -m "(case 09 mIQU)
Ref: https://github.com/sanskrit-lexicon/MWS/issues/190"
git push

------------------------------------------------------------
THE END
