MWS/mwauthorities/ls/issue134

Ref: https://github.com/sanskrit-lexicon/MWS/issues/136


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

Start with a copy of csl-orig/v02/mw/mw.txt at commit
  3336b724834e84ef0ae1010d73a95fa090292761

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this spruch directory
  git show 3336b724:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136/
# -------------------------------------------------------------
# -------------------------------------------------------------
temp_tooltip.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth

python tooltip.py roman mwauth.txt temp_tooltip.txt
737 auth records
737 lines written to temp_tooltip.txt

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136/
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/temp_tooltip.txt .

---------------------------------------------------------------------
temp_1.txt misc. changes
cp temp_mw_0.txt temp_mw_1.txt
touch change_1.txt

---------------------------------------------------------------------
look for RV ls references which do not start 'normally' and where
the previous ls IS normal.
Example:
in L=89869, dattra
 <ls n="RV.">viii, 49, 2.</ls>
in L= 89870, dattravat
 <ls>vi, 50, 8</ls>  -> <ls n="RV.">vi, 50, 8</ls>
 

-- option 1
  u roman, x and y digits
  <ls>A u, x and y</ls>
  <ls>A u, x</ls> and <ls n="A y,">y</ls>
python make_change_multi.py 1 temp_mw_1.txt temp_tooltip.txt temp_change_multi_1.txt
287 cases written to temp_change_multi_1.txt
# insert temp_change_multi_1.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt

-- option 2
  u and v roman, x and y digits
  <ls>A u, x and v, y</ls>
  <ls>A u, x</ls> and <ls n="A">v, y</ls>
python make_change_multi.py 2 temp_mw_1.txt temp_tooltip.txt temp_change_multi_2.txt
62 cases
# insert temp_change_multi_2.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
349 change transactions from change_1.txt

-- option 3a
 ' and<ls> ' -> '<ls> and '
python make_change_multi.py 3a temp_mw_1.txt temp_tooltip.txt temp_change_multi_3a.txt
28 cases written to temp_change_multi_3a.txt
# insert temp_change_multi_3a.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
377 change transactions from change_1.txt

-- option 3b
 ' and<ls>; <ls ' -> '<ls> and <ls'
python make_change_multi.py 3b temp_mw_1.txt temp_tooltip.txt temp_change_multi_3b.txt
56 cases written to temp_change_multi_3b.txt
# insert temp_change_multi_3b.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
433 change transactions from change_1.txt

-- option 4a
  u roman; x,y,z digits
  <ls>A u, x, y and z</ls>
  <ls>A u, x, y</ls> and <ls n="A x, y,">z</ls>
python make_change_multi.py 4a temp_mw_1.txt temp_tooltip.txt temp_change_multi_4a.txt
94 cases written to temp_change_multi_4a.txt
# insert temp_change_multi_4a.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
528 change transactions from change_1.txt

-- option 4b
  u roman; x,y,z,w digits
  <ls>A u, x, y and z, w</ls>
  <ls>A u, x, y</ls> and <ls n="A x,">z, w</ls>
python make_change_multi.py 4b temp_mw_1.txt temp_tooltip.txt temp_change_multi_4b.txt
60 cases written to temp_change_multi_4b.txt
# insert temp_change_multi_4b.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
588 change transactions from change_1.txt

-- option 4c
  u,v roman; x,y,z,w digits
  <ls>A u, x, y and v, z, w</ls>
  <ls>A u, x, y</ls> and <ls n="A">v, z, w</ls>
python make_change_multi.py 4c temp_mw_1.txt temp_tooltip.txt temp_change_multi_4c.txt
24 cases written to temp_change_multi_4c.txt
# insert temp_change_multi_4c.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
612 change transactions from change_1.txt

-- option 5
  x and y digits
  <ls>A x and y</ls>
  <ls>A x</ls> and <ls n="A">y</ls>
python make_change_multi.py 5 temp_mw_1.txt temp_tooltip.txt temp_change_multi_5.txt
58 cases written to temp_change_multi_5.txt
# insert temp_change_multi_5.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
670 change transactions from change_1.txt

-- option 6
These corrections are done manually. The program sets up the corrections.
  x and y are ARBITRARY strings
  <ls>A x and y</ls>
  <ls>A x</ls> and <ls n="A">y</ls>
python make_change_multi.py 6 temp_mw_1.txt temp_tooltip.txt temp_change_multi_6.txt
194 cases written to temp_change_multi_6.txt
# manual edit of temp_change_multi_6.txt
# insert temp_change_multi_6.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
864 change transactions from change_1.txt

Still some remain.
12 matches for "<ls[^<]* and" in buffer: temp_mw_1.txt
#Changes for these records constructed manually in temp_change_and.txt
# insert temp_change_and.txt into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
875 change transactions from change_1.txt

---------------------------------------------------------------------------
install of temp_mw_1.txt to check xml
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

--------------------------------------------------------------------------
FINISHED WITH make_change_multi for options with ' and' in <ls>
Now deal with ';' in <ls> and also a few misc. alterations
1011 matches in 998 lines for "<ls[^<]*;" in buffer: temp_mw_1.txt
cp temp_mw_1.txt temp_mw_2.txt
touch change_2.txt

-- option 7
 ' <ab>seq.</ab></ls>' -> '</ls> <ab>seq.</ab>'
python make_change_multi.py 7 temp_mw_2.txt temp_tooltip.txt temp_change_multi_7.txt
17 cases written to temp_change_multi_7.txt
# insert temp_change_multi_7.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
17 change transactions from change_2.txt

-- option 7a
 ';</ls>' -> '</ls>;'
python make_change_multi.py 7a temp_mw_2.txt temp_tooltip.txt temp_change_multi_7a.txt
25 cases written to temp_change_multi_7a.txt
# insert temp_change_multi_7a.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
42 change transactions from change_2.txt

-- option 7b
 ',</ls>' -> '</ls>,'
python make_change_multi.py 7b temp_mw_2.txt temp_tooltip.txt temp_change_multi_7b.txt
334 cases written to temp_change_multi_7b.txt
# insert temp_change_multi_7b.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
376 change transactions from change_2.txt

At this point,
989 matches in 976 lines for "<ls>[^<]*;" in buffer: temp_mw_2.txt
Now start the work to reformat these cases.

-- option 8
 u and v roman, x and y digits
  <ls>A u, x; v, y</ls>
  <ls>A u, x</ls>; <ls n="A">v, y</ls>
python make_change_multi.py 8 temp_mw_2.txt temp_tooltip.txt temp_change_multi_8.txt
301 cases written to temp_change_multi_8.txt
# insert temp_change_multi_8.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
677 change transactions from change_2.txt

-- option 8a
 u and v roman; x, y, z, w digits
  <ls>A u, x, y; v, z, w</ls>
  <ls>A u, x, y</ls>; <ls n="A">v, z, w</ls>
python make_change_multi.py 8a temp_mw_2.txt temp_tooltip.txt temp_change_multi_8a.txt
133 cases written to temp_change_multi_8a.txt
# insert temp_change_multi_8a.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
810 change transactions from change_2.txt

-- option 8b
 u roman, x and y digits
  <ls>A u, x; y</ls>
  <ls>A u, x</ls>; <ls n="A u,">y</ls>
python make_change_multi.py 8b temp_mw_2.txt temp_tooltip.txt temp_change_multi_8b.txt
99 cases written to temp_change_multi_8b.txt
# insert temp_change_multi_8b.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
909 change transactions from change_2.txt

-- option 8c
 x and y digits
  <ls>A x; y</ls>
  <ls>A x</ls>; <ls n="A">y</ls>
python make_change_multi.py 8c temp_mw_2.txt temp_tooltip.txt temp_change_multi_8c.txt
91 cases written to temp_change_multi_8c.txt
# insert temp_change_multi_8c.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1000 change transactions from change_2.txt


-- option 8d
 u,v,w roman, x,y,z digits
  <ls>A u, x; v, y; w, z</ls>
  <ls>A u, x</ls>; <ls n="A">v, y</ls>; <ls n="A">w, z</ls>
python make_change_multi.py 8d temp_mw_2.txt temp_tooltip.txt temp_change_multi_8d.txt
10 cases written to temp_change_multi_8d.txt
# insert temp_change_multi_8d.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1010 change transactions from change_2.txt

-- option 8e
 u roman; x, y, z, w digits
  <ls>A u, x, y; z, w</ls>
  <ls>A u, x, y</ls>; <ls n="A u,"> z, w</ls>
python make_change_multi.py 8e temp_mw_2.txt temp_tooltip.txt temp_change_multi_8e.txt
21 cases written to temp_change_multi_8e.txt
# insert temp_change_multi_8e.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1031 change transactions from change_2.txt

-- option 8f
 u roman; x, y, z digits
  <ls>A u, x, y; z</ls>
  <ls>A u, x, y</ls>; <ls n="A u, x,">z</ls>
python make_change_multi.py 8f temp_mw_2.txt temp_tooltip.txt temp_change_multi_8f.txt
38 cases written to temp_change_multi_8f.txt
# insert temp_change_multi_8f.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1069 change transactions from change_2.txt

-- option 8g
 u roman; v digits
  <ls>A u; v</ls>
  <ls>A u</ls>; <ls n="A">v</ls>
python make_change_multi.py 8g temp_mw_2.txt temp_tooltip.txt temp_change_multi_8g.txt
7 cases written to temp_change_multi_8g.txt
# insert temp_change_multi_8g.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1076 change transactions from change_2.txt

-- option 9
There remain 289 matches in 285 lines for "<ls>[^<]*;" in buffer: temp_mw_2.txt
 <ls>A x; y</ls>
 <ls>A x</ls>; <ls n="A">y</ls>
 These require manual adjustments.
 
python make_change_multi.py 9 temp_mw_2.txt temp_tooltip.txt temp_change_multi_9.txt
251 cases written to temp_change_multi_9.txt
# manual changes to temp_change_multi_9.txt
# insert temp_change_multi_9.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1323 change transactions from change_2.txt

---------------------------------------------------------------------------
install of temp_mw_2.txt to check xml
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors 
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

--------------------------------------------------------------------------
misc. punctuation changes
109 matches in 107 lines for " </ls>" in buffer: temp_mw_2.txt
cp temp_mw_2.txt temp_mw_3.txt
touch change_3.txt
Use make_change_regex.py with various options

-- option 1
 ', </ls>' -> '</ls>, '   
python make_change_regex.py 1 temp_mw_3.txt temp_change_regex_1.txt
21 cases written to temp_change_regex_1.txt
# manual revision to temp_change_regex_1.txt
# insert temp_change_regex_1.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
21 change transactions from change_3.txt

-- option 1a
 ' </ls> ' -> '</ls> '   
python make_change_regex.py 1a temp_mw_3.txt temp_change_regex_1a.txt
4 cases written to temp_change_regex_1a.txt
# manual revision to temp_change_regex_1a.txt
# insert temp_change_regex_1a.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
25 change transactions from change_3.txt

-- option 1b
 ' </ls><info' -> '</ls><info'   
python make_change_regex.py 1b temp_mw_3.txt temp_change_regex_1b.txt
46 cases written to temp_change_regex_1b.txt
# manual revision to temp_change_regex_1b.txt
# insert temp_change_regex_1b.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
71 change transactions from change_3.txt

-- option 1c
 ' </ls>' -> '</ls> '   
python make_change_regex.py 1c temp_mw_3.txt temp_change_regex_1c.txt
34 cases written to temp_change_regex_1c.txt
# manual revision to temp_change_regex_1c.txt
# insert temp_change_regex_1c.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
105 change transactions from change_3.txt

Note: there are no longer any instances of ' </ls>'.

-- option 1d
Next, ',</ls>' -> '</ls>,'
python make_change_regex.py 1d temp_mw_3.txt temp_change_regex_1d.txt
4 cases written to temp_change_regex_1d.txt
# manual revision to temp_change_regex_1d.txt
# insert temp_change_regex_1d.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
109 change transactions from change_3.txt

-- option 1e
 '</ls>; <ls>Kāś.'  -> '</ls>, <ls>Kāś.'
 This in agreement with print.
 
python make_change_regex.py 1e temp_mw_3.txt temp_change_regex_1e.txt
897 cases written to temp_change_regex_1e.txt
# manual revision to temp_change_regex_1e.txt
# insert temp_change_regex_1e.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1006 change transactions from change_3.txt

-- option 2
 '<ls>([^ <]+) ([xivcl]+), ([xivcl]+\.?)</ls>' ->
 '<ls>\1 \2</ls>, <ls n="\1">\3</ls>'
 example: <ls>ŚBr. xi, xiii.</ls> -> <ls>ŚBr. xi</ls>, <ls n="ŚBr.">xiii.</ls>
python make_change_regex.py 2 temp_mw_3.txt temp_change_regex_2.txt
897 cases written to temp_change_regex_2.txt
# manual revision to temp_change_regex_2.txt
# insert temp_change_regex_2.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1500 change transactions from change_3.txt

-- option 2a
 '<ls>([^ <]+) ([xivcl]+), ([xivcl]+), ([xivcl]+\.?)</ls>' ->
 '<ls>\1 \2</ls>, <ls n="\1">\3</ls>, <ls n="\1">\4</ls>'
 example: <ls>ŚBr. xi, xiii.</ls> -> <ls>ŚBr. xi</ls>, <ls n="ŚBr.">xiii.</ls>
python make_change_regex.py 2a temp_mw_3.txt temp_change_regex_2a.txt
80 cases written to temp_change_regex_2a.txt
# manual revision to temp_change_regex_2a.txt
# insert temp_change_regex_2a.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1583 change transactions from change_3.txt

-- option 2b
 '<ls>([^ <]+) ([xivcl]+), ([xivcl])' ->
 '<ls>\1 \2</ls>, <ls n="\1">\3'
# The change is incomplete and will be adjusted manually
python make_change_regex.py 2b temp_mw_3.txt temp_change_regex_2b.txt
82 cases written to temp_change_regex_2b.txt
# manual revision to temp_change_regex_2b.txt
# insert temp_change_regex_2b.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1659 change transactions from change_3.txt

-- option 2c
 'and ([ivxcl]+)\b'
 'and <ls n="">\1'
# The change is incomplete and will be adjusted manually
python make_change_regex.py 2c temp_mw_3.txt temp_change_regex_2c.txt
13 cases written to temp_change_regex_2c.txt
# manual revision to temp_change_regex_2c.txt
# insert temp_change_regex_2c.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1669 change transactions from change_3.txt

-- option 2d
 '([^.]) x'
 '\1 <ls n="">x'
# The change is incomplete and will be adjusted manually
python make_change_regex.py 2d temp_mw_3.txt temp_change_regex_2d.txt
193 cases written to temp_change_regex_2d.txt
# manual revision to temp_change_regex_2d.txt
# insert temp_change_regex_2d.txt into change_3.txt
python updateByLine.py temp_mw_2.txt change_3.txt temp_mw_3.txt
1745 change transactions from change_3.txt

install of temp_mw_3.txt to check xml
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors 
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

--------------------------------------------------------------------------
context regex
cp temp_mw_3.txt temp_mw_4.txt
touch change_4.txt
-- option 1
python make_change_regex1.py out,1 temp_mw_4.txt temp_change_regex1_1.txt
377 cases written to temp_change_regex1_1.txt
# manual revision to temp_change_regex1_1.txt
# insert temp_change_regex1_1.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
251 change transactions from change_4.txt

-- option 1a
NEXT ONE! missing a comma
165 matches in 151 lines for " [ivxcl]+ [0-9]" in buffer: temp_mw_4.txt
python make_change_regex1.py out,1a temp_mw_4.txt temp_change_regex1_1a.txt
111 cases written to temp_change_regex1_1a.txt
# manual revision to temp_change_regex1_1a.txt
# NOTE: Most of these are false-positives, like 'a metre of 4 x 12 syllables'
# insert temp_change_regex1_1a.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
253 change transactions from change_4.txt

-- option 2, with 'any'
57 matches in 56 lines for " [ivxcl]+\. [0-9]" in buffer: temp_mw_4.txt
python make_change_regex1.py ,1a temp_mw_4.txt temp_change_regex1_1a.txt
111 cases written to temp_change_regex1_1a.txt
# manual revision to temp_change_regex1_1a.txt
# NOTE: Most of these are false-positives, like 'a metre of 4 x 12 syllables'
# insert temp_change_regex1_1a.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
253 change transactions from change_4.txt

-- option 3a
 ' ([ivxcl]+)[.] ([0-9])'
 ' \1, \2'
# The change is incomplete and will be adjusted manually
python make_change_regex.py 3a temp_mw_4.txt temp_change_regex_3a.txt
56 cases written to temp_change_regex_3a.txt
# manual revision to temp_change_regex_3a.txt
# insert temp_change_regex_3a.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
306 change transactions from change_4.txt

-- option 3b
37 matches for "<ls[^<]* &" in buffer: temp_mw_4.txt
 '(<ls[^<]+) (&)'
 ' \1</ls> & <ls n="">'
# The change is incomplete and will be adjusted manually
python make_change_regex.py 3b temp_mw_4.txt temp_change_regex_3b.txt
37 cases written to temp_change_regex_3b.txt
# manual revision to temp_change_regex_3b.txt
# insert temp_change_regex_3b.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
354 change transactions from change_4.txt

-- option 3c
25 matches for "<ls[^<]*[0-9]\. [0-9]" in buffer: temp_mw_4.txt
 '(<ls[^<]*[0-9])[.] ([0-9]) '
 ' \1, \2'
# The change is incomplete and will be adjusted manually
python make_change_regex.py 3c temp_mw_4.txt temp_change_regex_3c.txt
25 cases written to temp_change_regex_3c.txt
# manual revision to temp_change_regex_3c.txt
# insert temp_change_regex_3c.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
426 change transactions from change_4.txt

several homonym markup errors in this list.
print change: hom 1.
361415 new <L>107372<pc>542,2<k1>nirvyaYjana<k2>nir—vyaYjana<h>1<e>3

05:12a	Maṇḍ.	unknown	Title  under bahu


--------------------------------------------------------------------------
install of temp_mw_4.txt to check xml
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

*************************************************************************
*************************************************************************
python ../issue134/diff_to_changes.py temp_mw_0.txt temp_mw_4.txt change_all.txt

---------------------------------------------------------------------------
Push the csl-orig and csl-pywork to Github,
and update the correspondents at Cologne web site.
DONE with this batch of corrections.
---------------------------------------------------------------------------
