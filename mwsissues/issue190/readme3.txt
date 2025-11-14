
11-14-2025 readme3.txt

corrections to work of readme2.txt

Andhrabharati and Aumsanskrit found errors/questions.

The revised mw.txt is temp_mw_3.txt: 
cp temp_mw_2.txt temp_mw_3.txt

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190

in comments below
'old mw' refers to the latest mw (that of readme2.txt) (my local temp_mw_2.txt)
'new mw' refers to revision of 'old mw' (my local temp_mw_3.txt)
----------------------------------------------------------
Scott says in email: 5 points in
https://github.com/sanskrit-lexicon/csl-corrections/issues/100 starting at Q59.

-------------------------------------------------------------------
Point 1: boDAyanIya
Q59 https://github.com/sanskrit-lexicon/csl-corrections/issues/100#issuecomment-3530905290

L = 145870, hw = boDAyanIya
old mw:
<L>145870<pc>734,3<k1>boDAyanIya<k2>boDAyanIya<e>2
<s>boDAyanIya</s> <lex>n.</lex> (and <s>-gfhya-mAlA</s> <lex>f.</lex>), ¦ <ab>N.</ab> of <ab>wks.</ab>
lex="f"/>
<LEND>

new mw:
<L>145870<pc>734,3<k1>boDAyanIya<k2>boDAyanIya<e>2
<s>boDAyanIya</s> <lex>n.</lex> (and <s>-gfhya-mAlA</s> <lex>f.</lex>), ¦ <ab>N.</ab> of <ab>wks.</ab>

<LEND>
-------------------------------------------------------------------
Point 2: smottara
Q65 smottara

old mw: in uttara, smottara marked as phw (parenthetical headword)
<L>31144<pc>178,1<k1>uttara<k2>u/ttara<e>2A
¦ followed by (<ab>e.g.</ab> <s>smo<srs/>ttara</s> <lex type="phw">mfn.</lex> followed by ‘<s>sma</s>’, <ls>Pāṇ. iii, 3, 176</ls>)<info lex="inh"/>
<LEND>

old mw: smottara not a headword
conclude: smottara should be a headword, pointing to parent
  the positioning of smottara is debateable.
  I'll use the same position (after the sma entries) as lostparent mw
new mw: (insert this entry)
<L>257061.11<pc>178,1<k1>smottara<k2>smottara<e>3
<s>smo<srs/>ttara</s> ¦ <lex>mfn.</lex>, followed by ‘<s>sma</s>’, <ls>Pāṇ. iii, 3, 176</ls><info phwparent="31144,uttara"/><info lex="m:f:n"/>
<LEND>

---
lostparent mw has smottara as headword (among the 'sma' entries)
<L>257061.11<pc>178,1<k1>smottara<k2>smottara<e>3
<s>smo<srs/>ttara</s> ¦ <lex>mfn.</lex>, followed by ‘<s>sma</s>’, <ls>Pāṇ. iii, 3, 176</ls><info phwparent="31144,uttara"/><info lex="m:f:n"/>
<LEND>

-------------------------------------------------------------
Point 3 and Point 4: napAt and napAtka
@aumsanskrit
Ref: https://github.com/sanskrit-lexicon/MWS/issues/190#issuecomment-3532306501
@andhrabharati
https://github.com/sanskrit-lexicon/MWS/issues/190#issuecomment-3532388968


napAtka missing headword

old mw:
<L>103690<pc>527,2<k1>napAt<k2>na/pAt<e>1
  <L>103690.1<pc>527,2<k1>naptf<k2>na/ptf<e>1
<L>103691<pc>527,2<k1>naptI<k2>naptI/<e>1
<L>103692<pc>527,2<k1>naptrI<k2>naptrI<e>1
<L>103693<pc>527,2<k1>napAt<k2>na/pAt<e>1  (the part at end [Prob. neither...]
  <L>103693.1<pc>527,2<k1>naptf<k2>na/ptf<e>1

L>103698<pc>527,2<k1>naptfkA<k2>naptfkA<e>2
<s>naptfkA</s> ¦ <lex>f.</lex> a species of bird, <ls>Suśr.</ls><info lex="f"/>
<LEND>

new mw:  (insert new entry; text from mw_lostparent, also from temp_mw_1.txt)
<L>103697<pc>527,2<k1>napAtka<k2>napAtka<e>2
<s>napAtka</s> ¦ <lex>mfn.</lex> relating to a grandson (applied to a <ab>partic.</ab> <ab>sacrif.</ab> fire), <ls>Kāṭh.</ls><info lex="m:f:n"/>
<LEND>

-------------------------------------------------------------
Point 5: ajaloma
ajaloma, ajaloman
@aumsanskrit
Q65: Follow Up
https://github.com/sanskrit-lexicon/csl-corrections/issues/100#issuecomment-3531612045
@Andhrabharati
https://github.com/sanskrit-lexicon/csl-corrections/issues/100#issuecomment-3531651897
@aumsanskrit
Q65: FINAL Follow up
https://github.com/sanskrit-lexicon/csl-corrections/issues/100#issuecomment-3531683006
@Andhrabharati
https://github.com/sanskrit-lexicon/csl-corrections/issues/100#issuecomment-3531728256

old mw:
<L>1996<pc>9,3<k1>ajaloma<k2>aja—loma/<e>3B 
<s>aja—loma/</s> ¦ (<s>a/</s>), <lex>n.</lex> goat's hair, <ls>ŚBr.</ls> &c.<info lex="n"/>
<LEND>

new mw:   change 3B to 3
<L>1996<pc>9,3<k1>ajaloma<k2>aja—loma/<e>3
<s>aja—loma/</s> ¦ (<s>a/</s>), <lex>n.</lex> goat's hair, <ls>ŚBr.</ls> &c.<info lex="n"/>
<LEND>

comment: re '(<s>a/</s>)' : normally a neuter word ending in 'a'
would be, in mw, '(<s>am</s>)'

-------------------------------------------------------------
# remake xml from temp_mw_3.txt and check
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# ok, as expected
# return here
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
-- end of 'remake xml ...'

================================================
INSTALLATION
sync to github:

------------------
# csl-orig  
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
diff temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt | wc -l
#0  as expected
cd /c/xampp/htdocs/cologne/csl-orig/
git pull
git add .
git commit -m "further corrections. readme3.txt
Ref: https://github.com/sanskrit-lexicon/mws/issues/190"
git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190

---------------------------------------------------
# sync to Cologne, pull changed repos

---------------
csl-orig #pull

---------------
# update displays for mw
cd csl-pywork/v02
sh generate_dict.sh mw  ../../MWScan/2020/

-----------------------------------------------------
# sync issue190 to github.
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue190
git pull
git add .
git commit -m "further corrections. readme3.txt
Ref: https://github.com/sanskrit-lexicon/MWS/issues/190"
git push

------------------------------------------------------------
THE END
