# csl-orig commit 989e371725adb839115b5359935a0247a9a11718
# diff ../../issue176/temp_mw_17.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
# 0
dirin="../../issue176"
filepfx="temp_mw_17"
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue178/code1
file1="${dirin}/${filepfx}.txt"  # cdsl form
file2="${filepfx}_ab1.txt"   # first AB form
file3="${filepfx}_ab2a.txt"  # second AB form
echo "convert cdsl to ab1 form"
python convert_ab1.py cdsl,ab $file1 $file2
echo
echo "convert_ab1 form to ab2a form"
python convert_ab2a.py cdsl,ab $file2 $file3

echo "checking agreement of ab2a form with original ab3 form"
diff temp_mw_17_ab2a.txt ../../issue176/temp_mw_16_ab3_orig.txt | wc -l

echo "checking invertibility of ab2a"
file2chk="${filepfx}_ab1_chk.txt"
python convert_ab2a.py ab,cdsl $file3 $file2chk
diff $file2 $file2chk | wc -l

echo "checking invertibility of ab1"
file1chk="${filepfx}_chk.txt"
python convert_ab1.py ab,cdsl $file2 $file1chk
diff $file1 $file1chk | wc -l
