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
missing in AB file
'<ab>Sax.</ab>' , '<lang>Sax.</lang>  (1)
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
04-08-2024 2PM
Post this repo to github for AB review.
---------------------------------------------------------
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
