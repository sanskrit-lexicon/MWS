MWS/mwauthorities/ls/20220628-rv

Ref: https://github.com/sanskrit-lexicon/MWS/issues/130


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

Start with a copy of csl-orig/v02/mw/mw.txt at commit
  ad4b858c0e319d3eabf22f1550a4410ebde138d7

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this spruch directory
  git show ad4b858c:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv/
# -------------------------------------------------------------
# -------------------------------------------------------------
temp_tooltip.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth

python tooltip.py roman mwauth.txt temp_tooltip.txt
737 auth records
737 lines written to temp_tooltip.txt

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv/
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/temp_tooltip.txt .

---------------------------------------------------------------------
temp_1.txt misc. changes
cp temp_mw_0.txt temp_mw_1.txt
touch change_1.txt
1. Remove 2 empty ls

python diff_to_changes.py temp_mw_0.txt temp_mw_1.txt temp_change_1.txt
2 changes written to temp_change_1.txt
# manually insert temp_change_1.txt into change_1.txt.
---------------------------------------------------------------------
cp /c/xampp/htdocs/sanskrit-lexicon/pwg/pwg_ls2/mbh1/lsextract_all.py .
# do summary of ls markup in mw before the (major) changes.
# This does include the two changes above.
python lsextract_all.py temp_mw_1.txt temp_tooltip.txt lsextract_mw_0.txt

---------------------------------------------------------------------
cp /c/xampp/htdocs/sanskrit-lexicon/pwg/pwg_ls2/ramayana0/lsextract_v1.py .
# Revise program for MW's RV format  (roman, digits, digits)
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
737 tooltips from temp_tooltip.txt
13553 entries with ls for  RV.
16318 = number of RV. ls references
1630 marked as abnormal for RV.
1630 abnormal change forms written to temp_rvchanges_1.txt
12 duplicate lnum instances in lscases

## Use make_change3_ls program to autogenerate various corrections.
## NOT USED! cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0/make_change3_ls.py .
cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0/parseheadline.py .

cp /c/xampp/htdocs/sanskrit-lexicon/PWG/pwg_ls2/ramayana0/make_change_3a.py .

python make_change_3a.py 1 temp_mw_1.txt temp_change3a_1.txt
80 records written to temp_change3a_1.txt
# manually insert temp_change3a_1.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
#-------------

python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
1550 abnormal change forms written to temp_rvchanges_1.txt

python make_change_3a.py 2 temp_mw_1.txt temp_change3a_2.txt
67 records written to temp_change3a_2.txt
# manually insert temp_change3a_2.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
149 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
1483 abnormal change forms written to temp_rvchanges_1.txt
python make_change_3a.py 2a temp_mw_1.txt temp_change3a_2a.txt
103 records written to temp_change3a_2a.txt
# manually insert temp_change3a_2_2a.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
252 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
python make_change_3a.py 1a temp_mw_1.txt temp_change3a_1a.txt
197 records written to temp_change3a_1a.txt
# manually insert temp_change3a_1a.txt into change_1a.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
449 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
1183 abnormal change forms written to temp_rvchanges_1.txt
python make_change_3a.py 3 temp_mw_1.txt temp_change3a_3.txt
84 records written to temp_change3a_3.txt
# manually insert temp_change3a_3.txt into change_1a.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
533 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
1098
python make_change_3a.py 3a temp_mw_1.txt temp_change3a_3a.txt
143 records written to temp_change3a_3a.txt
# manually make corrections in temp_change3a_3a.txt, then
# insert into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
677 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
#make_change_3a option 4
<ls>RV. x, 37, 4 and 63, 12</ls>  (ABNORMAL)
<ls>RV. i, 31, 12 and 164, 21.</ls>  (ABNORMAL)
python make_change_3a.py 4 temp_mw_1.txt temp_change3a_4.txt
70 records written to temp_change3a_4.txt
# manually insert temp_change3a_4.txt into change_1a.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
747 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
666 abnormal change forms written to temp_rvchanges_1.txt
# make_change_3a option 4a
<ls>RV. vi, 27, 5 and 8.</ls>  (ABNORMAL)
<ls>RV. vi, 17, 8 and 9</ls>  (ABNORMAL)
python make_change_3a.py 4a temp_mw_1.txt temp_change3a_4a.txt
39 records written to temp_change3a_4a.txt
# manually insert temp_change3a_4a.txt into change_1a.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
786 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
624 abnormal change forms written to temp_rvchanges_1.txt
# make_change_3a option 5
<ls>RV. iii, 25, 4; v, 43, 1 and vii, 76, 5</ls>  ->
 <ls>RV. iii, 25, 4</ls>; <ls n="RV.">v, 43, 1 and vii, 76, 5</ls>
python make_change_3a.py 5 temp_mw_1.txt temp_change3a_5.txt
99 records written to temp_change3a_5.txt
# manually insert temp_change3a_5.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
885 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
624 marked as abnormal for RV.
# change3a option 5a
<ls n="RV.">viii, 21, 15 and x, 39, 3.</ls> ->
<ls n="RV.">viii, 21, 15</ls> and <ls n="RV.">x, 39, 3.</ls> 
python make_change_3a.py 5a temp_mw_1.txt temp_change3a_5a.txt
10 records written to temp_change3a_5a.txt
# manually insert temp_change3a_5a.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
895 change transactions from change_1.txt
614 abnormal change forms written to temp_rvchanges_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
614 marked as abnormal for RV.
# change3a option 5b
<ls n="RV.">iv, 30, 17; x, 4, 5.</ls>
python make_change_3a.py 5b temp_mw_1.txt temp_change3a_5b.txt
45 records written to temp_change3a_5b.txt
# manually insert temp_change3a_5b.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
940 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
569 marked as abnormal for RV.
# change3a option 5c
<ls>RV. x, 76, 6; 94, 4</ls>  (ABNORMAL)
python make_change_3a.py 5c temp_mw_1.txt temp_change3a_5c.txt
58 records written to temp_change3a_5c.txt
# manually insert temp_change3a_5c.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
998 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
511 marked as abnormal for RV.
# change3a option 5d
<ls n="RV.">ix, 84, 3; 86, 33.</ls>  (ABNORMAL)
python make_change_3a.py 5d temp_mw_1.txt temp_change3a_5d.txt
11 records written to temp_change3a_5d.txt
# manually insert temp_change3a_5d.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1009 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
500 marked as abnormal for RV.
# change3a option 6
<ls>RV. vi, x.</ls> -> <ls>RV. vi</ls>, <ls n="RV.">x.</ls>
python make_change_3a.py 6 temp_mw_1.txt temp_change3a_6.txt
3 records written to temp_change3a_6.txt
# manually insert temp_change3a_6.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1012 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
497 marked as abnormal for RV.
# change3a option 6a
<ls>RV. i, v, vii, x</ls>
python make_change_3a.py 6a temp_mw_1.txt temp_change3a_6a.txt
3 records written to temp_change3a_6a.txt
# manually insert temp_change3a_6a.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1015 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
494 marked as abnormal for RV.
# change3a option 7
<ls>RV. vii,68, 7.</ls> -> <ls>RV. vii, 68, 7.</ls> 
python make_change_3a.py 7 temp_mw_1.txt temp_change3a_7.txt
12 records written to temp_change3a_7.txt
# manually insert temp_change3a_7.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1027 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
482 marked as abnormal for RV.
# change 4b
<ls>RV. i, 158, 1; 4</ls>
python make_change_3a.py 4b temp_mw_1.txt temp_change3a_4b.txt
29 records written to temp_change3a_4b.txt
# manually insert temp_change3a_4b.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1056 change transactions from change_1.txt


#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
453 marked as abnormal for RV.
# change 4c
<ls>RV. iv, 43 and 44</ls>
python make_change_3a.py 4c temp_mw_1.txt temp_change3a_4c.txt
6 records written to temp_change3a_4c.txt
# manually insert temp_change3a_4c.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1062 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
446 marked as abnormal for RV.
# change 4d
<ls>RV. iv, 43; 44</ls>
python make_change_3a.py 4d temp_mw_1.txt temp_change3a_4d.txt
25 records written to temp_change3a_4d.txt
# manually insert temp_change3a_4d.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1087 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
400 marked as abnormal for RV.
# change3a 8
<ls>RV. x, 9, 1-3</ls> ->
<ls>RV. x, 9, 1</ls>-<ls n="RV. x, 9,">3</ls>
python make_change_3a.py 8 temp_mw_1.txt temp_change3a_8.txt
26 records written to temp_change3a_8.txt
# manually insert temp_change3a_8.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1113 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
374 marked as abnormal for RV.
# change3a 8a
<ls>RV. vii, 29-3.</ls>
python make_change_3a.py 8a temp_mw_1.txt temp_change3a_8a.txt
22 records written to temp_change3a_8a.txt
# manually insert temp_change3a_8a.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1135 change transactions from change_1.txt

#-------------
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
352 marked as abnormal for RV.
# edit copy temp_rvchanges_1_edit.txt manually
# Note: several erroneous <hom>a</hom> instances unearthed and changed.
# Probably there may be more, where a homonym number was erroneously
# put at the end of previous entry.
# insert temp_rvchanges_1_edit.txt into change_1
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
1521 change transactions from change_1.txt

python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_RV_1.txt temp_rvchanges_1.txt
80 abnormal change forms written to temp_rvchanges_1.txt
# some revision of 'abnormal' definition
5 abnormal change forms written to temp_rvchanges_1.txt

</ls> <ls n="RV.">
_ ==>> </ls>
*****<xls> ==>> <ls>
---------------------------------------------------------------------------
install temp_mw_1.txt into csl-orig, to catch xml errors.

cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv

---------------------------------------------------------------------------
# redo the summary of all ls in mw after the above RV changes
python lsextract_all.py temp_mw_1.txt temp_tooltip.txt lsextract_mw.txt

# add lsextract_RV_1.txt to git coverage
python lsextract_v1.py 'RV.' temp_mw_1.txt temp_tooltip.txt lsextract_RV_1.txt temp_rvchanges_1.txt

---------------------------------------------------------------------------
OLD MATERIAL BELOW. 
---------------------------------------------------------------------------
---------------------------------------------------------------------------
python ../RV/lsextract.py 'R. GORR.' temp_mw_0.txt temp_tooltip.txt temp_lsextract_RGORR_0.txt
2701 tooltips from temp_tooltip.txt
2273 entries with ls for  R. GORR.
4023 = number of R. GORR. ls references

python ../RV/lsextract.py 'R. SCHL.' temp_mw_0.txt temp_tooltip.txt temp_lsextract_SCHL_0.txt
2701 tooltips from temp_tooltip.txt
144 entries with ls for  R. SCHL.
194 = number of R. SCHL. ls references

# -------------------------------------------------------------
temp_mw_1.txt. Manual changes 
1.  787 changes
<ls>R. A, B, C. D, E.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A,">D, E.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5.</ls>
----
1a. 44 changes
<ls>R. A, B, C. D, E</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A,">D, E</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5</ls>
----
2. 1379 changes
<ls>R. A, B, C. D, E, F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls>

2a. 24  changes (same redone at later time)
<ls>R. A, B, C. D, E, F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls>

3. 299  changes
<ls>R. A, B, C. D.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls>

3a. 16  changes
<ls>R. A, B, C. D</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, B,">D</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4</ls>


4. 226 changes
 R. 2, 3, 12. 76, 13. 5, 32, 36.
<ls>R. A, B, C. D, E. F, G, H.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A,">D, E.</ls> <ls n="R.">F, G, H.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5.</ls> <ls n="R.">\6, \7, \8.</ls>

5. 159 changes
R. 1, 1, 73. 5, 41, 4. 43, 7.
<ls>R. A, B, C. D, E, F. G, H.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R. D,">G, H.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls> <ls n="R. \4,">\7, \8.</ls>

7. 220  changes
R. R. 2, 26, 30. 3, 69, 3. 5, 89, 72.
<ls>R. A, B, C. D, E, F. G, H, I.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R.">G, H, I.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls> <ls n="R.">\7, \8, \9.</ls>

----
8. 2 changes
<ls>R. A, B, C. D, E, F,</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F</ls>,

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\,</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls>,

----
9. 25 changes
<ls>R. A, B, C. D, E. F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, D,">F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1">\4, \5</ls> <ls n="R. \1, \4,">\6.</ls>

----
10. 335  changes
<ls>R. A, B, C. D. E, F.</ls> -> <ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls> <ls> n="R. A,">E, F.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\. \([0-9]+\)\, \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4. </ls> <ls n="R. \1,">\5, \6.</ls>

11. 144 changes
R. 6, 29, 19. 31, 17. 73, 37.
<ls>R. A, B, C. D, E. F, G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A,">D, E.</ls> <ls n="R. A,">F, G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1,">\4, \5.</ls> <ls n="R. \1,">\6, \7.</ls>

12. 25 changes
R. 1, 40, 13. 5, 7, 39. 47.
<ls>R. A, B, C. D, E, F. G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R. E, F,"> G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls> <ls n="R. \4, \5,">\7.</ls>

---------------------------
13. 43 changes
R. 1, 63, 2. 2, 64, 21
<ls>R. A, B, C. D, E, F</ls> -> <ls>R. A, B, C.</ls> <ls n="R.">D, E, F</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6</ls>

---------------------------
14. 3 changes
R. 5, 40, 12. 13.
<ls>R. A, B, C. D.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls>

---------------------------
15. 39 changes
R. 5, 33, 34. 38. 1, 51, 4.
<ls>R. A, B, C. D. E, F, G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls> <ls n="R.">E, F, G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls> <ls n="R.">\5, \6, \7.</ls>

----
16. 4 changes
<ls>R. A, B, C. D, E, F. G, H, I.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R.">D, E, F.</ls> <ls n="R.">G, H, I.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls> <ls n="R.">\7, \8, \9.</ls>
----
17.  changes
R. 2, 72, 8. 12. 3, 22, 35.
<ls>R. A, B, C. D. E, F, G.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R. A, B,">D.</ls> <ls n="R.">E, F, G.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R. \1, \2,">\4.</ls> <ls n="R.">\5, \6, \7.</ls>

# -------------------------------------------------------------
temp_mw_2.txt   More manual changes.


1. 
R. 3, 20, 37. 5, 38, 30. 6, 30, 39. 37, 65.
<ls>R. A, B, C. D, E, F. G, H, I. J, K.</ls> ->
<ls>R. A, B, C.</ls> <ls n="R">D, E, F.</ls> <ls n="R.">G, H, I.</ls> <ls n="R. G,">J, K.</ls>

<ls>R\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\), \([0-9]+\)\. \([0-9]+\), \([0-9]+\)\.</ls>
<ls>R. \1, \2, \3.</ls> <ls n="R.">\4, \5, \6.</ls> <ls n="R.">\7, \8, \9.</ls> <ls n="R. \7,">\10, \11.</ls> X10 = \10

# -------------------------------------------------------------
python ../RV/lsextract.py 'R.' temp_mw_1.txt temp_tooltip.txt temp_lsextract_R_1.txt
2701 tooltips from temp_tooltip.txt
9710 entries with ls for  R.
27756 = number of R. ls references



# -------------------------------------------------------------
# temp_mw_2.txt   constructed iteratively
# not used
#python ../p/listls3_abnormal.py 'R.' temp_mw_1.txt temp_abnormal_r_00.txt temp_change_abnormal.txt

python ../p/make_change3_abnormal.py 'R.' temp_mw_1.txt temp_change3_abnormal.txt
1231 records written to temp_change3_abnormal.txt

# insert temp_change3_abnormal.txt into (new file) change_2.txt

python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1231 of type new
----

python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_01.txt
291 changes not yet done. See tempdbg.txt
10 changes deferred
4451 records written to temp_change3_01.txt
# insert temp_change3_01.txt into bottom of change_2.txt

python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
5682 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_02.txt
334 changes not yet done. See tempdbg.txt
4 changes deferred
1569 records written to temp_change3_02.txt

# insert temp_change3_02.txt into bottom of change_2.txt

python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
7251 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_03.txt
351 changes not yet done. See tempdbg.txt
3 changes deferred
1137 records written to temp_change3_03.txt
# insert temp_change3_03.txt into bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
8388 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_04.txt
359 changes not yet done. See tempdbg.txt
2 changes deferred
595 records written to temp_change3_04.txt

# insert temp_change3_04.txt into bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
8983 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_05.txt
360 changes not yet done. See tempdbg.txt
1 changes deferred
308 records written to temp_change3_05.txt

# insert temp_change3_05.txt into bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
9291 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_06.txt
363 changes not yet done. See tempdbg.txt
0 changes deferred
169 records written to temp_change3_06.txt

# insert temp_change3_06.txt into bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
9460 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_07.txt
365 changes not yet done. See tempdbg.txt
0 changes deferred
93 records written to temp_change3_07.txt
# insert temp_change3_07.txt into bottom of change_2.txt

python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
9553 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_08.txt
365 changes not yet done. See tempdbg.txt
0 changes deferred
58 records written to temp_change3_08.txt

# insert temp_change3_08.txt into bottom of change_2.txt

python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
9611 change transactions from change_2.txt

----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_09.txt
365 changes not yet done. See tempdbg.txt
0 changes deferred
31 records written to temp_change3_09.txt

# insert temp_change3_09.txt into bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
9642 change transactions from change_2.txt

2701 tooltips from temp_tooltip.txt
9710 entries with ls for  R.
36167 = number of R. ls references

python ../RV/lsextract.py 'R.' temp_mw_2.txt temp_tooltip.txt temp_lsextract_R_2.txt
2701 tooltips from temp_tooltip.txt
9710 entries with ls for  R.
36167 = number of R. ls references

# -------------------------------------------------------------
Now manually handle the tempdbg.txt (call it temp_change_09_dbg.txt)
<lsg1> -> <ls n="GORR. 1,"> 
<lsg2> -> <ls n="GORR. 2,">

QUESTION: <L>115535<pc>7-1463<k1>svasTa
  <ls n="R.">7, 18, 17.</ls> and following not found in ramayanaschl
QUESTION: <L>117897<pc>7-1677<k1>hlAd
  <ls n="R. GORR.">7, 97, 11.</ls> not found in ramayangorr
What is meaning of R. with 4 parameters? (100+ instances. first parm is '7')

#insert revised temp_change_09_dbg.txt at bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
10015 change transactions from change_2.txt

-----
python ../p/make_change3_ls.py 'R.' temp_mw_2.txt temp_change3_10.txt
6 changes not yet done. See tempdbg.txt
0 changes deferred
31 records written to temp_change3_10.txt


# insert temp_change3_10.txt into bottom of change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt

python ../RV/lsextract.py 'R.' temp_mw_2.txt temp_tooltip.txt temp_lsextract_R_2.txt
2701 tooltips from temp_tooltip.txt
9710 entries with ls for  R.
36747 = number of R. ls references


-------------------------------------------------------------
# local install temp_mw_2.txt and check for xml validity

cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv

-------------------------------------------------------------
temp_mw_3.txt
1142 matches in 1079 lines for "GORR" in buffer: temp_lsextract_R_2.txt
These need further work.
Initially, cp temp_mw_2.txt temp_mw_3.txt

--- option 1
python make_change_3a.py 1 temp_mw_3.txt temp_change3a_01.txt
498 records written to temp_change3a_01.txt
insert temp_change3a_01.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt
36747 = number of R. ls references

--- option 2
python make_change_3a.py 2 temp_mw_3.txt temp_change3a_02.txt
168 records written to temp_change3a_01.txt
insert temp_change3a_02.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt
36747 = number of R. ls references

--- option 3
python make_change_3a.py 3 temp_mw_3.txt temp_change3a_03.txt
203 records written to temp_change3a_01.txt

# insert temp_change3a_03.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
869 change transactions from change_3.txt

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt
36950 = number of R. ls references

--- option 2a
python make_change_3a.py 2a temp_mw_3.txt temp_change3a_02a.txt
4 records written to temp_change3a_02a.txt
insert temp_change3a_02a.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
875 changes

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt
36950 = number of R. ls references

--- option 1a
python make_change_3a.py 1a temp_mw_3.txt temp_change3a_01a.txt
14 records written to temp_change3a_01a.txt
insert temp_change3a_01a.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
887 changes

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt
36950 = number of R. ls references

--- option 4
python make_change_3a.py 4 temp_mw_3.txt temp_change3a_04.txt
63 records written to temp_change3a_04.txt
insert temp_change3a_04.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
887 changes

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt 
36977 = number of R. ls references

python lsextract_v1.py 'R.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_R_3.txt temp_changes_gorr.txt
224 GORR change forms written to temp_changes_gorr.txt

# Manually edit temp_changes_gorr_edit.txt.
</ls> <ls n="R. ed. Bomb.">
<ls n="R. GORR.">
</ls> <ls n="R. GORR.">
</ls> <ls n="R.">
<ls n="GORR.">
</ls> <ls n="GORR.">
</ls> <ls n="SCHL.">
</ls> <ls n="SCHL.">
</ls> <ls>
insert temp_changes_gorr_edit.txt into change_3.txt

python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1163 change transactions from change_3.txt

python ../RV/lsextract.py 'R.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_R_3.txt

python ../RV/lsextract.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_Rgorr_4.txt
2294 entries with ls for  R. GORR.
4341 = number of R. GORR. ls references

python ../p/make_change3_ls.py 'R. GORR.' temp_mw_3.txt temp_change3_11.txt
32 changes not yet done. See tempdbg.txt
2 changes deferred
503 records written to temp_change3_11.txt
# insert temp_change3_11.txt into change_3.txt. 
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1700

python ../RV/lsextract.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt temp_lsextract_Rgorr_4.txt
2701 tooltips from temp_tooltip.txt
2294 entries with ls for  R. GORR.
4875 = number of R. GORR. ls references

python ../p/make_change3_ls.py 'R. GORR.' temp_mw_3.txt temp_change3_12.txt
3 changes not yet done. See tempdbg.txt
1 changes deferred
92 records written to temp_change3_12.txt
# insert temp_change3_12.txt into change_3.txt. 
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1792 change transactions from change_3.txt

python ../p/make_change3_ls.py 'R. GORR.' temp_mw_3.txt temp_change3_13.txt
3 changes not yet done. See tempdbg.txt
0 changes deferred
29 records written to temp_change3_13.txt
# insert temp_change3_13.txt into change_3.txt. 
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1821 change transactions from change_3.txt

python ../p/make_change3_ls.py 'R. GORR.' temp_mw_3.txt temp_change3_14.txt
3 changes not yet done. See tempdbg.txt
0 changes deferred
13 records written to temp_change3_14.txt
# insert temp_change3_14.txt into change_3.txt. 
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1834 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
2388 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
499 GORR change forms written to temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
2887 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
301 GORR change forms written to temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
3188 change transactions from change_3.txt

python lsextract_v2.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v2_R_GORR_3.txt temp_changes_gorr.txt
2294 entries with ls for  R. GORR.
6319 = number of R. GORR. ls references
63 GORR change forms written to temp_changes_gorr.txt
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
3251 change transactions from change_3.txt

python lsextract_v3.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v3_R_GORR_3.txt temp_changes_gorr.txt
2294 entries with ls for  R. GORR.
6382 = number of R. GORR. ls references
469 GORR change forms written to temp_changes_gorr.txt

PRINT error: <L>44264<pc>4-0644<k1>pAtra  <ls n="R. GORR.">15, 6, 8 (9</ls>
  CORRECTED  1, 15, 6. 8.
4-num anomaly in R. GORR. <L>82519<pc>6-0193<k1>yogya
  <ls n="R. GORR.">7, 59, 1, 21.</ls>

# manual editing of temp_changes_gorr.txt.
# insert temp_changes_gorr.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
3685 change transactions from change_3.txt

python lsextract_v3.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v3_R_GORR_3.txt temp_changes_gorr.txt
52 GORR changes written --- these all seem to be legitimate exceptions

python lsextract_v1.py 'R.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_R_3.txt temp_changes_abnormal.txt
403 marked as abnormal for R.
403 abnormal change forms written to temp_changes_abnormal_R.txt
# manual corrections to temp_changes_abnormal_R.txt
 <xls> -> <ls>,  </xls> -> </ls>
 R. ed. Ser. still another (unknown) version of Ramayana

# insert temp_changes_abnormal_R.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4072 change transactions from change_3.txt

# How many are still abnormal for 'R.' ?
python lsextract_v1.py 'R.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_R_3.txt temp_changes_abnormal.txt
90 abnormal change forms written to temp_changes_abnormal.txt

4119 change transactions from change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt

One final time:
python lsextract_v1.py 'R.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_R_3.txt temp_changes_abnormal_R.txt
46 abnormal change forms written to temp_changes_abnormal.txt

Now try the same with R. GORR.
python lsextract_v1.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_Rgorr_3.txt temp_changes_abnormal_gorr.txt
47 abnormal change forms written to temp_changes_abnormal_gorr.txt
# manual adjust temp_changes_abnormal_gorr.txt
# insert into bottom of change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4135 change transactions from change_3.txt

# rerun 
python lsextract_v1.py 'R. GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_Rgorr_3.txt temp_changes_abnormal_gorr.txt
32 abnormal change forms written to temp_changes_abnormal_gorr.txt

[this version of temp_mw_3.txt has been xml-checked.

Do similar analysis for 'R. SCHL'

python lsextract_v1.py 'R. SCHL.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_Rschl_3.txt temp_changes_abnormal_schl.txt
149 entries with ls for  R. SCHL.
204 = number of R. SCHL. ls references
26 marked as abnormal for R. SCHL.
26 abnormal change forms written to temp_changes_abnormal_schl.txt

#examine temp_changes_abnormal_schl.txt
# insert temp_changes_abnormal_schl.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4162 change transactions from change_3.txt

# remaining R. SCHL. anomalies
python lsextract_v1.py 'R. SCHL.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_Rschl_3.txt temp_changes_abnormal_rschl.txt
206 = number of R. SCHL. ls references
0 marked as abnormal for R. SCHL.
0 abnormal change forms written to temp_changes_abnormal_rschl.txt


python lsextract_v1.py 'SCHL.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_schl_3.txt temp_changes_abnormal_schl.txt
# insert temp_changes_abnormal_schl.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4212 change transactions from change_3.txt

# <ls>adv.</ls> -> <ls> (9) inserted into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4221 change transactions from change_3.txt

python lsextract_v1.py 'SCHL.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_schl_3.txt temp_changes_abnormal_schl.txt
224 entries with ls for  SCHL.
328 = number of SCHL. ls references
2 marked as abnormal for SCHL.

python lsextract_v1.py 'R. SCHL.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_rschl_3.txt temp_changes_abnormal_rschl.txt
149 entries with ls for  R. SCHL.
206 = number of R. SCHL. ls references
0 marked as abnormal for R. SCHL.
0 abnormal change forms written to temp_changes_abnormal_rschl.txt

python lsextract_v1.py 'R. ed. Bomb.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_redbomb_3.txt temp_changes_abnormal_redbomb.txt
262 entries with ls for  R. ed. Bomb.
290 = number of R. ed. Bomb. ls references
28 marked as abnormal for R. ed. Bomb.
28 abnormal change forms written to temp_changes_abnormal_redbomb.txt

# manual changes to temp_changes_abnormal_redbomb.txt
# insert temp_changes_abnormal_redbomb.txt into change_3.txt TODO
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4250 change transactions from change_3.txt

python lsextract_v1.py 'R. ed. Bomb.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_redbomb_3.txt temp_changes_abnormal_redbomb.txt
262 entries with ls for  R. ed. Bomb.
309 = number of R. ed. Bomb. ls references
0 marked as abnormal for R. ed. Bomb.

python lsextract_v1.py 'GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_gorr_3.txt temp_changes_abnormal_gorr.txt
3270 = number of GORR. ls references
171 marked as abnormal for GORR.

# Manually edit temp_changes_abnormal_gorr.txt
# insert temp_changes_abnormal_gorr.txt into change_3
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
4403 change transactions from change_3.txt

# recompute abnormals
python lsextract_v1.py 'GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_gorr_3.txt temp_changes_abnormal_gorr.txt
1170 entries with ls for  GORR.
3285 = number of GORR. ls references
26 marked as abnormal for GORR.
26 abnormal change forms written to temp_changes_abnormal_gorr.txt

# manual adjustment of temp_changes_abnormal_gorr.txt and insert into change_3
$ python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt             1149413 lines read from temp_mw_2.txt
1149413 records written to temp_mw_3.txt
4404 change transactions from change_3.txt
4404 of type new

# rerun
python lsextract_v1.py 'GORR.' temp_mw_3.txt temp_tooltip.txt lsextract_v1_gorr_3.txt temp_changes_abnormal_gorr.txt
1170 entries with ls for  GORR.
3286 = number of GORR. ls references
17 marked as abnormal for GORR.
17 abnormal change forms written to temp_changes_abnormal_gorr.txt


START HERE
sh redo_lsextract_v1.sh
This remakes these files:
lsextract_v1_r.txt
lsextract_v1_gorr.txt
lsextract_v1_schl.txt
lsextract_v1_rgorr.txt
lsextract_v1_rschl.txt
lsextract_v1_redbomb.txt

grep 'ABNORMAL' lsextract_v1_*.txt > lsextract_abnormal.txt
 (98 lines -- mw Ramayana references considered as abnormal)

Summary of number of references with different abbreviations.
These are approximately the number of references with link targets.
The main purpose here is to identify the abnormal <ls> forms. The
exact references may be found by consulting the lsextract_v1_X.txt file(s).

abbrev     #entries  #references  #abnormal
R.          9705       37595       47
GORR.       1170        3287       17
SCHL.        224         328        2
R. GORR.    2295        7076       31
R. SCHL.     149         210        1
R. ed. Bomb. 263         310        0
R. ed. Ser.    4           4        0

# redo the summary of all ls references in mw, using temp_mw_3.txt
# note that ../mbh1/mw_tooltip.txt is same as temp_tooltip.txt
#  (as of this work)
python ../mbh1/lsextract_all.py temp_mw_3.txt ../mbh1/mw_tooltip.txt lsextract_mw.txt

# do the summary BEFORE the changes, i.e., with temp_mw_0.txt
python ../mbh1/lsextract_all.py temp_mw_0.txt ../mbh1/mw_tooltip.txt temp_lsextract_mw_0.txt

# edited version of comparison of temp_lsextract_mw_0.txt and lsextract_mw.txt
# This quantifies the markup improvements.
 OLD     NEW    category      
698067  714437  ALL           As of 2022-06-22
 36524   32387  NUMBER        ls starts with number
 02170   02161  UNKNOWN       ls is unknown
 
                Ramayan 
                abbrev        Current tooltip
 23287   37595  R.            RĀMĀYAṆA. Ohne eine nähere Angabe ist be
 04023   07076  R. GORR.      RĀMĀYAṆA, translation by Gaspare Gorresi
 00343   03287  GORR.         GORRESIO.
 00217   00328  SCHL.*        ?  
 00194   00210  R. SCHL.      RĀMĀYAṆA. ? [Cologne addition]
 00269   00310  R. ed. Bomb.  RĀMĀYAṆA. ? [Cologne addition]

* SCHL.  This is a shorter abbreviation with same meaning as 'R. SCHL.', namely,
  the Schlegel version of Kandas 1 and 2 of Ramayana.
  It MAY be that some instances of SCHL. in mw refer to other works by Schlegel.
   
# -------------------------------------------------------------
install temp_mw_3.txt and check xml
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv

# *************************************************************
further work on 'ed. Bomb.'
----------------------------------------------------------------
revision to mwbib_input.txt regarding tooltips.
 (new version of csl-pywork)
# revise local copy
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/mwbib_input.txt temp_tooltip.txt 

----------------------------------------------------------------
# markup for 'ed. Bomb.'
cp temp_mw_3.txt temp_mw_4.txt
manual changes from temp_mw_3.txt
touch change_4.txt

(<ls>ed. Bomb.)
python lsextract_v1.py 'ed. Bomb.' temp_mw_4.txt temp_tooltip.txt lsextract_v1_edbomb.txt temp_changes_edbomb.txt
# manual change to temp_changes_edbomb.txt
# insert temp_changes_edbomb.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
python lsextract_v1.py 'ed. Bomb.' temp_mw_4.txt temp_tooltip.txt lsextract_v1_edbomb.txt temp_changes_edbomb.txt
2702 tooltips from temp_tooltip.txt
24 entries with ls for  ed. Bomb.
29 = number of ed. Bomb. ls references
1 marked as abnormal for ed. Bomb.   THIS IS AN MBH REFERENCE
1 abnormal change forms written to temp_changes_edbomb.txt

# some further manual changes to change_4.
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
24 change transactions from change_4.txt

---  adding markup to ed. Bomb.
3053 matches in 2998 lines for "ed\. Bomb\." in buffer: temp_mw_4.txt
  27 matches for "<ls>ed\. Bomb\."  no action 
  27 matches for ">ed\. Bomb\." (same list as prev.) no action
   8 matches for "^ed\. Bomb\."  (lines starting with ed. Bomb.) marked
   3018 matches in 2967 lines for "[^>]ed\. Bomb\."  info, no action
   2 matches of [ed. Bomb.]  marked
  51 matches for "[(]ed\. Bomb\."  marked
   2965 matches in 2916 lines for "[^>]ed\. Bomb\."
     88 matches for "[^ ]ed\. Bomb\."
   2965 matches in 2916 lines for "[ ]ed\. Bomb\."
     88 matches for "<ls>ed\. Bomb\."
   So now, the unmarked 'ed. Bomb.' coincide with those with ' ed. Bomb' (preceding space)
-------------------------------------------------------------------------
   There are some of these (such as "<ls>R. ed. Bomb.") that we don't want to mark.
   Two examples: <ls>R. ed. Bomb.   AND "<ls n="R. ed. Bomb."
     temporarily change these to <ls>R._ed._Bomb. (271)  AND "<ls n="R._ed._Bomb." (44)
     Now 70 matches for "\. ed\. Bomb\."  
       <ls>BHĀG. P. ed. Bomb. (14) temporary: <ls>BHĀG._P._ed._Bomb.
       <ls>ŚUK. ed. Bomb.  (8) temporary: <ls>ŚUK._ed._Bomb.
       <ls>MBH. ed. Bomb.  (9) temporary: <ls>MBH._ed._Bomb.
       <ls>PAÑCAT. ed. Bomb. (18) temporary: <ls>PAÑCAT._ed._Bomb.
       <ls>MĀLAV. ed. Bomb. (8) temporary: <ls>MĀLAV._ed._Bomb.
       misc. others changed by adding ls markup (13)
       Now, there are no remaining matches of ". ed. Bomb."

    2 matches for " ed\. Bomb\. [0-9]".  Add <ls> markup to these
    247 matches for " ed\. Bomb\.$"   Change these to "<ls>ed. Bomb.</ls>"
    1081 matches in 1080 lines for " ed\. Bomb\. " Since none of these 
        is followed by a digit, we may safely add ls markup

    1049 matches in 1040 lines for " ed\. Bomb\.)"
        we may safely add ls markup to these
     128 matches for " ed\. Bomb\.,
        we may safely add ls markup to these
      51 matches for " ed\. Bomb\.;"
        we may safely add ls markup to these
       6 matches for " ed\. Bomb\.:"
        we may safely add ls markup to these
    There remain 16 matches for " ed\. Bomb\.</ls>"
      These are remarked manually.
16 matches for " ed\. Bomb\.</ls>" in buffer: temp_mw_4work.txt
 517081:<ls>BHĀG. P. 3, 19, 4. 8, 5, 15 ed. Bomb.</ls> (<ls>BURNOUF</ls>None {#baDyamAna#} für {#baDyamAna)#} . 
 525579:<ls>MBH. 3, 12729 ed. Bomb.</ls> und bei <ls>KULL.</ls> zu <ls>M. 3, 185</ls> {#brAhmadeyA#}, welche Form wohl die richtigere ist.
 532350:<ls>25 ed. Bomb.</ls> 
 554549:<ls>MBH. 11, 97, ed. Bomb.</ls> {#(pariBujyantaM#} ed. Calc.). {#varAhavasApariBfzwa#} 
 564983:<ls>MBH. 6, 360 ed. Bomb.</ls> {#(maDumatta#} ed. Calc.). sg. N. pr. eines Landes <is>gaṇa</is> {#kacCAdi#} zu 
 598267:<ls>MBH. 9, 2437 ed. Bomb.</ls> {#mitrahana#} ed. Calc. mit Weglassung eines {#Bo#} .
 620638:<ls>MBH. 12, 1509, ed. Bomb.</ls> {#(aBiBU#} ed. Calc.); nach dem Schol. = {#aSarIra#} .
 622912:<ls>MBH. 6, 342, ed. Bomb.</ls> {#(maniNgA#} ed. Calc.).
 628802:<ls>MBH. 7, 1487, ed. Bomb.</ls> {#(aprati°#} ed. Calc.).
 645824:<ls>MBH. 3, 16111 ed. Bomb.</ls> St. {#apASrayavant#} der ed. Calc.
 645858:<ls>MBH. 13, 3262 ed. Bomb.</ls> st. {#a°#} der ed. Calc. 
 657396:<ls>MBH. 1, 2988, ed. Bomb.</ls> <ls>Z. 17</ls> lies {#nAganAsoru#} st. {#nagna°#} . 
 665475:<ls>MBH. 3, 11383, ed. Bomb.</ls>
 701637:<ls>MBH. 5, 68 ed. Bomb.</ls>
1138062:<ls>Z. 6. 7 ed. Bomb.</ls> {#tasya kAlaH parAyaRam#}; vgl. 
1144538:<ls>MBH. 1, 7051. 7019 ed. Bomb.</ls>

# -------------------------------------------------------------
# install temp_mw_4.txt and check xml
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
 #prints 'ok'

***************************************************************************
# markup for 'ed. Calc.'
cp temp_mw_4.txt temp_mw_5.txt
# manual changes from temp_mw_4.txt
touch change_5.txt

Add tooltip for ed. Calc.  : "Calcutta edition of various works [Cologne addition]"
# revise local copy
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/mwbib_input.txt temp_tooltip.txt 

1350 matches in 1348 lines for "ed\. Calc\.(<ls>ed. Calc."
32 matches for "<ls>ed\. Calc\."
  manually revise
 No lines starting with 'ed. Calc.'
1318 matches in 1317 lines for "[^>]ed\. Calc\."

 5 Matches with "<ls>RAGH. (ed. Calc.)"  temporary change to "<ls>RAGH. (ed._Calc.)"
 6 matches for "P. (ed. Calc.)" temporary change to "P. (<ls>ed._Calc.</ls>)"
 Finally change all "(ed. Calc.)" to "(<ls>ed._Calc.</ls>)"

118 matches for "<ls>RAGH. ed. Calc." temporary change to "<ls>RAGH. ed._Calc."
475 matches for "<ls>LALIT. ed. Calc." temporary change to "<ls>LALIT. ed._Calc."
  9 matches for "<ls>RĀJA-TAR. ed. Calc." temporary change to "<ls>RĀJA-TAR. ed._Calc."
  2 matches for "<ls>MṚCCH. ed. Calc." temporary change to "<ls>MṚCCH. ed._Calc."
  2 matches for "<ls>M. ed. Calc." temporary change to "<ls>M. ed._Calc."

All instances of "<ls>ed. Calc." temporary change to "<ls>ed._Calc."
No instances of "ed. Calc." within an <ls>X</ls> (all temporarily changed to "ed._Calc.")
656 matches in 655 lines for "ed. Calc."  These remain to be marked.
Have marked all "(ed. Calc." instances to "(ed._Calc."
624 matches in 623 lines for "ed. Calc." These remain to be marked.
** break point 1** (change_5.txt updated)
110 changes of "ed. Calc.$" to "<ls>ed._Calc.</ls>".

45 matches for "ed. Calc. $"  temporarily marked as "<ls>ed._Calc. "
287 matches for " ed. Calc.)" temporarily marked as " <ls>ed._Calc.</ls>)"
 43 matches for " ed. Calc. {#" temporarily marked as " <ls>ed._Calc.</ls> {#"
 15 matches for " ed. Calc.;" temporarily marked as " <ls>ed._Calc.</ls>;
 21 matches for " ed. Calc. zu" temporarily marked as " <ls>ed._Calc.</ls> zu"
 24 matches for " ed. Calc.,"  temporarily marked as " <ls>ed._Calc.</ls>,"
 27 matches for " der ed. Calc. "  temporarily marked as " der <ls>ed._Calc.</ls> "
 23 matches for "die ed. Calc. " temporarily marked as "die <ls>ed._Calc.</ls> "
 21 matches for "ed. Calc."  are all that remain. temporarily marked as "<ls>ed._Calc.</ls>"

Now there are no "ed. Calc." -- all have been marked.
Remove temporary markup:  "ed._Calc." -> "ed. Calc."
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
# consolidate change_4.txt and change_5.txt
mv change_4.txt tempprev_change_4.txt
mv change_5.txt tempprev_change_5.txt
python diff_to_changes.py temp_mw_3.txt temp_mw_4.txt change_4.txt
# 2680 changes written to change_4.txt
python diff_to_changes.py temp_mw_4.txt temp_mw_5.txt change_5.txt
762 changes written to change_5.txt


# -------------------------------------------------------------

# install temp_mw_5.txt and check xml
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
 #prints 'ok'

# redo the summary
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/mwbib_input.txt temp_tooltip.txt
python ../mbh1/lsextract_all.py temp_mw_5.txt temp_tooltip.txt lsextract_mw.txt
********************************************************************
temp_mw_6, change_6.
Misc. corrections from
 https://github.com/sanskrit-lexicon/MW/issues/57
;
1. "<ls> "  14 instances. corrected variously.
2. prAjApatya problem previously corrected
3. aByudyAtA  problem previously corrected.
4. " >" one instance found and corrected. (hw. vedas)
5. <ls n="?">  3 instances corrected.
6. untagged 'R. ed. Ser.'  corrected
7. <ls n="R. SCHL. 2,">1, 26, 1.</ls>  corrected.
8. "R. ed. Bomb " -> "R. ed. Bomb. " (32)
9. 'R. ed. Bomb"' -> 'R. ed. Bomb."' (13)
10. <ls n="R. GORR.">7, x, y, z.</ls> -> <ls n="R. ed. Bomb.">7, x, y, z.</ls>
 8 instances
<ls n="R. GORR.">7, 23, 5, 8.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 59, 1, 21.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 59, 1, 22.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 23, 4, 18.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 23, 5, 61.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 23, 1, 14.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 59, 3, 26.</ls>  (ABNORMAL)
<ls n="R. GORR.">7, 23, 4, 32.</ls>  (ABNORMAL)

python diff_to_changes.py temp_mw_5.txt temp_mw_6.txt change_6.txt
417 changes written to change_6.txt

; ------------------------------------------------------------------
# install temp_mw_6.txt and check xml
cp temp_mw_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
 #prints 'ok'

# redo the summary
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/mwbib_input.txt temp_tooltip.txt
python ../mbh1/lsextract_all.py temp_mw_5.txt temp_tooltip.txt lsextract_mw.txt
sh redo_lsextract_v1.sh
grep 'ABNORMAL' lsextract_v1_*.txt > lsextract_abnormal.txt
********************************************************************
cp temp_mw_6.txt temp_mw_7.txt
touch change_7.txt
Suggestions by Andhrabharati
 at https://github.com/sanskrit-lexicon/MW/issues/57#issuecomment-1166420289
In Emacs syntax, do the regex replacement:
<ls>\([^<]*[.]\)\([0-9]\) → <ls>\1 \2
This must be done several times to get all the cases;
Roughly 5500 occurrences changed

After this, there are only 11 cases "\.[0-9]" (period followed by digit,
  not necessarily in <ls>X</ls>
  A couple of these changed as deemed appropriate.
Now the only "\.[0-9]" instances are in cases like <L>12345.6, which are ok.

Did not replace ",D" by ", D" (D a digit).  May do this later on.

python diff_to_changes.py temp_mw_6.txt temp_mw_7.txt change_7.txt
3756 lines changed.

# install
cp temp_mw_7.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
#ok
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/20220628-rv/
