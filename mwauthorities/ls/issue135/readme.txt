MWS/mwauthorities/ls/issue135

Ref: https://github.com/sanskrit-lexicon/MWS/issues/135


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

Start with a copy of csl-orig/v02/mw/mw.txt at commit
  1d017dc7741f3a7ffd1009dd37685d8ed78ef123

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  1d017dc7:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135/
# -------------------------------------------------------------
# -------------------------------------------------------------
Start with a copy of mwauth/tooltip.txt in csl-pywork at commit
 9e82ed54f9c43429f43863dc60b6ed042e0c63d9
 
temp_tooltip_0.txt
cd /c/xampp/htdocs/cologne/csl-pywork

git show 9e82ed54f:v02/distinctfiles/mw/pywork/mwauth/tooltip.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135/temp_tooltip_0.txt

cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135/

---------------------------------------------------------------------
temp_abbrevlist_unknown_resolved.txt
Start with a copy of Andhrabharati's
 [abbrevlist_unknown_resolved.txt](https://github.com/sanskrit-lexicon/MWS/files/9164857/abbrevlist_unknown_resolved.txt)
  (See comment in #135).
 This is done manually:
 1) put the url above into address bar of browser,
 2) This generates a 'download' dialog, so a local copy is made.
 3) cp ~/Downloads/abbrevlist_unknown_resolved.txt temp_abbrevlist_unknown_resolved.txt
 
 3) move this local copy into this issue135 directory
 
*********************************************************************
BEGIN change_1
---------------------------------------------------------------------
temp_tooltip_1.txt
# merge the 'resolved' file last field into temp_tooltip_0.txt
python merge_resolved.py temp_tooltip_0.txt temp_abbrevlist_unknown_resolved.txt temp_tooltip_1.txt

---------------------------------------------------------------------
NOTES:
1. Restored [Cologne Addition] to tooltip text
---------------------------------------------------------------------
temp_tooltip_2.txt some editing
Possible print changes to mw.txt and tooltip.txt
1. AAnukr. -> AV.Anukr. (2 instances)
 old tip: AtharvavedaAnukramaṇikā [more properly AV.Anukr.] [Cologne Addition]
 new tip: Atharvaveda Anukramaṇikā [Cologne Addition]

2. 90.02	AitrAnukr.	Ātreya-śakhā kāṇḍānukramaṇikā [print correction as ĀtrAnukr.] [Cologne Addition]	Title (edit)
a. AitrAnukr. -> ĀtrAnukr. (1 instances)
b. Remove 90.02
  Note: 01:45	ĀtrAnukr.	Ātreya-anukramaṇikā	Title

3. Bhavab.
 old tip: Bhavabhūti [Cologne Addition]
 new tip: Bhavabhūti (in Uttararāmacaritam) [Cologne Addition]
4. Bhavabh.
 old tip: Bhavabhūti [Cologne Addition]
 new tip: Bhavabhūti (in Uttararāmacaritam) [Cologne Addition]
5. Burnell. -> Burnell  ( 0 instances)
6. Bālabodh.
 old tip: Bālabodhanī [cf. PWG] [Cologne Addition]
 new tip: Bālabodhanī [Cologne Addition]
7. Bṛ. -> ?
 old tip: (possibly) Śat. Br. [cf. PWG entry- nI.] [Cologne Addition]
 new tip: Śatapatha-brāhmaṇa ? [Cologne Addition]
8. Bṛhas. and Bṛhasp.
 old tip: Bṛhaspati (an ancient authourity, often quoted in Dharmaśāstra treatises) [Cologne Addition]
 new tip: Bṛhaspati (an ancient authority, often quoted in Dharmaśāstra treatises) [Cologne Addition]
9. Cār.
 old tip: (possibly) Caraka [The context indicates that a work related to some herb, so some medical treatise is intended.] [Cologne Addition]
 new tip: Work by Caraka ? [Cologne Addition]
10. Damayantīk.
 old tip: = tooltip 02:41 [Cologne Addition]
 new tip: Damayantī-kathā, Nalacampū [Cologne Addition]
11. DharmaP.
 old tip: = tooltip 02:45 [Cologne Addition]
 new tip: Dāyabhāga [Cologne Addition]
12. Div.
 old tip: Divyâvadāna [cf. pwkvn] [Cologne Addition]
 new tip: Divyâvadāna [Cologne Addition]
13. 90.29	Divyâs.	[print correction as Divyâv.] [cf. the MW entry maRqalavAwa] [Cologne Addition]	Title (edit)
a. Divyâs. -> Divyâv. (1 instances)
b. delete 90.29
  Note: 02:60	Divyâv.	Divyāvadāna	Title
  
14. Dāy.
 old tip: = tooltip 02:45 [Cologne Addition]
 new tip: Dāyabhāga [Cologne Addition]
15. HaṉsUp.
 old tip: Haṃsopaniṣad [the text needs a global replacement of ṉ > ṃ] [Cologne Addition]
 new tip: Haṃsopaniṣad [Cologne Addition]
16. 90.41	Jam.	Jaimini’s Mīmāṃsādarśana [print correction as Jaim.] [Cologne Addition]	Title (edit)
a. Jam. -> Jaim. (1 instances)
b. delete 90.41
  Note: 03:40	Jaim.	Jaimini	Author

17. 90.46	Kop.	Vopadeva [print correction as Vop.] [Cologne Addition]	Title (edit)
a. Kop. -> Vop. (1 instance)
b. delete 90.46
 Note: 10:31	Vop.	Vopadeva	Author

18. Kriṭṭanim.
 old tip: Kuṭṭanīmatam [print correction as Kuṭṭanīm.] [Cologne Addition]
 new tip: Kuṭṭanīmatam [Cologne Addition]
19. Kāp.
 old tip: Kapila’s Sāṅkhyasūtra [print correction as Kap.] [Cologne Addition]
 new tip: Kapila’s Sāṅkhyasūtra [Cologne Addition]
20. 90.53	Kāvy.	(possibly) Kāv. [Cologne Addition]	Title (edit)
a. Kāvy. -> Kāv. (1 instances)
b. delete 90.53
 Note: 04:26	Kāv.	Kāvya literature	Literary category
 
21. 90.55	Kṛṣṇakarṇ.	Kṛṣṇakarṇāmṛta [tooltip 04:36 has it as Kṛs2ṇakarṇ.!!] [Cologne Addition]
  a. Correct error in 04:36
  b. delete 90.55 
22. 90.61	Naith.	Naiṣadhīyacaritam [print correction as Naish. (MW) and then as Naiṣ. (CDSL)] [cf. pwkvn] [Cologne Addition]	Title (edit)
a. mw.txt change Naith. -> Naiṣ. (1 instances)
b. delete 90.61  (use 05:35 for Naiṣ.)
 05:35	Naiṣ.	Naiṣadha-carita	Title
 
23. 90.62	Nastar.	Hastaratnāvalī [print correction as Hastar.] [Cologne Addition]	Title (edit)
a. Nastar. -> Hastar. (1 instances)
b. delete 90.62
 Note: 11:26	Hastar.	Hasta-ratnāvalī [Cologne Addition]	Title
 
 old tip: Hastaratnāvalī [print correction as Hastar.] [Cologne Addition]
 new tip: Hastaratnāvalī [Cologne Addition]
 
24. 90.63	NādapUp.	Nādabindūpaniṣad [print correction as NādabUp.] [Cologne Addition]	Title (edit)
a. NādapUp. -> NādabUp. (1 instances)
b. delete 90.63
 Note: 05:31	NādabUp.	Nādabindu-upaniṣad	Title

25. 90.65	Paddh.	[typo error <ls>Parāś.</ls>; <ls>Paddh.</ls> for <ls>Parāś.<ab>Paddh.</ab></ls>] [Cologne Addition]	Title (edit)
a. correction to mw.txt under L>74809<pc>401,2<k1>cUrRakAra
    <ls>Parāś.</ls>; <ls>Paddh.</ls> ->
    <ls>Parāś.</ls> <ab>Paddh.</ab> (1 instances)
b. delete 90.65
26. 90.66	Pallcat.	[print correction as Pañcat.] [cf. PWG, Ind. Spr. (II) 4895] [Cologne Addition]	Title (edit)
a. correction to mw.txt Pallcat. -> Pañcat. (1 instances)
b. delete 90.66

27. Pariś. -> ĀśvGṛ.Pariś.
a. mw.txt corrections  (2 instances)
   <ls>ĀśvGṛ.</ls>; <ls>Pariś.</ls> -> <ls>ĀśvGṛ.Pariś.</ls>
b. 
 old tip: ĀśvalāyanaGṛhyasūtraPariśiṣṭa [typo error <ls>ĀśvGṛ.</ls>; <ls>Pariś.</ls> for <ls>ĀśvGṛ.Pariś.</ls>] [Cologne Addition]
 new tip: ĀśvalāyanaGṛhyasūtraPariśiṣṭa [Cologne Addition]

28. 90.69	Parvad.	Sarvadarśanasaṃgraha [print correction as Sarvad.] [cf. pwk] [Cologne Addition]	Title (edit)
a. mw.txt correction Parvad. -> Sarvad. (1 instances)
b. delete 90.69  in favor of
   08:14	Sarvad.	Sarvadarśana-saṃgraha	Title

29. 90.70	Pañcav.	[print correction as Pañcar.] [cf. pwk] [Cologne Addition]	Title (edit)
a. mw.txt correction Pañcav. -> Pañcar. (3 instances)
b. delete 90.70

30. 90.71	PhP.	BhāgavataPurāṇa [print correction as BhP.] [cf. PWG] [Cologne Addition]	Title (edit)
a. mw.txt PhP. -> BhP. (1 instances)
b. delete 90.71 in favor of
   01:55	BhP.	Bhāgavata-purāṇa	Title

31. 90.73	Prasamar.	[print correction as Prasannar.] [cf. pwk] [Cologne Addition]	Title (edit)
a. mw.txt Prasamar. -> Prasannar. (1 instances)
b. delete 90.73 in favor of
   06:31	Prasannar.	Prasannarāghava	Title

32. Praśnôt.
 old tip: Praśnottararatnamālā [cf. PWG and Ind. Strufen thereupon] [Cologne Addition]
 new tip: Praśnottararatnamālā [Cologne Addition]

33. 90.78	Pālār.	[print correction as (Pālār). for (<ls>Pālār.</ls>)] [Pālār is just the proper name of a river, not a lexical ref.] [cf. pwk] [Cologne Addition]	Title (edit)
a. mw.txt correction as indicated Pālār (1 instances)
b. delete 90.78

34. Pār.
A variant abbreviation for PārGṛ.
 old tip: [more properly Pār. Gṛhy.] [cf. pwk] [Cologne Addition]
 new tip: Pāraskara-gṛhya-sūtra [Cologne Addition]

35. Pārv.
 old tip: Pārvatīpariṇayanāṭakam [cf. pwkvn] [Cologne Addition]
 new tip: Pārvatīpariṇayanāṭakam [Cologne Addition]
36. 90.81	Rasav.	Rasaratnākara [print correction as Rasar.] [cf. pwk] [Cologne Addition]	Title (edit)
a. Rasav. -> Rasar. (mw.txt) (1 instances)
b. delete 90.81 in favor of
  07:10	Rasar.	Rasaratnākara	Title
37. 90.84	Rudraj.	Rudrayāmalatantra [print correction for Rudray.] [Cologne Addition]	Title (edit)
a. mw.txt correct Rudraj. -> Rudray. (2 instances)
b. Delete 90.84, in favor of
  07:21	Rudray.	Rudrayāmala	Title

38. Rājyat.
 old tip: (possibly) Rājat. [Cologne Addition]
 new tip: Rājataraṃgiṇī ? [Cologne Addition]
39. Saddh.
 old tip: SaddharmaPuṇḍarīka [more properly Saddh.P.] [Cologne Addition]
 new tip: SaddharmaPuṇḍarīka [Cologne Addition]

40. 90.89	SaṃjUp.	Saṃnyāsopaniṣad [print correction as Saṃny. Up] [cf. pwk] [Cologne Addition]	Title (edit)
a. SaṃjUp. -> SaṃnyUp. in mw.txt (1 instances)
b. change 11:40
   OLD 11:40	SaṃnyUp.	NONE	Title
   NEW 11:40	SaṃnyUp.	Saṃnyāsopaniṣad	Title
c. delete 90.89

41. 90.94	SāmarBr.	SāmavidhānaBrāhmaṇa [print correction for SāmavBr.] [cf. pwk] [Cologne Addition]	Title (edit)
a. SāmarBr. -> SāmavBr. (1 instances)
b. delete 90.94
 Note: 07:35	SāmavBr.	Sāma-vidhāna-brāhmaṇa	Title

42. Sāṃkhyas
 old tip: Sāṃkhyasūtra [<ls>Sāṃkhyas.</ls>, <ab>Sch.</ab> refres to Mahadeva's commentary and <ls>Sāṃkhyas. vi, 52, Anir.</ls> refers to Aniruddha's commentary] [Cologne Addition]
 new tip: Sāṃkhyasūtra [Cologne Addition
Also, change  (1 instances)
  old <ls>Sāṃkhyas. vi, 52, Anir.</ls>
  new <ls>Sāṃkhyas. vi, 52</ls>, <ls>Anir.</ls>
 and add ls: (DONE)
 Anir. Aniruddha, author of commentary on Sāṃkhyasūtra Author

43. Tantr. 
 old tip: Tantra literature (Literary category) [as each citation appears in a different work!!] [Cologne Addition]
 new tip: Tantra literature [Cologne Addition]

44. 91.01	VaṛB-S.	Varāhamihira's BṛhatSaṃhitā [print correction as VarBṛS.] [Cologne Addition]	Title (edit)
a. VaṛB-S. -> VarBṛS. in mw.txt (1 instances)
b. delete 91.01
   NOTE: 10:10	VarBṛS.	Varāha-mihira's Bṛhat-saṃhitā

45. 91.02	VB.	[print correction as VP.] [cf. pwk] [Cologne Addition]	Title (edit)
a. VB. -> VP. in mw.txt (1 instances)
b. delete 91.02.
   Note: 10:28	VP.	Viṣṇu-purāṇa

46. ŚB.
 old tip: (possibly) ŚBr. [Cologne Addition]
 new tip: Śatapatha-brāhmaṇa ? [Cologne Addition]

47. 91.17	ŚāṅgS.	[print correction as ŚārṅgS.] [Cologne Addition]	Title (edit)
a. mw.txt change ŚāṅgS. ->  ŚārṅgS. (1 instances)
b. delete 91.17
 Note: 08:13	ŚārṅgS.	Śārṅgadhara-saṃhitā

48. 91.18	Śāṅkh.	[print correction as ŚāṅkhBr.] [Cologne Addition]	Title (edit)
a. Śāṅkh. -> ŚāṅkhBr. in mw.txt (2 instances)
b. delete 91.18
 Note: 08:04	ŚāṅkhBr.	Śāṅkhāyana-brāhmaṇa

49. 92.02	Kāth.	(possibly) Kathāsartsāgara [print correction as Kath.] [Cologne Addition]	Title (edit)
a. Kāth. -> Kath. mw.txt (1 instances)
b. delete 92.02
 Note: 92.20	Kath.	Kathāsartsāgara [Cologne Addition]

50. ŚāntiP. 
 old tip: ŚāntiParva [more properly MBh. xii, 2638] [Cologne Addition]
 new tip: ŚāntiParva [Cologne Addition]
 Note: How to include 'MBh. xii, 2638' ?

51. Gop.
 old tip: Gopathabrāhmaṇa [more properly  GopBr.] [Cologne Addition]
 new tip: Gopathabrāhmaṇa [Cologne Addition]

52. 92.12	Mantram	Mantramahodadhi [print correction as Mantram.] [Cologne Addition]	Title (edit)
a. Mantram -> Mantram. in mw.txt  (1 instances)
b. delete 92.12
 Note: 05:16	Mantram.	Mantramahodadhi

53. 92.18	Krauñca-dvīpa	[<ls>Krauñca-dvīpa, ii, 4, 53</ls> print correction as <s1 slp1="krOYca-dvIpa">Krauñca-dvīpa</s1>, <ls n="VP.">ii, 4, 53</ls>] [Cologne Addition]	Title (edit)
a. mw.txt correction  (1 instances)
b. delete 92.18

54. 92.22	Bañc.	Pañcatantra [print correction as Pañc.] [Cologne Addition]	Title (edit)
a. Bañc. -> Pañc. in mw.txt
b. delete 92.22
 Note: 06:08x	Pañc.	Pañcatantra (1 instances)

55. Manu -> Manu.  (4 instances in mw.txt) (1 instances)
 old tip: Manusmṛti [print correction as Manu.] [Cologne Addition]
 new tip: Manusmṛti [Cologne Addition]

56. 92.25	Pur.	= tooltip 06:41 [Cologne Addition]	Title (edit)
 delete 92.25  (duplicate of 06:41)
 Note: 06:41	Pur.	Purāṇas	Literary category

57. 92.26	MWB.	= tooltip 05:26 [Cologne Addition]	Title (edit)
 delete 92.26  (duplicate of 05:26)
 Note: 05:26	MWB.	Monier-Williams' Buddhism in ...

58. Kaegi, Der Ṛgveda
 old tip: Adolf Kaegi, Der RigVeda: die älteste literature der Inder [there is another instance of Kaegi untagged] [Cologne Addition]
 new tip: Adolf Kaegi, Der RigVeda: die älteste literature der Inder [Cologne Addition]
Note: under <L>38960<pc>226,2<k1>
a. in mw.txt:  TODO <<<<
 old: Kaegi, <ls>RV.</ls> p. 53 f.
 new: <ls>Kaegi, RV. p. 53 f.</ls>
b. Add new tooltip entry:
 93.03a	Kaegi, RV.	Adolf Kaegi, Der RigVeda: die älteste literature der Inder [Cologne Addition]	Title (edit)

59. 93.05	Kielhorn, Mahābhāṣya	= tooltip 92.04 [Cologne Addition]	Title (edit)
a. delete 93.05  duplicate of 92.04

60. Ludwig, RV.
 old tip: Alfred Ludwig, Der RigVeda [there is another instance of Ludwig alone] [Cologne Addition]
 new tip: Alfred Ludwig, Der RigVeda [Cologne Addition]
Note: 12:39	Ludwig	Alfred Ludwig, Der Rigveda (1876)

61. Uttamac.²
 old tip: Uttamacaritra in about 700 verses [tooltip 09:42 has it as Uttamac.2; and there are another 6 tooltips having plain numbers instead of superscripts] [Cologne Addition]	
 new tip: Uttamacaritra in about 700 verses [Cologne Addition]
a. delete 09:42
  09:42	Uttamac.2	2 Uttamacaritra in about 700 verses	Title
b. ?? ' another 6 tooltips having plain numbers' ??

62. 93.11	R. (B)	Rāmāyaṇa (Bombay ed.) [Cologne Addition]	Title (edit)
a. R. (B) -> R. (B.) (1 instances)
b. delete 93.11
 Note: 93.10	R. (B.)	Rāmāyaṇa (Bombay ed.) [Cologne Addition]

63. 99.99	Unknown	Unknown reference [Cologne Addition]	Title
delete 99.99 (All of these now resolved)
 old tip: 
------------------------------------------------------------

python make_change_ls.py temp_mw_0.txt temp_change_1.txt
; manually edit and insert into change_1.txt
python updateByLine.py temp_mw_0.txt change_1.txt temp_mw_1.txt
42 change transactions from change_1.txt

python ls_unknown.py temp_mw_1.txt temp_tooltip_2.txt temp_ls_unknown.txt
879 tooltips from temp_tooltip_2.txt
0 with unknown ls abbreviation
0 cases written to temp_ls_unknown.txt

python lsextract_all.py temp_mw_1.txt temp_tooltip_2.txt temp_lsextract_all.txt
887 tooltips from temp_tooltip_2.txt

51 of the tooltips in temp_tooltip_2.txt have no instances.
These 51 lines from temp_lsextract_all.txt are copied to
tooltip_2_unused.txt.

---------------------------------------------------------------------------
temp_tooltip_3.txt
python remove_unused_tooltips.py temp_tooltip_2.txt tooltip_2_unused.txt temp_tooltip_3.txt
879 tooltips from temp_tooltip_2.txt
51 tooltip1 objects from tooltip_2_unused.txt
828 tips written to temp_tooltip_3.txt

Note: also remove the ' (edit)' at end of lines.
  This was added for temporary utility.

# rerun with temp_tooltip_3.txt
python ls_unknown.py temp_mw_1.txt temp_tooltip_3.txt temp_ls_unknown.txt
828 tooltips from temp_tooltip_3.txt
0 with unknown ls abbreviation

python lsextract_all.py temp_mw_1.txt temp_tooltip_3.txt temp_lsextract_all.txt
Note: no abbreviations have 0 count.
---------------------------------------------------------------------
TODO QUESTIONS
Pañcav. -> Pañcar.  could it be PañcavBr.	PañcaviṃśaBrāhmaṇa?
---------------------------------------------------------------------
temp_mw_1.txt
cp temp_mw_0.txt temp_mw_1.txt
touch change_1.txt

---------------------------------------------------------------------
# install temp_tooltip_3.txt
cp temp_tooltip_3.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt

---------------------------------------------------------------------------
install of temp_mw_1.txt to check xml
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135

---------------------------------------------------------------------------
# identify print changes in change_1.txt
print_change.txt  (also see 'print change' lines in change_1.txt.)
These also posted to csl-corrections/dictionaries/mw/mw_printchange.txt.

-------------------------------------------------------------------------
Push repositories to Github.
 csl-pywork  commit 8c29bcc080315e89ecf237ca0b82cb7123454412
 csl-orig  commit bca895c43b6c3c7bc461d17c674193150a1e1748
 csl-apidev  commit 913c93f4bc85e38171f6bf489bfcaea52a55e7e9
 csl-websanlexicon  commit 37109961bf3dee6128ee2c2fb25e0bf0f08939b9
 csl-corrections  commit c17958209d2492821e7bdbe252cf88503c585d0d
 mws 
and update the correspondents at Cologne web site.
DONE with this batch of corrections.

End change_1
*************************************************************************
