---------------------------------------------------------------------------
#  'iast' version of mw
# transcoding to iast, using the revised transcoder files.
cd ../../mwtranscode
python mw_transcode2.py slp1 roman ../mwsissues/issue142/temp_mw_extra.txt ../mwsissues/issue142/temp1_mw_extra_iast.txt

#confirm invertibility:
python mw_transcode2.py roman slp1 ../mwsissues/issue142/temp1_mw_extra_iast.txt ../mwsissues/issue142/temp1_mw_extra_slp1.txt
----------------------------------------------------------------
diff ../mwsissues/issue142/temp_mw_extra.txt ../mwsissues/issue142/temp1_mw_extra_slp1.txt

# no difference
# remove checking file
rm ../mwsissues/issue142/temp1_mw_extra_slp1.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142/
--------------------------------------------------------
zip revised iast version
zip temp1_mw_extra_iast.zip temp1_mw_extra_iast.txt

