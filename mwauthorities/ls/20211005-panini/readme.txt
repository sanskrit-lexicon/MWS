Re https://github.com/sanskrit-lexicon/csl-orig/issues/519

cp ../mw.txt temp_mw0.txt
# construct change1.txt in several steps
python change1a.py temp_mw.txt temp_change1a.txt
 
 n="Pāṇ."

python updateByLine.py temp_mw0.txt change1.txt temp_mw1.txt


#<s>X</s> is in Devanagari in pan.txt. Convert to slp1
python mw_transcode.py deva slp1 pan.txt pan_slp1.txt

# generate change transactions based on finding lines that contain
 certain strings, these strings having be extracted
 into pan1_slp1.txt from pan_slp1.txt
 
python change1b.py temp_mw0.txt pan1_slp1.txt temp_change1b.txt
