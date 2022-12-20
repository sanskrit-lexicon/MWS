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
page 63, col1 aBi-dUzita bad print
-----------------------------------------------------------------
-----------------------------------------------------------------
TODO
NOTE: anya/to'raRya  ' in k2pwg   apuro'nuvAkya^ka
pwg: ftu\Sa/s   prA/cInayogIpu/tra  (also mw shows 2 accents!) va/naspa/ti
mw prA/SnI-putra/
<L>185990<pc>918,1<k1>vanaspati<k2>va/na-s-pa/ti<h>a<e>3
<L>189485<pc>934,3<k1>vAtajUta<k2>vA/ta—jUta^<e>3
=====
girijA in mw:  not a pwg headword. cdsl incorrectly shows 'inherited' accent
bahutiTa print change see page 626 -> see page 726  va/naspa/ti
<L>258981<pc>1280,3<k1>svapnanaMSana mw print shows only svapna-na
  page 1280 may be truncated in 3rd column.  PAGE OK -- this is not error!
  https://archive.org/details/in.ernet.dli.2015.31959/page/n1318/mode/1up
  page 160 truncated
Mismarked in k2, but NOT in pwg, so not yet caught.

<L>1321<pc>6,3<k1>agrepA<k2>agre—pA/<e>3
  headline pU/ not marked.  This is an OR with two words
<L>1405.1<pc>7,1<k1>aGnyA<k2>a/-GnyA<e>2B
<L>1405.2<pc>7,1<k1>aGnyA<k2>a/-GnyA<e>2B
<L>16138<pc>92,1<k1>arDaKArI<k2>arDa/—KArI<e>3 no accent - and others
<L>20166.6<pc>116,1<k1>azAQA<k2>a/-zAQA<e>1B
<L>126351<pc>636,3<k1>purunizWA<k2>puru/—nizWA<e>3
<L>162307<pc>807,2<k1>mAtfbanDU<k2>mAtf/—banDU<e>3B
<L>204122<pc>1008,1<k1>vfkatAti<k2>vf/ka—tAti<e>3
<L>113613<pc>576,1<k1>paYcacitIka<k2>paYca—citIka<e>3  pa/
<L>114548<pc>580,1<k1>paqvISa<k2>paq—vISa<e>3 pa/
<L>114549<pc>580,1<k1>paqviMSa<k2>pa/q—viMSa<e>3 pa/
<L>128466.1<pc>646,1<k1>pfTivizWA<k2>pfTivi—zWA<e>4
<L>140878<pc>711,3<k1>pruzvA<k2>pruzvA/<e>2B info or
<L>25998<pc>149,2<k1>Arti<k2>Arti<e>2  text refers to hom1 and 2, but no h2.

NEW or entries for L=5164  5164.1, 5164.2, 5164.3
-----------------------------------------------------------------
-----------------------------------------------------------------
2229 matches for "<k2>[^<]*[\/^][^<]*[\/^][^<]*<" in buffer: temp_mw_4.txt
example: <L>96<pc>1,2<k1>aMsadaGna<k2>a/Msa—daGna/<e>3
<L>126347<pc>636,3<k1>puruDa<k2>puru—Da/<e>3 headline
<L>126348<pc>636,3<k1>puruDA<k2>puru/—DA/<e>3 headline

<L>4799<pc>24,2<k1>anakzasaNgam   missing or and anakzastamBam
<L>5164<pc>26,1<k1>anaBiSasta  missing or and entries
<L>5412<pc>27,2<k1>anasTa<k2>an-asTa/<e>1

-----------------------------------------------------------------
<L>18500.2<pc>106,3<k1>avAcI<k2>a/vAcI<e>1B  missing first sense. new entry
<L>18737<pc>108,1<k1>avicftya<k2>a-vicftya/<e>1 new entry
L>40350<pc>233,3<k1>Ekzava<k2>Ekzava/<e>1  Ekzavya new entry
   <s>Ekzava/</s> ¦ <lex>mf(<s>I</s>)n.</lex> and <s>Ekzavya^</s>
<L>41472.1<pc>1323,3<k1>kakuBvat<k2>kaku/Bvat<e>3B  Bv?
<L>43060<pc>248,3<k1>kanInakA<k2>kanI/nakA<e>2B
   ¦ (<s>kanI/nakA</s> and <s>kanI/nikA</s>), kanI/nikA entry
<L>45102<pc>257,3<k1>kartave<k2>ka/rtave<e>1
  <s>ka/rtave</s> ¦ [<ls>RV.</ls> & <ls>AV.</ls>] and ENTRY <s>ka/rtavE/</s>
<L>65154.01<pc>1326,2<k1>girijAdevI<k2>giri—jAdevI<e>4
   is it jAdevI or jadevI?  Similar for several others following.
<L>87140<pc>455,3<k1>tokma<k2>to/kma<e>3C  should it be tokman?
  also, is 87139 ok, or should key1=tokman?
<L>87150<pc>455,3<k1>tote<k2>to/te<e>1 add entry toto?
L>87476.3<pc>457,2<k1>trayastriMSatsaMmita<k2>trayas—triMSat—saMmita
  should it be prajApates-trayas—triMSat—saMmita ?
<L>94867<pc>489,2<k1>dUtI<k2>dUtI<e>1B  short-long
<L>104496<pc>530,3<k1>navajA<k2>nava—jA/<e>3 mfn?
<L>115179.1<pc>583,1<k1>pattastodASa<k2>pat—tas—to-dASa<e>4 pat-to-dASa ?
<L>158007<pc>789,2<k1>mayanta<k2>ma/yanta<e>1  entry maganda add
<L>160055<pc>797,3<k1> ... phrase -- into prior entry?

498 matches for "¦ <lex>[mfn]+\.</lex> *<info lex=" in buffer: temp_mw_09a.txt
  likely missing text, such as N. of wk.

660 matches for "(for <hom>[0-9]+\.</hom> See" in buffer: temp_mw_09a.txt
  Conjecture most should change to '... see'

<L>208302<pc>1029,1<k1>vyenI<k2>vy—e^nI<e>3 PWG vyenI vi/enI and other words
<L>219565<pc>1082,3<k1>Sunavat<k2>Suna/—vat<e>3 entry SunA/-vat
<L>223428<pc>1101,1<k1>SrutakIrti<k2>Sruta/—kIrti<e>3B scan has (<s>A</s>), ?
<L>228598<pc>1129,1<k1>saMgItaka<k2>saM-gItaka<e>3 print may have gi^taka ?
  PW gItaka. MW print change?
<L>228989<pc>1131,1<k1>sajUs<k2>sa—jU/s<e>3C
<s>sa—jU/s</s> ¦ <lex>ind.</lex> (or <s>U/r</s>)  add sajUr entry

<L>232494.15<pc>1149,2<k1>saptadaSaDA<k2>sapta—daSa-DA/<e>4
  missing record sapta-daSa-rAtra/
<L>248396<pc>1231,2<k1>sumIQa<k2>su—mIQa/<e>3  add mI|a entry
<L>248447<pc>1231,2<k1>sumfqIka<k2>su—mf/qIka<e>3 add mf|Ika entry
<L>249722<pc>1235,3<k1>surApAna<k2>surA—pA/na<e>3B
   add cpd surA-pAna-prAyaScitta
<L>249811<pc>1236,2<k1>suvargya<k2>suvargya^<e>2 add suvargya entry
<L>261246<pc>1291,1<k1>harizac<k2>hari—za/c<e>3
   <s>hari—za/c</s> ¦ (<s>zA/c</s>) mfn  << meaning of zA/c ?
<L>262803<pc>1298,1<k1>hiNkAra<k2>hiN—kAra/<e>3
   insert 262803.1 hiN-kf new entry

-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------

mw page 87 3rd col. truncated  
https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/servepdf.php?dict=mw&page=0087
mw page 648 3rd col. problem  NOT A PROBLEM!
mw page 142 problems NOT A PROBLEM
mw page 728 PROBLEM NOT FOUND
page 796 PROBLEM NOT FOUND

