cd ../code1
file1="../rev1a/temp_rev1a_ab_slp1.txt"
python mw_transcode.py roman slp1 ../rev1a/temp_rev1a_ab_iast.txt $file1

echo "exiting convert_rev1a"

cd ../rev1a

file2="temp_rev1a_ab1.txt" 
python ../code1/convert_ab2a.py ab,cdsl $file1 $file2

echo
echo "check invertibility"
# 
file1chk="temp_rev1a_ab_slp1_chk.txt"
python ../code1/convert_ab2a.py cdsl,ab $file2 $file1chk
echo "check: diff $file1 $file1chk | wc -l"
diff $file1 $file1chk | wc -l

echo "Second part of conversion"
echo

python ../code1/convert_ab1.py ab,cdsl temp_rev1a_ab1.txt temp_rev1a_cdsl.txt
# check invertible
echo "invertibility"
echo
python ../code1/convert_ab1.py cdsl,ab temp_rev1a_cdsl.txt temp_rev1a_ab1_chk.txt 
echo
echo "diff temp_rev1a_ab1.txt temp_rev1a_ab1_chk.txt | wc -l"
diff temp_rev1a_ab1.txt temp_rev1a_ab1_chk.txt | wc -l

