MWS/mwsissues/issue156

Ref: https://github.com/sanskrit-lexicon/MWS/issues/156

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
 ecada0255c927a37611e75f482ade4261726fe37

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  ecada0255:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue156/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue156/
 
*********************************************************************
Extract the references to '<s>[^<]*\.'

python make_change.py temp_mw_0.txt change_1.txt

880519 lines read from temp_mw_0.txt
287605 entries found
select 19 entries matching "<s>a.s°</s>"

# manually change 'new' lines in change_1.txt 
# apply changes, getting temp_mw_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt

18 change transactions from change_1.txt

# -------------------------------------------------------------
---------------------------------------------------------------------------
install  temp_mw_1.txt 
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue156


 
