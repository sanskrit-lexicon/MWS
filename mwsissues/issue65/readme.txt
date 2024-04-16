work for https://github.com/sanskrit-lexicon/mws/issues/65
04-05-2024 begun ejf

# this directory
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65

# start with copy of mw.txt
  at commit 640c6e43e740004c051aed435f77d911a1de5b68
cd /c/xampp/htdocs/cologne/csl-orig
git show 640c6e43e:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65/temp_mw_0.txt


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

python make_change_countdiff.py lang_tags_checking.CDSL.vs.AB_1.txt temp_mw_4.txt temp_countdiff.org countdiff_tags_del.txt ab_lnums_del.txt

45 groups found in lang_tags_checking.CDSL.vs.AB_1.txt
880516 lines read from temp_mw_4.txt
66 distinct lnums found, excluding AB deletes
11 lnums found more than once
66 change records written to temp_countdiff.org
39 distinct lnums found from AB deletes
50 lnums found more than once
89 written to countdiff_tags_del.txt
89 items written to countdiff_tags_del.txt
0 lnums in both chg and del
39 written to ab_lnums_del.txt

# manually edit temp_countdiff.org
---
DONE: W. = Welsh (AB discovered) - see issues/65 comment
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
04-10-2024
  resolving.lang.diff.counts.txt (From Andhrabharati)
  
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
*************************************************************
04-12-2024
Further work to resolve diffs in lang tags between temp_mw_5.txt and
AB's unpublished version of mw.txt.

Since this issue65 directory is getting cluttered, keep most intermediate
files and code in a new subdirectory,
mkdir lla  # lnum_lang_analysis
# start with AB file posted in github comment
 https://github.com/sanskrit-lexicon/mws/issues/65#issuecomment-2051868713
and downloaded.  change name to lla0.txt
cp ~/Downloads/andhrabharati/MWS/lnum_lang.analysis.CDSL.vs.AB.txt lla/lla0.txt

-----------------------------
reproduce the cdsl lines of lla0.txt using temp_mw_5.txt.
python lla/extract_cdsl_lnum_lang.py temp_mw_5.txt lla/extract_cdsl_lnum_lang.txt
2024 written to lla/extract_cdsl_lnum_lang.txt

grep '(CDSL)' lla/lla0.txt > lla/temp_lla0_cdsl.txt
diff lla/extract_cdsl_lnum_lang.txt  lla/temp_lla0_cdsl.txt > lla/diff_extract_cdsl_lnum_lang_lla0.txt

There are differences:
 in 6 lines (lnums = 74272, 216876, 577271, 727187, 727190, 767696),
   temp_mw_5.txt has <lang>ved.</lang> (lower-case) but
   lla0.txt CDSL has <lang>Ved.</lang>.  Why?
Assume Ved. is correct, these need to be changed in cdsl.
Solution:
 cp lla/lla0.txt lla/lla1.txt
 manually edit lla1 and change CDSL (to 'ved.') in those 6 lines.
 
# redo the comparison:
grep '(CDSL)' lla/lla1.txt > lla/temp_lla1_cdsl.txt
diff lla/extract_cdsl_lnum_lang.txt  lla/temp_lla1_cdsl.txt | wc -l
# 0 As expected.

Further work uses lla1.txt, whose CDSL lines are consistent with temp_mw_5.txt.

Note: 1 further change to lla1.txt.  Add a group-ending line at end of file
-----------------------------

63 matches for ";; deleted (dup. entry)" in buffer: lla1.txt
   Cf. ab_lnums_del.txt  had '39' lines so identfied.
   Why the extra 24?

80 matches for ";; matter rearranged," in buffer: lla1.txt
  These also are 'non-standard'

Analysis of these two groups (143 lnums) is more complex and
will be deferred.

First order is to extract 'simple' lnums where there are lang-tag diffs
between AB and cdsl.

python simple_diff.py lla1.txt lla1_simplediff.txt
1982 groups
1839 simple groups
24 TODO among simplediffs
24 records written to lla1_simplediff.txt

# generate changes based on simplediff
# 
python lla/make_change_simple.py temp_mw_5.txt lla/lla1_simplediff.txt lla/temp_change_mw_5_1.org

# manual edit lla/temp_change_mw_5_1.org
Notes:
---  
(CDSL):	276122	<lang>Ved.</lang>, <lang>class.</lang>
(AB):	276122	<lang>Ved.</lang>, <lang>Class.</lang>   print has 'class.'
; Jim request AB to change
---

------------------
After the editing: 
cp lla/temp_change_mw_5_1.org lla/temp_change_mw_5_1.txt
# remove Emacs Org mode markup in lla/temp_change_mw_5_1.txt
touch change_mw_5_6.txt
# manual insert lla/temp_change_mw_5_1.txt into change_mw_5_6.txt
# compute temp_mw_6.txt
python updateByLine.py temp_mw_5.txt change_mw_5_6.txt temp_mw_6.txt
880516 lines read from temp_mw_5.txt
880516 records written to temp_mw_6.txt
23 change transactions from change_mw_5_6.txt
23 of type new


--------------------------------------------
lla1 -- revise CDSL lines based on temp_mw_6.txt
python lla/revise_lla.py temp_mw_6.txt lla/lla1.txt lla/lla2.txt
880516 read from temp_mw_6.txt
6203 read from lla/lla1.txt
6203 written to lla/lla2.txt

As a check, redo
python lla/simple_diff.py lla/lla2.txt lla/lla2_simplediff.txt
1982 groups
1839 simple groups
1 TODO among simplediffs
1 records written to lla/lla2_simplediff.txt
NOTE: That 1 records is 276122 (where AB is to change Class. to class.

--------------------------------------------
Generate prototype change file for ';; deleted'

Also, generate file of lnums which AB marks as deleted

python deleted_diff.py lla2.txt lla2_deletediff.txt ab_lnums_del2.txt
1982 groups
63 groups marked as deleted (in AB version)
63 records written to lla2_deletediff.txt
63 written to ab_lnums_del2.txt


python lla/make_change_deleted.py temp_mw_6.txt lla/lla2_deletediff.txt lla/temp_change_mw_5_2.org

880516 lines read from temp_mw_6.txt
63 groups
63 change records written to lla/temp_change_mw_5_2.org

# manual edit lla/temp_change_mw_5_2.org

Notes:
---
2 matches for "<lang>ved\." in buffer: temp_mw_6.txt
 727187:<lang>ved.</lang> and <ab>ep.</ab> also <ab>cl.</ab> 1. <s>Sa/yate</s>, <s>°ti</s>;
 727190:<ab>p.</ab> <lang>ved.</lang> <s>SaSayAna/</s>, <lang>Class.</lang> <s>SiSyAna</s>;


------------------
After the editing: 
cp lla/temp_change_mw_5_2.org lla/temp_change_mw_5_2.txt
# remove Emacs Org mode markup in lla/temp_change_mw_5_2.txt

# manual insert lla/temp_change_mw_5_2.txt into change_mw_5_6.txt
# compute temp_mw_6.txt
python updateByLine.py temp_mw_5.txt change_mw_5_6.txt temp_mw_6.txt
880516 lines read from temp_mw_5.txt
880516 records written to temp_mw_6.txt
25 change transactions from change_mw_5_6.txt
25 of type new

--------------------------------------------
Generate prototype change file for ';; matter rearranged'  

python rearranged_diff.py lla2.txt lla2_rearrangediff.txt ab_lnums_rear2.txt
1982 groups
80 groups marked as deleted (in AB version)
80 records written to lla2_rearrangediff.txt
122 written to ab_lnums_rear2.txt

Note: lla/make_change_rearranged.py is functionally identical to
lla/make_change_deleted.py

python lla/make_change_rearranged.py temp_mw_6.txt lla/lla2_rearrangediff.txt lla/temp_change_mw_5_3.org
880516 lines read from temp_mw_6.txt
80 groups
122 change records written to lla/temp_change_mw_5_3.org

# manual edit lla/temp_change_mw_5_3.org

Notes:
---
;(AB):	239110	<lang>Lat.</lang>, <lang>class. Sanskṛt</lang>, <lang>Ved.</lang>, <lang>Class. Sanskṛt</lang>
last one shld be <lang>class. Sanskṛt</lang>  request AB to change
---
;(AB):	278150	<lang>Class.</lang>
should be <lang>class.</lang>  request AB to change
---

------------------
After the editing: 
cp lla/temp_change_mw_5_3.org lla/temp_change_mw_5_3.txt
# remove Emacs Org mode markup in lla/temp_change_mw_5_3.txt

# manual insert lla/temp_change_mw_5_3.txt into change_mw_5_6.txt
# compute temp_mw_6.txt
python updateByLine.py temp_mw_5.txt change_mw_5_6.txt temp_mw_6.txt
880516 lines read from temp_mw_5.txt
880516 records written to temp_mw_6.txt
28 change transactions from change_mw_5_6.txt

--------------------------------------------
lla3 -- revise CDSL lines based on temp_mw_6.txt
python lla/revise_lla.py temp_mw_6.txt lla/lla2.txt lla/lla3.txt
880516 read from temp_mw_6.txt
6203 read from lla/lla1.txt
6203 written to lla/lla2.txt

--------------------------------------------
compare lang lists for each group except those marked as ';; deleted'
python lla/diffgroups.py lla/lla3.txt lla/diffgroups_lla3.txt
1982 groups
1919 groups marked as non-deleted (in AB version)
3 records written to lla/diffgroups_lla3.txt


--------------------------------------------
zip temp_mw_6.zip temp_mw_6.txt
post to issues/65 comment
commit this repository.
--------------------------------------------
Further changes to cdsl mentioned in AB comments
cp temp_mw_6.txt temp_mw_7.txt

Manual changes to temp_mw_7.txt

---
Māgadhī in line 519281 is tagged as <s1, but to be done in line 207634 as well.
 made the change at 207634 
---
Avantī in line 63845 is wrongly tagged as <lang, instead of in line 505970 (as suggested above).
  this was done in temp_mw_6.txt
---
https://github.com/sanskrit-lexicon/mws/issues/65#issuecomment-2051868713
TODO: Jim appears yet to consider the posts 1 and 2 above
1: https://github.com/sanskrit-lexicon/MWS/issues/65#issuecomment-2048362664
 Also, I had changed the <ab>ep.</ab> to <lang>ep.</lang>, as it stands for the "Epic Sanskrit" language.

[Note: In a school of thought, the Skt. language is divided as (a) Vedic, (b) Brahmanic (and Upanishadic), (c) Epic, (d) classic and (e) later period types.]

Jim changes temp_mw_7.txt :  <ab>ep.</ab> -> <lang>ep.</lang>
 replaced 345 occurrences
---
Re: https://github.com/sanskrit-lexicon/MWS/issues/65#issuecomment-2048393555
<s> tags to be easily identified as non-Skt. language terms near the <lang tags.

Jim changes in temp_mw_7.txt:
156672 <s>cancer</s> -> <etym>cancer</etym>

263223 ' <s>pas</s>' deleted

566277  <s>y</s> -> <i>y</i>
566277  <s>j</s> -> <i>j</i>
------------------------------
Generate change file for possible reference
python diff_to_changes_dict.py temp_mw_6.txt temp_mw_7.txt change_6_7.txt
339 changes written to change_6_7.txt

python updatebyLine.py temp_mw_6.txt change_6_7.txt temp.txt
diff temp_mw_7.txt temp.txt | wc -l
# 0 as expected

*************************************************************

*************************************************************
work on tooltips. 

# start with copy of mwab_input.txt
  at commit 4877c0f725656ecd069b4562ef6d1f02058a2454
cd /c/xampp/htdocs/cologne/csl-pywork
git show 4877c0f7:v02/distinctfiles/mw/pywork/mwab/mwab_input.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue65/mwab_input_0.txt

04-10-2024.
Changed mwab_input.txt by removing the <id>X</id> item. This item is unused
in displays or elsewhere.
old format:
abbrv<TAB><id>abbrv</id> <disp>tooltip</disp>
new format:
abbrv<TAB><disp>tooltip</disp>

mkdir tooltips  # do work here
mv mwab_input_0.txt tooltips
# manually edit, so 'new format' is used
-------------------------------------------------
04-13-2024
mwab_input_1.txt  tooltips for:
* <ab>X</ab>  The original purpose of these tooltips
* <lang>X</lang>  New usage.
   cf. csl-websanlexicon/v02/.../webtc/basicadjust.php at '// 04-08-2024'
        preg_replace('|<lang>(.*?)</lang>|', '<ab>\1</ab>',$line1);
cd tooltips
python tips1.py ab,lang ../temp_mw_7.txt mwab_input_0.txt mwab_input_1.txt

-------------------------------
cp mwab_input_1.txt mwab_input_2.txt
edit mwab_input_2.txt to provide tooltips for the lang elements.
112 abbreviations X appear in <lang>X</lang> in temp_mw_7.txt
extract these 112 as temp_mwab_input_2_lang.txt

-------------------------------------------
04-14-2024

# AB revisions to tooltips for <lang> tags.
cp ~/Downloads/andhrabharati/MWS/mwab_input_2_lang.AB.txt  .
diff temp_mwab_input_2_lang.txt mwab_input_2_lang.AB.txt
notes:

# temp_mwab_input_2_ab.txt
  The 'non-lang' tooltips
mwab_input_3.txt is concatenation of 

----------------------------------------
temp_mw_8.txt  Several changes Jim missed.
Ref: https://github.com/sanskrit-lexicon/mws/issues/65#issuecomment-2053882550
   and next comment.

cp temp_mw_7.txt temp_mw_8.txt
# manual edit temp_mw_8.txt
---
(CDSL): 254116 old Prākṛt
(AB): 254116 ----------
;; deleted (dup. entry)
Jim changes.
---
54627:	<lang n="Hindūstānī">Hind.</lang> done ?
---
413624:	<lang n="Persian">P°</lang> done
---
413633:	<lang n="Persian">P°</lang> done
413633:	<lang n="Sanskṛt">S°</lang> done
---
413636:	<lang n="Persian">P°</lang> done
413636:	<lang n="Sanskṛt">S°</lang> done
---
413639:	<lang n="Persian">P°</lang> done
413639:	<lang n="Sanskṛt">S°</lang> done
413639:	<lang>Arab</lang> done
note 'Arab.' is in mwab_input
Add 'Arab' to mwab_input
---
from note in AB's
< Fr.	<disp>From or French</disp> <count>lang,2</count>
> Fr.	<disp>French</disp> <count>lang,2</count>
;;  AB has tagged the two places as <ab n="From">Fr.</ab> to avoid the duality
This previously done by Jim
---
------------------------------------------------
Generate change file for possible reference
python diff_to_changes_dict.py temp_mw_7.txt temp_mw_8.txt change_7_8.txt
6 changes written to change_7_8.txt


------------------------------------------------
Back to revisions of mwab_input_3.txt
---
Add 'Arab' to mwab_input
Arab	<disp>Arabic</disp> <count>lang,4</count>

------------------
mwab_input_4.txt
# recompute counts
python tips1.py ab,lang ../temp_mw_8.txt mwab_input_3.txt mwab_input_4.txt

The lex tag in mw is complex. See basicadjust.php in
 csl-websanlexicon/v02/makotemplates/web/webtc/basicadjust.php
 in function add_lex_markup_mw.
 This ultimately depends on mwab_input.txt for the abbreviation tooltips.
 Thus, we need to revise mwab_input_4.txt to include lex tag.

# recompute counts, using also lex tag
# A revision to tips1 program required

python tips2.py lex,lang,ab ../temp_mw_8.txt mwab_input_4.txt mwab_input_5.txt


Changes to temp_mw_8.txt, mwab_input_4 based on examination of mwab_input
---
<L>90572<pc>470,3<k1>darvI
<ab>Vārtt. 2</ab> -> <ab>Vārtt.</ab> 2
remove: Vārtt. 2	<disp>?</disp>
---
<L>195583<pc>963,1<k1>vitF
<ab>Caus</ab>: -> <ab>Caus.</ab>
remove: Caus	<disp>?</disp> <count>ab,1</count>
---
old: ff.	<disp>?</disp>
new: ff.	<disp>and the following ones</disp>
---
<L>84012<pc>443,1<k1>tAmasa
old: <ls>Pravar. i, 1 (<ab>J</ab>)</ls>
new: <ls>Pravar. i, 1 (J)</ls>
remove mwab: J	<disp>?</disp>
---
<L>26943.3<pc>154,2<k1>Ava
old: <ab>Loc</ab>. <s>Ava/yos</s>
new: <ab>Loc.</ab> <s>Ava/yos</s>
remove mwab: Loc	<disp>?</disp> 
---
old: masc.	<disp>?</disp>
new: masc.	<disp>masculine</disp>
---
<L>257781<pc>1275,1<k1>sva
old: N.B.	<disp>?</disp>
new: N.B.	<disp>nota bene (note well)</disp> 
---
<L>75185<pc>403,1<k1>cOdrAyaRa
old: <ab>p></ab> 1323
new: <ab>p.</ab> 1323
remove mwab: p>	<disp>?</disp>
---
<L>22293<pc>128,1<k1>Akenipa
old: <ab>q̲.v.</ab>
new: <ab>q.v.</ab>
remove mwab: q̲.v.	<disp>?</disp> <count>ab,1</count>
---
old: sq.	<disp>?</disp> <count>ab,2</count>
new: sq.	<disp>sequentia (the following one)</disp>
---
old: sqq.	<disp></disp> <count>ab,1</count>
new: sqq.	<disp>sequentiae (the following ones)</disp>
---
<L>111813.1<pc>567,3<k1>nf
<ab>st</ab>. -> <ab>st.</ab>
remove mwab: st	<disp>?</disp> <count>ab,1</count>
---
old: subj.	<disp>?</disp>
new: subj.	<disp>subjunctive</disp>
---
<L>99564<pc>509,2<k1>Danurdurga
old: (<ab>v.l</ab> <s>Danva-</s>)
new: (<ab>v.l.</ab> <s>Danva-</s>)

<L>105268<pc>534,1<k1>nAgarika
old: (<ab>v.l</ab> <s>°raka</s>)
new: (<ab>v.l.</ab> <s>°raka</s>)

Remove mwab: v.l	<disp>?</disp> <count>ab,2</count>
---
mwab
old: Voc.	<disp>?</disp>
new: Voc.	<disp>vocative case</disp> 
---
Ā	<disp>?</disp> <count>ab,9</count>
<ab>Ā</ab> -> <ab>Ā.</ab>  9 occurrences changed in temp_mw_8
remove mwab: Ā	<disp>?</disp> 
---
L. occurs 7 times as <ab>L.</ab>
L. occurs 6 times as <lex>L.</lex>
      41267 as <ls>L.</ls>
Change <ab>L.</ab> to <ls>L.</ls>  7 occurrences
Change <lex>L.</lex> to <ls>L.</ls> 6 occurrences
Remove mwab: L.	<disp>lexicographers (i.e. a word or meaning which although give in native lexicons, has not yet been met with in any published text)</disp>

---
Add tooltips for two <lex>X</lex>
nf.	<disp>neuter or feminine</disp>
nm.	<disp>neuter or masculine</disp>
---
TODO: met.	<disp>?</disp> <count>ab,30</count>  need a tooltip!

---
old: <ab n="root">rt.</ab>
new: <ab>rt.</ab>
3 instances.
---

-----------------------------------------------------------------
# rerun tips2

python tips2.py lex,lang,ab ../temp_mw_8.txt mwab_input_4.txt mwab_input_5.txt
880516 read from ../temp_mw_8.txt
460 tips read from mwab_input_4.txt
460 written to mwab_input_5.txt

-----------------------------------------------------------------
mwab_input_6.txt
 Remove those with <count></count> These are unused. in temp_mw_8.txt.
 38 instances.
 save as:
 mwab_input_5_unused.txt
 
-----------------------------------------------------------------
04-15-2024
# regenerate change_7_8
python diff_to_changes_dict.py temp_mw_7.txt temp_mw_8.txt change_7_8.txt
40 changes written to change_7_8.txt

# from tooltips directory:
cp mwab_input_6.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Unexpected glitch
The change (from change_7_8.txt
; <L>15014<pc>86,2<k1>araGawwa<k2>ara—Gawwa<e>3
;54627 old <s>ara—Gawwa</s> ¦ <lex>m.</lex> a wheel or machine for raising water from a well (<lang>Hind.</lang> <lang script="Arabic" n="Hindustani">ارهٿ</lang>), <ls>Pañcat.</ls><info lex="m"/>
; ***************
; next change does not work - some  error from xmlvalidate
; ***************
; 54627 new <s>ara—Gawwa</s> ¦ <lex>m.</lex> a wheel or machine for raising water from a well (<lang n="Hindūstānī">Hind.</lang> <lang script="Arabic" n="Hindustani">ارهٿ</lang>), <ls>Pañcat.</ls><info lex="m"/>

Here is error from xmlvalidate
python3 ../../xmlvalidate.py ../../mw/pywork/mw.xml ../../mw/pywork/mw.dtd
Problem validating
Traceback (most recent call last):
  File "C:\xampp\htdocs\cologne\xmlvalidate.py", line 29, in <module>
    validate(xmlfile,dtdfile)
  File "C:\xampp\htdocs\cologne\xmlvalidate.py", line 21, in validate
    print(errmsg)
  File "C:\Users\jimfu\AppData\Local\Programs\Python\Python39\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u1e5b' in position 77: character maps to <undefined>

SOLUTION: change one.dtd.
Apparently the problem occurs when lxml generates an error message when
an 'invalid' (xml doesn't agree with dtd) message. Probably because
being run on Windows.  Could be that my version of lxml is incompatible
with Python 3.9 on Windows.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

------------------------------
display problem.
For araGawwa, there is no tooltip for 'Hind.'
<lang n="Hindūstānī">Hind.</lang>

Probably basicadjust (or basicdisplay) need tweaking.

<i>Hind.</i> missing 'title' attribute
and <i>ارهٿ</i>  should not be italic

04-16-2024
To solve this display problem, it seems necessary to use the 'gk' and 'arab'
tags, instead of <lang n="greek">X</lang>

python lang_to_tag.py temp_mw_8.txt temp_mw_9.txt

40 matches in 38 lines for "<lang script="Arabic" n="Persian">"
In some of these, there is no <lang>Pers.</lang>.
Example:
<L>62463<pc>342,3<k1>gaYja<k2>gaYja<h>2<e>1
<hom>2.</hom> <s>gaYja</s> ¦ <lex>mn.</lex> = <lang script="Arabic" n="Persian">گنج</lang> a treasury

If we change this to
<hom>2.</hom> <s>gaYja</s> ¦ <lex>mn.</lex> = <arab>گنج</arab> a treasury

then we have lost the information that this is a word in the Persian language.

<lang>Pers.</lang> <lang script="Arabic" n="Persian">هندي</lang>

-----------------------
solution:
Add 'lang' attribute to 'arab' tag
(So 'arab' tag represents 'arabic script'.
 <arab>X</arab>  X is in Arabic language and Arabic script
 <arab lang="LANGNAME">X</arab>  X is in LANGNAME language and Arabic script
Minor adjustments to basicadjust.php and basicdisplay.php
Note: there still remain 8 instances of <lang n="Y">X</lang>
---------------------------------------------------------
For possible reference, generate change_8_9.txt 
python diff_to_changes_dict.py temp_mw_8.txt temp_mw_9.txt change_8_9.txt
828 changes written to change_8_9.txt

---------------------------------------------------------
For possible reference, generate change_0_8.txt 
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_8.txt change_0_8.txt
2343 changes written to change_0_8.txt

change_0_8.txt along with change_8_9.txt provide all changes to mw.txt

---------------------------------------------------------
Installation of csl-orig, csl-pywork, csl-websanlexicon, csl-apidev

# install version 9 of mw.txt into csl-orig
cp temp_mw_9.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt

# recompute local installation

cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok

# sync to github
--- csl-orig
cd /c/xampp/htdocs/cologne/csl-orig
git add .
git commit -m "MW lang tag and related.
Ref: https://github.com/sanskrit-lexicon/mws/issues/65"

#  1 file changed, 2553 insertions(+), 2553 deletions(-)

git push

--- csl-pywork
cd /c/xampp/htdocs/cologne/csl-pywork
git status
#       modified:   v02/distinctfiles/mw/pywork/mwab/mwab_input.txt
        modified:   v02/makotemplates/pywork/one.dtd

git add .
git commit -m "MW lang tag and related.
Ref: https://github.com/sanskrit-lexicon/mws/issues/65"

git push

--- csl-websanlexicon
cd /c/xampp/htdocs/cologne/csl-websanlexicon
git status
#       modified:   v02/distinctfiles/mw/websanlexicon/mwab/mwab_input.txt
        modified:   v02/makotemplates/websanlexicon/one.dtd

git add .
git commit -m "MW lang tag and related.
Ref: https://github.com/sanskrit-lexicon/mws/issues/65"

 2 files changed, 12 insertions(+), 5 deletions(-)

git push

--- csl-apidev
cd /c/xampp/htdocs/cologne/csl-apidev
git status
        modified:   basicadjust.php
        modified:   basicdisplay.php

git add .
git commit -m "MW lang tag and related.
Ref: https://github.com/sanskrit-lexicon/mws/issues/65"

 2 files changed, 12 insertions(+), 5 deletions(-)

git push

---------------------------------------------------------

install changes to cologne server from repositories
 csl-orig, csl-pywork, csl-websanlexicon, csl-apidev

recompute mw displays in csl-pywork/v02 at cologne server
---------------------------------------------------------
zip temp_mw_9.zip temp_mw_9.txt

push this MWS repository to github

in addition to this readme.txt file, additional files this commit:
        change_0_8.txt
        change_7_8.txt
        change_7_8_prev.txt
        change_8_9.txt
        lang_to_tag.py
        tooltips/mwab_input_1.txt
        tooltips/mwab_input_2.txt
        tooltips/mwab_input_2_lang.AB.txt
        tooltips/mwab_input_3.txt
        tooltips/mwab_input_4.txt
        tooltips/mwab_input_5.txt
        tooltips/mwab_input_5_unused.txt
        tooltips/mwab_input_6.txt
        tooltips/tips1.py
        tooltips/tips2.py


---------------------------------------------------------
THE END
