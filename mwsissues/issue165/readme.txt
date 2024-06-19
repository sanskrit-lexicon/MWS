MWS/mwsissues/issue165

Ref: https://github.com/sanskrit-lexicon/MWS/issues/165

Related to https://github.com/sanskrit-lexicon/csl-orig/issues/1638#issuecomment-2155866315
# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
cecd350ac61459f07ddb7610de71f3857e1243d7

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  cecd350ac:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue165/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue165/

# -------------------------------------------------------------
Start with a copy of Andhrabharati's k1/k2 diff
k1.k2.different.txt
4 tab-delimited columns : entry	k1	k2	k2 (bare)
entry = <L>x<pc>y
k2 (bare) is the 'implied' k1.
The lines were (probably) chosen by AB so that k2(bare)!=k1.
*********************************************************************
# in /c/xampp/htdocs/cologne/csl-orig/v02/pw/althws/multik2a.py,
the function k2_to_k1(k2) converts (a single) k2 to k1.
Use this function to independently derive k1 from k2 for mw
and make a list of the differences.  This will be similar to
AB's k1.k2.different.txt

# option 1: use k2_to_k1 function
python k2_to_k1_diffs.py 1 temp_mw_0.txt k2_to_k1_diffs_0_1.txt
880480 read from temp_mw_0.txt
520 lines written to k2_to_k1_diffs_0.txt

This is not quite what we want.
There are some k2 which have multiple entries (comma-delimited) for
  accent-alternates. We don't want to count those as diffs.
  

# option 2: use k2_to_k1 for comma-delimited k2s,
  convert each alternate to a k1, and count as an error
  if one gives a diff
python k2_to_k1_diffs.py 2 temp_mw_0.txt k2_to_k1_diffs_0_2.txt
70 lines written to k2_to_k1_diffs_0_2.txt

This is more like it!

BUt 
AB's file has 114 items -- why the difference?
*********************************************************************
# compare the two diff files 
python diffs_separate.py k2_to_k1_diffs_0_2.txt k1.k2.different.txt diffs_both.txt  diffs_unique_cdsl.txt diffs_unique_ab.txt
70 read from k2_to_k1_diffs_0_2.txt
114 read from k1.k2.different.txt
46 lines written to diffs_both.txt
24 lines written to diffs_unique_cdsl.txt
68 lines written to diffs_unique_ab.txt
47 23 67   these are counts using just <L>X.  Almost the same don't worry about it.

(+ 46 46 24 68) 184
(+ 70 114) 184  
*********************************************************************
# make prototype changes for both 
python make_change.py temp_mw_0.txt diffs_both.txt temp_change_both.txt
46 records written to temp_change_both.txt
cp temp_change_both.txt change_both.txt
# manual edit to resolve
# apply changes
python updateByLine.py temp_mw_0.txt change_both.txt temp_mw_1.txt
880480 lines read from temp_mw_0.txt
880480 records written to temp_mw_1.txt
51 change transactions from change_both.txt

;
----------------------------------------------------
# make prototype changes for cdsl 
python make_change.py temp_mw_1.txt diffs_unique_cdsl.txt temp_change_unique_cdsl.txt
24 records written to temp_change_unique_cdsl.txt
cp temp_change_unique_cdsl.txt change_unique_cdsl.txt
# manual edit to resolve
# apply changes
python updateByLine.py temp_mw_1.txt change_unique_cdsl.txt temp_mw_2.txt
880480 lines read from temp_mw_1.txt
880480 records written to temp_mw_2.txt
28 change transactions from change_unique_cdsl.txt

----------------------------------------------------
# make prototype changes for ab 
python make_change.py temp_mw_2.txt diffs_unique_ab.txt temp_change_unique_ab.txt
68 records written to temp_change_unique_ab.txt
cp temp_change_unique_ab.txt change_unique_ab.txt
# manual edit to resolve
# apply changes
python updateByLine.py temp_mw_2.txt change_unique_ab.txt temp_mw_3.txt
880480 lines read from temp_mw_2.txt
880480 records written to temp_mw_3.txt
71 change transactions from change_unique_ab.txt
71 of type new

Note:
9  'real' changes (status=done)
59 status=nochange  (Jim thinks no change required)
3  additional lines changed (; extra)

*********************************************************************
# misc. manual changes to temp_mw_3.txt
cp temp_mw_3.txt temp_mw_4.txt

--------------------------------------------
169898, 169898.1, 169898.2,  merge .1, .2 yaTAyogam
169899, 169899.1, 169899.2,  merge .1, .2 yaTAyogena

remove .1 and .2 of both
OLD:
<L>169898<pc>842,3<k1>yaTAyogam<k2>yaTA—yogam<e>3
<s>yaTA—yogam</s> (<ls>KātyŚr.</ls>; <ls>Mn.</ls>; <ls>MBh.</ls> &c.) or <s>yaTA—yo°gena</s> (<ls>Kām.</ls>), ¦ <lex>ind.</lex> as is fit, <ab n="according">acc°</ab> to circumstances, <ab n="according">acc°</ab> to requirements<info or="169898,yaTAyogam;169899,yaTAyogena"/><info lex="ind"/>
<LEND>
<L>169898.1<pc>842,3<k1>yaTAyogam<k2>yaTA—yogam<e>3A
¦ in due order, <ls>MW.</ls><info lex="inh"/>
<LEND>
<L>169898.2<pc>842,3<k1>yaTAyogam<k2>yaTA—yogam<e>3B
<s>yaTA—yogam</s> ¦ <lex>ind.</lex> <ab n="according">acc°</ab> to usage, as hitherto, usual, <ls>MBh.</ls><info lex="ind"/>
<LEND>
<L>169899<pc>842,3<k1>yaTAyogena<k2>yaTA—yogena<e>3
<s>yaTA—yogam</s> (<ls>KātyŚr.</ls>; <ls>Mn.</ls>; <ls>MBh.</ls> &c.) or <s>yaTA—yo°gena</s> (<ls>Kām.</ls>), ¦ <lex>ind.</lex> as is fit, <ab n="according">acc°</ab> to circumstances, <ab n="according">acc°</ab> to requirements<info or="169898,yaTAyogam;169899,yaTAyogena"/><info lex="ind"/>
<LEND>
<L>169899.1<pc>842,3<k1>yaTAyogena<k2>yaTA—yogena<e>3A
¦ in due order, <ls>MW.</ls><info lex="inh"/>
<LEND>
<L>169899.2<pc>842,3<k1>yaTAyogena<k2>yaTA—yogena<e>3B
<s>yaTA—yo°am</s> ¦ <lex>ind.</lex> <ab n="according">acc°</ab> to usage, as hitherto, usual, <ls>MBh.</ls><info lex="ind"/>
<LEND>
NEW:
<L>169898<pc>842,3<k1>yaTAyogam<k2>yaTA—yogam<e>3
<s>yaTA—yogam</s> (<ls>KātyŚr.</ls>; <ls>Mn.</ls>; <ls>MBh.</ls> &c.) or <s>yaTA—yo°gena</s> (<ls>Kām.</ls>), ¦ <lex>ind.</lex> as is fit, <ab n="according">acc°</ab> to circumstances, <ab n="according">acc°</ab> to requirements; in due order, <ls>MW.</ls>; (<s>am</s>), <lex>ind.</lex> <ab n="according">acc°</ab> to usage, as hitherto, usual, <ls>MBh.</ls><info or="169898,yaTAyogam;169899,yaTAyogena"/><info lex="ind"/>
<LEND>
<L>169899<pc>842,3<k1>yaTAyogena<k2>yaTA—yogena<e>3
<s>yaTA—yogam</s> (<ls>KātyŚr.</ls>; <ls>Mn.</ls>; <ls>MBh.</ls> &c.) or <s>yaTA—yo°gena</s> (<ls>Kām.</ls>), ¦ <lex>ind.</lex> as is fit, <ab n="according">acc°</ab> to circumstances, <ab n="according">acc°</ab> to requirements; in due order, <ls>MW.</ls>; (<s>am</s>), <lex>ind.</lex> <ab n="according">acc°</ab> to usage, as hitherto, usual, <ls>MBh.</ls><info or="169898,yaTAyogam;169899,yaTAyogena"/><info lex="ind"/>
<LEND>

------------------------------------------------
---
<L>192641<pc>948,3<k1>vAstuyAgaviDestattva
 and 192641.1 --  and 'info or='
OLD:
<L>192641<pc>948,3<k1>vAstuyAgaviDestattva<k2>vAstu—yAga—viDes tattva<e>4
<s>vAstu—yAga—viDes tattva</s> ¦ <lex>n.</lex> <ab>N.</ab> of <ab>wk.</ab> (giving the rules for the above sacrifice). <info lex="n"/>
<LEND>
<L>192641.1<pc>948,3<k1>vAstuyAgaviDitattva<k2>vAstu—yAga—viDi-tattva<e>4
<s>vAstu—yAga—viDi-tattva</s> ¦ <lex>n.</lex> <ab>N.</ab> of <ab>wk.</ab> (giving the rules for the above sacrifice). <info lex="n"/>
<LEND>
NEW:
<L>192641<pc>948,3<k1>vAstuyAgaviDestattva<k2>vAstu—yAga—viDes tattva<e>4
<s>vAstu—yAga—viDes tattva</s> or <s>vAstu—yAga—viDi-tattva</s> ¦ <lex>n.</lex> <ab>N.</ab> of <ab>wk.</ab> (giving the rules for the above sacrifice).<info or="192641,vAstuyAgaviDestattva;192641,vAstuyAgaviDitattva"/> <info lex="n"/>
<LEND>
<L>192641.1<pc>948,3<k1>vAstuyAgaviDitattva<k2>vAstu—yAga—viDi-tattva<e>4
<s>vAstu—yAga—viDes tattva</s> or <s>vAstu—yAga—viDi-tattva</s> ¦ <lex>n.</lex> <ab>N.</ab> of <ab>wk.</ab> (giving the rules for the above sacrifice).<info or="192641,vAstuyAgaviDestattva;192641,vAstuyAgaviDitattva"/> <info lex="n"/>
<LEND>

----------------------------------------------
There are many more similar rewrite candidates.
The benefit of such rewrites seems small.

----------------------------------------------
Commit these changes to csl-orig
Use 4 commits, for easy reviews.

------------------------------------------------------------------------
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "change_1 Ref: https://github.com/sanskrit-lexicon/MWS/issues/165"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue165

------------------------------------------------------------------------
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "change_unique_cdsl Ref: https://github.com/sanskrit-lexicon/MWS/issues/165"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue165

------------------------------------------------------------------------
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "change_unique_ab Ref: https://github.com/sanskrit-lexicon/MWS/issues/165"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue165

------------------------------------------------------------------------
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "small misc rewrite Ref: https://github.com/sanskrit-lexicon/MWS/issues/165"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue165

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
THE END

