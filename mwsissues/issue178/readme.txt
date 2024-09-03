
Begin 09-02-2024

Ref: https://github.com/sanskrit-lexicon/MWS/issues/178

This directory:
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue178

# -------------------------------------------------------------
slight code modification to simplify conversion
mkdir code1
# put conversion code (from issue176/)
  digentry.py
  convert_ab1.py
  convert_ab2a.py
# test1.sh
This repeats construction of temp_mw_16_ab3_orig.txt from
temp_mw_17.txt in issue176.

# -------------------------------------------------------------

https://github.com/sanskrit-lexicon/MWS/issues/176#issuecomment-2323840570

mkdir rev1
# AB provided a test revision. with relatively small number of changes
rev1/
cp ~/Downloads/andhrabharati/MWS/"CDSL (temp_mw_16_ab3_IAST) [matched].TXT" temp_rev1_ab_orig.txt

cp temp_rev1_ab_orig.txt temp_rev1_ab_iast.txt

Some changes needed to temp_rev1_ab_orig.txt
See change_notes_orig_iast.txt

diff temp_rev1_ab_orig.txt temp_rev1_ab_iast.txt | wc -l
163
  So approximately 40 changes.
diff temp_rev1_ab_orig.txt temp_rev1_ab_iast.txt > diff_orig_iast.txt
----------------------------------------

# current conversion script: convert_ab_cdsl.sh in rev1 directory

cd ../rev1
# convert temp_rev1_ab_iast.txt to temp_rev1_cdsl.txt
# with invertibility checks.

sh convert_ab_cdsl.sh

------------------------
# to facilitate AB review of this work.
zip temp_rev1_ab_iast.zip temp_rev1_ab_iast.txt

End of work as of 09-03-2024
*******************************************************************
mkdir rev1a

Examine ../rev1/temp_rev1_cdsl.txt.

-----------------------
construct local version based on temp_rev1_cdsl.tx
cd rev1a
cp ../rev1/temp_rev1_cdsl.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh



  digentry.py
  convert_ab1.py
  convert_ab2a.py
# test1.sh
This repeats construction of temp_mw_16_ab3_orig.txt from
temp_mw_17.txt in issue176.

# -------------------------------------------------------------

https://github.com/sanskrit-lexicon/MWS/issues/176#issuecomment-2323840570

mkdir rev1
# AB provided a test revision. with relatively small number of changes
rev1/
cp ~/Downloads/andhrabharati/MWS/"CDSL (temp_mw_16_ab3_IAST) [matched].TXT" temp_rev1_ab_orig.txt

cp temp_rev1_ab_orig.txt temp_rev1_ab_iast.txt

Some changes needed to temp_rev1_ab_orig.txt
See change_notes_orig_iast.txt

diff temp_rev1_ab_orig.txt temp_rev1_ab_iast.txt | wc -l
163
  So approximately 40 changes.
diff temp_rev1_ab_orig.txt temp_rev1_ab_iast.txt > diff_orig_iast.txt
----------------------------------------

# current conversion script: convert_ab_cdsl.sh in rev1 directory

cd ../rev1
# convert temp_rev1_ab_iast.txt to temp_rev1_cdsl.txt
# with invertibility checks.

sh convert_ab_cdsl.sh

------------------------
# to facilitate AB review of this work.
zip temp_rev1_ab_iast.zip temp_rev1_ab_iast.txt

End of work as of 09-03-2024
*******************************************************************
mkdir rev1a
see rev1a/readme.txt

cd rev1a
zip temp_rev1a_ab_iast.zip temp_rev1a_ab_iast.txt
-------------
# sync this repo to github
