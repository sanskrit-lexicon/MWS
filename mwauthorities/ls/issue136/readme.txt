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
temp_1.txt misc
. changes
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
 (commit 22529fc647d41f22215eebfb55b2cb3c438067e5)
and update the correspondents at Cologne web site.
DONE with this batch of corrections.
*************************************************************************
 Further corrections
 cp temp_mw_4.txt temp_mw_5.txt
 touch change_5.txt
 
*************************************************************************
---------------------------------------------------------------------------
-- option 4a
https://github.com/sanskrit-lexicon/MWS/issues/136#issuecomment-1185768296
-- s1 within ls
  r'(<ls[^<]*)<s1',
  r'**\1<s1'
python make_change_regex.py 4a temp_mw_5.txt temp_change_regex_4a.txt
3 cases written to temp_change_regex_4a.txt
# manual revision to temp_change_regex_4a.txt
# insert temp_change_regex_4a.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt

---------------------------------------------------------------------------
https://github.com/sanskrit-lexicon/MWS/issues/136#issuecomment-1185774457
-- option 4b space between digits
r'([0-9]) ([0-9])',
r'\1**\2'
python make_change_regex.py 4b temp_mw_5.txt temp_change_regex_4b.txt
69 cases written to temp_change_regex_4b.txt
# manual revision to temp_change_regex_4b.txt
# insert temp_change_regex_4b.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
61 change transactions from change_5.txt

NOTE: Uttamac.²  ls abbreviation. 2 instances @ gopAcala and gOrjara
NOTE: space between digits kept for fractional measures, e.g.
     ' a <ab>partic.</ab> weight (= 1 1/2 <s1 slp1="mAzaka">Māṣaka</s1>s)'
     
---------------------------------------------------------------------------
-- option 4c space between digits
r'( *- *</ls>)',
r'</ls>**'
python make_change_regex.py 4c temp_mw_5.txt temp_change_regex_4c.txt
7 cases written to temp_change_regex_4c.txt
# manual revision to temp_change_regex_4c.txt
# insert temp_change_regex_4c.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
82 change transactions from change_5.txt

# change_5 includes temp_misc_1, derived from
https://github.com/sanskrit-lexicon/MWS/issues/136#issuecomment-1185806744


---------------------------------------------------------------------------
# search for unknown ls abbreviations
-- option 1:  missing period at end of ls abbrev
python ls_unknown.py 1 temp_mw_5.txt temp_tooltip.txt temp_ls_unknown_1.txt
60 cases written to temp_ls_unknown_1.txt
# insert temp_ls_unknown_1.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
142 change transactions from change_5.txt

-- option 2: no space in ls, and unknown ls abbrev.
python ls_unknown.py 2 temp_mw_5.txt temp_tooltip.txt ls_unknown_2.txt
741 tooltips from temp_tooltip.txt
271 with unknown ls abbreviation
271 cases written to ls_unknown_2.txt
118 Records written to ls_unknown_mwauth.txt


python ls_unknown.py 2 temp_mw_5.txt temp_tooltip.txt ls_unknown_2.txt ls_unknown_mwauth.txt
# ls_unknown_2.txt  the instances with unknown ls abbreviations
# ls_unknown_mwauth.txt to be added to mwath.
#  edit c:/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/
#  insert lines from ls_unknown_mwauth.txt at bottom
# Also  add 'ib.' 'ibidem' to temp_tooltip.txt
# Now install
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth
python tooltip.py roman mwauth.txt tooltip.txt
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt temp_tooltip1.txt

python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
186 change transactions from change_5.txt

# rerun with temp_tooltip: should get no examples
python ls_unknown.py 2 temp_mw_5.txt temp_tooltip1.txt temp_ls_unknown_2.txt temp_ls_unknown_mwauth.txt

-- option 3: manual change of remaining unknown ls abbreviations
# note use of temp_tooltip1.txt 
python ls_unknown.py 3 temp_mw_5.txt temp_tooltip1.txt temp_ls_unknown_3.txt
77 cases written to temp_ls_unknown_3.txt
# manual correction to temp_ls_unknown_3.txt.
# insert temp_ls_unknown_3.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
185 cases
change transactions from change_5.txt

Additional tooltips needed: (27)
Wilson, Hindu Theatre
Kāth.
ŚāntiP.
Kielhorn, Mahābhāṣya
Lassen, IA.
ChandS.
Jyotirv.
Gop.
Śivak.
Nidān.
BP.
Mantram
VāsiṣṭhalP.
Vardhamānac
Sūtrakṛt.
GārUp.
ŚulbPariś.
Krauñca-dvīpa
HanRāmUp.
Kath.
ĀpDh.
Bañc.
Manu
Ind. Ant.
Pur.
MWB.
Śivas.
Rām.

# Put this list into temp_abbrevlist.txt (manual)
# construct file of prototype mwauth lines, starting with code at 92.00
python make_mwauth_entries.py 92.00 temp_abbrevlist.txt temp_mwauth_entries.txt
28 lines written to temp_mwauth_entries.txt
# Sample line:
92.02	Kāth.	Kāth.	ti	<expandNorm><ti>Unknown reference</ti> [Cologne Addition]</expandNorm>

#  edit c:/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/
#  insert lines from ls_unknown_mwauth.txt at bottom
# Also  add 'ib.' 'ibidem' to temp_tooltip.txt
# Now install
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth
python tooltip.py roman mwauth.txt tooltip.txt
888 lines written to tooltip.txt
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136
# next version of tooltip: temp_tooltip2.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt temp_tooltip2.txt

# rerun with tooltip2
python ls_unknown.py 3 temp_mw_5.txt temp_tooltip2.txt temp_ls_unknown_3_rev.txt
0 cases written to temp_ls_unknown_3_rev.txt

--------------------------------------------------------------------------
ls_abbrev_instances.py
 Given a list of ls abbreviations, generate a list of instance lines from
 mw.txt for each instance of each abbreviation.
We first apply this to the list of abbreviations in temp_tooltip2.txt which
  are 'unknown' (the list in file abbrevlist_unknown.txt, 147 items).
python ls_abbrev_instances.py temp_mw_5.txt abbrevlist_unknown.txt temp_tooltip2.txt ls_abbrev_instances_unknown.txt

--------------------------------------------------------------------------
python ls_abnormal.py temp_mw_5.txt temp_tooltip2.txt temp_abnormal.txt
680 cases written to temp_abnormal.txt
# manual edit corrections in temp_abnormal.txt
# insert revised temp_abnormal.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
734 change transactions from change_5.txt


# additions to mwauth:
python make_mwauth_entries.py 93.00 temp_abbrevlist1.txt temp_mwauth_entries1.txt
21 Records written to temp_mwauth_entries1.txt

#  edit c:/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/
#  insert lines from ls_unknown_mwauth.txt at bottom
# Also  add 'ib.' 'ibidem' to temp_tooltip.txt
# Now install
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth
python tooltip.py roman mwauth.txt tooltip.txt
910 lines written to tooltip.txt
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt temp_tooltip3.txt

temp_abbrevlist1.txt contains these 22:
Śak. (Pi.)
Zachariae, Beiträge
Kaegi, Der Ṛgveda
Muir, S. T.
Kielhorn, Mahābhāṣya
Ludwig, RV.
Pat. (K.)
RV. AnuvAnukr.
Uttamac.²
R. (B.)
R. (B)
R. [B.]
YajurV. Parīś.
R. G.
AV. Paipp.
Śak. (Chézy)
Pañc. B.
SV.Anukr.
ĀpastPray.
AV., SBE.
Muir's Sanskrit Texts
ĀpGṛh.

# rerun after changes and tooltip revisions.
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
188 cases written to temp_abnormal1.txt

# revisions to what are considered 'normal' part of ls references
# revision 1: allow 'p.' and 'pp.'
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
101 cases written to temp_abnormal1.txt

# revision 2: also, allow n and note
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
89 cases written to temp_abnormal1.txt

# revision 3: also, allow a/b.  Example: <ls>Sāh. vi, 212 a/b.</ls> 
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
58 cases written to temp_abnormal1.txt

python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
743 change transactions from change_5.txt

# revision 4: also, allow 14/v, 14c/v.
  Example: <L>71033<pc>383,3<k1>caRqIdAsa    <ls>Sāh. iv, 14c/v</ls> 
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
47 cases written to temp_abnormal1.txt

# revision 5: also, allow 'vol'
  Example: <ls>Siddh. vol. i, p. 17</ls>
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
43 cases written to temp_abnormal1.txt

# revision 6: also, allow 'Introd'
  Example: <ls n="Sūryad.">Introd. 43.</ls> 
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt temp_abnormal1.txt
39 cases written to temp_abnormal1.txt

There are certain other rare regularities among the 39. But let's stop
and just keep the list:
python ls_abnormal.py temp_mw_5.txt temp_tooltip3.txt lsabnormal_5.txt

--------------------------------------------------------------------------
48 matches for "<ls[^<]* [^<]*[cixlv][.]? [0-9]" in buffer: temp_mw_5.txt
-- option 5
   
python make_change_regex.py 5 temp_mw_5.txt temp_change_regex_5.txt
48 cases written to temp_change_regex_5.txt
# manual revision to temp_change_regex_5.txt
# insert temp_change_regex_5.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
786 change transactions from change_5.txt

<ab>sq.</ab>  only 1 instance
--------------------------------------------------------------------------
9 matches for "<ls[^<]*\b[xivlc]+, [xivlc]" in buffer: temp_mw_5.txt
-- option 5a
python make_change_regex.py 5a temp_mw_5.txt temp_change_regex_5a.txt
9 cases written to temp_change_regex_5a.txt
# manual revision to temp_change_regex_5a.txt
# insert temp_change_regex_5a.txt into change_5.txt
python updateByLine.py temp_mw_4.txt change_5.txt temp_mw_5.txt
794 change transactions from change_5.txt

--------------------------------------------------------------------------
Miscellaneous notes to self
<ls n="">  </ls>  ī
</ls>-<ls n="">
print change
369808 old <L>109733<pc>556,1<k1>nirBinna<k2>nir-Binna<h>b<e>
  h = 2.  not shown in print.
 
----------------
install of temp_mw_5.txt to check xml
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

---------------------------------------------------------------------------
Push the csl-orig and csl-pywork to Github,
 (commit a741782ce4cad4e8dc742419c5950df5cc02154a)
and update the correspondents at Cologne web site.
DONE with this batch of corrections.

*************************************************************************
 Further corrections, continued
 cp temp_mw_5.txt temp_mw_6.txt
 touch change_6.txt
 
*************************************************************************

---------------------------------------------------------------------------
7 matches for "-[0-9].<info" in buffer: temp_mw_6.txt
-- option 6
python make_change_regex.py 6 temp_mw_6.txt temp_change_regex_6.txt
7 cases written to temp_change_regex_6.txt
# manual revision to temp_change_regex_6.txt
# insert temp_change_regex_6.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
14 change transactions from change_6.txt

After changes:
1. <ls>MBh. vi</ls>, chs. 1-6.<info lex="n"/>
   under jambUKaRqavinirmARaparvan
2. <ls>PadmaP., Svargakh. 1-5.</ls>  This also abnormal
  under <L>211385<pc>1046,3<k1>SakuntalopAKyAna

---------------------------------------------------------------------------
112 matches in 109 lines for "  " in buffer: temp_mw_6.txt
-- option 7a
 "  " -> " "
python make_change_regex.py 7a temp_mw_6.txt temp_change_regex_7a.txt
112 cases written to temp_change_regex_7a.txt
# insert temp_change_regex_7a.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
123 change transactions from change_6.txt

---------------------------------------------------------------------------
10 matches for " ," in buffer: temp_mw_6.txt
-- option 7b
 " ," -> ","
python make_change_regex.py 7b temp_mw_6.txt temp_change_regex_7b.txt
10 cases written to temp_change_regex_7b.txt
# manual change:  some of these require other changes
# e.g.  <ls n="Pāṇ.">v, ,1, 29</ls> => <ls n="Pāṇ.">v, 1, 29</ls>
# insert temp_change_regex_7b.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
133 change transactions from change_6.txt

---------------------------------------------------------------------------
9 matches for " ;" in buffer: temp_mw_6.txt

-- option 7d
 " ." -> "."
python make_change_regex.py 7d temp_mw_6.txt temp_change_regex_7d.txt
6 cases written to temp_change_regex_7d.txt
# manual change - two periods removed. Others within <s>xx</s> unchanged.
# insert temp_change_regex_7d.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
135 change transactions from change_6.txt
---------------------------------------------------------------------------

9 matches for " ;" in buffer: temp_mw_6.txt

-- option 7d
 " ;" -> ";"
python make_change_regex.py 7d temp_mw_6.txt temp_change_regex_7d.txt
9 cases written to temp_change_regex_7d.txt
# manual 
# insert temp_change_regex_7d.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
144 change transactions from change_6.txt
---------------------------------------------------------------------------

10 matches for " )" in buffer: temp_mw_6.txt

-- option 7e
 " )" -> ")"
python make_change_regex.py 7e temp_mw_6.txt temp_change_regex_7e.txt
10 cases written to temp_change_regex_7e.txt
# insert temp_change_regex_7e.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
154 change transactions from change_6.txt

---------------------------------------------------------------------------

3 matches for " >" in buffer: temp_mw_6.txt

-- option 7f
 " >" -> " "
python make_change_regex.py 7f temp_mw_6.txt temp_change_regex_7f.txt
10 cases written to temp_change_regex_7f.txt
# insert temp_change_regex_7f.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
161 change transactions from change_6.txt
(Also a few 'misc' changes)

---------------------------------------------------------------------------

10 matches for "<ls n="Unknown" in buffer: temp_mw_6.txt

-- option 7g
Manually change per https://github.com/sanskrit-lexicon/MWS/issues/136#issuecomment-1191246505

 <L>81877<pc>433,1<k1>tattvaboDa
   knowledge or understanding of truth, <ls n="Sarvad.">xii, 46</ls>
   [cf. PWG, and MW tattvaprakASa]
python make_change_regex.py 7g temp_mw_6.txt temp_change_regex_7g.txt
10 cases written to temp_change_regex_7g.txt
# insert temp_change_regex_7g.txt into change_6.txt
python updateByLine.py temp_mw_5.txt change_6.txt temp_mw_6.txt
171 change transactions from change_6.txt

----------------------------------------------------------
temp_tooltip4.txt
1 new ls : Saṃgīta-darpaṇa added to mwauth an
#  edit c:/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/
# Now install
cd /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth
python tooltip.py roman mwauth.txt tooltip.txt
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt temp_tooltip4.txt



---------------------------------------------------------------------------
install of temp_mw_6.txt to check xml
cp temp_mw_6.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue136

---------------------------------------------------------------------------
Push the csl-orig and csl-pywork to Github,
 (csl-orig commit 1d017dc7741f3a7ffd1009dd37685d8ed78ef123)
and update the correspondents at Cologne web site.
DONE with this second additional batch of corrections.

---------------------------------------------------------------------------
TODO: some action is taken on the issue #135
TODO: regenerate 'unknown instances' listing, with the extra 22 Unknown.
comment: <L>95073.9<pc>490,2<k1>df|a and <L>95074<pc>490,2<k1>dfQa
have the 'or' markup: <info or="95074,dfQa;95073.9,df|a"/>

---------------------------------------------------------------------------
Generate
cd ../../../mwtranscode
python mw_transcode.py slp1 roman ../mwauthorities/ls/issue136/temp_mw_6.txt ../mwauthorities/ls/issue136/temp_mw_6_iast.txt
#confirm invertibility:
python mw_transcode.py roman slp1 ../mwauthorities/ls/issue136/temp_mw_6_iast.txt ../mwauthorities/ls/issue136/temp_mw_6_slp1.txt
cd ../mwauthorities/ls/issue136/
diff temp_mw_6.txt temp_mw_6_slp1.txt
# no difference

> What is the reason for the difference of 21  (in mwauth unknown)

The second group was discovered after the first group; see the list in readme.txt following
'temp_abbrevlist1.txt contains these 22'
[temp_mw_6_iast.zip](https://github.com/sanskrit-lexicon/MWS/files/9163019/temp_mw_6_iast.zip)


---------------------------------------------------------------------------
generate instances of unknown ls abbreviations
# list of unknowns
grep Unknown temp_tooltip4.txt > abbrevlist_unknown.txt
# instances
python ls_abbrev_instances1.py temp_mw_6.txt abbrevlist_unknown.txt temp_tooltip4.txt ls_abbrev_instances_unknown1.txt
1963 cases written to ls_abbrev_instances_unknown1.txt

# iast instances
python ls_abbrev_instances1.py temp_mw_6_iast.txt abbrevlist_unknown.txt temp_tooltip4.txt ls_abbrev_instances_unknown1_iast.txt
1963 cases written to ls_abbrev_instances_unknown1_iast.txt
---------------------------------------------------------------------------
