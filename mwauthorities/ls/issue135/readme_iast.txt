cd ../../../mwtranscode
python mw_transcode.py slp1 roman ../mwauthorities/ls/issue135/temp_mw_3.txt ../mwauthorities/ls/issue135/temp_mw_3_iast.txt
#confirm invertibility:
python mw_transcode.py roman slp1 ../mwauthorities/ls/issue135/temp_mw_3_iast.txt ../mwauthorities/ls/issue135/temp_mw_3_slp1.txt
cd ../mwauthorities/ls/issue135/
diff temp_mw_3.txt temp_mw_3_slp1.txt
# no difference
