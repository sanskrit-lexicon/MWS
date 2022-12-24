---------------------------------------------------------------------------
#  'iast' version 1 12-24-2022
==============================
# create temp_version_01.txt from latest version of csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git log  # get sha for latest
# commit ad09f13811772014a79b23c7f8c158736533d53a  
# Sat Dec 24 01:00:10 2022
# git show REVISION:path/to/file
git show ad09f138:v02/mw/mw.txt > temp_mw_01.txt
# move to the directory containing this readme_iast.txt file
mv temp_mw_01.txt /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue145/
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue145/
==============================
# transcoding to iast, using the revised transcoder files.
cd ../../mwtranscode
python mw_transcode2.py slp1 roman ../mwsissues/issue145/temp_mw_01.txt ../mwsissues/issue145/temp_mw_01_iast.txt

#confirm invertibility:
python mw_transcode2.py roman slp1 ../mwsissues/issue145/temp_mw_01_iast.txt ../mwsissues/issue145/temp_mw_01_slp1.txt
----------------------------------------------------------------
diff ../mwsissues/issue145/temp_mw_01.txt ../mwsissues/issue145/temp_mw_01_slp1.txt

# no difference
# remove checking file
rm ../mwsissues/issue145/temp_mw_01_slp1.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue145/
--------------------------------------------------------
zip revised iast version
zip temp_mw_01_iast.zip temp_mw_01_iast.txt

--------
optional: upload temp_mw_01_iast.zip by dragging it to comment in
