
Start with temp_mw0.txt as copy of csl-orig/mw.txt
  at commit f8dd2a5b78fdd134dc1fc15fd4a9f55daad671bc

change_1.txt  manually constructed in several steps

Mostly based on list of words at
 https://github.com/sanskrit-lexicon/MWS/blob/master/mws_issue_99/unique_section-wise_entries_Andhrabharati/(Capital letter) unique words extracted.txt
 renamed locally to temp_capwords.txt
 
#Generate change_1.txt (a list of change transactions) manually by
#  various means.
#And apply the changes to get a new version temp_mw1.txt.

python updateByLine.py temp_mw0.txt change_1.txt temp_mw1.txt

#Then install this version into csl-orig:
cp temp_mw1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt

Helper program: change1a (with various options)

Examine the Capital words (capwords.txt) one by one and add
changes to change_1.txt
 See also capwords.txt notes for words that were deemed 'ok' (no change needed)

Here is the LOG of changes.
==========================
python change1a.py 1 temp_mw1.txt temp_change1a.txt  # 1 is an option
  A°  exclude occcurrences in <s>X</s>, 'A°</ab>', (3)
python change1a.py 2 temp_mw1.txt temp_change1a.txt  
  A.D  excluding occurrences in abbreviation <ab>A.D.</ab>  (108)
manual
  A.S. <ab>A.S.</ab> (1)
manual AV.  <ls>AV.</ls>  (1)  (the rest are already marked ls.
manual Acacia arabica -> <bot>Acacia arabica</bot> (3) Acacia -> <bot>Acacia</bot>
manual Accord. -> <ab n="According">Accord.</ab>  (1)
manual AdhyR  -> ls markup (aDyAtma rAmAyaRa) (1 unmarked)
Note: Aethiops Mineralis  is a homeopathic medicine, unmarked.
manual Afghan. -> <ab>Afghan.</ab> = 'language of Afghanistan' (etymology under 'giri')
Ait.  <bot>Phaseolus Trilobus Ait.</bot> (2),
Ait.Br.  AitBr. print change to usual abbreviation for Etareya brAhmaRa (1)
Alexanndrinus -> Alexandrinus  (person) 1
Aloe  Add bot markup to 2. [One spelling is Aloes] Some bot markup questionable <bot>Aloe</bot>
Am.  <ls>Am.</ls>  Reference unknown ??  hw = paruzIkfta  <<<
Anargh  1 unmarked ls.
Andropngon 1 typo bot.  Variant spellings 'Andropogon Schoenanthus'(16)  Schaenunthes (1)
Anisum -- left unchanged (2) Possible common Latin name for a plant (Anethum Sowa)
Ind. Ant.  and IndAnt. (mark as literary source) Reference unknown <<
ApSr. typo <ls>ĀpŚr.</ls>
Arc  typo for abbreviation
Areca-nut -> <bot>Areca</bot>-nut  (24 other marked instances)
Aribic -> Arabic (1)
Arum -> <bot>Arum</bot> (3)
Asp. Abbreviation for plant name (hw = aBIrupattrI)
Asparagus : mark as bot (2)
Astera, : missing text under vajra, 184808 Could split into two entries.
Asteracantha  Missing bot markup (8).  Capitalizing 'Asteracantha longifolia' Longifolia
     unmarked as print change
Aufrecht  mark as ls (2)
Auukr. typo, ls (1)
Av,  <ls>AV.</ls>, (1)
Avayavas <s1 slp1="avayava">Avayava</s1>s (1)
Böhler -> <ls>Bühler</ls> (2)
Böhtl. -> <ls>Böhtl.</ls> (1)
B.C. -> <ab>B.C.</ab>  (8)
B) -> <ab>B</ab>)
   (Bombay) Used with R. (Ramayana) and Pañc. (paYcatantra) (~35)
     BhP=BAgavata-purARa, MBh
C) -> <ab>C</ab>)  Calcutta edition (~25)
Bahar -- print change to Bihar?
Balar -> Bālar  (ls bAlarAmAyaRa) (4)
Bambus -> Bambusa (print change, bot, hw=taRqulOGa) (1)
Batatus  bot markup (1)
Baudh, ls markup (1)
BaudhP ls markup (1)
Beames  unknown ls (1) hw=utkala
Hunter  unknown ls (1) hw=utkala
Zachariae, Beiträge  ls (1) Author, work
  Theodor Zachariae,  Die indischen Wörterbücher
   (Ref: https://www.indologie.uni-halle.de/institutsgeschichte/theodor_zachariae/)
Beng.  <ab>Beng.</ab> (2) Tooltip =? Bengali  (hw = upacakzus, karcarikA)  <<< help wanted for tooltip
Beta Unmarked bot. (3)
Betel Unmarked Piper Betel (4)
Bh. unmarked <ls>Bh.</ls> (1) Tooltip=BAgavata-purARA (?) hw=nAkulI   <<< help wanted for tooltip
     24 <ls>Bh.</ls> instances marked.
Bhar. unmarked ls. (1) (Bharata)
Bignonia unmarked bot. (1)
Bloomfield unmarked ls: tooltip=Maurice Bloomfield (au)  (4)
Bn. unmarked ls: tooltip unknown (1) 94428<pc>487,2<k1>durga  <<<  help wanted for tooltip
Boehtlingk unmarked ls (1)
Bombay  (used as ed. Bombay.  Not marked) eleven instances
Bonibax -> Bombax unmarked bot (1)
Bos unmarked bio (1)
Brahms -> Brahmā
Buddhac. unmarked ls (1)  tooltip=Buddhacarita ?  <<<  help wanted for tooltip  259649<pc>1283,3<k1>svABAvika
Burnouf unmarked ls: Eugène Burnouf
Calc.  unmarked abbreviation (Calcutta edition) (19)
Calotropis unmarked bot (1)
Cathartocarpus unmarked bot (4)
Caur. unmarked ls (2)
python change1a.py 3 temp_mw1.txt temp_change1a.txt  
  Caus.  excluding occurrences in abbreviation <ab>Caus.</ab>  (358)
python change1a.py 4 temp_mw1.txt temp_change1a.txt  
  Cf.  unmarked abbrev (20)
ChUP. -> ChUp. ls (2)
Chandoiu -> Chandom. ls (1)
Charantia Momordica bot unmarked (1)
Smilax China bot unmarked (1)
Class. unmarked abbrev. (17)
class. unmarked abbrev. (13)
negat. unmarmed abbrev. (2)
Coc. abbreviation of Cocculus (1). print change to Cocculus and mark bot   << not sure of print change
Colebrooke mark as ls (1)
Colocynth mark as bot (2)
python change1a.py 5 temp_mw1.txt temp_change1a.txt  
  Comm.  unmarked abbrev (180)
python change1a.py 6 temp_mw1.txt temp_change1a.txt  
  Compar.  unmarked abbrev (11)
Concl. unmarked abbrev (3)
Conim. -> Comm. (1)
Conj. unmarked abbrev (3) tooltip = Conjectural ?
   << help wanted tooltip. <L>2943<pc>13,2<k1>atiKyA and <L>3038<pc>14,2<k1>atiDvaMs
Cowell  unmarked ls (Edward Byles Cowell) (1)
Ct. -> <ab>Cf.</ab> (1)
D.  'A. D.' -> <ab>A.D.</ab> (4)
Dat. unmarked abbrev (1)
Dattakac. unmarked ls (2)
Daucns -> Daucus bot unmarked (1)
Delphinus Gangeticus bot unmarked (1)
Kaegi ls (1)  tooltip = Adolf Kaegi (au)
Des. unmarked abbrev (Desiderative) (1)
Dharnsas. -> Dharmas. ls (1)
Dhstup. -> Dhātup. ls (1)
Dig.ambaras ->  Dig-ambaras (sky-clothed ones)
Diospyros Ebenaster unmarked bot (1)
Dor. New abbrev. Tooltip = Doric (1) <L>25924<pc>149,1<k1>Ayus
Dosid. -> Desid. (1)
Echites Scholaris bot unmarked (2)
Engl. unmarked abbrev (8)
Feb. unmarked abbrev (1) February
O. S. -> O.S. unmarked abbrev (1) <<< tooltip help wanted: <L>171842<pc>854,1<k1>yuga
Fistula Lacrymalis bot unmarked (1)
Physalis Flexuosa bot unmarked (1)
Fo  unneeded text (1) diva
Fr. unmarked abbrev (3) tooltip: 'From or French'
Sl. unmarked abbrev (3) tooltip: Slovak  <<< Help wanted tooltip
  <L>92977.1<pc>481,3<k1>dIrGa   <L>93282.05<pc>482,3<k1>du   <L>93282.55<pc>482,3<k1>dU
G°ermany  <ab n="Germany">G°</ab> (2)
 G -> <ab>G</ab>  (Gorresio) (32)
GS unmarked ls (1)
Gaelic in an 'etymology' (1)
Sk. <etym>kaccha</etym> -> <ab>Sk.</ab> <s>kacCa</s>  (<L>41526.1<pc>241,3<k1>kakza) (1)
Ganar -> Gaṇar ls unmarked (1)
Gant -> Gaut ls unmarked (1)
GarP ls unmarked (3)
Gardenia bot unmarked (1)
Gaut ls unmarked (3)
Gen. ab unmarked (2)
Gmn ls unmarked (1)
Go  <s1 slp1="go">Go</s1> (3)
Goldst. ls unmarked tooltip = 'Theodor Goldstücker'  << help wanted
Gorr. ab unmarked (3)
Gorresio ab unmarked (4)
Got. ab unmarked (3)
Gr. ab unmarked (6) (Whitney's Grammar)
Gymnema bot unmarked (1)
H. Germ. -> HGerm. (1)
HGerm. unmarked ab (5)
NHGerm. unmarked ab (1)
HParit -> HPariś unmarked ls (1)
Harikandra -> Hariścandra
Haughton  unmarked ls. tooltip="Dictionary of Bengali-Sanskrit-English, Graves C. Haughton"
  tooltip right? << help wanted. <L>50953<pc>285,3<k1>kucelI
Hcat. ls unmarked (1)
Hcit. -> Hcat. ls unmarked (1)
Hedysaruni lagopodioides -> Hedysarum lagopodioides bot unmarked (1)
Hir -> ls unmarked (1)
Hit -> ls unmarked (6)
Hpar. -> ls unmarked (2)  (variant of HPariś., Hemacandra's pariSizwaparvan ?)
   << help wanted tooltip >1639<pc>8,1<k1>aNgArakArin
I  variously changed (12)
I.W. -> IW. ls unmarked (1)
IW, -> IW. ls unmarked (1)
Ia, spurious text under <L>182659<pc>902,3<k1>limpawa
Iiving -> Living
Imp. unmarked ab (1)
Imper. unmarked ab (114)
Impf. unmarked ab (1)
Impv. unmarked ab (5)
In, -> 'In ' (3)
Inc. -> loc. unmarked ab (1)
Ind, -> Ind. unmarked ab (1)
Ind. unmarked ab (2)
Indic. -> unmarked ab (1) 
  Tooltip = "indicative (= optative)"  << help wanted
  <L>262729.1<pc>1297,3<k1>hi  <L>170219<pc>844,3<k1>yadi
Indras -> Indra's (1)
Inf. unmarked ab (31)
Intesis. -> Intens. unmarked ab (1)
Introd. unmarked ab (2)
Ist -> 1st (10)
Panicum Italicum unmarked bot (1)
Iv -> lv (1)
J  unmarked abbrev tooltip=? (1)  <L>84012<pc>443,1<k1>tAmasa
   <ls>Pravar. i, 1 (J)</ls>
JBr. unmarked ls (1)
  Same as JaimBr. ? (jEminIya-brAhmaRa) <L>107266.1<pc>542,1<k1>nirvaruRatA
Jaim Up. -> JaimUp. unmarked ls (1)
K. unmarked ls (6)
Kaiy. unmarked ls (2)
Kap unmarked ls (1)
Kathls. -> Kathās. unmarked ls (1)
Kaus, -> Kauś. unmarked ls (1)
Kelt. unmarked ab (1)  Tooltip: "Keltic or Celtic".
   << tooltip Help wanted <L>176837.1<pc>874,3<k1>rAjan
KenaUp. unmarked ls (1)
Kosegarten unmarked ls (1)
  tooltip="Johann Gottfried Ludwig Kosegarten" << Help wanted <L>33211<pc>189,3<k1>udDAraRa
Kull. unmarked ls (1)
Kuu, -> Kum. unmarked ls (1)
Kuv. unmarked ls (1)
L. unmarked ls (30+)
LaMghan -> Lamghan (1)
Larus ridibundus unmarked bio (1)
Lin -> unmarked abbrev. Tooltip="Carl Linnaeus"  << help wanted. check tooltip
Luders -> unmarked ls. Tooltip="Heinrich Lüders"  << help wanted. check tip.
   <L>97153.1<pc>1329,1<k1>dohada   <L>97163.1<pc>1329,1<k1>dohala<k2>dohala<e>2A
Ludwig. -> unmarked ls (2)  Tooltip=?  <<<help wanted for tooltip
  <L>15276<pc>87,3<k1>arAvan   <L>38960<pc>226,2<k1>fBu
MBh. unmarked ls (1)
MBh, unmarked ls (2)
MPh. -> MBh. unmarked ls (1)
Mahidh. -> Mahīdh. unmarked ls (6)
Maitr, unmarked ls (1)
Maitr. unmarked ls (1)
MaitrS. unmarked ls (1)
Mallin unmarked ls (2)
Phaseolus Max. unmarked bot (1)
Mbh -> MBh. unmarked ls (1)
Mid -> said (typo) (1)
Miliaceum unmarked bot (1)
Mimosa abstergens unmarked bot (2)
Aethiops Mineralis unmarked - homeopathy
Minusops unmarked bot (1)
Mit. unmarked ls (4)
'Mn,' and 'Mn ' unmarked ls (9)
Mod. unmarked ab (1)
Muir unmarked ls (3) tooltip="John Muir"  << help wanted check tooltip
   <L>28925<pc>166,1<k1>indra   <L>29632<pc>169,3<k1>izwApUrta  <L>254246<pc>1257,1<k1>skamBa
N. unmarked ab (~10)
Naigh. unmarked ls (1)
Naish -> Naiṣ unmarked ls (1)
Naishidhs -> Naishidha (2)
Nalac unmarked ls (1)
Nanclea Cadamba -> Nauclea Cadamba unmarked bot (1)
Nar. -> Nār. unmarked ls (2)
Naravelia zeylanica unmarked bot (1)
Helleborus Niger unmarked bot (1)
Nov. unmarked ab (1)
OGerm. unmarked ab (1)
OR -> or (2)
OSax. unmarked ab (1)  tooltip="Old Saxon"
   << help wanted tooltip text (<L>104741.1<pc>531,3<k1>navan)
Old <ab>Germ.</ab> -> <ab>Old Germ.</ab> (42)
Old <ab>Slav.</ab> -> <ab>Old Slav.</ab> (1)
Old <ab>Pers.</ab> -> <ab>Old Pers.</ab> (4)
Osk. <ab>Osk.</ab> (1)  << help wanted for tooltip (<L>40047.1<pc>231,2<k1>etad)
Old <ab>Pruss.</ab> -> <ab>Old Pruss.</ab> (4)
Old <ab>Sax.</ab> -> <ab>Old Sax.</ab> (5)
Old <ab>HGerm.</ab> -> <ab>Old HGerm.</ab> (1)
Old <ab>Lat.</ab> -> <ab>Old Lat.</ab> (3)
<ab>Goth.</ab> Old S. -> <ab>Goth. Old S.</ab> (1)
  << "Gothic Old Saxon" tooltip help wanted.  <L>147598.1<pc>743,1<k1>Baj
Onjein -> Oujein (1)
Opt. unmarked ab (28)
Or -> or (1)
Orig. unmarked ab (5)
P unmarked ab (2)
PBr unmarked ls (10)
Paddh. unmarked ab (7)
Paining -> paining (1)
Paipp. -> unmarked ls (5)
Pan -> Pāṇ. unmarked ls (2)
Pan. unmarked ls ? << help wanted
  print error for Pāṇ.?  <L>74573<pc>400,1<k1>cud
Pancar -> Pañcar unmarked ls (1)
Panting -> panting (1)
Part -> part (1)
Partic. -> partic. unmarked ab (6)
Pass. unmarked ab (2)
Past -> past (1)
Patr. -> patr. unmarked abbrev (3)
<ls>Patr.</ls> <<< help wanted. Is this a 'ls', if so what is tooltip
  or is it an upper-case of 'patr.' (patronymic) abbreviation?
  <L>208715<pc>1031,2<k1>vyapakarza<k2>vy-apakarza<e>3
  <s>vy-°apakarza</s> ¦ <lex>m.</lex> exception (from a rule), <ls>Patr.</ls><info lex="m"/>
Penance -> penance (1)
People -> people (3)
Perceive -> perceive (2)
Perform -> perform (1)
Performer -> performer (1)
Perplexity -> perplexity (1)
Person -> person (1)
Persons -> persons (1)
Phsseolus -> Phaseolus unmarked bot (1)
Physalia flexuosa unmarked bot (1)
Piece -> piece (1)
Pischel unmarked ls. tooltip="Richard Pischel"  << help wanted verify tooltip
 <L>26267<pc>151,1<k1>AroDana
Pl. -> pl. unmarked ab. (6)
Place -> place (2)
Planet -> planet (1)
Plant -> plant (6)
Play -> play (1)
Poet -> poet (1)
Pol. unmarked ab (1)
Pomegranate -> pomegranate (1)
Possessing -> possessing (2)
Postvedic -> Post-vedic (1)
Pot unmarked ab (3)
Pour -> pour (1)
Power -> power (4)
Practice -> practice (2)
Prasann. unmarked ls (2)
Prav. unmarked ls (3) <<< help wanted to confirm this is same
  as 'Pravar.' (pravara - literary category)
   <L>95089<pc>490,2<k1>dfQacyuta   <L>96405<pc>496,1<k1>devala and 6 others
Prays -> prays (1)
Pre-eminence -> pre-eminence (1)
Prec. unmarked ab (1)
Precipitous -> precipitous (1)
Preposition -> preposition (1)
Pres. unmarked ab (5)
Present -> present (4)
Preserving -> preserving (1)
Priests -> priests (1)
Prince -> prince (3)
Priyad unmarked ls (1)
Prob. unmarked ab (5)
Producing -> producing (1)
Produced -> produced (1)
Producer -> producer (1)
Prologue -> prologue (1)
Promise -> promise (1)
Proof -> proof (1)
Prst -> Prāt. unmarked ls (1)
RPrst -> RPrāt. unmarked ls (1)
Psoralea corylifolia unmarked bot (1)
Public -> public (1)
Pur  unmarked ls (3)
Purification -> purification (1)
Purport -> purport (1)
Purpose -> purpose (1)
Putting -> putting (2)
R. unmarked ls (21)
RTL unmarked ls (1)
RV unmarked ls (1)
Raljat -> Rājat unmarked ls (1)
Raphanus sativus unmarked bot (1)
Ratnak. unmarked ls (1)
Ratnav -> Ratnāv unmarked ls (1)
RhP. -> BhP. unmarked ls (1)
Wh. unmarked ls; and Ro. unmarked ls. (Wh. and Ro.) (1)
  << help wanted for tooltip.  <L>27372<pc>157,1<k1>ASaMs
Rubriflora unmarked bot (1)
Ry. -> RV. unmarked ls (1)
S << help wanted <L>74857<pc>401,2<k1>cUlA  (<ab>ifc.</ab>; <s>cOla</s>, S)
SBr -> ŚBr unmarked ls (3)
Saddhp -> SaddhP unmarked ls (1)
Saivad -> Sarvad unmarked ls (1)
Same -> same (1)
Sarvad unmarked ls (1)
Satum -> Saturn (1)
Sch. unmarked ab (1)
Schlegel unmarked ls (2)  Tooltip: "Friedrich Schlegel"  << help wanted confirm tooltip
See, -> See  (261) 
  Some should be lower case 'see' based on text; but not sure which. << help wanted
Siddh. unmarked ls (1)
Sidonia unmarked bot (1)
Siksh -> Śikṣ unmarked ls (1)
Sil. -> Śīl. unmarked ls (4)
Simia unmarked bio (1)
Siva -> Śiva (1)
Sk. unmarked ab (1)
Skr. unmarked ab (1)
Sly. -> Sāy. unmarked ls (1)
Speaking -> speaking  (1)
Sphex unmarked bio (1)
Stones -> stones (1)
Subj. unmarked ab (6)
Sukh, -> Sukh. unmarked ls (3)
Sulb. -> Śulb. unmarked ls (1)
Sulr, -> Suśr. unmarked ls (2)
Superl. unmarked ab (3)
TS unmarked ls (4)
Taitt.Up. unmarked ls (1)
Tantr. unmarked ls (4)
Teüri -> Teöri (1)
Terra unmarked bot (1)
Tesbania unmarked bot (1)
The, -> The (1)
Them. unmarked ab (2)  << tooltip help wanted
  <L>60259<pc>332,1<k1>kzetra<k2>kzetra<e>1E
  <L>14451.1<pc>83,2<k1>ambA<k2>ambA<e>1E
Theme unmarked ab (4) << tooltip help wanted
  <L>7915.105<pc>42,3<k1>anta<k2>anta<e>1E  and 3 others
Thema unmarked ab (1) << tooltip help wanted
  <L>8567.1<pc>45,2<k1>anya<k2>anya<e>1E
Thora unmarked bot (4)
Transl. unmarked ab (1)
UP -> Up unmarked ls (2)
Umbr. unmarked ab (1) Tooltip = "Umbrian"  << help wanted confirm tooltip
  <L>127307.1<pc>640,3<k1>pU<k2>pU<e>1E
Up. unmarked ls (4)
Uttarar unmarked ls (1)
V. -> W. unmarked ls (1)
 << <L>75248<pc>403,2<k1>cOli<k2>cOli<e>2  What are B and V ?
V. unmarked ls (3)
VRJ. unmarked ls (1) tooltip=? << help wanted tooltip
   <L>84423<pc>444,2<k1>tArukzAyaRi
VS unmarked ls (1)
Vaidyakaparibh unmarked ls (1)
Valeriana unmarked bot (1)
Vallisneria unmarked bot (1)
Var unmarked ls (5)
VarBIS. -> VarBṛS. unmarked ls (1)
Vart -> Vārt unmarked ab (1)
Vastuv -> Vāstuv unmarked ls (1)
Ved, -> Ved. unmarked ab (2)
Ved.inf. -> <ab>Ved.</ab> <ab>inf.</ab> (7)
Ved. unmarked ab (10)
Versed -> versed (1)
Vet unmarked ls (4)
Voc. unmarked ab (2)
Vp. -> VP. unmarked ls (1)
Uṇ.Vr. -> Uṇvṛ. unmarked ls (1)
Vssav -> Vāsav unmarked ls (1)
W. unmarked ls (8)
Washing -> washing (1)
Water -> water (1)
Weber unmarked ls (3) tooltip: Albrecht Weber  << help check tooltip
Whitney's Gr.  unmarked ls (3)
Who -> who (1)
Windisch ?? << help wanted. <L>14876<pc>85,3<k1>ayAsya
With -> with (2)
Woman -> woman (1)
Wrightla -> Wrightia unmarked bot (1)
X, -> x, (2)
Xanthophyllum virens unmarked bot (1)
YV unmarked ab (8)
'Yanma, a,' -> Yama (1)
Yog. unmarked ls (1)  tooltip = "Yogasūtra"  << help wanted
  <L>114151<pc>578,2<k1>paYcataya
Z. unmarked ab (1) tooltip="Zend" << help wanted
  <L>92472.1<pc>479,3<k1>diS<k2>diS<e>1E
Zanthorrhizza unmarked bot (1)
Zend unmarked ab (8)
