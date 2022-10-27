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

-----------------------------------------------------------------
# emacs tool.
search-forward-regexp <k2>[^<]*[\/^]

(<s></s>), 
(<s>as</s>), 
(<s>a/s</s>), 
(<s>am</s>), 
(<s>a/m</s>), 
(<s>A</s>), 
<s></s>, 
<s>am</s>, 
<s>as</s>, 
<s>tA</s>, 
°
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
  page 1280 may is truncated in 3rd column.
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
mw page 648 3rd col. problem
mw page 142 problems
mw page 728
page 796

