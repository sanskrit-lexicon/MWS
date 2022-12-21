MWS/mwsissues/issue142

Ref: https://github.com/sanskrit-lexicon/MWS/issues/142
This continues the work of issue141
# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
  3630a00de9b5a5288432b1e1f414851d6f2ed54a
# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_00.txt in this directory
  git show  3630a00d:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142/temp_mw_00.txt

# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142/
 Note: temp_mw_00.txt is same as issue141/temp_mw_6.txt.
 

*********************************************************************
PHASE 4. MW ACCENT CORRECTIONS by hand
*********************************************************************
-----------------------------------------------------------------
Manual comparison of mw.txt with scan, page by page.
At this stage, pages 1-59 have been examined and changes made.
temp_mw_00.txt is the starting digitization
The next one will be temp_mw_01.txt, with changes change_mw_01.txt
cp temp_mw_00.txt temp_mw_01.txt
cp temp_mw_01.txt temp_mw_01a.txt
touch change_mw_01.txt

start with pppp = 0060 (the next page to review)

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_01a.txt for accents on page pppp
# 2. find differences between temp_mw_00.txt and temp_mw_01a.txt
python diff_to_changes.py temp_mw_01.txt temp_mw_01a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_01.txt
# 4. install further changes into temp_mw_01.txt
python updateByLine.py temp_mw_00.txt change_mw_01.txt temp_mw_01.txt
# 5. now, should have
diff temp_mw_01.txt temp_mw_01a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0100
Then install temp_mw_01.txt into csl-orig.
-------------------------------------------------------------------------
Start another 'batch' ....

Repeat this update loop until done (pppp = 1308).

Through page 0059.
Install temp_mw_6.txt into csl-orig.


------------------------------------------------------------
# continue this work for pages 0060-1308 in issue142
# Related comments in https://github.com/sanskrit-lexicon/MWS/issues/142.

change_mw-01.txt has the changes for pages 60-130.
Install The corresponding digitization version into csl-orig.

-----------------------------------------------------------------
install  temp_mw_01.txt to check xml
cp temp_mw_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0060-0130.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0060-0130.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.
-----------------------------------------------------------------
BEGIN page 0131
cp temp_mw_01.txt temp_mw_02.txt
cp temp_mw_02.txt temp_mw_02a.txt
touch change_mw_02.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_02a.txt for accents on page pppp
# 2. find differences between temp_mw_02.txt and temp_mw_02a.txt
python diff_to_changes.py temp_mw_02.txt temp_mw_02a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_02.txt
# 4. install further changes into temp_mw_02.txt
python updateByLine.py temp_mw_01.txt change_mw_02.txt temp_mw_02.txt
# 5. now, should have
diff temp_mw_02.txt temp_mw_02a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0100
Then install temp_mw_02.txt into csl-orig.

-----------------------------------------------------------------
install  temp_mw_02.txt to check xml
cp temp_mw_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0131-0220.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0131-0220.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN page 0221
cp temp_mw_02.txt temp_mw_03.txt
cp temp_mw_03.txt temp_mw_03a.txt
touch change_mw_03.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_03a.txt for accents on page pppp
# 2. find differences between temp_mw_03.txt and temp_mw_03a.txt
python diff_to_changes.py temp_mw_03.txt temp_mw_03a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_03.txt
# 4. install further changes into temp_mw_03.txt
python updateByLine.py temp_mw_02.txt change_mw_03.txt temp_mw_03.txt
# 5. now, should have
diff temp_mw_03.txt temp_mw_03a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 299

-----------------------------------------------------------------
install  temp_mw_03.txt to check xml
cp temp_mw_03.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0221-0299.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0221-0299.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

# 1. manually change temp_mw_01a.txt for accents on page pppp
# 2. find differences between temp_mw_00.txt and temp_mw_01a.txt
python diff_to_changes.py temp_mw_01.txt temp_mw_01a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_01.txt
# 4. install further changes into temp_mw_01.txt
python updateByLine.py temp_mw_00.txt change_mw_01.txt temp_mw_01.txt
# 5. now, should have
diff temp_mw_01.txt temp_mw_01a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0100
Then install temp_mw_01.txt into csl-orig.
-------------------------------------------------------------------------
Start another 'batch' ....

Repeat this update loop until done (pppp = 1308).

Through page 0059.
Install temp_mw_6.txt into csl-orig.


------------------------------------------------------------
# continue this work for pages 0060-1308 in issue142
# Related comments in https://github.com/sanskrit-lexicon/MWS/issues/142.

change_mw-01.txt has the changes for pages 60-130.
Install The corresponding digitization version into csl-orig.

-----------------------------------------------------------------
install  temp_mw_01.txt to check xml
cp temp_mw_01.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0060-0130.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0060-0130.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.
-----------------------------------------------------------------
BEGIN page 0131
cp temp_mw_01.txt temp_mw_02.txt
cp temp_mw_02.txt temp_mw_02a.txt
touch change_mw_02.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_02a.txt for accents on page pppp
# 2. find differences between temp_mw_02.txt and temp_mw_02a.txt
python diff_to_changes.py temp_mw_02.txt temp_mw_02a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_02.txt
# 4. install further changes into temp_mw_02.txt
python updateByLine.py temp_mw_01.txt change_mw_02.txt temp_mw_02.txt
# 5. now, should have
diff temp_mw_02.txt temp_mw_02a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0100
Then install temp_mw_02.txt into csl-orig.

-----------------------------------------------------------------
install  temp_mw_02.txt to check xml
cp temp_mw_02.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0131-0220.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0131-0220.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN page 0300
cp temp_mw_03.txt temp_mw_04.txt
cp temp_mw_04.txt temp_mw_04a.txt
touch change_mw_04.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_04a.txt for accents on page pppp
# 2. find differences between temp_mw_04.txt and temp_mw_04a.txt
python diff_to_changes.py temp_mw_04.txt temp_mw_04a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_04.txt
# 4. install further changes into temp_mw_04.txt
python updateByLine.py temp_mw_03.txt change_mw_04.txt temp_mw_04.txt
# 5. now, should have
diff temp_mw_04.txt temp_mw_04a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 399 

-----------------------------------------------------------------
install  temp_mw_04.txt to check xml
cp temp_mw_04.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0300-0399.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0300-0399.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 0400-0499
cp temp_mw_04.txt temp_mw_05.txt
cp temp_mw_05.txt temp_mw_05a.txt
touch change_mw_05.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_05a.txt for accents on page pppp
# 2. find differences between temp_mw_05.txt and temp_mw_05a.txt
python diff_to_changes.py temp_mw_05.txt temp_mw_05a.txt temp_change_page_pppp.txt
# 3. insert temp_change_page_pppp.txt into change_mw_05.txt
# 4. install further changes into temp_mw_05.txt
python updateByLine.py temp_mw_04.txt change_mw_05.txt temp_mw_05.txt
# 5. now, should have
diff temp_mw_05.txt temp_mw_05a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 399 

-----------------------------------------------------------------
install  temp_mw_05.txt to check xml
cp temp_mw_05.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0400-0499.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0400-0499.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 0500-0599
cp temp_mw_05.txt temp_mw_06.txt
cp temp_mw_06.txt temp_mw_06a.txt
touch change_mw_06.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_06a.txt for accents on page pppp
# 2. find differences between temp_mw_06.txt and temp_mw_06a.txt
python diff_to_changes.py temp_mw_06.txt temp_mw_06a.txt temp_change_page_0500.txt
# 3. insert temp_change_page_0500.txt into change_mw_06.txt
# 4. install further changes into temp_mw_06.txt
python updateByLine.py temp_mw_05.txt change_mw_06.txt temp_mw_06.txt
# 5. now, should have
diff temp_mw_06.txt temp_mw_06a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0599

-----------------------------------------------------------------
install  temp_mw_06.txt to check xml
cp temp_mw_06.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0500-0599.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0500-0599.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 0600-0699
cp temp_mw_06.txt temp_mw_07.txt
cp temp_mw_07.txt temp_mw_07a.txt
touch change_mw_07.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_07a.txt for accents on page pppp
# 2. find differences between temp_mw_07.txt and temp_mw_07a.txt
python diff_to_changes.py temp_mw_07.txt temp_mw_07a.txt temp_change_page_0600.txt
# 3. insert temp_change_page_0600.txt into change_mw_07.txt
# 4. install further changes into temp_mw_07.txt
python updateByLine.py temp_mw_06.txt change_mw_07.txt temp_mw_07.txt
# 5. now, should have
diff temp_mw_07.txt temp_mw_07a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0699

-----------------------------------------------------------------
install  temp_mw_07.txt to check xml
cp temp_mw_07.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0600-0699.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0600-0699.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 0700-0799
cp temp_mw_07.txt temp_mw_08.txt
cp temp_mw_08.txt temp_mw_08a.txt
touch change_mw_08.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_08a.txt for accents on page pppp
# 2. find differences between temp_mw_08.txt and temp_mw_08a.txt
python diff_to_changes.py temp_mw_08.txt temp_mw_08a.txt temp_change_page_0700.txt
# 3. insert temp_change_page_0700.txt into change_mw_08.txt
# 4. install further changes into temp_mw_08.txt
python updateByLine.py temp_mw_07.txt change_mw_08.txt temp_mw_08.txt
# 5. now, should have
diff temp_mw_08.txt temp_mw_08a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0799

-----------------------------------------------------------------
install  temp_mw_08.txt to check xml
cp temp_mw_08.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0700-0799.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0700-0799.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 0800-0899
cp temp_mw_08.txt temp_mw_09.txt
cp temp_mw_09.txt temp_mw_09a.txt
touch change_mw_09.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_09a.txt for accents on page pppp
# 2. find differences between temp_mw_09.txt and temp_mw_09a.txt
python diff_to_changes.py temp_mw_09.txt temp_mw_09a.txt temp_change_page_0800.txt
# 3. insert temp_change_page_0800.txt into change_mw_09.txt
# 4. install further changes into temp_mw_09.txt
python updateByLine.py temp_mw_08.txt change_mw_09.txt temp_mw_09.txt
# 5. now, should have
diff temp_mw_09.txt temp_mw_09a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0899

-----------------------------------------------------------------
install  temp_mw_09.txt to check xml
cp temp_mw_09.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0800-0899.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0800-0899.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 0900-0999
cp temp_mw_09.txt temp_mw_10.txt
cp temp_mw_10.txt temp_mw_10a.txt
touch change_mw_10.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_10a.txt for accents on page pppp
# 2. find differences between temp_mw_10.txt and temp_mw_10a.txt
python diff_to_changes.py temp_mw_10.txt temp_mw_10a.txt temp_change_page_0900.txt
# 3. insert temp_change_page_0900.txt into change_mw_10.txt
# 4. install further changes into temp_mw_10.txt
python updateByLine.py temp_mw_09.txt change_mw_10.txt temp_mw_10.txt
# 5. now, should have
diff temp_mw_10.txt temp_mw_10a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 0999

-----------------------------------------------------------------
install  temp_mw_10.txt to check xml
cp temp_mw_10.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 0900-0999.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 0900-0999.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 1000-1099
cp temp_mw_10.txt temp_mw_11.txt
cp temp_mw_11.txt temp_mw_11a.txt
touch change_mw_11.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_11a.txt for accents on page pppp
# 2. find differences between temp_mw_11.txt and temp_mw_11a.txt
python diff_to_changes.py temp_mw_11.txt temp_mw_11a.txt temp_change_page_1000.txt
# 3. insert temp_change_page_1000.txt into change_mw_11.txt
# 4. install further changes into temp_mw_11.txt
python updateByLine.py temp_mw_10.txt change_mw_11.txt temp_mw_11.txt
# 5. now, should have
diff temp_mw_11.txt temp_mw_11a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 1099

-----------------------------------------------------------------
install  temp_mw_11.txt to check xml
cp temp_mw_11.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 1000-1099.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 1000-1099.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 1100-1199
cp temp_mw_11.txt temp_mw_12.txt
cp temp_mw_12.txt temp_mw_12a.txt
touch change_mw_12.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_12a.txt for accents on page pppp
# 2. find differences between temp_mw_12.txt and temp_mw_12a.txt
python diff_to_changes.py temp_mw_12.txt temp_mw_12a.txt temp_change_page_1100.txt
# 3. insert temp_change_page_1100.txt into change_mw_12.txt
# 4. install further changes into temp_mw_12.txt
python updateByLine.py temp_mw_11.txt change_mw_12.txt temp_mw_12.txt
# 5. now, should have
diff temp_mw_12.txt temp_mw_12a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 1199

-----------------------------------------------------------------
install  temp_mw_12.txt to check xml
cp temp_mw_12.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 1100-1199.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 1100-1199.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
BEGIN pages 1200-1308
cp temp_mw_12.txt temp_mw_13.txt
cp temp_mw_13.txt temp_mw_13a.txt
touch change_mw_13.txt

# Now do the following 'loop' for each page pppp
# 1. manually change temp_mw_13a.txt for accents on page pppp
# 2. find differences between temp_mw_13.txt and temp_mw_13a.txt
python diff_to_changes.py temp_mw_13.txt temp_mw_13a.txt temp_change_page_1200.txt
# 3. insert temp_change_page_1200.txt into change_mw_13.txt
# 4. install further changes into temp_mw_13.txt
python updateByLine.py temp_mw_12.txt change_mw_13.txt temp_mw_13.txt
# 5. now, should have
diff temp_mw_13.txt temp_mw_13a.txt # no difference!

Increment page number pppp and go back to step 1.

Repeat this update loop through pppp = 1308

-----------------------------------------------------------------
install  temp_mw_13.txt to check xml
cp temp_mw_13.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142

# commit csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git pull # in case some other work has been done
git add v02/mw/mw.txt
git commit -m "MW accent update pages 1200-1308.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent update pages 1200-1308.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.
-----------------------------------------------------------------
See readme_extra.txt for a few more manual changes.

-----------------------------------------------------------------
# emacs tool.
search-forward-regexp <k2>[^<]*[\/^]

(<s></s>), 
(<s>as</s>), 
(<s>a/s</s>), 
(<s>am</s>), 
(<s>a/m</s>), 
(<s>A</s>), 
(<s>I</s>), 
<s></s>, 
<s>am</s>, 
<s>as</s>, 
<s>tA</s>, 
°
(<s>°</s>), 
(<s></s>), 
-----------------------------------------------------------------
NEW SCANS NEEDED
page 63, col1 aBi-dUzita bad print
-----------------------------------------------------------------
----------------
An archive.org version of MW
  https://archive.org/details/in.ernet.dli.2015.31959/page/n1318/mode/1up
-----------------------------------------------------------------

-----------------------------------------------------------------
498 matches for "¦ <lex>[mfn]+\.</lex> *<info lex=" in buffer: temp_mw_09a.txt
  likely missing text, such as N. of wk.

660 matches for "(for <hom>[0-9]+\.</hom> See" in buffer: temp_mw_09a.txt
  Conjecture most should change to '... see'
