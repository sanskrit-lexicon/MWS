MWS/mwsissues/issue159

Ref: https://github.com/sanskrit-lexicon/MWS/issues/164


# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
cc39ac1ea1f27a9f1e452092f0c882a7e9cba606


# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
git show  cc39ac1e:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/
 
*********************************************************************
Generate changes

python make_change_1.py temp_mw_0.txt temp_change_1.txt
cp temp_change_1.txt change_1.txt
# manual edit of change_1.txt

# apply the changes
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
880513 lines read from temp_mw_0.txt
880480 records written to temp_mw_1.txt
114 change transactions from change_1.txt
81 of type new, 33 of type del


----------------------------------------------
check local install
------------------------------------------------------------------------
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164
---------------------------------------------

expand other <shortlong/>
177 matches in 154 lines for "<shortlong" in buffer: temp_mw_1.txt

python make_change_2.py temp_mw_1.txt temp_change_2.txt
# 119 entries changed
cp temp_change_2.txt change_2.txt
# manual edit of change_2.txt == note: no changes

# apply the changes
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
145 change transactions from change_2.txt

----------------------------------------------
check local install
------------------------------------------------------------------------
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164

---------------------------------------------
There are still 12 <shortlong/> instances.
Handle these manually
cp temp_mw_2.txt temp_mw_3.txt

python diff_to_changes_dict.py temp_mw_2.txt temp_mw_3.txt change_3.txt
10 changes written to change_3.txt

----------------------------------------------
check local install
------------------------------------------------------------------------
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164

---------------------------------------------
# install versions 1,2,3 separately into csl-orig


---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
# install mw_1
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: shortlong headwords. #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

---------------------------------------------
# install mw_2
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: non-headword shortlong expansion #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

---------------------------------------------
# install mw_3
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: non-headword shortlong expansion, the rest of them #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

*****************************************************************
take into account change_X.AB.remarks.txt comments 
  REF: https://github.com/sanskrit-lexicon/MWS/issues/164#issuecomment-2172078003

Since some other changes have been made to mw.txt in csl-orig,
get the latest mw.txt from csl-orig
 csl-orig commit 09bcaa10d595cf10fefab7d30856d26ad5abd1c2

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_4a.txt in this directory
git show  09bcaa10d:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/temp_mw_4a.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

cp temp_mw_4a.txt temp_mw_4b.txt
# manual changes to temp_mw_4b.txt

------------------------------------
re change_1
AB: (c) at one place [L-111916.1] having only one element and one meaning [missing the first element & second (gender and) meaning]!! ;; AB version doesn't contain this error, having combined all the grouped entries together.

done -
-----------------------------------
re change_2
-----'
L=10089.
old: <s>apa-</s> or <s>apA-</s>
new: <s>apa-</s>
-----
L=32836
old: <s>a</s> or <s>A</s> before <s>f</s>
new: <s>a</s> before <s>f</s>
-----
L=150904
old: <s>BindimAla</s> or <s>°laka</s>
new: <s>BindimAlA</s> or <s>BindimAla</s> or <s>°laka</s>
-----
L=150904.1 
same change as 150904
-----
L=152430
old: (for <s>sAh</s> or <s>sah</s>)
new: (for <s>sah</s> or <s>sAh</s>)
-----
L=152431
same change as 152430
-----
L=186529
old: (for <s>vayuna-DA</s> or <s>vayuna-Da</s>)
new: (for <s>vayuna-Da</s> or <s>vayuna-DA</s>)
-----
L=186530
same change as 186529
-----
L=191029
old: <s>°rU-tarA</s> or <s>°ru-tarA</s>
new: <s>°ru-tarA</s> or <s>°rU-tarA</s>
-----
L=191030
same change as 191029
-----
L=239967
old: <s>sA/hizIma/hi</s>
new: <s>sAhizIma/hi</s> or <s>sahizIma/hi</s>
-----
L=254632
old: <s>stAyamAna</s> or <s>stayamAna</s>
new: <s>stUyamAna</s>
-----
-----------------------------------
re change_3
-----
L=33378
old: <lex>mf(<s>BvI/</s>)n.</lex> (<s>Bu/</s> or <s>BU/</s>)
new: <lex>mf(<s>BvI/</s>)n(<s>Bu/</s>).</lex>
-----
L=109667
old: (also <s>-Du/ta</s> or <s>-DU/ta</s>)
new: (also <s>-Du/ta</s>)
-----
L=126299
old: (<s>°ru/</s> or <s>°rU/</s>. much,
new: (<s>°ru/</s>, <lex>ind.</lex>  much,
------------------------------------------
# generate changes
python diff_to_changes_dict.py temp_mw_4a.txt temp_mw_4b.txt change_4.txt
12 changes written to change_4.txt
------------------------------------------
check install local mw_4b
cp temp_mw_4b.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164
---------------------------------------------
# install mw_4b
cp temp_mw_4b.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: shortlong headwords, AB revisions #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164  change_4"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

-----
install at cologne
---------------------------------------------
https://github.com/sanskrit-lexicon/mw-dev/issues/4#issue-1549401986
In this post of Jan 18, 2023, AB has noted 10 cases where
the printed te

cp temp_mw_4b.txt temp_mw_5.txt

a<shortlong/> : 4
-----
<L>10089: <s>apa<shortlong/>-</s> as <s>apă-</s>
Current : for <s>apa-</s>
  No change as ă has no rendering in slp1
-----
<L>13034: <s>abhī-pa<shortlong/>da</s> as <s>abhī-pā<shortlong/>da</s>
current:
13034 <s>aBI-pAda</s> or <s>aBI-pada</s>
interchange metalines so 13034 = pA and 13034.1 = pa
  13034
----- 
<L>32836: <s>a<shortlong/></s> as <s>ă</s>
  No change as ă has no rendering in slp1

-----
<L>108203: <s>-cā́yya<shortlong/></s> as <s>-cā́yyā<shortlong/></s>
old: <s>-cA/yya</s> or <s>-cA/yyA</s>
new: <s>-cA/yyA</s> or <s>-cA/yya</s>
-----
i<shortlong/> : 3
-----
<L>94728: <s>duli<shortlong/></s> as <s>dulī<shortlong/></s>
old: <s>duli</s> or <s>dulI</s>
new: <s>dulI</s> or <s>duli</s>
ALSO:
Similar change in L=94728.1
ALSO:
 interchange 94728, 24728.1 so dulI is first
-----
<L>106376: <s>niḥ—śreṇi<shortlong/></s> as <s>niḥ—śreṇī<shortlong/></s>
OLD:
<L>106376<pc>538,3<k1>niHSreRi<k2>niH—SreRi<e>3
<s>niH—SreRi</s> ¦ <lex>f(<s>i</s> or <s>I</s>). </lex> = <s>ni-SreRI</s>, <ls>L.</ls><info lex="f#i:f#I"/>
<LEND>
<L>106377<pc>538,3<k1>niHSreRi<k2>niH—SreRi<e>3A
¦ the wild date tree, <ls>L.</ls><info lex="inh"/>
<LEND>
NEW:
<L>106376<pc>538,3<k1>niHSreRI<k2>niH—SreRI<e>3
<s>niH—SreRI</s> or <s>niH—SreRi</s> ¦ <lex>f.</lex> = <s>ni-SreRI</s>, <ls>L.</ls>; the wild date tree, <ls>L.</ls><info orsl="106376,niHSreRI;106377,niHSreRi"/><info lex="f#I:f#i"/>
<LEND>
<L>106377<pc>538,3<k1>niHSreRi<k2>niH—SreRi<e>3
<s>niH—SreRI</s> or <s>niH—SreRi</s> ¦ <lex>f.</lex> = <s>ni-SreRI</s>, <ls>L.</ls>; the wild date tree, <ls>L.</ls><info orsl="106376,niHSreRI;106377,niHSreRi"/><info lex="f#I:f#i"/>
<LEND>

-----
<L>113820: <s>pañca—muṣṭi<shortlong/></s> as <s>pañca—muṣṭī<shortlong/></s>
old: <s>paYca—muzwi</s> or <s>paYca—muzwI</s>
new: <s>paYca—muzwI</s> or <s>paYca—muzwi</s>
Also 113820.1 same change
Also, interchange 113820 and 113820.1 so muzWI is first

-----
ú<shortlong/> : 3
-----
<L>33378: <s>bhú<shortlong/></s> as <s>bhŭ́</s>
current: <lex>mf(<s>BvI/</s>)n(<s>Bu/</s>).</lex>
no further change required
-----
<L>109667: <s>-dhú<shortlong/>ta</s> as <s>-dhŭ́ta</s>
current: (also <s>-Du/ta</s>)
no further change required
-----
<L>126299: <s>°rú<shortlong/></s>. as <s>°rŭ́</s> <lex>ind.</lex>
current: <s>°ru/</s>, <lex>ind.</lex>
No further change required.


------------------------------------------
# generate changes
python diff_to_changes_dict.py temp_mw_4b.txt temp_mw_5.txt change_5.txt
21 changes written to change_5.txt

------------------------------------------
check install local mw_5
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164

---------------------------------------------
# install mw_5
cp temp_mw_5.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/v02/

git add mw/mw.txt
git commit -m "MW: shortlong headwords, AB revisions, 2 #1639 
 Ref: https://github.com/sanskrit-lexicon/MWS/issues/164  change_
 5"
git push

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue164/

*****************************************************************
THE END

