work for https://github.com/sanskrit-lexicon/mws/issues/65
04-05-2024 begun ejf

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65

# start with copy of mw.txt
  at commit 640c6e43e740004c051aed435f77d911a1de5b68
cd /c/xampp/htdocs/cologne/csl-orig
git show 640c6e43e:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65/temp_mw_0.txt

# start with copy of mwab_input.txt
  at commit 4877c0f725656ecd069b4562ef6d1f02058a2454
cd /c/xampp/htdocs/cologne/csl-pywork
git show 4877c0f7:v02/distinctfiles/mw/pywork/mwab/mwab_input.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65/mwab_input_0.txt

cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65

# start with lang tags file from AB.
File lang.tags.txt
  Ref: https://github.com/sanskrit-lexicon/mws/issues/65#issuecomment-2036161171
cp ~/Downloads/andhrabharati/mws/lang.tags.txt lang_tags.txt


---------------------------------------------------------
Modify basicadjust.php so lang tag will be treated as 'ab' tag in displays.
old: (line 114)
if (in_array($this->getParms->dict,array('gra', 'md'))) {
new:
if (in_array($this->getParms->dict,array('gra', 'md', 'mw'))) {

Make this change in both csl-websanlexicon and in csl-apidev versions of
basicadjust.php

---------------------------------------------------------
temp_mw_1.txt
change '<ab>X</ab>' to '<lang>X</lang>' for X in lang_tags.txt

python tag_to_lang.py 'ab' lang_tags.txt temp_mw_0.txt temp_mw_1.txt lang_tags_unmarked_1.txt

113 lang tags read from lang_tags.txt
880516 lines read from temp_mw_0.txt
1629 lines changed
880516 written to temp_mw_1.txt
53 written to lang_tags_unmarked_1.txt

---------------------------------------------------------
lang_tags_unmarked_1.txt What to do with these?

These 53 lang tags must be handled differently.
--
<ns>X</ns> -> <lang>X</lang> where
 
python tag_to_lang.py 'ns' lang_tags_unmarked_1.txt temp_mw_1.txt temp_mw_2.txt lang_tags_unmarked_2.txt
53 lang tags read from lang_tags_unmarked_1.txt
880516 lines read from temp_mw_1.txt
330 lines changed
880516 written to temp_mw_2.txt
38 written to lang_tags_unmarked_2.txt

---------------------------------------------------------
example: <s1 slp1="apaBraMSa">Apabhraṃśa</s1> -> <lang>Apabhraṃśa</lang>
python tag_to_lang.py 's1' lang_tags_unmarked_2.txt temp_mw_2.txt temp_mw_3.txt lang_tags_unmarked_3.txt
38 lang tags read from lang_tags_unmarked_2.txt
880516 lines read from temp_mw_2.txt
45 lines changed
880516 written to temp_mw_3.txt
29 written to lang_tags_unmarked_3.txt

---------------------------------------------------------
misc changes relative to lang_tags_unmarked_3.txt
python tag_to_lang.py 'misc' lang_tags_unmarked_3.txt temp_mw_3.txt temp_mw_4.txt lang_tags_unmarked_4.txt

29 lang tags read from lang_tags_unmarked_3.txt
880516 lines read from temp_mw_3.txt
97 lines changed
880516 written to temp_mw_4.txt
4 written to lang_tags_unmarked_4.txt

The 4 AB lang tags not found in cdsl mw:
<lang>Angl.-Sax.</lang>
<lang>Angl.S.</lang>
<lang>E.</lang>
<lang>W.</lang>

---
print change ?
<L>204858.1<pc>1332,2<k1>vfz  Gaelic -> Gaëlic

---------------------------------------------------------
# count of AB lang tags in revised MW
python lang_tags_count.py lang_tags.txt temp_mw_4.txt lang_tags_count.txt

113 lang tags read from lang_tags.txt
880516 lines read from temp_mw_4.txt
113 written to lang_tags_count.txt

---------------------------------------------------------
04-08-2024 
Post this repo to github for AB review.
---------------------------------------------------------
Greek text italic.
change basicadjust.php and basicdispla.php in csl-websanlexicon
copy these two files to csl-apidev
redo local display as a check.

sync csl-websanlexicon to  github

upload to cologne server and recompute mw displays

---------------------------------------------------------
04-09-2024
Resolving differences in count bewtween AB version and cdsl version.
Since AB's version of mw is 'private', he prepared a file for this purpose.
AB prepared lang_tags_checking.CDSL.vs.AB.txt
To implement these:
 edit lang_tags_checking.CDSL.vs.AB.txt to make readily parseable. Result is:
 lang_tags_checking.CDSL.vs.AB_1.txt

Generate a change transaction file from lang_tags_checking.CDSL.vs.AB_1.txt.

countdiff_tags_del.txt has the tags on lines deleted by AB.
These must be taken into account when comparing counts.

python make_change_countdiff.py lang_tags_checking.CDSL.vs.AB_1.txt temp_mw_4.txt temp_countdiff.org countdiff_tags_del.txt


# manually edit temp_countdiff.org
---
TODO:
  <ls>W.</ls> -> <lang>W.</lang>  really - there is <ls>W.</ls>
  <L>44711<pc>256,1<k1>karkara
---
<L>88580<pc>461,3<k1>trita  line 298763
no Zend (or Zd.) found
---
<L>94676.1<pc>488,2<k1>dus<k2>dus<e>2A
; <lang>O. H. G.</lang>  not found
---
342487 new <L>101804<pc>519,1<k1>DUsara
  There is no E. or Eng.  342847 wrong line number
---
<lang>Prākṛ.</lang>
;; addl. lines 348646, 354182, 360125, 399179, 469333, 482982, 498615, 518511, 519151;; lines 347649, 617106, 617148 missed in AB version
347649 old <LEND> wrong line number
---
---

---------------------------------
# Remove 'org mode' markup, and save as change_countdiff1.txt
# a change transaction file suitable for updateByLine.py

construct temp_mw_5.txt
python updateByline.py temp_mw_4.txt change_countdiff1.txt temp_mw_5.txt
# install
880516 lines read from temp_mw_4.txt
880516 records written to temp_mw_5.txt
67 change transactions from change_countdiff1.txt
67 of type new

# count of AB lang tags in revised MW
cp ~/Downloads/andhrabharati/MWS/lang_tags_count.CDSL.vs.AB.txt  .

# exclude those lines of cdsl which have been marked as 'deleted' by AB,
 which are from countdiff_tags_del.txt
python lang_tags_count1.py lang_tags_count.CDSL.vs.AB.txt countdiff_tags_del.txt temp_mw_5.txt lang_tags_count_5.txt

114 lang tags read from lang_tags_count.CDSL.vs.AB.txt
39 lnums read from countdiff_tags_del.txt
880516 lines read from temp_mw_5.txt
114 written to lang_tags_count_5.txt
TAG     CDSL    CDSLREV AB      CDSLREV-AB
<lang>Apabhraṃśa</lang> 7       6       5       1
<lang>Class.</lang>     35      33      32      1
<lang>Germ.</lang>      218     210     209     1
<lang>Lat.</lang>       539     526     523     3
<lang>Prākṛ.</lang>     3       11      9       2
<lang>Prākṛt</lang>     233     227     231     -4
<lang>Ved.</lang>       634     632     604     28
<lang>Zd.</lang>        149     140     139     1
<lang>Zend</lang>       12      20      21      -1


line 505970  <L>150486<pc>755,3<k1>BAzA   to mark as lang? Avanti
<lang>W.</lang> -> <ls>W.</ls> (WILSON)  ?
wrong line numbers in lang_tags_checking.CDSL.vs.AB.txt
  342487 <L>101804<pc>519,1<k1>DUsara<k2>DUsara<e>1B
  347649 <LEND>

04-10-2024 post zip of temp_mw_5.txt to issue at AB request.

---------------------------------------------------------
TODO: https://github.com/sanskrit-lexicon/mw-dev/issues/21
  AB suggests using '<gk>X</gk>' instead of <lang n="Greek">x</lang>
  Similarly for Arabic , <ar>

  
---------------------------------------------------------
check local installation
# Where did I do redolocal.sh?
grep -Rnw ../../../PWK/pwkissues -e 'sh redolocal.sh' 
# one place is ../../../PWK/pwkissues/issue106/readme.txt
cp ../../../PWK/pwkissues/issue106/redolocal.sh .

# modify redolocal.sh for mw
# temp generate local displays using temp_mw_1.txt
sh redolocal.sh 1
# ok


Examine display for 'a'. Looks ok
