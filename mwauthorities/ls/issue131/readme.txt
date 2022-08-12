MWS/mwauthorities/ls/issue131

Ref: https://github.com/sanskrit-lexicon/MWS/issues/131

Homonymd
# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

Start with a copy of csl-orig/v02/mw/mw.txt at commit
  846e7f032140f3c1206ff05a55d613beb14d8501

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show 846e7f03:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue131/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue131/
# -------------------------------------------------------------
*********************************************************************
BEGIN change_1
---------------------------------------------------------------------
# temp_mw_1.txt
cp temp_mw_0.txt temp_mw_1.txt
touch change_1.txt
----------------------------------------------------------
# <hom>n</hom> -> <hom>n.</hom>  (n a digit, 1 to 6)

python make_change_regex.py 1 temp_mw_1.txt temp_change_regex_1.txt
158 cases written to temp_change_regex_1.txt
# insert temp_change_regex_1.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
158 change transactions from change_1.txt

---------------------------------------------------------------------
123 matches for "<hom>[a-c]\." in buffer: temp_mw_1.txt

# <hom>n\.</hom> -> <hom>n</hom>  (n a lower-case letter , [a-c]
python make_change_regex.py 1a temp_mw_1.txt temp_change_regex_1a.txt
123 cases written to temp_change_regex_1a.txt
# insert temp_change_regex_1a.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
281 change transactions from change_1.txt

---------------------------------------------------------------------
1 match for "</hom><s>" in buffer: temp_mw_1.txt

#  </hom><s> -> </hom> <s>
python make_change_regex.py 1b temp_mw_1.txt temp_change_regex_1b.txt
1 cases written to temp_change_regex_1b.txt
# insert temp_change_regex_1b.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
282 change transactions from change_1.txt

---------------------------------------------------------------------
31 matches for "^<s>[^<]*</s> <hom>[0-9][.]</hom> ¦" in buffer: temp_mw_1.txt
# change so hom comes first.
python make_change_regex.py 1c temp_mw_1.txt temp_change_regex_1c.txt
31 cases written to temp_change_regex_1c.txt
# insert temp_change_regex_1c.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
313 change transactions from change_1.txt

Note: in case of the three homonyms of 'tva', the print shows
 tva 1.,  tva 2., and 3. tva
 This is because the tva 1. is an H1 (Devanagari shows in print)
 while tva 2. and tva 3. are H2 (IAST only)

---------------------------------------------------------------------
15 matches for "= <s>[^<]*</s> <hom>[0-9][.]</hom>" in buffer: temp_mw_1.txt
python make_change_regex.py 1d temp_mw_1.txt temp_change_regex_1d.txt
15 cases written to temp_change_regex_1d.txt
# insert temp_change_regex_1d.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
328 change transactions from change_1.txt

---------------------------------------------------------------------
1 misc. change in change_1.
<L>20545<pc>118,2<k1>asatkftya
74050 old <hom>1.</hom> <s>a/-sat—kftya</s> <hom>1.</hom> ¦ <ab>ind.p.</ab> not taking notice of (<ab>acc.</ab>), <ls>MBh. xiii, 2766.</ls>
74050 new <hom>1.</hom> <s>a/-sat—kftya</s> ¦ <ab>ind.p.</ab> not taking notice of (<ab>acc.</ab>), <ls>MBh. xiii, 2766.</ls>
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
329 change transactions from change_1.txt

Note:  Now,
47 matches for "<s>[^<]*</s> <hom>[0-9][.]</hom>" in buffer: temp_mw_1.txt
But also
47 matches for "<s>[^<]*</s> <hom>[0-9][.]</hom> <s>" in buffer: temp_mw_1.txt
so no change is required for remaining <s>[^<]*</s> <hom>[0-9][.]</hom>


---------------------------------------------------------------------
141 matches for "<h>[0-9][a-z]" in buffer: temp_mw_1.txt
134 matches for "<hom>[0-9][a-z]</hom>" in buffer: temp_mw_1.txt
  These 134 all occur before ¦
These need to be examined individually, And together.
python make_change_hom1.py temp_mw_1.txt temp_change_hom1.txt
598 change transactions from change_1.txt
python make_change_hom1.py temp_mw_1.txt temp_change_hom1_rerun.txt
66  cases   (These are the remaining Number-letter homonyms)
   
NOTES:
1. dU has two hom 2.
   <L>93282.1<pc>482,3<k1>dU<k2>dU<h>2<e>1
   <L>94860<pc>489,2<k1>dU<k2>dU<h>2<e>1
1a. dU also has two hom 1.
    <L>93281.1<pc>482,3<k1>dU<
    <L>94693<pc>488,2<k1>dU<
2. check parItta
3. There are two hom 1 for vidyut:
   <L>193132<pc>951,1<k1>vidyut
   <L>196283<pc>966,3<k1>vidyut
4. two hom 1 for vft:
   <L>203984<pc>1007,2<k1>vft
   <L>204340<pc>1009,1<k1>vft
5. two hom 1 for Sas:
   <L>210869<pc>1044,1<k1>Sas
   <L>214531<pc>1060,3<k1>Sas
6. two hom 1 for sajj
   <L>229022<pc>1131,2<k1>sajj
   <L>229217.1<pc>1132,3<k1>sajj
7. no hom 1 for kzAmi

---------------------------------------------------------------------
11 matches in 8 lines for "<s> " in buffer: temp_mw_1.txt
 remove the space
python make_change_regex.py 1e temp_mw_1.txt temp_change_regex_1e.txt
8 cases written to temp_change_regex_1e.txt
# insert temp_change_regex_1e.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
606 change transactions from change_1.txt
 
---------------------------------------------------------------------
1 match for " </s>" in buffer: temp_mw_1.txt remove the space
# remove the space
python make_change_regex.py 1f temp_mw_1.txt temp_change_regex_1f.txt
1 cases written to temp_change_regex_1f.txt
# insert temp_change_regex_1f.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
607 change transactions from change_1.txt
 
---------------------------------------------------------------------
31 matches for "<hom>[d-r]" in buffer: temp_mw_1.txt
  many with 'sa'
python make_change_regex.py 1g temp_mw_1.txt temp_change_regex_1g.txt
31 cases written to temp_change_regex_1g.txt

# parisyand
cp temp_mw_1.txt temp_mw_1a.txt
# edit temp_mw_1a.txt manually.
# construct change file
python diff_to_changes.py temp_mw_1.txt temp_mw_1a.txt temp_change_parisyand.txt
# insert temp_change_parisyand.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
616 change transactions from change_1.txt

# SravaRA  hom a-d.   All except hom b are feminie forms of
  homonyms 1-3 of SravaRa.  The text makes no homonym marking for
  these feminie forms.
  Could use hom 1-3 instead of hom a,c,d, but this change not made now.

# sa  hom a-r  no change
  These are short entries preceding sequences of compounds beginning with 'sa'
  
# Examine these manually and change as required.
# insert temp_change_regex_1g.txt into change_2.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
607 change transactions from change_1.txt
 
---------------------------------------------------------------------------
consistency of hom between metaline and 'header'.
  The 'header' is section of line following metaline that precedes ¦.
# discrepancies with numeric hom.
metaline <h>N
header ^<hom>N.</hom>   (^ means line must start with this)

# first, with numbers  (option 'num')
python make_change_hom2.py num temp_mw_1.txt temp_change_hom2_num.txt
76 cases written to temp_change_hom2_num.txt
# manually alter temp_change_hom2_num.txt
# insert temp_change_hom2_num.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
715 change transactions from change_1.txt

# some of these need further review
python make_change_hom2.py num temp_mw_1.txt temp_change_hom2_num_rerun.txt
38 cases written to temp_change_hom2_num_rerun.txt
Note: nothing currently done with these 38 cases.

---------------------------------------------------------------------------

# option 'letter'
python make_change_hom2.py letter temp_mw_1.txt temp_change_hom2_letter.txt
cases written to temp_change_hom2_letter.txt
# manually alter temp_change_hom2_letter.txt
# insert temp_change_hom2_letter.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
change transactions from change_1.txt

No changes made here.  It is unclear what to do.

---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------

# install of temp_mw_1.txt 
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
 
-------------------------------------------------------------------------
Push repositories to Github.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/131 (change_1)
 csl-orig  commit a4b2854a2b8acca106f7cb6d08c5834e5417000d
and update at Cologne web site.

 push this MWS repository to Github.

DONE with this batch of corrections.

End change_1

*********************************************************************
---------------------------------------------------------------------
Possible TODO:
1. 94 matches in 93 lines for " only," in buffer: temp_mw_1.txt
 some of these should drop the comma after "only" such as
 <L>14953<pc>86,1<k1>ayuta
 ([<s>as</s> <lex type="hwalt">m.</lex> only, <ls>MBh. iii, 801</ls>])
2.
  855 matches in 738 lines for "(\[" in buffer: temp_mw_1.txt
 1066 matches in 943 lines for "\])" in buffer: temp_mw_1.txt
  849 matches in 732 lines for "(\[[^]]*\])" in buffer: temp_mw_1.txt
 Why different count?  Maybe some ([X]) go over two lines.

 Spot check with print suggests the change: ([X]) -> [X]

*********************************************************************
