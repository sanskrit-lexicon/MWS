# MW block detector — gold-standard worksheet

200-entry stratified sample (seed=2026). For each entry, mark the detector errors:
`FP:` detected blocks not actually present; `FN:` present blocks the detector missed.
Record decisions in `GOLD_SAMPLE.json` (annotations.A / annotations.B), then run `gold_score.py`.

| stratum | entries |
|---|---:|
| adjective-mfn | 14 |
| biographical | 14 |
| botanical | 14 |
| compound | 14 |
| continuation | 14 |
| derived | 13 |
| etymological-ie | 13 |
| indeclinable | 13 |
| lexicographer-only | 13 |
| noun-f | 13 |
| noun-m | 13 |
| noun-n | 13 |
| other | 13 |
| root | 13 |
| vedic-accented | 13 |


## adjective-mfn

### L14989  k2=`a-yoni/`  e=1B
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn vedic-accented
- body: `<s>a-yoni/</s> ¦ <lex>mfn.</lex> = <s>a-yoni-ja</s> below, <ls>MaitrS.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L18770  k2=`avita`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F16(cross-reference) F17(machine annotation)
- detected types: adjective-mfn lexicographer-only
- body: `<s>avita</s> ¦ <lex>mfn.</lex> (√ <s>av</s>). protected, <ls>L.</ls> (<ab>cf.</ab> <s>a/droGA<srs/>vita</s>.)<info lex="m:f:n"/><info hui="b"/>`
- FP: ___   FN: ___

### L54480  k2=`kftArGa`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>kftA<srs/>rGa</s> ¦ <lex>mfn.</lex> received or welcomed by the <s1>Argha</s1> offering, <ls>PārGṛ.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L96264  k2=`devAsura/`  e=3B
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn vedic-accented
- body: `<s>devA<srs/>sura/</s> ¦ <lex>mfn.</lex> (with <s>yudDa</s>, <s>raRa</s> &c. the war) of the <ab n="gods">g˚</ab> and <s1 n="Asura">A˚</s1>s <ls>MBh.</ls>; <ls>R.</ls>; <ls>BhP.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L127749  k2=`pUrRArTa`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>pUrRA<srs/>rTa</s> ¦ <lex>mfn.</lex> one who has attained his object, whose wishes have been realized, <ls>BhP.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L159685.40  k2=`mahA—tmya`  e=4
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>mahA<srs/>—˚tmya</s> ¦ <lex>mfn.</lex> magnanimous, <ls>MW.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L163937  k2=`mAsAnumAsika`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>mAsA<srs/>numAsika</s> ¦ <lex>mfn.</lex> performed or occurring every <ab n="month">m˚</ab>, monthly, <ls>Mn. iii, 122</ls>,<info lex="m:f:n"/>`
- FP: ___   FN: ___

### L185088  k2=`vajrASani`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: adjective-mfn lexicographer-only
- body: `<s>vajrA<srs/>Sani</s> ¦ <lex>mfn.</lex> <s1>Indra</s1>'s <ab n="thunderbolt">th˚</ab>, <ls>L.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L190631  k2=`vAtsa—banDa—vi/d`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: adjective-mfn vedic-accented
- body: `<s>vAtsa—banDa—vi/d</s> ¦ <lex>mfn.</lex> knowing the text called <s1>Vātsabandha</s1>, <ls>ib.</ls> (<s>vAtsambanDa-vid</s>, <ls>MaitrS.</ls>)<info lex="m:f:n"/>`
- FP: ___   FN: ___

### L199064  k2=`vi-racita—vapus`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>vi-˚racita—vapus</s> ¦ <lex>mfn.</lex> one who has his body formed or arranged, <ls>MW.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L213579  k2=`SarAsanin`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>SarA<srs/>sanin</s> ¦ <lex>mfn.</lex> armed with a bow, <ls>MBh.</ls>; <ls>Hariv.</ls>; <ls>MārkP.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L224005  k2=`SlaTodyama`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>SlaTo<srs/>dyama</s> ¦ <lex>mfn.</lex> relaxing one's effort, <ls>Bhartṛ.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L234221  k2=`sam-A-DUta`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>sam-A-DUta</s> ¦ <lex>mfn.</lex> (√ <s>DU</s>) driven away, dispersed, scattered, <ls>R.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L258568  k2=`svayaM—grAha—nizakta-bAhu`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: adjective-mfn
- body: `<s>svayaM—grAha—nizakta-bAhu</s> ¦ <lex>mfn.</lex> putting the arms spontaneously round (<ab>loc.</ab>), embracing ardently, <ls>Kum.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___


## biographical

### L45846.1  k2=`kalANkura`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `¦ the bird <bio>Ardea Sibirica</bio>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L49023  k2=`kAla`  e=1B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: biographical
- body: `¦ the poisonous serpent <bio>Coluber Naga</bio> (= <s>kAlasarpa</s>), <ls>Vet.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L51432  k2=`kucika`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `<s>kucika</s> ¦ <lex>mf(<s>A</s>) </lex> a kind of fish (in shape like an eel, commonly <ns>Kuñciya</ns>, <bio>Unibranchapertura Cuchiya</bio>, or <bio>Muraena apterygia synbrache</bio>; the <ns>Hindūs</ns> affirm that its bite is mortal to cows, though perfectly harmless to men), <ls>L.</ls><info lex="m:f#A"/>`
- FP: ___   FN: ___

### L55149  k2=`kfzRa/`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F16(cross-reference) F17(machine annotation)
- detected types: biographical vedic-accented
- body: `¦ the Indian cuckoo or <bio>Kokila</bio> (<ab>cf.</ab> <ls>R. ii, 52, 2</ls>), <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L57621  k2=`krakaca`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: biographical
- body: `¦ <bio>Ardea virgo</bio>, <ls>Npr.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L68235  k2=`gOra/`  e=1B
- detected blocks: F01(record header) F02(display headword) F09(editorial commentary) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: biographical vedic-accented
- body: `¦ a kind of buffalo (<bio>Bos Gaurus</bio>, often classed with the <s1>Gavaya</s1>), <ls>RV.</ls>; <ls>VS.</ls> &c.<info lex="inh"/>`
- FP: ___   FN: ___

### L71490  k2=`catura`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: biographical
- body: `¦ the fish <bio>Cyprinus Rohita</bio>, <ls>Gal.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L81283  k2=`wuRwuka`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `¦ the bird <bio>Sylvia sutoria</bio>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L141946  k2=`PalottamA`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `¦ the 3 <bio>myrobalans</bio>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L144485  k2=`bAla`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `¦ <bio>Cyprinus Denticulatus</bio> or <bio>Rohita</bio>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L150147  k2=`BAlANka`  e=3B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `¦ <bio>Cyprinus Rohita</bio>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L173669  k2=`raktAkza`  e=3B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical lexicographer-only
- body: `¦ <bio>Perdix Rufa</bio>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L215933  k2=`SAla/`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: biographical vedic-accented
- body: `¦ a kind of fish, <bio>Ophiocephalus Wrahl</bio>, <ls>Vās.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L222044  k2=`SyAma/`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: biographical vedic-accented lexicographer-only
- body: `¦ the <bio>Kokila</bio> or Indian cuckoo, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___


## botanical

### L14428  k2=`ambarI/za`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical vedic-accented lexicographer-only
- body: `¦ the hog-plum plant (<bot>Spondias Magnifera</bot>), <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L28655  k2=`iNguda`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F14(botanical name) F17(machine annotation)
- detected types: botanical
- body: `<s>iNguda</s> ¦ <lex>mf(<s>I</s>). </lex> the medicinal tree <bot>Terminalia Catappa</bot> (in Bengal confounded with <ns>Putrañjīva</ns> <bot>Roxburghii Wall.</bot>), <ls>MBh.</ls>; <ls>R.</ls>; <ls>Suśr.</ls>; <ls>Śak.</ls>; <ls>Ragh.</ls><info lex="m:f#I"/>`
- FP: ___   FN: ___

### L45065  k2=`karRAwI`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical lexicographer-only
- body: `¦ a kind of <bot>Mimosa</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L45981  k2=`kaliNga`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical lexicographer-only
- body: `¦ <bot>Acacia Sirissa</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L55151  k2=`kfzRa/`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical vedic-accented lexicographer-only
- body: `¦ <bot>Carissa Carandas</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L55183  k2=`kfzRA`  e=1B
- detected blocks: F01(record header) F02(display headword) F09(editorial commentary) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F15(biographical content) F17(machine annotation)
- detected types: botanical
- body: `¦ <ab>N.</ab> of several plants (<bot>Piper longum</bot>, <ls>L.</ls>; the Indigo plant, <ls>L.</ls>; a grape, <ls>L.</ls>; a <s1>Punar-navā</s1> with dark blossoms, <ls>L.</ls>; <bot>Gmelina arborea</bot>, <ls>L.</ls>; <bot>Nigella indica</bot>, <ls>L.</ls>; <bot>Sinapis</bot> ramosa, <ls>L.</ls>; <bot>Vernonia anthelminthica</bot>, <ls>L.</ls>; = <s>kAkolI</s>, <ls>L.</ls>; a sort of <s1>Sārivā</s1>, <ls>L.</ls>), <ls>Suśr.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L102984  k2=`naKANka`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical lexicographer-only
- body: `¦ <bot>Unguis Odoratus</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L155773  k2=`ma/Du`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical vedic-accented lexicographer-only
- body: `¦ <bot>Jonesia Asoka</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L168410.5  k2=`mo/GA`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical vedic-accented lexicographer-only
- body: `¦ <bot>Embelia Ribes</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L170807  k2=`yavanezwa`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical lexicographer-only
- body: `¦ <bot>Azadirachta Indica</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L217923  k2=`Sivezwa`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical lexicographer-only
- body: `¦ <bot>Getonia Floribunda</bot>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L246027  k2=`su—ganDa—mUlA`  e=4A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F14(botanical name) F17(machine annotation)
- detected types: botanical
- body: `¦ <bot>Hibiscus Mutabilis</bot>, <ls>ib.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L249591  k2=`surezwa`  e=3B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F14(botanical name) F17(machine annotation)
- detected types: botanical
- body: `¦ <bot>Agati Grandiflora</bot>, <ls>ib.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L252097  k2=`se/tu`  e=1B
- detected blocks: F01(record header) F02(display headword) F08(inflection form) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: botanical vedic-accented lexicographer-only
- body: `¦ <bot>Crataeva Roxburghii</bot> or <bot>Tapia Crataeva</bot> (= <s>varaRa</s>, <s>varuRa</s>), <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___


## compound

### L55926  k2=`keSa—karzaRa`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound
- body: `<s>keSa—karzaRa</s> ¦ <lex>n.</lex> pulling or tearing by the hair, <ls>Veṇīs.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L78040  k2=`jala—raRqa`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: compound lexicographer-only
- body: `¦ a snake, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L79649  k2=`jIva—koSa`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F17(machine annotation)
- detected types: compound
- body: `¦ <ls n="BhP.">x.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L99298  k2=`Dana—M-jaya/`  e=3B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound vedic-accented
- body: `¦ of a merchant, <ls>SkandaP.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L117985  k2=`pari-pUta`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound
- body: `<s>pari-pUta</s> ¦ <lex>mfn.</lex> purified, strained, winnowed, threshed, <ls>RV.</ls>; <ls>Mn.</ls> &c.<info lex="m:f:n"/>`
- FP: ___   FN: ___

### L135080  k2=`pra-pAWita`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F06(etymology root marker) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: compound lexicographer-only
- body: `<s>pra-˚pAWita</s> ¦ <lex>mfn.</lex> (<ab>fr.</ab> <ab>Caus.</ab>) taught, expounded, <ls>L.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L136210  k2=`pra/-yasta`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound vedic-accented
- body: `<s>pra/-˚yasta</s> ¦ (<s>pra/-</s>), <lex>mfn.</lex> bubbling over, <ls>RV.</ls>; <ls>AV.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___

### L145178  k2=`bindu—matI`  e=3B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F15(biographical content) F16(cross-reference) F17(machine annotation)
- detected types: compound
- body: `¦ of the wife of <s1>Marīci</s1> (<ab>cf.</ab> above), <ls>BhP.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L168582  k2=`moha—cUqottara`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: compound
- body: `<s>moha—cUqo<srs/>ttara</s> or <s>moha—cUqo<srs/>tta˚ra-SAstra</s>, ¦ <lex>n.</lex> <ab>N.</ab> of <ab>wk.</ab><info lex="n"/>`
- FP: ___   FN: ___

### L172167  k2=`yuva—KalatI`  e=3B
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound
- body: `<s>yuva—KalatI</s> ¦ <lex>f.</lex> bald in girlhood, <ls>Pāṇ. ii, 1, 67</ls>, <ab>Sch.</ab><info lex="f"/>`
- FP: ___   FN: ___

### L199960.1  k2=`vi-vAda—candrikA`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: compound
- body: `<s>vi-vAda—candrikA</s> ¦ <lex>f.</lex> <ab>N.</ab> of <ab>wk.</ab><info lex="f"/>`
- FP: ___   FN: ___

### L211667  k2=`SaNKA-vatI`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound
- body: `<s>SaNKA-vatI</s> ¦ <lex>f.</lex> (for <s>SaNKa-v˚</s>) <ab>N.</ab> of a river, <ls>MārkP.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L227864  k2=`sa—ganDa`  e=3A
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound
- body: `¦ having the same smell as (<ab>instr.</ab> or <ab>comp.</ab>), <ls>VarBṛS.</ls>; <ls>Vop.</ls> (also <s>˚Din</s>, <ls>MBh.</ls>)<info lex="inh"/>`
- FP: ___   FN: ___

### L240415  k2=`sahAya—kftya`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: compound
- body: `<s>sahA<srs/>ya—kftya</s> ¦ <lex>n.</lex> = <s>karaRa</s>, <ls>R.</ls><info lex="n"/>`
- FP: ___   FN: ___


## continuation

### L3936  k2=`a/-dvEta`  e=1A
- detected blocks: F01(record header) F17(machine annotation)
- detected types: continuation vedic-accented
- body: `¦ peerless<info lex="inh"/>`
- FP: ___   FN: ___

### L5158  k2=`an-aBilAza`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F17(machine annotation)
- detected types: continuation
- body: `¦ want of appetite<info lex="inh"/>`
- FP: ___   FN: ___

### L5716  k2=`an-AsTA`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F17(machine annotation)
- detected types: continuation
- body: `¦ want of consideration<info lex="inh"/>`
- FP: ___   FN: ___

### L11160  k2=`a-Bava`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F17(machine annotation)
- detected types: continuation
- body: `¦ destruction, end of the world.<info lex="inh"/>`
- FP: ___   FN: ___

### L19309  k2=`a-vyaya`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F17(machine annotation)
- detected types: continuation
- body: `¦ ‘not spending’, parsimonious<info lex="inh"/>`
- FP: ___   FN: ___

### L21489  k2=`a-sPuwa`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: continuation
- body: `¦ not quite correct, approximate (as a number), <ls>Sūryas.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L43272  k2=`kandala`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: continuation lexicographer-only
- body: `¦ reproach, censure, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L44366.2  k2=`kara`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: continuation
- body: `¦ royal revenue, toll, tax, tribute, duty, <ls>Mn.</ls>; <ls>Yājñ.</ls>; <ls>MBh.</ls> &c.<info lex="inh"/>`
- FP: ___   FN: ___

### L164663  k2=`mImAMsaka`  e=1A
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: continuation
- body: `¦ a follower of the <s1>Mīmāṃsā</s1> system (see below), <ls>TPrāt.</ls>; <ls>Śaṃk.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L165846  k2=`mu/rmura`  e=1A
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: continuation vedic-accented
- body: `¦ burning chaff, <ls>Kāv.</ls> (<ab>v.l.</ab> <s>murmara</s>)<info lex="inh"/>`
- FP: ___   FN: ___

### L180061  k2=`rohi`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: continuation lexicographer-only
- body: `¦ (only <ls>L.</ls>) a seed<info lex="inh"/>`
- FP: ___   FN: ___

### L190665  k2=`vAda`  e=1A
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F17(machine annotation)
- detected types: continuation
- body: `¦ causing to sound, playing (see <s>vIRA-v˚</s>)<info lex="inh"/>`
- FP: ___   FN: ___

### L191097  k2=`vAmana/`  e=1A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: continuation vedic-accented
- body: `¦ small, minute, short (also of days), <ls>MBh.</ls>; <ls>Kāv.</ls> &c.<info lex="inh"/>`
- FP: ___   FN: ___

### L211320  k2=`Sakuna/`  e=1A
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: continuation vedic-accented
- body: `¦ <ab>N.</ab> of an <s1>Asura</s1>, <ls>BhP.</ls><info lex="inh"/>`
- FP: ___   FN: ___


## derived

### L11902  k2=`aBi-prApta`  e=2
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: derived
- body: `<s>aBi-prA<srs/>pta</s> ¦ <lex>mfn.</lex> reached, obtained.<info lex="m:f:n"/>`
- FP: ___   FN: ___

### L29610  k2=`izira/`  e=2A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived vedic-accented
- body: `¦ vigorous, active, quick, <ls>RV.</ls>; <ls>AV.</ls>; <ls>VS.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L33062  k2=`ud-Ga`  e=2A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived
- body: `¦ a model, pattern, <ls>Pāṇ. iii, 3, 86</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L36082  k2=`upa-saMgraha`  e=2A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived
- body: `¦ a pillow, cushion, <ls>MBh. iv, 517.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L79021  k2=`jAraRa`  e=2A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived
- body: `¦ condiment, a digester, <ls>W.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L82258  k2=`ta/naya`  e=2B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived vedic-accented
- body: `¦ <ab>pl.</ab> <ab>N.</ab> of a people, <ls>MBh. vi, 371</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L200604  k2=`vi-Seza`  e=2
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived
- body: `<s>vi-Seza</s> ¦ <lex>m.</lex> (once in <ls>Pañcat.</ls> <lex type="hwalt">n.</lex>; <ab>ifc.</ab> <lex type="hwifc">f(<s>A</s>). </lex>) distinction, difference between (two <ab>gen.</ab>, two <ab>loc.</ab>, or <ab>gen.</ab> and <ab>instr.</ab>), <ls>GṛŚrS.</ls>; <ls>MBh.</ls> &c.<info lex="m:f#A:n"/><info hui="a"/>`
- FP: ___   FN: ___

### L214481  k2=`SaSin`  e=2A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived
- body: `¦ a kind of metre, <ls>Col.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L221438  k2=`So/Ra`  e=2B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: derived vedic-accented lexicographer-only
- body: `¦ red sugar cane, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L233474.2  k2=`samanA/`  e=2A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived vedic-accented
- body: `¦ likewise, uniformly, <ls>ib.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L241502  k2=`sA/Da`  e=2
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived vedic-accented
- body: `<s>sA/Da</s> ¦ <lex>m.</lex> accomplishment, fulfilment, <ls>RV.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L258792  k2=`svadita/`  e=2B
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F15(biographical content) F16(cross-reference) F17(machine annotation)
- detected types: derived vedic-accented
- body: `<s>svadita/</s> ¦ <lex>n.</lex> ‘may it be well tasted or eaten!’ (an exclamation used at a <s1>Śrāddha</s1> after presenting the oblation of food to the <s1>Pitṛ</s1>s; <ab>cf.</ab> <s>su-Sruta</s>, <s>sva-DA</s>), <ls>Mn. iii, 251</ls>; <ls n="Mn. iii,">254.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L258804  k2=`svAdin`  e=2
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: derived
- body: `<s>svAdin</s> ¦ <lex>mfn.</lex> tasting, enjoying (<ab>ifc.</ab>), <ls>Nalod.</ls><info lex="m:f:n"/>`
- FP: ___   FN: ___


## etymological-ie

### L4271  k2=`aDi-Df`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F07(IE cognate) F08(inflection form) F10(sense gloss) F17(machine annotation)
- detected types: etymological-ie
- body: `<s>aDi-√ Df</s> ¦ <ab>Caus.</ab> <ab>P.</ab> <s>-DArayati</s>, <lang>Ved.</lang> to carry over or across.<info verb="pre" cp="P" parse="aDi+Df"/>`
- FP: ___   FN: ___

### L10235  k2=`apI`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F06(etymology root marker) F07(IE cognate) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: etymological-ie
- body: `<hom>2.</hom> <s>apI<srs/></s> ¦ (√ <s>i</s>), (<lang>Ved.</lang>) <s>a/py-eti</s> to go in or near;
<div n="to"/>to enter into or upon;
<div n="to"/>to come near, approach (also in copulation, <ls>RV. ii, 43, 2</ls> <ab>ind.p.</ab> <s>apI/<srs/>tyA</s>);
<div n="to"/>to partake, have a share in;
<div n="to"/>to join to pour out (as a river). <info verb="pre" cp="" parse="api+i"/>`
- FP: ___   FN: ___

### L36608  k2=`upA-GrA`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F07(IE cognate) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: etymological-ie
- body: `<s>upA<srs/>-√ GrA</s> ¦ <ab>P.</ab> <s>-jiGrati</s> (and <s>-GrAti</s> <ab>Ā.</ab> <s>-jiGrate</s>, <lang>ep.</lang>) to smell at;
<div n="to"/>to kiss, apply the lips to (<ab>loc.</ab>), <ls>MBh.</ls>; <ls>R.</ls>; <ls>Ragh.</ls><info verb="pre" cp="PĀ" parse="upa+A+GrA"/>`
- FP: ___   FN: ___

### L44028  k2=`ka/ya`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F07(IE cognate) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation)
- detected types: etymological-ie vedic-accented
- body: `<s>ka/ya</s> ¦ (<lang>Ved.</lang> for <hom>2.</hom> <s>ka</s>; only <ab>gen.</ab> <ab>sg.</ab> with <s>cid</s>), every one (<ab>e.g.</ab> <s>ni/ zU/ namA/<srs/>timatiM ka/yasya cit</s>, bow well down the haughtiness of every one, <ls>RV. i, 129, 5</ls>), <ls>RV. i, 27, 8</ls>; <ls n="RV.">viii, 25, 15</ls>;`
- FP: ___   FN: ___

### L55793  k2=`kel`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F07(IE cognate) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: etymological-ie
- body: `<s>kel</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <s>kelati</s>, to shake, tremble, <ls>Dhātup. xv, 30</ls>;
<div n="to"/>to go or move, <ls>ib.</ls>;
<div n="to"/>to be frolic-some, sport (<ab>cf.</ab> <lang>Prākṛt</lang> √ <i>kīl</i> = <s>krIq</s>), <ls>W.</ls><info westergaard="kelf,15.30,01.0352"/><info verb="root" cp="1P"/>`
- FP: ___   FN: ___

### L65883.1  k2=`guD`  e=1E
- detected blocks: F01(record header) F02(display headword) F07(IE cognate) F10(sense gloss) F16(cross-reference)
- detected types: etymological-ie
- body: `<s>guD</s> ¦ [<ab>cf.</ab> <lang>Gk.</lang> <gk>κεύθω</gk>; <lang>Old Germ.</lang> <etym>hūt</etym>; <lang>Germ.</lang> <etym>haut</etym>; <lang>Angl.Sax.</lang> <etym>hyde</etym>, <etym>hyd</etym>; <lang>Lat.</lang> <etym>cutis</etym> ?]`
- FP: ___   FN: ___

### L66808.1  k2=`gF`  e=1E
- detected blocks: F01(record header) F02(display headword) F07(IE cognate) F10(sense gloss) F16(cross-reference)
- detected types: etymological-ie
- body: `<s>gF</s> ¦ [<ab>cf.</ab> <gk>γηρύω</gk>, <gk>γλῶσσα</gk>; <lang>Hib.</lang> <etym>goirim</etym>; <lang>Old Germ.</lang> <etym>quar</etym>, <etym>quir</etym>, &c.; <lang>Old Pruss.</lang> <etym>gerbu</etym>, ‘to speak’; <lang>Angl.Sax.</lang> <etym>gale</etym>; <lang>Germ.</lang> <etym>Nachtigal</etym>; <lang>Lat.</lang> <etym>gallus</etym> ?]`
- FP: ___   FN: ___

### L152459.1  k2=`BUrja`  e=1E
- detected blocks: F01(record header) F02(display headword) F07(IE cognate) F10(sense gloss) F16(cross-reference)
- detected types: etymological-ie
- body: `<s>BUrja</s> ¦ [<ab>cf.</ab> <lang>Slav.</lang> <etym>brěza</etym>; <lang>Lith.</lang> <etym>bérżas</etym>; <lang>Germ.</lang> <etym>bircha</etym>, <etym>Birke</etym>; <lang>Eng.</lang> <etym>birch</etym>.]`
- FP: ___   FN: ___

### L158241.1  k2=`maru`  e=1E
- detected blocks: F01(record header) F02(display headword) F07(IE cognate) F10(sense gloss) F16(cross-reference)
- detected types: etymological-ie
- body: `<s>maru</s> ¦ [<ab>cf.</ab> <lang>Lat.</lang> <etym>mare</etym> (?); <lang>Angl.Sax.</lang> <etym>môr</etym>; <lang>Germ.</lang> and <lang>Eng.</lang> <etym>moor</etym>.]`
- FP: ___   FN: ___

### L198616  k2=`vi-mad`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F06(etymology root marker) F07(IE cognate) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: etymological-ie
- body: `<hom>1.</hom> <s>vi-√ mad</s> ¦ <ab>P.</ab> <s>-mAdyati</s> (<lang>Ved.</lang> also <s>-madati</s>), to be joyful or merry (only <ab>p.</ab> <s>-ma/dat</s>), <ls>AV.</ls>;
<div n="to"/>to become perplexed or discomposed, <ls>AitBr.</ls>;
<div n="to"/>to confound, embarrass, disturb, <ls>ŚāṅkhBr.</ls> : <ab>Caus.</ab> (only <ab>aor.</ab> <s>vy-amImadam</s>),
<div n="to"/>to confuse, perplex, bewilder, <ls>AV.</ls><info verb="pre" cp="P" parse="vi+mad"/>`
- FP: ___   FN: ___

### L230505.1  k2=`sad`  e=1E
- detected blocks: F01(record header) F02(display headword) F07(IE cognate) F10(sense gloss) F16(cross-reference)
- detected types: etymological-ie
- body: `<s>sad</s> ¦ [<ab>cf.</ab> <lang>Gk.</lang> <gk>ἵζω</gk> for <gk>σίσδω</gk>; <lang>Lat.</lang> <etym>sidere</etym>, <etym>sedere</etym>; <lang>Lith.</lang> <etym>sė́sti</etym>, <etym>sedė́ti</etym>; <lang>Slav.</lang> <etym>sěsti</etym>; <lang>Goth.</lang> <etym>sitan</etym>; <lang>Germ.</lang> <etym>sitzen</etym>; <lang>Angl.Sax.</lang> <etym>sittan</etym>; <lang>Eng.</lang> <etym>sit</etym>.]`
- FP: ___   FN: ___

### L237276  k2=`sam-mfd`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F07(IE cognate) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: etymological-ie
- body: `<s>sam-√ mfd</s> ¦ <ab>P.</ab> <s>-mfdnAti</s>, <s>-mardati</s> (<lang>Ved.</lang> <ab>inf.</ab> <s>-marditoH</s>), to press or squeeze together, rub or grind to pieces, crush, destroy, <ls>TS.</ls> :
<div n="vp"/><ab>Caus.</ab> <s>-mardayati</s> (<ab>pr. p.</ab> <s>-mardayAna</s>), to cause to be rubbed together, crush, pound, bruise, <ls>R.</ls>; <ls>BhP.</ls>;
<div n="to"/>to rub, <ls>Suśr.</ls>;
<div n="to"/>to clean, <ls>MW.</ls><info verb="pre" cp="P" parse="sam+mfd"/>`
- FP: ___   FN: ___

### L258948.1  k2=`svap`  e=1E
- detected blocks: F01(record header) F02(display headword) F07(IE cognate) F10(sense gloss) F16(cross-reference)
- detected types: etymological-ie
- body: `<s>svap</s> ¦ [<ab>cf.</ab> <lang>Gk.</lang> <gk>ὕπ-νος</gk>; <lang>Lat.</lang> <etym>somnus</etym> for <etym>sop-nus</etym>, <etym>sopor</etym>, <etym>sopire</etym>; <lang>Slav.</lang> <etym>sǔpati</etym>; <lang>Lith.</lang> <etym>sápnas</etym>; <lang>Angl.Sax.</lang> <etym>swefan</etym>, ‘to sleep’.]`
- FP: ___   FN: ___


## indeclinable

### L243.1  k2=`a-kAraRena`  e=1C
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: indeclinable
- body: `<s>a-kAra˚Rena</s> ¦ <lex>ind.</lex> causelessly.<info lex="ind"/>`
- FP: ___   FN: ___

### L7872.1  k2=`anevam`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable
- body: `<s>anevam</s> ¦ <lex>ind.</lex> not so, <ls>Bādar.</ls><info n="sup"/><info lex="ind"/>`
- FP: ___   FN: ___

### L8809  k2=`anv-aha/m`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: indeclinable vedic-accented
- body: `<s>anv-aha/m</s> ¦ <lex>ind.</lex> day after day, every day.<info lex="ind"/>`
- FP: ___   FN: ___

### L18543.1  k2=`avAntarA/m`  e=1C
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable vedic-accented
- body: `<s>avA<srs/>ntarA/m</s> ¦ (<s>A/m</s>), <lex>ind.</lex> between, <ls>ŚBr.</ls><info lex="ind"/>`
- FP: ___   FN: ___

### L70303  k2=`cakita—cakitam`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable
- body: `<s>cakita—cakitam</s> ¦ <lex>ind.</lex> with great alarm, <ls>Megh. 14.</ls><info lex="ind"/>`
- FP: ___   FN: ___

### L107328  k2=`nir—viSaNkitam`  e=4C
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable
- body: `<s>nir—viSaNkitam</s> ¦ <lex>ind.</lex>, <ls>Hariv.</ls><info lex="ind"/><info hui="b"/>`
- FP: ___   FN: ___

### L116565  k2=`paramArTa—tas`  e=4
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable
- body: `<s>paramA<srs/>rTa—tas</s> ¦ <lex>ind.</lex> in reality, really, in the true sense of the word, <ls>R.</ls>; <ls>Kālid.</ls> &c.<info lex="ind"/>`
- FP: ___   FN: ___

### L139213  k2=`prAcA/`  e=1C
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable vedic-accented
- body: `<s>prAcA/</s> ¦ <lex>ind.</lex> forwards, onwards, <ls>RV.</ls><info lex="ind"/><info hui="a"/>`
- FP: ___   FN: ___

### L140658  k2=`priyArTam`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable
- body: `<s>priyA<srs/>rTam</s> ¦ <lex>ind.</lex> for the sake of a beloved object, as a favour, <ls>MBh.</ls>; <ls>Megh.</ls>; <ls>Rājat.</ls><info lex="ind"/>`
- FP: ___   FN: ___

### L153009.1  k2=`BEravam`  e=1C
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: indeclinable
- body: `<s>BEravam</s> ¦ <lex>ind.</lex><info phwparent="152990,BErava"/><info lex="ind"/>`
- FP: ___   FN: ___

### L173118  k2=`rakzArTam`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable
- body: `<s>rakzA<srs/>˚rTam</s> ¦ (<s>˚kzA<srs/>rT˚</s>), <lex>ind.</lex> for the sake of protection, <ls>MW.</ls><info lex="ind"/>`
- FP: ___   FN: ___

### L241341  k2=`sAcIvi/t`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: indeclinable vedic-accented
- body: `<s>sAcIvi/t</s> ¦ <lex>ind.</lex> swiftly, rapidly (= <s>kzipram</s>), <ls>Naigh. ii, 15.</ls><info lex="ind"/>`
- FP: ___   FN: ___

### L263546  k2=`hum`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: indeclinable
- body: `<s>hum</s> or <s>hUm</s>, ¦ <lex>ind.</lex> or <s>hum</s> an exclamation (of remembrance, doubt, interrogation, assent, anger, reproach, fear &c., not translatable);
<div n="P"/> a mystical syllable used in spells and magical texts or sentences;
<div n="P"/> in Vedic ritual used immediately before the singing of the <s1>Prastāva</s1> or prelude as well as during the chanting of the <s1>Pratihāra</s1> or response, <ls>ŚrS.</ls>; <ls>MBh.</ls>; <ls>Kāv.</ls> &c.
<info lex="ind"/>`
- FP: ___   FN: ___


## lexicographer-only

### L19231  k2=`a-vyakta`  e=1B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ of <s1>Śiva</s1>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L42880  k2=`kadalI`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ a flag, banner, flag carried by an elephant, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L46663  k2=`kaSipu`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ clothing, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L51308  k2=`kukUla`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ armour, mail, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L57240  k2=`kOmudI`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ a festival in general, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L88187  k2=`tri—lokeSa`  e=4A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ the sun, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L91874  k2=`dASera`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ camel, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L93258  k2=`dIrGAyus`  e=3B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ of <s1>Mārkaṇḍeya</s1>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L121243  k2=`pAYcAla`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ the country of the <s1 n="Pañcāla">P˚</s1>s <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L145116  k2=`biqAlI`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ a species of plant, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L154163  k2=`maNgalA`  e=1B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F15(biographical content) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ of the mother of the 5th <s1>Arhat</s1> of the present <s1>Avasarpiṇī</s1>, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L157624  k2=`manTara`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `¦ whirling, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L187798  k2=`varP`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F08(inflection form) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: lexicographer-only
- body: `<s>varP</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <s>varPati</s>, ‘to go’ or ‘to kill’, <ls>L.</ls><info verb="root" cp="1P"/>`
- FP: ___   FN: ___


## noun-f

### L4814  k2=`anaGAzwamI`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F09(editorial commentary) F10(sense gloss) F15(biographical content) F17(machine annotation)
- detected types: noun-f
- body: `<s>anaGA<srs/>zwamI</s> ¦ <lex>f.</lex> <ab>N.</ab> of an eighth day (spoken of in the fifty-fifth <s1>Adhyāya</s1> of the <s1>Bhaviṣyottara-Purāṇa</s1>). <info lex="f"/>`
- FP: ___   FN: ___

### L43347  k2=`kapanA/`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-f vedic-accented
- body: `<s>kapanA/</s> ¦ <lex>f.</lex> (√ <s>kamp</s>, <ls>Nir. vi, 4</ls>), a worm, caterpillar, <ls>RV. v, 54, 6</ls><info n="rev" pc="1323,3"/><info lex="f"/>`
- FP: ___   FN: ___

### L74141  k2=`cintokti`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-f
- body: `<s>cinto<srs/>kti</s> ¦ <lex>f.</lex> midnight cry, <ls>W.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L128224  k2=`pUrvAzAQA`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F09(editorial commentary) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-f
- body: `<s>pUrvA<srs/>zAQA</s> ¦ <lex>f.</lex> the first of two constellations called <s1>Aṣāḍhā</s1> (the 18th or 20th <s1>Nakṣatra</s1> or lunar asterism), <ls>Var.</ls>; <ls>Pur.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L162591  k2=`mADavAnala—kaTA`  e=4
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F16(cross-reference) F17(machine annotation)
- detected types: noun-f
- body: `<s>mADavA<srs/>nala—kaTA</s>, <lex>f.</lex>, or <s>mADavA<srs/>nala—kAma-kandala-kaTA</s>, <lex>f.</lex> ¦ <ab>id.</ab><info lex="f"/>`
- FP: ___   FN: ___

### L162691.50  k2=`mADya—M-dina—SAKA`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-f
- body: `<s>mADya—M-dina—SAKA</s> ¦ <lex>f.</lex> the school of the <s1>Mādhyaṃdina</s1>s (<s>˚KIya</s>. <lex type="phw">mfn.</lex> belonging to it), <ls>Cat.</ls><info phwchild="162691.51"/><info lex="f"/>`
- FP: ___   FN: ___

### L186166  k2=`vanyopodakI`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: noun-f lexicographer-only
- body: `<s>vanyo<srs/>po<srs/>dakI</s> ¦ <lex>f.</lex> a species of creeper, <ls>L.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L188302.1  k2=`vallaBa—tara—tA`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-f
- body: `<s>vallaBa—tara—tA</s> ¦ <lex>f.</lex>, <ls>Kād.</ls><info phwparent="188302,vallaBatara"/><info lex="f"/>`
- FP: ___   FN: ___

### L230474  k2=`satI`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F04(grammatical category) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: noun-f lexicographer-only
- body: `<hom>2.</hom> <s>satI</s> ¦ <lex>f.</lex> (for <hom>1.</hom> See <pcol>p. 1135, col. 1</pcol>) = <s>sAti</s>, <ls>L.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L246296  k2=`su—jana—parisevitA`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-f
- body: `<s>su—jana—parisevitA</s> ¦ <lex>f.</lex> <ab>N.</ab> of a <s1>Kiṃ-narī</s1>, <ls>ib.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L249404  k2=`sura—rAja—tA`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-f
- body: `<s>sura—rAja—tA</s> ¦ <lex>f.</lex> the state or rank of <s1>Indra</s1>, <ls>Kāv.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L249997  k2=`suvarRAhvA`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: noun-f lexicographer-only
- body: `<s>suvarRA<srs/>hvA</s> ¦ <lex>f.</lex> yellow jasmine, <ls>L.</ls><info lex="f"/>`
- FP: ___   FN: ___

### L256904.1  k2=`sPuwArTa—tA`  e=4
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: noun-f
- body: `<s>sPuwA<srs/>rTa—tA</s> ¦ <lex>f.</lex><info phwparent="256904,sPuwArTa"/><info lex="f"/>`
- FP: ___   FN: ___


## noun-m

### L20692.1  k2=`a-samanvAhAra`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-m
- body: `<s>a-samanvAhAra</s> ¦ <lex>m.</lex> thoughtlessness (?), <ls>Divyāv.</ls><info n="sup"/><info lex="m"/>`
- FP: ___   FN: ___

### L38288  k2=`UrDveqa`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-m
- body: `<s>UrDve<srs/>qa</s> ¦ <lex>m.</lex> <ab>N.</ab> of a <s1>Sāman</s1>, <ls>TāṇḍyaBr.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L40922  k2=`OdabudDi`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-m
- body: `<s>OdabudDi</s> ¦ <lex>m.</lex> a descendant of <s1>Udabuddha</s1> <ab>g.</ab> <s>pElA<srs/>di</s>, <ls>Pāṇ. ii, 4, 59.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L83449  k2=`tarda/`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F07(IE cognate) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: noun-m etymological-ie vedic-accented
- body: `<s>tarda/</s> ¦ <lex>m.</lex> a kind of bird (<ab>cf.</ab> <lang>Lat.</lang> <etym>turdus</etym>), <ls>AV. vi, 50, 1 f.</ls><info lex="m"/><listinfo n="sup"/>`
- FP: ___   FN: ___

### L85198  k2=`tiri/ndira`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-m vedic-accented
- body: `<s>tiri/ndira</s> ¦ <lex>m.</lex> <ab>N.</ab> of a man, <ls>RV. viii, 6, 46</ls>; <ls>ŚāṅkhŚr. xvi, 11, 20.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L93546  k2=`dugDASman`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: noun-m lexicographer-only
- body: `<s>dugDA<srs/>Sman</s> ¦ <lex>m.</lex> calcareous spar, <ls>L.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L132934.2  k2=`prati-yogi—jYAna-kAraRatA-vAda`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: noun-m
- body: `<s>prati-˚yogi—jYAna-kAraRatA-vAda</s> ¦ <lex>m.</lex> <ab>N.</ab> of <ab>wk.</ab><info lex="m"/>`
- FP: ___   FN: ___

### L140161.22  k2=`prAyaS—citta—pratyAmnAya`  e=4
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: noun-m
- body: `<s>prA<srs/>yaS—citta—pratyAmnAya</s> ¦ <lex>m.</lex> <ab>N.</ab> of work<info lex="m"/>`
- FP: ___   FN: ___

### L180044  k2=`rohaRAcala`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: noun-m
- body: `<s>rohaRA<srs/>cala</s> ¦ <lex>m.</lex> <ab>id.</ab>, <ls>Sarvad.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L186003  k2=`vanAcArya`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-m
- body: `<s>vanA<srs/>cArya</s> ¦ <lex>m.</lex> <ab>N.</ab> of an author, <ls>Cat.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L237966  k2=`sarpa—PaRa—ja`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F09(editorial commentary) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F14(botanical name) F17(machine annotation)
- detected types: noun-m botanical lexicographer-only
- body: `<s>sarpa—PaRa—ja</s> ¦ <lex>m.</lex> ‘produced in a <ab n="snake">sn˚</ab>'s hood’, the <ab n="snake">sn˚</ab>-stone (a gem or pearl said to be found in a <ab n="snake">sn˚</ab>'s head and to resemble the berry of the <bot>Abrus Precatorius</bot>), <ls>L.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L245169  k2=`sImADipa`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-m
- body: `<s>sImA<srs/>˚Dipa</s> ¦ (<s>˚mA<srs/>D˚</s>), <lex>m.</lex> a frontier guardian, keeper of the borders, <ls>Pañcat.</ls><info lex="m"/>`
- FP: ___   FN: ___

### L253131  k2=`somApi`  e=3
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-m
- body: `<s>somA<srs/>pi</s> ¦ <lex>m.</lex> <ab>N.</ab> of a son of <s1>Sahadeva</s1>, <ls>Pur.</ls><info lex="m"/>`
- FP: ___   FN: ___


## noun-n

### L46254  k2=`kalmAzABiBava`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: noun-n lexicographer-only
- body: `<s>kalmAzA<srs/>BiBava</s> ¦ <lex>n.</lex> sour boiled rice, <ls>L.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L48083  k2=`kAma—deva—tva`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>kAma—deva—tva</s> ¦ <lex>n.</lex> the being the god of love, <ls>Kathās.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L53205  k2=`ku/lmala`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n vedic-accented
- body: `<s>ku/lmala</s> ¦ <lex>n.</lex> the part of an arrow or spear by which the head is attached to the shaft, <ls>MaitrS.</ls>; <ls>AV.</ls> (once <s>ku/rmala</s>), <ls>ŚBr. iii</ls><info lex="n"/>`
- FP: ___   FN: ___

### L53551  k2=`kuzmARqa`  e=1B
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>kuzmARqa</s> ¦ <lex>n.</lex> <ab>N.</ab> of the verses, <ls>VS. xx, 14 ff.</ls>; <ls>TĀr.</ls> (<s>kUSm˚</s>), <ls>MBh. xiii, 6236 ff.</ls> (<s>kUSm˚</s> <ab>ed.</ab> <ab>Bomb.</ab>)<info lex="n"/>`
- FP: ___   FN: ___

### L72374  k2=`a-carama—vayas`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>a-carama—vayas</s> ¦ <lex>n.</lex> youth, <ls>Uttarar. v, 12.</ls><info lex="n"/><listinfo n="sup"/>`
- FP: ___   FN: ___

### L115056  k2=`pati—vratA—tva`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>pati—vratA—tva</s> ¦ <lex>n.</lex> devotion or loyalty to a <ab n="husband">h˚</ab>, <ls>MBh.</ls>; <ls>R.</ls>; <ls>Kathās.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L116352  k2=`parAmfta`  e=3
- detected blocks: F01(record header) F03(homophone disambiguator) F04(grammatical category) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: noun-n lexicographer-only
- body: `<hom>1.</hom> <s>parA<srs/>mfta</s> ¦ <lex>n.</lex> (for <hom>2.</hom> See <pcol>p. 590, col. 2</pcol>) ‘the best nectar’, rain, <ls>L.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L122075  k2=`pAdodaka—tIrTa`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: noun-n
- body: `<s>pAdo<srs/>daka—tIrTa</s> ¦ <lex>n.</lex> <ab>N.</ab> of a <s1>Tīrtha</s1>, <ls>Cat.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L134852  k2=`pradyumnAstra`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>pradyumnA<srs/>stra</s> ¦ <lex>n.</lex> <s1 n="Pradyumna">P˚</s1>'s weapon, <ls>Kathās.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L144534.2  k2=`bAla—grahopaSamana`  e=4
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: noun-n
- body: `<s>bAla—gra˚ho<srs/>paSamana</s> ¦ <lex>n.</lex> <ab>N.</ab> of <ab>wk.</ab><info lex="n"/>`
- FP: ___   FN: ___

### L155569  k2=`madanAtapatra`  e=3
- detected blocks: F01(record header) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>madanA<srs/>tapatra</s> ¦ <lex>n.</lex> the vulva, <ls>Bhpr.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L237372.1  k2=`samyag—dfzwi—tva`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F17(machine annotation)
- detected types: noun-n
- body: `<s>samyag—dfzwi—tva</s> ¦ <lex>n.</lex><info phwparent="237372,samyagdfzwi"/><info lex="n"/>`
- FP: ___   FN: ___

### L238297  k2=`sarva—jYAtf—tva`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: noun-n
- body: `<s>sarva—jYAtf—tva</s> ¦ <lex>n.</lex> omniscience, <ls>Cat.</ls><info lex="n"/>`
- FP: ___   FN: ___


## other

### L7482  k2=`anu-zWA`  e=1
- detected blocks: F01(record header) F02(display headword) F06(etymology root marker) F08(inflection form) F10(sense gloss) F17(machine annotation)
- detected types: other
- body: `<s>anu-zWA</s> ¦ (√ <s>sTA</s>) to stand near or by;
<div n="to"/>to follow out;
<div n="to"/>to carry out, attend to;
<div n="to"/>to perform, do, practise;
<div n="to"/>to govern, rule, superintend;
<div n="to"/>to appoint:
<div n="vp"/><ab>Pass.</ab> <s>-zWIyate</s>, to be done;
<div n="to"/>to be followed out:
<div n="vp"/><ab>Desid.</ab> <s>-tizWAsati</s>, to be desirous of doing, &c.<info verb="pre" cp="" parse="anu+sTA"/><info hui="a"/>`
- FP: ___   FN: ___

### L16739  k2=`ali-garda`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F08(inflection form) F10(sense gloss)
- detected types: other
- body: `<s>ali-garda</s> and <s>-garDa</s>. ¦ See <hom>1.</hom> <s>ali</s>`
- FP: ___   FN: ___

### L17172  k2=`ava-Gaww`  e=1
- detected blocks: F01(record header) F02(display headword) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `<s>ava-√ Gaww</s> ¦ <ab>Caus.</ab> (<ab>p.</ab> <s>-Gawwayat</s>) to push away, push open, <ls>R. v, 15, 10</ls> (<ab>Gorresio</ab>);
<div n="to"/>to push together, rub, <ls>Suśr.</ls>;
<div n="to"/>to stir up, <ls>Car.</ls>; <ls>Suśr.</ls><info verb="pre" cp="" parse="ava+Gaww"/>`
- FP: ___   FN: ___

### L69168  k2=`glev`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F08(inflection form) F09(editorial commentary) F10(sense gloss) F16(cross-reference) F17(machine annotation)
- detected types: other
- body: `<s>glev</s> ¦ <ab>cl.</ab> 1. <ab>Ā.</ab> <s>˚vate</s>, to serve, worship, <ls n="Dhātup.">xiv, 32</ls> (<ab>cf.</ab> √ <s>gev</s>, <s>Kev</s>, <s>sev</s>.)<info verb="root" cp="1Ā"/>`
- FP: ___   FN: ___

### L76466  k2=`jaNgama`  e=1
- detected blocks: F01(record header) F02(display headword) F08(inflection form) F10(sense gloss) F17(machine annotation)
- detected types: other
- body: `<s>jaNgama</s> ¦ <s>˚mana</s>. See <s>jaga</s>.<info hui="b"/>`
- FP: ___   FN: ___

### L102726  k2=`naMSuka`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F04(grammatical category) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `<s>naMSuka</s> ¦ <lex>mf(<s>A</s>)n.</lex> (√ <hom>2.</hom> <s>naS</s>) perishing, <ls>Kāṭh.</ls><info lex="m:f#A:n"/>`
- FP: ___   FN: ___

### L114933.1  k2=`pattra—SAka—tfRa`  e=4
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `<s>pattra—SAka—tfRa</s> ¦ <lex>n. <ab>pl.</ab></lex> leaves, pot-herbs and grass, <ls>Mn. vii, 132.</ls><info lex="n"/>`
- FP: ___   FN: ___

### L116853  k2=`parA-tras`  e=1
- detected blocks: F01(record header) F02(display headword) F06(etymology root marker) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `<s>parA-√ tras</s> ¦ only <ab>Caus.</ab> <ab>aor.</ab> <s>parA<srs/>titrasat</s>, to drive away, <ls>AV.</ls><info verb="pre" cp="" parse="parA+tras"/>`
- FP: ___   FN: ___

### L131571  k2=`prati—pakzita`  e=4A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `¦ nullified by a contradictory premiss (one of the 5 kinds of fallacious middle terms), <ls>MW.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L134427  k2=`praty-upa-hve`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `<s>praty-upa-√ hve</s> ¦ <ab>Ā.</ab> <s>-havate</s>, to call, invite, <ls>Br.</ls><info verb="pre" cp="Ā" parse="prati+upa+hve"/>`
- FP: ___   FN: ___

### L177274  k2=`rAma`  e=1B
- detected blocks: F01(record header) F02(display headword) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `¦ of various authors and teachers (also with <s>AcArya</s>, <s>upA<srs/>DyAya</s>, <s>kavi</s>, <s>cakra-vartin</s>, <s>jyotir-vid</s>, <s>jyOtizaka</s>, <s>tarka-vAg-ISa</s>, <s>dIkzita</s>, <s>dEva-jYa</s>, <s>paRqita</s>, <s>Bawwa</s>, <s>BawwA<srs/>cArya</s>, <s>vAjapeyin</s>, <s>Sarman</s>, <s>SAstrin</s>, <s>saMyamin</s>, <s>sUri</s> &c.), <ls>Cat.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L233657  k2=`sam-aBi-pIq`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `<s>sam-aBi-√ pIq</s> ¦ <ab>P.</ab> <s>-pIqayati</s>, to squeeze together, crush, <ls>Hariv.</ls><info verb="pre" cp="P" parse="sam+aBi+pIq"/>`
- FP: ___   FN: ___

### L261362  k2=`hariRASva`  e=3A
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: other
- body: `¦ <ab>N.</ab> of a man, <ls>MBh.</ls><info lex="inh"/>`
- FP: ___   FN: ___


## root

### L7900  k2=`ant`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F08(inflection form) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F16(cross-reference) F17(machine annotation)
- detected types: root lexicographer-only
- body: `<s>ant</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <s>antati</s>, to bind, <ls>L.</ls> (<ab>cf.</ab> √ <s>and</s>, <s>Int</s>.)<info verb="genuineroot" cp="1P"/>`
- FP: ___   FN: ___

### L27851  k2=`As`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: root
- body: `<hom>2.</hom> <s>As</s> ¦ <ab>cl.</ab> 2. <ab>Ā.</ab> <s>A/ste</s> (and <s>A/sate</s>, <ls>AV. xi, 8, 32</ls>, &c.; <ab>Impv.</ab> 2. <ab>sg.</ab> <s>As-sva</s>, <s>Asva</s>, and <s>Asasva</s>; 2. <ab>pl.</ab> <s>ADvam</s>; <ab>p.</ab> <s>AsAna/</s>, <s>Asat</s> [<ls>R.</ls>], and <s>AsIna</s> [see below]; <s>AsAM-cakre</s> [<ls>Pāṇ. iii, 1, 87</ls>]; <s>Asizyate</s>; <s>Asizwa</s>; <s>Asitum</s>)
<div n="to"/>to sit, sit down, rest, lie, <ls>RV.</ls>; <ls>AV.</ls>; <ls>ŚBr.</ls>; <ls>Mn.</ls>; <ls>MBh.</ls>; <ls>Śak.</ls> &c.;
<div n="to"/>to be present;
<div n="to"/>to exist;
<div n="to"/>to inhabit, dwell in;
<div n="to"/>to make one's abode in <ls>RV.</ls>; <ls>AV.</ls>; <ls>VS.</ls>; <ls>MBh.</ls> &c.;
<div n="to"/>to sit quietly, abide, remain, continue, <ls>RV.</ls>; <ls>AV.</ls> &c.;
<div n="to"/>to cease, have an end, <ls>Pañcat.</ls>; <ls>Daś.</ls>; <ls>Hit.</ls> &c.;
<div n="to"/>to solemnize, celebrate;
<div n="to"/>to do anything without interruption;
<div n="to"/>to continue doing anything;
<div n="to"/>to continue in any situation;
<div n="to"/>to last;
<div n="vp"/> (it is used in the sense of ‘continuing’, with a participle, <ab>adj.</ab>, or <ab>subst.</ab>, <ab>e.g.</ab> <s>etat sAma gAyann Aste</s>, ‘he continues singing this verse’; with an indeclinable participle in <s>tvA</s>, <s>ya</s>, or <s>am</s>, <ab>e.g.</ab> <s>upa-ruDya arim AsIta</s>, ‘he should continue blockading the foe’; with an adverb, <ab>e.g.</ab> <s>tUzRIm Aste</s>, ‘he continues quiet’; <s>suKam Asva</s>, ‘continue well’; with an <ab>inst.</ab> case, <ab>e.g.</ab> <s>suKenA<srs/>ste</s>, ‘he continues well’; with a <ab>dat.</ab> case, <ab>e.g.</ab> <s>AstAM tuzwaye</s>, ‘may it be to your satisfaction’) :
<div n="vp"/><ab>Caus.</ab> <s>Asayati</s>, to cause any one to sit down <ab>Comm.</ab> on <ls>Pāṇ.</ls> :
<div n="vp"/><ab>Desid.</ab> <ab>Ā.</ab> <s>Asisizate</s>, <ls>ib.</ls>; <info whitneyroots="As,6"/><info verb="genuineroot" cp="2Ā"/>`
- FP: ___   FN: ___

### L37931  k2=`uh`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F08(inflection form) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F16(cross-reference) F17(machine annotation)
- detected types: root lexicographer-only
- body: `<s>uh</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <s>ohati</s>, <s>uvoha</s>, <s>OhIt</s>, &c., to give pain, hurt, kill, <ls>L.</ls> (<ab>cf.</ab> <hom>1.</hom> <s>Uh</s>.)<info verb="genuineroot" cp="1P"/>`
- FP: ___   FN: ___

### L53796  k2=`kUj`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: root
- body: `<s>kUj</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <s>kU/jati</s> (<ab>perf.</ab> <s>cukUja</s>, <ls>Kum. iii, 32</ls> &c.), to make any inarticulate or monotonous sound, utter a cry (as a bird), coo (as a pigeon), caw (as a crow), warble, moan, groan, utter any indistinct sound, <ls>AV. vii, 95, 2</ls>; <ls>MBh.</ls>; <ls>R.</ls> &c.;
<div n="vp"/> ‘to fill with monotonous sounds’, &c. See <s>kUjita</s>;
<div n="to"/>to blow or breathe (the flute), <ls>BhP. x, 21, 2.</ls><info whitneyroots="kUj,20"/><info verb="genuineroot" cp="1P"/>`
- FP: ___   FN: ___

### L69841  k2=`Guz`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: root
- body: `<hom>1.</hom> <s>Guz</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <s>Gozati</s> (rarely <ab>Ā.</ab> <s>˚te</s>, <ls>R. v, 56, 139</ls>; <ab>Subj.</ab> <s>Go/zAt</s>; <ab>pf.</ab> <s>juGoza</s>, <ls>JaimBr.</ls>; 3. <ab>pl.</ab> <s>juGuzur</s>, <ls>Pāṇ. vii, 2, 23</ls>, <ls>Kāś.</ls>; <ab>aor.</ab> <ab>Ā.</ab> <s>Go/zi</s>) <ab>Ā.</ab> to sound, <ls>RV. iv, 4, 8</ls>;
<div n="vp"/> <ab>P.</ab> to cry or proclaim aloud, call out, announce publicly, declare, <ls n="RV.">i, 139, 8</ls>; <ls>MBh. xiii</ls>, <ls n="MBh.">xiv</ls>; <ls>R.</ls> &c.:
<div n="vp"/><ab>Caus.</ab> <s>Gozayati</s> (<ab>subj.</ab> 2. <ab>sg.</ab> <s>˚za/yas</s>), to call to, invite, <ls>RV. ix, 108, 3</ls>;
<div n="to"/>to cause to proclaim aloud, <ls>MBh. i</ls>, <ls n="MBh.">iii</ls>;
<div n="to"/>to proclaim aloud, <ls>MBh.</ls>; <ls>R.</ls> &c.<info whitneyroots="Guz,42"/><info verb="genuineroot" cp="1P,1Ā"/>`
- FP: ___   FN: ___

### L86265  k2=`tuz`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: root
- body: `<s>tuz</s> ¦ <ab>cl.</ab> 4. <s>˚zyati</s> (metrically also <s>˚te</s>; <ab>fut.</ab> <s>tokzyati</s>, <s>tozwA</s>, and <ab>inf.</ab> <s>tozwum</s> [<ls>MBh. iv, 1562</ls>] <ls>Pāṇ. vii, 2, 10</ls>; <ls>Kār.</ls> [<ls>Siddh.</ls>]; <ab>aor.</ab> <s>atuzat</s>, <ls>Bhaṭṭ. xv, 8</ls>; <ab>pf.</ab> <s>tutoza</s>)
<div n="to"/>to become calm, be satisfied or pleased with any one (<ab>gen.</ab> <ab>dat.</ab> <ab>instr.</ab> <ab>loc.</ab>, or <ab>acc.</ab> with <s>prati</s>) or anything (<ab>instr.</ab>), <ls>ŚāṅkhŚr. i, 17, 5</ls>; <ls>MBh.</ls> &c.;
<div n="to"/>to satisfy, please, appease, gratify,<ls n="MBh.">i, 4198</ls> :
<div n="vp"/><ab>Caus.</ab> <s>tozayati</s> (or metrically <s>˚te</s>) <ab>id.</ab>, <ls>RV. x, 27, 16</ls> (<ab>p.</ab> <lex type="part">f.</lex> <s>tuza/yantI</s>), <ls>MBh.</ls> &c.;
<div n="vp"/> <ab>Desid.</ab> <s>tutukzati</s>, <ls>W.</ls> :
<div n="vp"/><ab>Intens.</ab> <s>totuzyate</s>, <s>totozwi</s>, <ls>W.</ls>;
<div n="vp"/> <ab>cf.</ab> <s>tUzRI/m</s>.<info whitneyroots="tuz,64"/><info verb="genuineroot" cp="4"/>`
- FP: ___   FN: ___

### L102824  k2=`nakz`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: root
- body: `<s>nakz</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <ab>Ā.</ab> <s>na/kzati</s>, <s>˚te</s> (<ab>perf.</ab> <s>nanakzu/r</s>, <s>˚kze/</s>, <ls>RV.</ls>; <ab>aor.</ab> <s>anakzIt</s> <ab>Gr.</ab>; <ab>fut.</ab> <s>nakzizyati</s>, <s>nakzitA</s>, <ls>ib.</ls>) to come near, approach, arrive at, get, attain, <ls>RV.</ls>; <ls>AV.</ls>; <ls>VS.</ls> (<ab>cf.</ab> <hom>1.</hom> <s>naS</s> <pb n="524,2"/>; <s>inakz</s>). <info whitneyroots="nakz,87"/><info verb="genuineroot" cp="1P,1Ā"/>`
- FP: ___   FN: ___

### L164311  k2=`miT`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: root
- body: `<s>miT</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <ab>Ā.</ab> (<ab>cf.</ab> <ls>Dhātup. xxi, 7</ls>) <s>me/Tati</s>, <s>˚te</s> (<ab>pr. p.</ab><lex type="part">f.</lex> <s>miTatI/</s>, <ls>RV.</ls>; <ab>pf.</ab> <s>mimeTa</s>, <ls>ib.</ls>; <ab>ind.p.</ab> <s>miTitvA</s>, <ls>BhP.</ls>),
<div n="to"/>to unite, pair, couple, meet (as friend or antagonist), alternate, engage in altercation;
<div n="to"/> (<ab>Ā.</ab>) to dash together, <ls>RV. i, 113, 3</ls> (<ab>accord.</ab> to <ls>Dhātup.</ls> also ‘to understand’ or ‘to kill’). <info westergaard="medf,21.7,01.0600;meDf,21.7,01.0601"/><info whitneyroots="miT,120"/><info verb="genuineroot" cp="1P,1Ā"/>`
- FP: ___   FN: ___

### L174870  k2=`raB`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F06(etymology root marker) F07(IE cognate) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: root etymological-ie
- body: `<s>raB</s> or <s>ramB</s> ¦ (mostly <ab>comp.</ab> with a <ab>prep.</ab>; <ab>cf.</ab> √ <s>graB</s> and See √ <s>laB</s> with which <s>raB</s> is connected) <ab>cl.</ab> 1. <ab>Ā.</ab> (<ls>Dhātup. xxiii, 5</ls>) <s>ra/Bate</s> (<ab>mc.</ab> also <s>˚ti</s> and <lang>ep.</lang> <s>ramBati</s>, <s>˚te</s>; <ab>pf.</ab> <s>reBe/</s>, <ls>RV.</ls>; also <s>rAraBe</s> and 1. <ab>pl.</ab> <s>raraBmA/</s>; <ab>aor.</ab> <s>a/rabDa</s>, <ls>RV.</ls>; <ab>fut.</ab> <s>rabDA</s> <ab>Gr.</ab>; <s>rapsyati</s>, <ls>MBh.</ls>; <s>˚te</s>, <ls>ib.</ls> &c.; <ab>inf.</ab> <s>rabDum</s>, <ls>MBh.</ls>; <lang>Ved.</lang> <s>ra/Bam</s>, <s>ra/Be</s>; <ab>ind.p.</ab> <s>ra/Bya</s>, <ls>RV.</ls> &c.),
<div n="to"/>to take hold of, grasp, clasp, embrace, <ls>BhP.</ls> (<s>araBat</s>, <ls>Hariv. 8106</ls> <ab>w.r.</ab> for <s>A<srs/>raBat</s>);
<div n="to"/>to desire vehemently, <ls>MW.</ls>;
<div n="to"/>to act rashly, <ls>ib.</ls> (<ab>cf.</ab> <s>raBas</s>, <s>raBasa</s>) :
<div n="vp"/><ab>Pass.</ab> <s>raByate</s> <ab>aor.</ab> <s>aramBi</s>, <ls>Pāṇ. vii, 1, 63</ls> :
<div n="vp"/><ab>Caus.</ab> <s>ramBayati</s>, <s>˚te</s> <ab>aor.</ab> <s>araramBat</s>, <ls>ib.</ls> :
<div n="vp"/><ab>Desid.</ab> <s>ripsate</s>, <ls>Pāṇ. vii, 4, 54</ls> :
<div n="vp"/><ab>Intens.</ab> <s>rAraByate</s>, <s>rAraBIti</s>, <s>rArabDi</s> (as far as these forms really occur, they are only found after prepositions; <ab>cf.</ab> <s>anv-A-</s>, <s>A-</s>, <s>prA<srs/>-</s>, <s>vy-A-</s>, <s>pari-</s>, <s>saM-raB</s> &c.)<info westergaard="raBa,23.5,01.0693"/><info whitneyroots="raB,136"/><info verb="genuineroot" cp="1Ā"/>`
- FP: ___   FN: ___

### L186291  k2=`vap`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: root
- body: `<hom>2.</hom> <s>vap</s> ¦ <ab>cl.</ab> 1. <ab>P.</ab> <ab>Ā.</ab> (<ls>Dhātup. xxiii, 34</ls>) <s>va/pati</s>, <s>˚te</s> (<ab>Pot.</ab> <s>upet</s>, <ls>GṛS.</ls>; <ab>pf.</ab> <s>uvApa</s>, <s>Upu/H</s>; <s>Upe</s>, <ls>RV.</ls> &c.; <s>vavApa</s>, <ls>MBh.</ls>; <s>-vepe</s>, <ls>Kāś.</ls> on <ls>Pāṇ. vi, 4, 120</ls>; <ab>aor.</ab> <s>avA<srs/>psIt</s>, <ls>Br.</ls> &c.;<s>avapta</s> <ab>Gr.</ab>; <ab>Pot.</ab> <s>upyAt</s>, <ls>ib.</ls>; <ab>fut.</ab> <s>vaptA</s>, <ls>ib.</ls>; <s>vapsya/ti</s>, <ls>Br.</ls>; <s>vapizyati</s>, <ls>MBh.</ls> &c.; <ab>inf.</ab> <s>vaptum</s> <ab>Gr.</ab>; <ab>ind.p.</ab> <s>uptvA</s>, <ls>MBh.</ls>; <s>-u/pya</s>, <ls>RV.</ls> &c.),
<div n="to"/>to strew, scatter (<ab>esp.</ab> seed), sow, bestrew, <ls>RV.</ls> &c. &c.;
<div n="to"/>to throw, cast (dice), <ls>ib.</ls>;
<div n="to"/>to procreate, beget (see <s>vapus</s> and <hom>2.</hom> <s>vaptf</s>);
<div n="to"/>to throw or heap up, dam up, <ls>AV.</ls> :
<div n="vp"/><ab>Pass.</ab> <s>upya/te</s> (<ab>aor.</ab> <s>vApi</s>, <ls>Br.</ls>), to be strewn or sown, <ls>RV.</ls> &c. &c.:
<div n="vp"/><ab>Caus.</ab> <s>vApayati</s> (<ab>aor.</ab> <s>avIvapat</s> <ab>Gr.</ab>) to sow, plant, put in the ground, <ls>MBh.</ls> :
<div n="vp"/><ab>Desid.</ab> <s>vivapsati</s>, <s>˚te</s> <ab>Gr.</ab>:
<div n="vp"/><ab>Intens.</ab> <s>vAvapyate</s>, <s>vAvapti</s>, <ls>ib.</ls><info westergaard="quvapa,23.34,01.0725"/><info whitneyroots="vap1,154"/><info verb="genuineroot" cp="1P,1Ā"/>`
- FP: ___   FN: ___

### L203453  k2=`vIj`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F06(etymology root marker) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: root
- body: `<s>vIj</s> ¦ (<ab>cf.</ab> √ <hom>1.</hom> <s>vij</s>) <ab>cl.</ab> 1. <ab>P.</ab> <ab>Ā.</ab> <s>vIjati</s>, <s>˚te</s> (<ab>pf.</ab> <s>vivyajuH</s>), to fan, cool by blowing upon or fanning, <ls>Hariv.</ls>;
<div n="to"/>to sprinkle with water, <ls>MBh.</ls> (according to <ls>Dhātup. vi, 25</ls> only <ab>Ā.</ab> ‘to go’) :
<div n="vp"/><ab>Caus.</ab> or <ab>cl.</ab> 10. (<ls>Dhātup. xxxv, 84</ls>), <s>vIjayati</s> (<ab>Pass.</ab> <s>vIjyate</s>), to fan, blow, kindle (fire), <ls>MBh.</ls>; <ls>R.</ls> &c.;
<div n="to"/>to stroke, caress, <ls>Suśr.</ls><info westergaard="vIja,6.25,01.0112"/><info whitneyroots="vIj,162"/><info verb="genuineroot" cp="1P,1Ā,10"/>`
- FP: ___   FN: ___

### L208354  k2=`vyac`  e=1
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F05(verb inflection class) F06(etymology root marker) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F16(cross-reference) F17(machine annotation)
- detected types: root
- body: `<hom>1.</hom> <s>vyac</s> ¦ (<ab>cf.</ab> √ <s>vic</s>; <ab>prob.</ab> <ab>orig.</ab> identical with <hom>2.</hom> <s>vy-√ ac</s>) <ab>cl.</ab> 6. <ab>P.</ab> (<ls>Dhātup. xxviii, 12</ls>) <s>vicati</s> (only in <ab>cl.</ab> 3. <ab>pr.</ab> <s>vivyakti</s>, 3. <ab>du.</ab> <s>vivikta/s</s>, <ab>Subj.</ab> <s>vivya/cat</s>, <ls>RV.</ls> <pb n="1029,2"/>; <ab>impf.</ab> <s>avivyak</s>, 3. <ab>pl.</ab> <s>avivyacus</s>, <ls>ib.</ls>; <ab>pf.</ab> <s>vivyAca</s>, 2. <ab>sg.</ab> <s>vivya/kTa</s>, <ls>ib.</ls>; <ls>Br.</ls>; <ab>Gr.</ab> also <ab>aor.</ab> <s>avyAcIt</s> or <s>avyacIt</s>; <ab>Prec.</ab> <s>vicyAt</s>; <ab>fut.</ab> <s>vyacitA</s>, <s>vicitA</s>; <s>vyacizyati</s>; <ab>inf.</ab> <s>vyacitum</s>; <ab>ind.p.</ab> <s>vicitvA</s>),
<div n="to"/>to encompass, embrace, comprehend, contain, <ls>RV.</ls>; <ls>AitBr.</ls>;
<div n="to"/> (<s>vicati</s>) to cheat, trick, deceive, <ls>Dhātup.</ls> :
<div n="vp"/><ab>Caus.</ab> <s>vyAcayati</s> (<ab>aor.</ab> <s>avivyacat</s>) <ab>Gr.</ab>:
<div n="vp"/><ab>Desid.</ab> <s>vivyacizati</s>, <ls>ib.</ls> :
<div n="vp"/><ab>Intens.</ab> <s>vevicyate</s>, <s>vAvyacIti</s>, <s>vAvyakti</s>, <ls>ib.</ls><info westergaard="vyaca,28.12,06.0015"/><info whitneyroots="vyac,166"/><info verb="genuineroot" cp="6P,3"/>`
- FP: ___   FN: ___

### L211426  k2=`SaNk`  e=1
- detected blocks: F01(record header) F02(display headword) F05(verb inflection class) F07(IE cognate) F08(inflection form) F09(editorial commentary) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: root etymological-ie
- body: `<s>SaNk</s> ¦ <ab>cl.</ab> 1. <ab>Ā.</ab> (<ls>Dhātup. iv, 12</ls>) <s>Sa/Nkate</s> (<lang>ep.</lang> also <ab>P.</ab>; <ab>aor.</ab> 2. <ab>sg.</ab> <s>aSaNkIs</s>, <s>aSaNkizwa</s>, <s>SaNkizWAs</s>, <s>SaNkiTAs</s>, <ls>MBh.</ls> &c. <ab>inf.</ab> <s>SaNkitum</s>, <ls>ib.</ls>; <ab>ind.p.</ab>; <s>-SaNkya</s>, <ls>ib.</ls>; <ab>Gr.</ab> also <ab>pf.</ab> <s>SaSaNke</s> <ab>fut.</ab> <s>SaNkitA</s>, <s>SaNkizyate</s>),
<div n="to"/>to be anxious or apprehensive, be afraid of (<ab>abl.</ab>), fear, dread, suspect, distrust (<ab>acc.</ab>), <ls>Br.</ls>; <ls>MBh.</ls>;
<div n="to"/>to be in doubt or uncertain about (<ab>acc.</ab>), hesitate, <ls>MBh.</ls>; <ls>Kāv.</ls> &c.;
<div n="to"/>to think probable, assume, believe, regard as (with two <ab>acc.</ab>), suppose to be (<s>SaNke</s>, ‘I think’, ‘I suppose’, ‘it seems to me’), <ls>ib.</ls>;
<div n="to"/> (in argumentative works) to ponder over or propound a doubt or objection:
<div n="vp"/><ab>Pass.</ab> <s>SaNkyate</s> (<ab>aor.</ab> <s>aSaNki</s>), to be feared or doubted &c.:
<div n="vp"/><ab>Caus.</ab> <s>SaNkayati</s>, to cause to fear or doubt, render anxious about (<ab>loc.</ab>), <ls>Mālav.</ls><info westergaard="Saki,4.12,01.0070"/><info whitneyroots="SaNk,170"/><info verb="genuineroot" cp="1Ā,1P"/>`
- FP: ___   FN: ___


## vedic-accented

### L8481  k2=`a/nna`  e=1B
- detected blocks: F01(record header) F09(editorial commentary) F10(sense gloss) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ food in a mystical sense (or the lowest form in which the supreme soul is manifested, the coarsest envelope of the Supreme Spirit)<info lex="inh"/>`
- FP: ___   FN: ___

### L18261  k2=`a/va-saBa`  e=1
- detected blocks: F01(record header) F02(display headword) F04(grammatical category) F08(inflection form) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: vedic-accented
- body: `<s>a/va-saBa</s> ¦ only in <lex>mf(<s>A</s>)n.</lex>, excluded from a (husband's) company [<ls>Sāy.</ls>], fallen into wrong (<ab>i.e.</ab> into men's) company [<ls>NBD.</ls>], <ls>ŚBr. iii, 1, 1, 21.</ls><info lex="m:f#A:n"/>`
- FP: ___   FN: ___

### L21117  k2=`a/sura`  e=1
- detected blocks: F01(record header) F02(display headword) F08(inflection form) F10(sense gloss) F17(machine annotation)
- detected types: vedic-accented
- body: `<s>a/sura</s> ¦ See <s>a/su</s>.<info hui="b"/>`
- FP: ___   FN: ___

### L21244  k2=`a/sta`  e=1B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ ‘end, death’, see <s>asta-samaya</s> below<info lex="inh"/>`
- FP: ___   FN: ___

### L39787  k2=`e/kAdaSa`  e=3
- detected blocks: F01(record header) F02(display headword) F03(homophone disambiguator) F08(inflection form) F10(sense gloss) F17(machine annotation)
- detected types: vedic-accented
- body: `<hom>2.</hom> <s>e/kAdaSa</s> ¦ (in <ab>comp.</ab> for <s>e/kAdaSan</s> below)<info lexcat="LEXID=card,STEM=ekAdaSan"/>`
- FP: ___   FN: ___

### L41534  k2=`ka/kzA`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ the periphery, circumference, <ls>Sūryas. xii, 65</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L57937  k2=`kravyA/d`  e=3B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F15(biographical content) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ <ab>N.</ab> of a <s1>Rakṣas</s1>, <ls>W.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L58359  k2=`krUra/`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ blood-shedding, slaughter, cruelty, any horrible deed, harshness, <ls>AV.</ls>; <ls>AitBr. i, 26</ls>; <ls>Mn. i, 29</ls> &c.<info lex="m"/>`
- FP: ___   FN: ___

### L98015  k2=`dro/Ra`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ of <ab>sev.</ab> other men, <ls>VP.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L119659  k2=`pary-anta/`  e=1B
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ extending in all directions, <ls>Hariv.</ls> (<ab>v.l.</ab> <s>pary-asta</s>). <info lex="inh"/>`
- FP: ___   FN: ___

### L139212  k2=`prA/k`  e=1C
- detected blocks: F01(record header) F02(display headword) F10(sense gloss) F12(source citation)
- detected types: vedic-accented
- body: `¦ <ab>w.r.</ab> for <s>drAk</s>, <ls>MBh.</ls>`
- FP: ___   FN: ___

### L149953  k2=`BA/rata`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F13(hedge marker (L.)) F17(machine annotation)
- detected types: vedic-accented lexicographer-only
- body: `¦ fire, <ls>L.</ls><info lex="inh"/>`
- FP: ___   FN: ___

### L180022  k2=`ro/ha`  e=1B
- detected blocks: F01(record header) F10(sense gloss) F12(source citation) F17(machine annotation)
- detected types: vedic-accented
- body: `¦ the increasing of a number from a smaller to a higher denomination, <ls>MW.</ls><info lex="inh"/>`
- FP: ___   FN: ___
