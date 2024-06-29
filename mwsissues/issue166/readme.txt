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
Ref: 
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166

------------------------------------------------------------------------
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "change_unique_cdsl Ref: https://github.com/sanskrit-lexicon/MWS/issues/166"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166

------------------------------------------------------------------------
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "change_unique_ab Ref: https://github.com/sanskrit-lexicon/MWS/issues/166"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166

------------------------------------------------------------------------
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "small misc rewrite Ref: https://github.com/sanskrit-lexicon/MWS/issues/166"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue166

*********************************************************************
Minor revision
python k2_to_k1_diffs.py 3 temp_mw_0.txt k2_to_k1_diffs_0_3.txt
73 lines written to k2_to_k1_diffs_0_3.txt
  comparable to k2_to_k1_diffs_0_2.txt
-----------------------------
$ diff k2_to_k1_diffs_0_2.txt k2_to_k1_diffs_0_3.txt
9a10,12
> <L>20488.3<pc>118,1   asaNga  a/-saNga(<s>as</s>),
> <L>20488.5<pc>118,1   asaNga  a/-saNga(<s>as</s>),
> <L>20488.6<pc>118,1   asaNga  a/-saNga(<s>as</s>),
17,20c20,23
< <L>40032<pc>231,2     etaSa   e/taSa,
< <L>40033<pc>231,2     etaSa   e/taSa,
< <L>40034<pc>231,2     etaSa   e/taSa,
< <L>40035<pc>231,2     etaSa   e/taSa,
---
> <L>40032<pc>231,2     etaSa   e/taSa,<s>etaSa/        setaSa
> <L>40033<pc>231,2     etaSa   e/taSa,<s>etaSa/        setaSa
> <L>40034<pc>231,2     etaSa   e/taSa,<s>etaSa/        setaSa
> <L>40035<pc>231,2     etaSa   e/taSa,<s>etaSa/        setaSa
----------------------------------

Look for problems in temp_mw_4:
python k2_to_k1_diffs.py 3 temp_mw_4.txt k2_to_k1_diffs_4_3.txt
0 lines written to k2_to_k1_diffs_4_3.txt
# thus, no additional cases to consider.
*********************************************************************
06-20-2024
Revise two corrections per AB review:
 https://github.com/sanskrit-lexicon/MWS/issues/166#issuecomment-2179293508
THE END

