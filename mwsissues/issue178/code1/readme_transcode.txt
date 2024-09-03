transcoders for iast are in transcoder_ab directory.


cp  /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder1/roman_slp1.xml transcoder_ab/roman_slp1.xml
Add line for combining candra-bindu

cp  /c/xampp/htdocs/sanskrit-lexicon/MWS/mwtranscode/transcoder1/slp1_roman.xml transcoder_ab/slp1_roman.xml

cd ../code1
python mw_transcode.py roman slp1 ../rev1/temp_rev1_ab_iast.txt ../rev1/temp_rev1_ab.txt

python mw_transcode.py slp1 roman ../rev1/temp_rev1_ab.txt ../rev1/temp_rev1_ab_iast_chk.txt

diff ../rev1/temp_rev1_ab_iast.txt ../rev1/temp_rev1_ab_iast_chk.txt | wc -l
# 0
-------------------------------------------


cd ../code1
python mw_transcode.py roman slp1 ../rev1/temp_rev1_ab_iast.txt ../rev1/temp_rev1_ab.txt
