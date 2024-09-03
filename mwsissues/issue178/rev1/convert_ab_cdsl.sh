cd ../code1
python mw_transcode.py roman slp1 ../rev1/temp_rev1_ab_iast.txt ../rev1/temp_rev1_ab.txt

cd ../rev1

file1="temp_rev1_ab.txt"  # from AB  assume it is in 'ab2a' form
file2="temp_rev1_ab1.txt" 
python ../code1/convert_ab2a.py ab,cdsl $file1 $file2

echo
echo "check invertibility"
# 
file1chk="temp_rev1_ab_chk.txt"
python ../code1/convert_ab2a.py cdsl,ab $file2 $file1chk
echo "check: diff $file1 $file1chk | wc -l"
diff $file1 $file1chk | wc -l

echo "Second part of conversion"
echo

python ../code1/convert_ab1.py ab,cdsl temp_rev1_ab1.txt temp_rev1_cdsl.txt
# check invertible
echo "invertibility"
echo
python ../code1/convert_ab1.py cdsl,ab temp_rev1_cdsl.txt temp_rev1_ab1_chk.txt 
echo
echo "diff temp_rev1_ab1.txt temp_rev1_ab1_chk.txt | wc -l"
diff temp_rev1_ab1.txt temp_rev1_ab1_chk.txt | wc -l

