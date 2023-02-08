MWS/mwsissues/issue152

Ref: https://github.com/sanskrit-lexicon/MWS/issues/152

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
 a365b8f1d018df3a8489d46be756b386fdfeab39

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  a365b8f1:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue152/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue152/
 
*********************************************************************
Extract the references to '<ls>Gr.'

python extract_gr.py temp_mw_0.txt extract_gr.txt

880519 lines read from temp_mw_0.txt
287605 entries found
select 11 entries matching "<ls>Gr."


The displays the 11 instances of Gr. literary source 
# -------------------------------------------------------------
