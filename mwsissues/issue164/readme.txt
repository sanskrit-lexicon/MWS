MWS/mwsissues/issue159

Ref: https://github.com/sanskrit-lexicon/MWS/issues/164


# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
cc39ac1ea1f27a9f1e452092f0c882a7e9cba606


# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  cc39ac1e:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/
 
*********************************************************************
Generate changes

python make_change_1.py temp_mw_0.txt temp_change_1.txt
cp temp_change_1.txt change_1.txt
# manual edit of change_1.txt

# apply the changes
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
880513 lines read from temp_mw_0.txt
880480 records written to temp_mw_1.txt
114 change transactions from change_1.txt
81 of type new, 33 of type del


----------------------------------------------
check local install
------------------------------------------------------------------------
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164
---------------------------------------------

expand other <shortlong/>
177 matches in 154 lines for "<shortlong" in buffer: temp_mw_1.txt

python make_change_2.py temp_mw_1.txt temp_change_2.txt
# 119 entries changed
cp temp_change_2.txt change_2.txt
# manual edit of change_2.txt == note: no changes

# apply the changes
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
145 change transactions from change_2.txt

----------------------------------------------
check local install
------------------------------------------------------------------------
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164

---------------------------------------------
There are still 12 <shortlong/> instances.
Handle these manually
cp temp_mw_2.txt temp_mw_3.txt

python diff_to_changes_dict.py temp_mw_2.txt temp_mw_3.txt change_3.txt
10 changes written to change_3.txt

----------------------------------------------
check local install
------------------------------------------------------------------------
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164

---------------------------------------------
# install versions 1,2,3 separately into csl-orig


---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
# install mw_1
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: shortlong headwords. #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

---------------------------------------------
# install mw_2
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: non-headword shortlong expansion #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

---------------------------------------------
# install mw_3
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: non-headword shortlong expansion, the rest of them #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

*****************************************************************
THE END

