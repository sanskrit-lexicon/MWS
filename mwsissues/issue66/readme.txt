MWS/mwsissues/issue66
04-03-2024
Ref: https://github.com/sanskrit-lexicon/MWS/issues/66

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  8d90e462a24ad7e4f28255a6093ad7e4a02c172e

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this issue66 directory
  git show  8d90e46:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue66/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue66/
 
*********************************************************************
BEGIN change_1
cp temp_mw_0.txt temp_mw_1.txt
touch change_1.txt
python make_change.py temp_mw_0.txt change_1.txt
880516 from temp_mw_0.txt
36 changes

# examine change_1.txt , possibly make manual changes

# apply changes
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
880516 lines read from temp_mw_0.txt
880516 records written to temp_mw_1.txt
37 change transactions from change_1.txt

# install changes locally
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
# redo local displays, check for xml validity
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
python3 ../../xmlvalidate.py ../../mw/pywork/mw.xml ../../mw/pywork/mw.dtd
# ok

# sync csk-orig to github
cd /c/xampp/htdocs/cologne/csl-orig

git add v02/mw/mw.txt
git commit -m "MW cleanup.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/66"
git push

# sync this repo (MWS) to github
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue66/
git add .
etc.
