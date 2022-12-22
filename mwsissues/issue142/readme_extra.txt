readme_extra.txt
-----------------------------------------------------------------
MISCELLANEOUS CHANGES.
Many of these change the number of lines in mw.txt.
Start with a copy of the latest version.
cp temp_mw_13.txt temp_mw_extra.txt
Manually alter temp_mw_extra.txt.
----------------------
----------------------

<L>128466.1<pc>646,1<k1>pfTivizWA<k2>pfTivi—zWA<e>4
<L>128466.1<pc>646,1<k1>pfTivizWA<k2>pfTivi—zWA/<e>4
  should lex be f.  (rather than mfn?)
----------------------
<L>25999<pc>149,2<k1>Arti<k2>A/rti<e>2A
text refers to hom1 and 2, but no h2.
OLD:
¦ sickness, <ls>AV.</ls>; <ls>VS.</ls>; <ls>KātyŚr.</ls>; <ls>R.</ls>; <ls>Megh.</ls> &c.<info lex="inh"/>
NEW:
¦ sickness, <ls>AV.</ls>; <ls>VS.</ls>; <ls>KātyŚr.</ls>; <ls>R.</ls>; <ls>Megh.</ls> &c.; (for <hom>2.</hom> <s>Arti</s> see <ab>s.v.</ab>)<info lex="inh"/>
NOTE: No hom 2 Arti found!
----------------------
NEW or entries for L=5164 at  5164.1, 5164.2, 5164.3
<L>5164<pc>26,1<k1>anaBiSasta  missing or and entries
----------------------
<L>4799<pc>24,2<k1>anakzasaNgam   missing or and anakzastamBam
new entry 4799.1 
----------------------
<L>5412<pc>27,2<k1>anasTa<k2>an-asTa/<e>1
new or entries: 5412.01, 5412.02, 5412.03, 5412.04, 5412.05
----------------------
<L>18500.2<pc>106,3<k1>avAcI<k2>a/vAcI<e>1B  missing first sense
----------------------
<L>18737<pc>108,1<k1>avicftya<k2>a-vicftya/<e>1
new or entry entry a-vicartya
----------------------
<L>40350<pc>233,3<k1>Ekzava<k2>Ekzava/<e>1  Ekzavya new entry
   <s>Ekzava/</s> ¦ <lex>mf(<s>I</s>)n.</lex> and <s>Ekzavya^</s>
   40350.2 Ekzavya
----------------------
L>43060<pc>248,3<k1>kanInakA<k2>kanI/nakA<e>2B
   ¦ (<s>kanI/nakA</s> and <s>kanI/nikA</s>), kanI/nikA entry 43060.1
----------------------
<L>45102<pc>257,3<k1>kartave<k2>ka/rtave<e>1
  <s>ka/rtave</s> ¦ [<ls>RV.</ls> & <ls>AV.</ls>]
  new 'and' ENTRY <s>ka/rtavE/</s> 45102.1
----------------------
<L>87150<pc>455,3<k1>tote<k2>to/te<e>1
  add 'and' entry toto 87150.1
----------------------
<L>94867<pc>489,2<k1>dUtI<k2>dUtI<e>1B  short-long
  add 94869.1 dUti  orsl
----------------------
<L>158007<pc>789,2<k1>mayanta<k2>ma/yanta<e>1
  mayanda add 'and' entry 158007.1
----------------------
<L>160055<pc>797,3<k1> ... phrase -- into prior entry?
 Delete 160055 -- I think it is a phrase, not a headword.
 Put the phrase into 160054
 The 'n.'  at end is puzzling.
----------------------
<L>219565<pc>1082,3<k1>Sunavat<k2>Suna/—vat<e>3
 and 'or' entry SunA/-vat 219565.1
----------------------
<L>228989<pc>1131,1<k1>sajUs<k2>sa—jU/s<e>3C
<s>sa—jU/s</s> ¦ <lex>ind.</lex> (or <s>U/r</s>)
 add sajUr as 'or' entry 228989.1
----------------------
<L>232494.15<pc>1149,2<k1>saptadaSaDA<k2>sapta—daSa-DA/<e>4
  missing record sapta-daSa-rAtra/ at 232494.16
----------------------
<L>248396<pc>1231,2<k1>sumIQa<k2>su—mIQa/<e>3
add mI|a as 'or' entry
----------------------
<L>248447<pc>1231,2<k1>sumfqIka<k2>su—mf/qIka<e>3
 add mf/LIka entry
 248447, 248447.1, 248447.2 copied to 248447.3, 248447.4, 248447.5
 248447 and 248447.3 tread as 'or'
----------------------
<L>249718<pc>1235,3<k1>surApARaprAyaScitta<k2>surA—pARa—prAyaScitta<e>4
add surA—pANa—prAyaScitta  as 'or' entry, 249723.
----------------------
<L>262803<pc>1298,1<k1>hiNkAra<k2>hiN—kAra/<e>3
  hiN-kf (a verb) is incorrectly part of hiN-kAra.
  Make new entry 262803.1 for hiN-kf
end miscellaneous changes
----------------------

remove 103 blank lines.
----------------------
one error noticed and corrected at line 501971 of temp_mw_extra.txt
< <L>149229<pc>750,1<k1>BavizyatkAla<k2>Bavizyat        —kAla<e>3
---
> <L>149229<pc>750,1<k1>BavizyatkAla<k2>Bavizyat—kAla<e>3


-----------------------------------------------------------------
install  temp_mw_extra.txt to check xml
cp temp_mw_extra.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
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
git commit -m "MW correction noticed during IAST conversion.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push
# commit mws
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue142
git add .
git commit -m "MW accent review.  extra changes.
  Ref: https://github.com/sanskrit-lexicon/MWS/issues/142"
git push

# pull csl-orig at cologne and csl-pywork/v02 redo mw.

-----------------------------------------------------------------
MISC OBSERVATIONS
-----------------
A few entries have 2 accents.  Just a fact of life.
file two_accents.txt lists these, 177 found.  These should be
checked manually against scan.
----------------
girijA in mw:  not a pwg headword. cdsl incorrectly shows 'inherited' accent
bahutiTa print change see page 626 -> see page 726  va/naspa/ti

-----------------------------------------------------------------
NOTES WITH NO ACTION TAKEN
----------------

These observations were examined, but no action taken
<L>1321<pc>6,3<k1>agrepA<k2>agre—pA/<e>3
  headline pU/ not marked.  This is an OR with two words
<L>16138<pc>92,1<k1>arDaKArI<k2>arDa/—KArI<e>3 no accent - and others
<L>20166.6<pc>116,1<k1>azAQA<k2>a/-zAQA<e>1B
<L>162307<pc>807,2<k1>mAtfbanDU<k2>mAtf/—banDU<e>3B
<L>113613<pc>576,1<k1>paYcacitIka<k2>paYca—citIka<e>3  pa/ short-long OK
-------------
<L>140878<pc>711,3<k1>pruzvA<k2>pruzvA/<e>2B info or already added.
-------------
<L>126347<pc>636,3<k1>puruDa<k2>puru—Da/<e>3 headline
<L>126348<pc>636,3<k1>puruDA<k2>puru/—DA/<e>3 headline
-------------
<L>41472.1<pc>1323,3<k1>kakuBvat<k2>kaku/Bvat<e>3B  Bv?
-------------
<L>65154.01<pc>1326,2<k1>girijAdevI<k2>giri—jAdevI<e>4
   is it jAdevI or jadevI?  Similar for several others following.
   Scan of annexure shows jA-devI. No change.
-------------
<L>87476.3<pc>457,2<k1>trayastriMSatsaMmita<k2>trayas—triMSat—saMmita
  should it be prajApates-trayas—triMSat—saMmita ? I don't think so.
-------------
<L>208302<pc>1029,1<k1>vyenI<k2>vy—e^nI<e>3
  PWG vyenI vi/enI and other words
-------------
<L>249811<pc>1236,2<k1>suvargya<k2>suvargya^<e>2
  add suvargya as 'or' entry 249811.1   ALREADY DONE.
-------------
<L>261246<pc>1291,1<k1>harizac<k2>hari—za/c<e>3
   <s>hari—za/c</s> ¦ (<s>zA/c</s>) mfn  << meaning of zA/c ?
   PW:  'starch' = strong.
-------------
-------------  end no change
-----------------------------------------------------------------
OPEN QUESTIONS
<L>126351<pc>636,3<k1>purunizWA<k2>puru/—nizWA<e>3  
  In scan, the final character appears to have both a long-short diacritic
  and an udAtta accent diacritic.  It is marked as 'mfn.'  does the mfn
  apply also to the 'A/' version
--------------
<L>204121<pc>1008,1<k1>vfkatAt<k2>vfka/—tAt<e>3
<L>204122<pc>1008,1<k1>vfkatAti<k2>vf/ka—tAti<e>3
  does the 'vfka/' note apply to BOTH? or just to tAti?
<L>114548<pc>580,1<k1>paqvISa<k2>paq—vISa<e>3 pa/  
<L>114549<pc>580,1<k1>paqviMSa<k2>pa/q—viMSa<e>3 pa/
   should it be pa/q-vISa also?
--------------
<L>87140<pc>455,3<k1>tokma<k2>to/kma<e>3C  or should it be tokman?
  also, is 87139 ok, or should key1=tokman?

--------------
<L>104496<pc>530,3<k1>navajA<k2>nava—jA/<e>3
<s>nava—jA/</s> and <s>na/va—jAta</s> ¦ <lex>mfn.</lex> ‘<ab>id.</ab>’, fresh, new, <ls>RV.</ls><info lex="m:f:n"/><info and="104496,navajA;104497,navajAta"/>

  This implies navajA is mfn.  Correct?
--------------
<L>115179.1<pc>583,1<k1>pattastodASa<k2>pat—tas—to-dASa<e>4
  pat-to-dASa ?
--------------
<L>223428<pc>1101,1<k1>SrutakIrti<k2>Sruta/—kIrti<e>3B scan has (<s>A</s>),
scan has (A) f.   This appears to be a print error.
current digitization:
<s>Sruta—kIrti</s> ¦ <lex>f.</lex> <ab>N.</ab> of a daughter of <s1 slp1="kuSa-Dvaja">Kuśa-dhvaja</s1> (wife of <s1 slp1="Satru-Gna">Śatru-ghna</s1>), <ls>R.</ls><info lex="f"/>

--------------
<L>228598<pc>1129,1<k1>saMgItaka<k2>saM-gItaka<e>3
  'I' in print is unclear.  PW gItaka. 
--------------
--------------
--------------

END OPEN QUESTIONS
