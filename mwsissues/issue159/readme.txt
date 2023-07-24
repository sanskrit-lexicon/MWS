MWS/mwsissues/issue159

Ref: https://github.com/sanskrit-lexicon/MWS/issues/159

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
 bc01533ece078d65fdc949454b418fa72aa2ebf1

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  bc01533ec:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue159/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue159/
 
*********************************************************************
Extract the references to '<ls>Gram.</ls>' and '<ls>Gr.</ls>'

python extract.py temp_mw_0.txt extract.txt

880519 lines read from temp_mw_0.txt
287605 entries found
select 19 instances

