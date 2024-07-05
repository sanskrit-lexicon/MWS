mwsissues/issue172  tooltips/

Ref: https://github.com/sanskrit-lexicon/MWS/issues/172

This directory:

cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue172

Goal: identify 'titular' <ls*>X</ls> instances.
  Then revise the markup for these.

Using some code from MWS/mwauthorities/ls/issue135

cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue172

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  45cad97424c2ab8c9a6bfb7cb8c14c7cc9a508cf  (07-05-2024)

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  45cad9742:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue172/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue172

# -------------------------------------------------------------
Start with a copy of mwauth/tooltip.txt in csl-pywork at commit
 9d0595ca5ed23e488d783625906d5b81360521e4  (07-05-2024)
     9e82ed54f9c43429f43863dc60b6ed042e0c63d9  the commit used in issue135
 
# temp_tooltip_0.txt
cd /c/xampp/htdocs/cologne/csl-pywork

git show 9d0595ca5e:v02/distinctfiles/mw/pywork/mwauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue172/temp_tooltip_0.txt

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue172

# -------------------------------------------------------------
python lsextract_all.py temp_mw_0.txt temp_tooltip_0.txt temp_lsextract_all_0_0.txt

867 tooltips from temp_tooltip_0.txt
unknown tip at <L>106080<pc>537,2<k1>nArasiMhopapurARa
lstxt = <ls>Upapur.</ls>, elt="Upapur."

# Revise to add this tooltip.  We will later carry this into
  csl-pywork
cp temp_tooltip_0.txt temp_tooltip_1.txt
# add Upapur to temp_tooltip_1.txt
# rerun lsextract_all:
python lsextract_all.py temp_mw_0.txt temp_tooltip_1.txt temp_lsextract_all_0_1.txt
868 tooltips from temp_tooltip_1.txt
871 lines written to temp_lsextract_all_0_1.txt
327652  ALL     As of 2024-07-05

Note: there are 3 extra 'summary' lines at the top.

---------------------------------------------------------------------
# lsextract_all1.py partition count into titular/non-titular

python lsextract_all1.py temp_mw_0.txt temp_tooltip_1.txt temp_lsextract_all1_0_1.txt

---------------------------------------------------------------------
Make changes to csl-websanlexicon
  basicadjust.php, basicdisplay.php
  DON"T YET COMMIT THESE CHANGES

---------------------------------------------------------------------
mwtestls
  Generate a temporary display

--- first, locally
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mwtest
   This test version displays empty ls markup (such as <ls>RV.</ls>)
   in a different way (with ls tooltip, dotted underline, and inherited font)
   This change just applies to mw, but could be adapted to other dictionaries.
--- upload to cologne serve
/c/xampp/htdocs/cologne/mwtest/downloads/mwweb1.zip
put in work/mwtestls folder.
url: https://sanskrit-lexicon.uni-koeln.de/work/mwtestls/web/webtc/indexcaller.php  (and also other displays).
Note apidev not revised.
And the current 'normal' cologne url is unchanged.

*********************************************************************
