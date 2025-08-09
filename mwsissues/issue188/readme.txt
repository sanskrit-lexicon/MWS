mwsissues/issue188/readme.txt
08-08-2025 begun ejf
VIKRAMORVAŚĪ (1879)  for mw links

Ref: https://github.com/sanskrit-lexicon/MWS/issues/188

This issue188 directory in local file system:
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188

-----------------
pdf: 'Vikramorvasiyam [SP Pandit, 1879] (Hathitrust).pdf'

Index file : Vikramorvasiyam_1879.Index.xlsx
  Convert to txt (tsv) file Vikramorvasi.Index.tsv

cp /e/pdfwork/vikramor_mw/Vikramorvasiyam_1879.Index.tsv index_orig.txt 

cp index_orig.txt index.txt
--  edit index.txt:
 - remove last 4 lines (epage >= 189)
 - remove first 3 lines (epage 13-26

There remain 162 records, corresponding to ipage=1 to 162

----------------------------------------
# get temporary local copy of kosha
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt temp_mw_0.txt

----------------------------------------
Reference forms in kosha
--- mw
0 matches for "<ls>Vikr. [0-9]+,[0-9]+"
69 matches for "<ls>Vikr. [iv]+, *[0-9]+"
3 matches for "<ls>Vikr.  [0-9]+[^0-9,]

0 matches for "<ls>Vikram. [0-9]+,[0-9]+"
0 matches for "<ls>Vikram. [0-9]+[^0-9,]

--------------------------------------
parameters:  
1:  verse  (continuous across anka).
2:  ipage,line-number

---------------------
index_orig.txt format observations
format 5 fields tab-separated values
page
anka
fromv
tov
ipage
remarks  # optional.

Note: '---' changed to '0' .
such lines will never be used in the apps
-----------------------------------
# Prepare index.js
python make_js_index.py index.txt index.js

==========================================
apps in sanskrit-lexicon-scans

https://github.com/sanskrit-lexicon-scans/vikramor
# initialize local repo, where the link target apps will be installed.
cd /c/xampp/htdocs/sanskrit-lexicon-scans/
git clone git@github.com:sanskrit-lexicon-scans/vikramor.git

# edit README.md 

# Install apps in vikramor repo
readme_app0.txt  internal page
readme_app1.txt  anka,verse

========================================
--- links from kosha to app
mw
see readme_websanlexicon.txt
 basicadjust.php

========================================
----------------------------------------
# Begin checking consistency with dictionaries

----------------------------------------
Make misc checks between pwg , the pdf and index

----------------------
 'mw':r'<ls>Vikr. ([iv]+), *([0-9]+)',

python generate_random.py ALL mw2 temp_mw_0.txt index.txt check_mw2_ALL.txt check_mw2_nopagerec.txt

========================================
Found 10 Vikr. refs in MW from anka iv, verse in range 44-74.   These are outside the scope according to index.  

For example under sTAnaka , Vikr. iv,44. 

Our 1879 edition has a section
'Appendix 1. Act iv. with the additional passages as read by two mss.' 
which has 74 verses.

 Have not found sTAnaka in this appendix.

=======================================


==================================================
splitting kosha refs for mw.

Note lsfix2.py does not work: first parameter is ROMAN
 Example:  <ls>Vikr. iii, 0/1</ls>
 
# python lsfix2.py vikr temp_pwg_0.txt lsfix2_vikr_0.txt

---------------------------
cp temp_mw_0.txt temp_mw_1.txt
edit temp_mw_1.txt to split '<ls>Vikr. X' as needed.

----
72334 : carcarI : <ls>Vikr. iv</ls>  irregular. not linked
72341 : carcarikA : <ls>Vikr. iv</ls>  irregular. not linked
======================================

<ls n="Vikr. iv,">
-----------------------------------------------------------
# remake xml from temp_mw_1.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188
-- end of 'remake xml ...'

---------------------------
How to handle xmlchk error (documentation)
1. Open /c/xampp/htdocs/cologne/mw/pywork/mw.xml in Emacs
 use C-cC-n to find xml errors.
 Make correction in temp_mw_1.txt
 When done
3. Redo the 'remake xml ...' steps.
   continue these steps until xmlchk  says 'ok'.
---- end of 'How to handle xmlchk error'
-------------------------------------------------------------
Create Some documentation files


---------------------------------------------------
---- documentation in change files
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_mw_1.txt
20 changes written to change_mw_1.txt


============================================================
sync to github:
------------------
# csl-orig # git pull
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188
diff temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "MW: VIKRAMORVAŚĪ link target
Ref: https://github.com/sanskrit-lexicon/MWS/issues/188"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188

------------------
# csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon/
git pull
git add .
git commit -m "VIKRAMORVAŚĪ mw link target. 
Ref: https://github.com/sanskrit-lexicon/MWS/issues/188"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188

sh apidev_copy.sh

------------------
# csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev/
git pull
git add .
git commit -m "VIKRAMORVAŚĪ mw link target. 
Ref: https://github.com/sanskrit-lexicon/MWS/issues/188"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188

------------------

---------------------------------------------------
sync Cologne to Github, pull changed repos
redo the mw displays

---------------
csl-orig # pull
csl-websanlexicon # pull
csl-apidev # pull
-------------------------------------
# sync Cologne to github
# sync to cologne
# regenerate displays for mw

cd csl-pywork/v02

sh generate_dict.sh mw  ../../MWScan/2020/

--------------------------------------------

# sync this MW (issue188)
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188
git pull
git add .
git commit -m "#188"
git push

-------------------------------------
# sync this repo to github
====================================
THE END

