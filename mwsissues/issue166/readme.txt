MWS/mwsissues/issue166

Ref: https://github.com/sanskrit-lexicon/MWS/issues/166

Related to https://github.com/sanskrit-lexicon/csl-orig/issues/1645#issuecomment-2198054242
# this directory in local file system
/c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166/

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
0f763c00b11218fce54d9976043d489daf70ee2c

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0.txt in this directory
git show  0f763c00b:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166/

# -------------------------------------------------------------
Start with a copy of Andhrabharati's dot.corrections.txt file

2 tab-delimited columns :
 (lnum):  the line number in temp_mw_0.txt
 text  the problematic text.

# -------------------------------------------------------------
# make prototype changes
python make_change.py temp_mw_0.txt dot.corrections.txt temp_change_1.txt temp_mw_0a.org
"comm. on  " not found at line# 66974
"explan. of  " not found at line# 80342
"( r. for " not found at line# 407384
"calming. soothing," not found at line# 464393
"self. psychology, " not found at line# 490029
"measuring. meting " not found at line# 546451
"proof. demonstration," not found at line# 546469
"saying. any  " not found at line# 614023
"masc. stem ) " not found at line# 703428
"pleasure. mountain’  " not found at line# 704488
"white. flowering  " not found at line# 708150
"having. a  " not found at line# 708183
"gold. smith, ; " not found at line# 874770
"masc. or  " not found at line# 876694

To resolve these:
 cp dot.corrections.txt dot.corrections1.txt
 # manual edit of dot.corrections1.txt
# rerun with dot.corrections1.txt
python make_change.py temp_mw_0.txt dot.corrections1.txt temp_change_1.txt temp_mw_0a.org
# cp temp_change_1.txt change_1.txt
# manual edit change_1.txt.  <<<< current
<ab>comm.</ab> commentary
<ab>masc.</ab> masculine
<ab>metric.</ab>  ? "metri causa, or ‘for the sake of the meter’ in poetry"  (7)
<ab n="accented">accent.</ab>  ?
<ab n="magical">magic.</ab>
<ab n="mythical">mythic.</ab>
<ab n="dramatical">dramatic.</ab> ?
<ab n="beginning">beg.</ab>
<ab n="infinitive">infin.</ab>
<ab n="pleonastically">pleonast.</ab>
<ab n="enclitically">enclit.</ab>  ?
<ab n="finite">fin.</ab>

TODO:
--- delete this entry. It is a duplicate of 203568.
<L>203569<pc>1005,2<k1>vIra<k2>vIra/<e>2A
¦ {{(collect. male}} progeny), <ls>RV.</ls>; <ls>AV.</ls>; <ls>Br.</ls>; <ls>GṛŚrS.</ls><info lex="inh"/>
<LEND>

# apply change_1 to mw_0
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
880453 records written to temp_mw_1.txt
247 change transactions from change_1.txt

# ready to install.
*********************************************************************

------------------------------------------------------------------------
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "MW dot.corrections :
Ref: https://github.com/sanskrit-lexicon/csl-orig/issues/1645#issuecomment-2198054242
Ref: https://github.com/sanskrit-lexicon/MWS/issues/166"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166

# also sync csl-pywork (for mwab)
