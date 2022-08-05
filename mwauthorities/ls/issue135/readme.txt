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
 new tip: DharmaPurāṇa [Cologne Addition]
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
a. in mw.txt: 
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
  PW confirms Pañcar. for vidAya.
  PWG confirms Pañcar. for viDAtrI (viDAtar)
  no confirmation yet for Pañcar. under vftti.
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
*********************************************************************
BEGIN change_2
cp temp_mw_1.txt temp_mw_2.txt
touch change_2.txt
cp temp_tooltip_3.txt temp_tooltip_4.txt

1a. <ls>Kath. mw.txt</ls> -> <ls>Kath.</ls>
1b. '1. <s>bandin</s>1' -> '<hom>1.</hom> <s>bandin</s>'
1c. <ls>MBh. xii,i 1220 -> <ls>MBh. xii, 11220</ls>

---------------------------------------------------------------------
20 cases of <ls>RTL.</ls> p.[0-9]+
python make_change_regex.py 1 temp_mw_2.txt temp_change_regex_1.txt
20 cases written to temp_change_regex_1.txt
# insert temp_change_regex_1.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
23 change transactions from change_2.txt


---------------------------------------------------------------------
939 cases of <ab>Vārtt.</ab> [0-9]+, to be linked appropriately to the resp. P. (Pāṇini) number-seq.

DEFER:

---------------------------------------------------------------------
#download ls.orphans-3.txt and copy to this issue135 directory
#cp ~/Downloads/ls.orphans-3.txt temp_ls.orphans-3.txt
python make_change_orphans.py temp_mw_2.txt temp_ls.orphans-3.txt temp_change_orphans_3.txt
10 changes found
# manual correct temp_change_orphans_3.txt  
# insert temp_change_orphans_3.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
33 change transactions from change_2.txt

---------------------------------------------------------------------
#download ls.orphans-2.txt and copy to this issue135 directory
#cp ~/downloads/ls.orphans-2.txt temp_ls.orphans-2.txt
python make_change_orphans.py temp_mw_2.txt temp_ls.orphans-2.txt temp_change_orphans_2.txt
15 changes written to temp_change_orphans_2.txt
# manual correct temp_change_orphans_2.txt 
# insert temp_change_orphans_2.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
48 change transactions from change_2.txt

---------------------------------------------------------------------
download ls.orphans-1.txt and copy to this issue135 directory
cp ~/downloads/ls.orphans-1.txt temp_ls.orphans-1.txt
python make_change_orphans.py temp_mw_2.txt temp_ls.orphans-1.txt temp_change_orphans_1.txt
96 cases
# manual correct temp_change_orphans_1.txt
# insert temp_change_orphans_1.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
138 change transactions from change_2.txt

# Note: checked xml validity of temp_mw_2.txt
# now check for unknown ls abbreviations
python ls_unknown.py temp_mw_2.txt temp_tooltip_4.txt temp_ls_unknown.txt

python ls_abnormal.py temp_mw_2.txt temp_tooltip_4.txt temp_abnormal.txt

Add tooltips:
---------------------------------------------------------------------------
04:58a	MBh. (ed. Bomb.)	Mahābhārata, Bombay edition	Title
  2 instances (so far)
     <L>26030<pc>149,3<k1>Ara
     <L>41764<pc>242,3<k1>kacCA
These 4 from Andhrabharati comment : 90.76, 90.87, 91.07, 92.15.

91.16 Śāntaś. Unknown reference [Cologne Addition] Title > Śāntiśataka [print correction as Śāntiś.] [Śāntiś. 3.8]
 a. change_2 
  ; <L>223754<pc>1102,3<k1>SreyorTin  print change
  ; Śāntaś. -> Śāntiś.
 b. delete 91.16 tooltip,
 c. mark printchange in csl-corrections

---- Tooltips for 14 'NONE' cases --------
11.39 Śūdradh. | NONE (Title) > Śūdradharma
11.37 Śaṃkaracetov. | NONE (Title) > Śaṅkaracetovilāsacampū
11.38 Śrāddhac. | NONE (Title) > Śrāddhacintāmaṇi
11.34 DrāhyŚr. | NONE (Title) > Drāhyāyana Śrautasūtra
11.35 Mit. | NONE (Title) > Mitākṣarā
11.36 Ratnak. | NONE (Title) > Ratnakoṣa
11.40 SaṃnyUp. | NONE (Title) > Saṃnyāsopaniṣad  (This one already found)
11.41 TAnukr. | NONE (Title) > TaittirīyaAnukramaṇikā
11.44 Udbh. | NONE (Author) > Udbhaṭa (Kāvyālaṅkārasārasaṅgraha)
11.47 Vākyap. | NONE (Title) > Vākyapadīya, a grammatical treatise (by Bhartṛhari)
11.48 Vaidyajīv. | NONE (Title) > Vaidyajīvana (of Lolimbarāja)
11.48x Vaidyaj. | NONE (Title) > Vaidyajīvana (of Lolimbarāja)
12.47 Vaidyakaparibh. | NONE (Title) > Vaidyakaparibhāṣā
11.50 Vidvanm. | NONE (Title) > Vidvanmodataraṅgiṇī

---------------------------------------------------------------------------
' Jain\b' -> ' <ns>Jain</ns>'
python make_change_regex.py 1a temp_mw_2.txt temp_change_regex_1a.txt
78 cases written to temp_change_regex_1a.txt
# insert temp_change_regex_1a.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
217 change transactions from change_2.txt
---------------------------------------------------------------------------
3 misc changes
1. 164391): 'V' (u+0056), mentioned as a symbol, could be changed to a true symbol like character
 '⋎' (u+22CE), Curly Logical Or   or at least as  << USED THIS
 '⋁' (u+22C1). N-Ary Logical Or
 
2. (41998): (a Lyrae) to be changed as (<lang n="greek">α</lang> Lyræ)
  Did not change 'ae' to 'æ'
3. (706145): <ls>Ked.</ls>N. to be changed as <ls>Ked.</ls>; <ab>N.</ab>
;[should this portion be split into a separate line from here??]
 YES! should be two entries
 See temp_mw_3.txt (far) below)
  Must do this separately since this will change number of lines in mw.txt.
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
220 change transactions from change_2.txt

---------------------------------------------------------------------------
Cap.letter.ls.related.txt 
cp ~/Downloads/Cap.letter.ls.related.txt temp_Cap.letter.ls.related.txt
python make_change_3tab.py temp_mw_2.txt temp_Cap.letter.ls.related.txt temp_change_cap_ls.txt

NOTE: 433344 not found
(433344):	W	<ls>W.</ls> ;[Wilson's Dictionary]
 line 433344 is <L>128651<pc>646,3<k1>pfTuka<k2>pf/Tuka<e>2.
# manually review/change temp_change_cap_ls.txt
# insert temp_change_cap_ls.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
291 change transactions from change_2.txt


NEW tooltips added:
93.30 Śukasaṃdeśa  
    <L>23448<pc>135,1<k1>Atara
93.31 Boehtlingk's edition  Pāṇini's grammatik by Otto von Böhtlingk  
    <L>24702<pc>141,3<k1>AntarIpaka
93.32 AgniP.  == AgP.
    <L>26660<pc>153,1<k1>Arhata
93.33 Hariv. (Langlois' transl.) "Harivansa, ou Histoire de la Famille de Hari by S. A. Langlois, 1834"
   <L>37337<pc>218,1<k1>urubindu
93.34 R. ed. Bombay
   <L>39701<pc>229,3<k1>ekasAla
93.35 BhP. (ed. Burnouf) Bhāgavata-purāṇa, by Eugène Burnouf, 1844
   <L>42176<pc>244,2<k1>kawvANga
93.36 Garga  cf.  90.32 Garg.  "Garga, the composer of Gargasaṃhitā"
   <L>87719<pc>458,2<k1>triRavAtmaka
   
10:34 W.  change tooltip to mention Wilson's dictionary
    "Horace H. Wilson, author of first Sanskrit-English dictionary in 1819"
93.37 Pañc. [B.]  same as Pañc. B.  (Bombay edition)
93.38 BhP. (B.)  Is this Bombay or Burnouf?  I guess Burnouff
93.39  Hunter's Gazetteer "The Imperial Gazetteer of India, by William Wilson Hunter, 1869-1881"
   <L>206288<pc>1018,3<k1>velAkUla
93.40 Almagest "astronomical manual written about 150 CE by Ptolemy"
   <L>244633<pc>1216,2<k1>sidDAntasAra
   
new abbreviation:
 <ab n="Bombay and Calcutta editions">BC</ab>  
 
jim changes to coding (see change_2)
 <L>32530<pc>185,2<k1>udArAkza
 <L>33692<pc>192,2<k1>udvf  '<ab>ed.</ab> Bombay' non-specific.
 <L>34674<pc>199,1<k1>upadAtf  also ed Bombay
 <L>34429.1<pc>1322,1<k1>upacaturam   <ab>Sch.</ab> not in ls
 <L>39454<pc>228,3<k1>ekapuzkala ed bombay
 <L>39916<pc>230,3<k1>ekAhArya Bombay
 <L>44643<pc>256,1<k1>karkAkza Bombay
 <L>76051<pc>407,1<k1>Cedya  (<ab>C.</ab>)
 <L>77184<pc>412,1<k1>jabDf Sch.
---------------------------------------------------------------------------
===========================================================================
---------------------------------------------------------------------------
Cap.letter.ls.miscellaneous
cp ~/Downloads/Cap.letter.miscellaneous.txt temp_Cap.letter.miscellaneous.txt
Edit temp_Cap.letter.miscellaneous.txt

remove :
(9544):	Anise	<bot>Anise</bot>  not a scientific name
(9553):	Anise	<bot>Anise</bot>  not a scientific name
(250381):	S.E.	<ab>S.E.</ab>   duplicate

2nd item in line removed for convenience.  more than one change made.
DONE (94497):	bened.	<ab>bened.</ab>  <ab n="benedictive">bened.</ab>
??   (255424):	<s>°lakāyana</s> <ab n="Boehtlingk text of Pravarādhyāya (?)">B</ab>	<s>°lakāyana</s> <ab>B</ab> ;[Bharadvāja gotra??]
DONE (269533):	<etym>gIvas</etym>	<etym>gīvas</etym>
DONE (293684):	V.	<ab n="Vaiśampāyana">V.</ab> ;[2 instances]
DONE (305762):	Vaiśeṣika	<s1>Vaiśeṣika</s1>
DONE (312402):	S.W.	<ab>S.W.</ab>
DONE (312402):	N.E.	<ab>N.E.</ab>

python make_change_3tab.py temp_mw_2.txt temp_Cap.letter.miscellaneous.txt temp_change_cap_misc.txt
150 changes written to temp_change_cap_misc.txt
# manual examination of temp_change_cap_misc.txt
Notes:
1. on s1 tag:  <s1 slp1="jEna">Jaina</s1>
2. 72 matches in 71 lines for "<ns>Sanskṛt</ns>"
 <ns>Sanskrit</ns> -> <ns>Sanskṛt</ns>  (3 instances)
3. <s1>Kalkia</s1> -> <ns>Kalkia</ns> <L>20084.1<pc>1318,1<k1>aSvAvatAr.
  Assuming 'Kalkia' is not a Sanskrit word.
4. Aethiops Mineralis: a homeopathic substance, not a plant. <L>41822<pc>243,1<k1>kajjalI
5. <ns>Pindur</ns> <L>44882<pc>257,1<k1>karRaprayAga
6. <L>75248<pc>403,2<k1>cOli  B and V are quite speculative
255424 new <s>cOli</s> ¦ <lex>m.</lex> = <s>cOqi</s>, <ls n="Pravar.">vi, 1</ls> (<s>°lakAyana</s> <ab n="Boehtlingk text of Pravarādhyāya OR Bharadvāja gotra? ">B</ab>, <s>°lika</s> <ab n="Viśvāmitra gotra ?">V</ab>). <info lex="m"/>

Also (B) in previous entry currently is <ab>B</ab> (tooltip=Bombay edition)
 <L>75247<pc>403,2<k1>cOlakAyana
7. <bio>Os Sepiae</bio>  Cuttlefish bone. This is not an animal. Should it
  be marked with <bio> tag?  Not sure.
8. 305762 no change: keep the brackets around [Purva-]
python make_change_3tab.py temp_mw_2.txt temp_Cap.letter.miscellaneous.txt temp_change_cap_misc.txt
9. Br°āhman -> <s1 slp1="brahman">Br°ahman</s1>
10. <ab>Gaelic</ab>  NOT an abbreviation. no change <L>204858.1<pc>1332,2<k1>vfz
11. Vaidic -> Vedic  (not <ns>Vedic</ns>) print change.

# insert temp_change_cap_misc.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
438 change transactions from change_2.txt

# -------------------------------------------------------------
edit /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt
at commit  8c29bcc080315e89ecf237ca0b82cb7123454412
 


additional abbreviations added to mwab_input.txt
 N.W., S.E., S.W., N.E., S. (south), Up.
---------------------------------------------------------------------------
<L>248403<pc>1231,2<k1>sumuKa  Par. -> Pur.  print change.
from temp_tooltip_4.txt, remove
90.67	Par.	Unknown reference [Cologne Addition]	Title

---------------------------------------------------------------------------
small.letters.ls.and.misc
cp ~/Downloads/small.letters.ls.and.misc.txt temp_small.letters.txt
python make_change_3tab.py temp_mw_2.txt temp_small.letters.txt temp_change_small.txt
44 records read from temp_small.letters.txt
44 found in init_cases
44 changes written to temp_change_small.txt
# manually adjust temp_change_small.txt
# insert temp_change_small.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
481 change transactions from change_2.txt

Add abbreviations to mwab_input
pref.	<id>pref.</id> <disp>preface</disp>
introd.	<id>introd.</id> <disp>Introduction</disp>
imp.	<id>imp.</id> <disp>imperative</disp> <INFER/>
quot.	<id>quot.</id> <disp>quotation</disp>

---------------------------------------------------------------------------
untagged.or.new.abbr.s.txt 
cp ~/Downloads/untagged.or.new.abbr.s.txt temp_untagged.or.new.abbr.s.txt
cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt temp_mwab_input.txt
python make_change_abbrev.py temp_mw_2.txt temp_untagged.or.new.abbr.s.txt temp_mwab_input.txt temp_change_abbrev.txt
# manual adjust temp_change_abbrev.txt
# insert temp_change_abbrev.txt into change_2
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
827 change transactions from change_2.txt

Abbreviations added to mwab
Mr.	<id>Mr.</id> <disp>Mister</disp>
St.	<id>St.</id> <disp>Saint</disp>
absol.	<id>absol.</id> <disp>absolutive</disp>
act.	<id>act.</id> <disp>active</disp>
astr.	<id>astr.</id> <disp>astronomy</disp>
caus.	<id>caus.</id> <disp>causal</disp>
chs.	<id>chs.</id> <disp>chapters</disp>
col.	<id>col.</id> <disp>column</disp>
coll.	<id>coll.</id> <disp>collectively</disp>
comps.	<id>comps.</id> <disp>compounds</disp>
contr.	<id>contr.</id> <disp>contraction</disp>
corr.	<id>corr.</id> <disp>corrected ?</disp>
correl.	<id>correl.</id> <disp>correlative</disp>
deriv.	<id>deriv.</id> <disp>derived</disp>
etc.	<id>etc.</id> <disp>et cetera, and so on</disp>
etymol.	<id>etymol.</id> <disp>etymology</disp>
exc.	<id>exc.</id> <disp>except</disp>
gr.	<id>gr.</id> <disp>grammar</disp>
gramm.	<id>gramm.</id> <disp>grammar</disp>
interrog.	<id>interrog.</id> <disp>interrogative</disp>
lang.	<id>lang.</id> <disp>language</disp>
latit.	<id>latit.</id> <disp>latitude</disp>
lbs.	<id>lbs.</id> <disp>pounds</disp>
metaph.	<id>metaph.</id> <disp>metaphorically</disp>
metr.	<id>metr.</id> <disp>metronymic</disp>
mus.	<id>mus.</id> <disp>music</disp>
mythol.	<id>mythol.</id> <disp>mythology</disp>
necess.	<id>necess.</id> <disp>necessitative</disp>
neut.	<id>neut.</id> <disp>neuter</disp>
nomin.	<id>nomin.</id> <disp>nominative</disp>
num.	<id>num.</id> <disp>number</disp>
obl.	<id>obl.</id> <disp>oblique</disp>
onom.	<id>onom.</id> <disp>onomatopoetic</disp>
onomatop.	<id>onomatop.</id> <disp>onomatopoetic</disp>
ozs.	<id>ozs.</id> <disp>ounces</disp>
patron.	<id>patron.</id> <disp>patronymic</disp>
philos.	<id>philos.</id> <disp>philosophy</disp>
plur.	<id>plur.</id> <disp>plural</disp>
polit.	<id>polit.</id> <disp>politics</disp>
prop.	<id>prop.</id> <disp>?</disp>
pros.	<id>pros.</id> <disp>prosody</disp>
rel.	<id>rel.</id> <disp>relative</disp>
relat.	<id>relat.</id> <disp>relative</disp>
relig.	<id>relig.</id> <disp>religion</disp>
rhetor.	<id>rhetor.</id> <disp>rhetoric, rhetorical</disp>
sacrif.	<id>sacrif.</id> <disp>sacrificial</disp>
interr.	<id>interr.</id> <disp>interrogative</disp>


cp /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt temp_mwab_input_1.txt



---------------------------------------------------------------------------
interr. <ab>interr.</ab>
python make_change_regex.py 1b temp_mw_2.txt temp_change_regex_1b.txt
5 cases written to temp_change_regex_1b.txt
# insert temp_change_regex_1b.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
832 change transactions from change_2.txt

---------------------------------------------------------------------------
 missing space between numbers in ls 
python make_change_regex.py 1c temp_mw_2.txt temp_change_regex_1c.txt
12 cases written to temp_change_regex_1c.txt
# plus one additional not caught by regex
# insert temp_change_regex_1c.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
845 change transactions from change_2.txt

Ramayana links are not working in mw.txt(examples in regex_1c changes)
basicadjust.php
Always use Goressio version for link target. Bombay versions not linked.
 asaMkalpa  <ls>R. i, 67, 15. not working

--------------------------------------------------------------------------
1. Kath. Kathāsartsāgara -> Kathāsaritsāgara corrected in mwauth/tooltip.txt
2.
; <L>22121<pc>127,1<k1>AkASajananI
79462 old <s>A-kASa/—jananI</s> ¦ <lex>f.</lex> a loophole, casement, embrasure, <ls>ŚāntiP. 2638</ls><info lex="f"/>
79462 new <s>A-kASa/—jananI</s> ¦ <lex>f.</lex> a loophole, casement, embrasure, <ls>ŚāntiP.</ls> <ls n="MBh. xii,">2638</ls><info lex="f"/>
tooltip
old
92.03	ŚāntiP.	ŚāntiParva [Cologne Addition]	Title
new
92.03	ŚāntiP.	ŚāntiParva (Mahābhārata, section xii) [Cologne Addition]	Title

NOTE: The MBh link at AkAsajananI now works.  Revised basicadjust.php
Cologne 'Mbh.' link target is the Calcutta edition?

------------------------------------------------------------
This should be Nidānasūtra, Weber's Transcript (https://www.worldcat.org/title/anupadasutram-nidanasutra/oclc/62126850), quoted in various issues of Indische Studien.
92.10	Nidān.	 Nidānasūtra, edition by Albrecht Weber (quoted in various issues of Indische Studien) [Cologne Addition]	Title
------------------------------------------------------------
Restore tooltip:
01:49	Bādar., Sch.	Śaṃkara's Śārīraka-mīmāṃsā on Bādarāyaṇa's Brahma-sūtras	Title
46 instances of <ls>Bādar.</ls> <ab>Sch.</ab>
'<ls>Bādar.</ls>,? <ab>Sch.</ab>' -> <ls>Bādar., Sch.</ls>
Tooltip:
Bādar., Sch. 
python make_change_regex.py 1d temp_mw_2.txt temp_change_regex_1d.txt
47 cases written to temp_change_regex_1d.txt
# insert temp_change_regex_1d.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
893 change transactions from change_2.txt
------------------------------------------------------------
00000 03:22 :: HaṃsUp. :: Haṃsa-upaniṣad :: Title
restore 03:22 tooltip
remove 90.38 tooltip 90.38	HaṉsUp.	Haṃsopaniṣad [Cologne Addition]	Title
# HaṉsUp -> HaṃsUp
python make_change_regex.py 1e temp_mw_2.txt temp_change_regex_1e.txt
4 cases written to temp_change_regex_1e.txt
# insert temp_change_regex_1e.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
897 change transactions from change_2.txt

------------------------------------------------------------
curl https://sanskrit-lexicon.uni-koeln.de/mwupdate/monier_dump_20071130.zip -o monier_dump_20071130.zip
unzip monier_dump_20071130.zip
 mv monier_dump_20071130.zip temp_monier_dump_20071130.zip
 mv monier_dump_20071130.txt temp_monier_dump_20071130.txt



------------------------------------------------------------
Kāraṇḍ.2.
1 match for "<ls>Ka1ran2d2\._2" in buffer: temp_monier_dump_20071130.txt
# add to change_2:
<L>79366<pc>421,2<k1>jinaSrI
268635 old <s>jina—SrI</s> ¦ <lex>m.</lex> <ab>N.</ab> of a king, <ls>Kāraṇḍ. 2</ls><info lex="m"/>
268635 new <s>jina—SrI</s> ¦ <lex>m.</lex> <ab>N.</ab> of a king, <ls>Kāraṇḍ.²</ls><info lex="m"/>

python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt

in temp_tooltip_4.txt,
restore 
04:03 :: Kāraṇḍ.2. :: metrical recension of the text Kāraṇḍa-vyūha :: Title
as 
04:03 :: Kāraṇḍ.² :: metrical recension of the text Kāraṇḍa-vyūha :: Title

------------------------------------------------------------
00000	01:12 :: Alaṃkāras.2 :: 2 Alaṃkārasarvasva, by Maṅkhaka :: Title
no changes warranted.

10 matches for "¯Alam2ka1ras" in buffer: MONIER.ALL.txt
print examined, no superscript found. marked as NONE FOUND in tooltip_2_unused.txt
 133876:.; N. of the author of a ¯Comm. on ¯Alam2ka1ras. , Prata1par. ¯Sch.
 142314:.{cauryasurata}3{caurya--surata} ·n. »= %{-rata} ¯Alam2ka1ras.
 143952:.; opposed to %{lATA7n°}) , Prata1par. ¯Alam2ka1ras3. x , 5/6.
 143996:.; ·n. a citron ¯Alam2ka1ras3. xiv , 2 ; 35 ; 47. _
 182916:.; %{°kIya} ·Nom. ·P. %{°yati} , ¸to become twice as thin ¯Alam2ka1ras3.
 284777:.{marujuS}3{maru4--juS} ·m. the inhabitant of a desert ¯Alam2ka1ras.
 328747:(·i.e. to be quite valueless) ¯Alam2ka1ras. _
 374704:.{vyAnamra}2{vy-Anamra} ·mfn. bowed or bent down ¯Alam2ka1ras.
 377395:opp. to %{lakSya} and %{vyaGgya}) ¯Alam2ka1ras3.
 468105:.{hATakIya}2{hATakIya} ·mfn. made or consisting of gold ¯Alam2ka1ras3. _

------------------------------------------------------------
<<<<< start here
00000	06:05 :: Pañcad.2. :: Pañcadaṇḍacchattra-prabandha, metrical recension :: Title
193 matches for "<ls>Pan5cad.</ls>" in buffer: temp_monier_dump_20071130.txt
31 matches for "<ls>Pan5cad\.[^<]" in buffer: temp_monier_dump_20071130.txt
None of these are followed by '_2'
no changes made. 
----------------------------------------------------------
00000	08:11 :: Sarasv.2. :: Sarasvatī-kaṇṭhābharaṇa, by Kṣemendra :: Title
23 matches for "Sarasv\." in buffer: MONIER.ALL.txt
None followed by a 2.
No changes made
------------------------------------------------------------
00000	08:30 :: Siṃhās.2. :: Siṃhāsana-dvātriṃśikā, metrical recension of the Ind. Off., E.I.H.2897 :: Title
00000	08:31 :: Siṃhās.3. :: Siṃhāsana-dvātriṃśikā, recension of E.I.H.2523 :: Title

481 matches for "<ls>Siṉhâs." in buffer: temp_mw_2.txt
# <ls>Siṉhâs. -> <ls>Siṃhās.
python make_change_regex.py 1f temp_mw_2.txt temp_change_regex_1f.txt
481 cases written to temp_change_regex_1f.txt
# insert temp_change_regex_1f.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1379 change transactions from change_2.txt

# <ls n="Siṉhâs." -> <ls n="Siṃhās."
python make_change_regex.py 1g temp_mw_2.txt temp_change_regex_1g.txt
4 cases written to temp_change_regex_1g.txt
# insert temp_change_regex_1g.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1383 change transactions from change_2.txt

No more 'Siṉhâs' in mw.txt.

Change temp_tooltip_4.txt
08:29 Siṉhâs. -> 08:29 Siṃhās.

By temp_monier_dump_20071130.txt, there is
one superscript 2 and one superscript 3
make changes in change_2.txt
<L>72878<pc>392,3<k1>cAtuzprAharika
  <ls>Siṃhās. 3 i, 59</ls> -> <ls>Siṃhās.³ i, 59</ls>
<L>76325<pc>408,2<k1>jagadISitf
; Siṃhās. 2 -> Siṃhās.²
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1385 change transactions from change_2.txt

Reinsert into temp_tooltip_4.txt
 (using superscript character)
08:30 :: Siṃhās.² :: Siṃhāsana-dvātriṃśikā, metrical recension of the Ind. Off., E.I.H.2897 :: Title
08:31 :: Siṃhās.³ :: Siṃhāsana-dvātriṃśikā, recension of E.I.H.2523 :: Title

------------------------------------------------------------
02:41 :: Damayantī-kathā. :: Nalacampū :: Title
1 match for "Damayantī-k" in buffer: temp_mw_2.txt
<L>104400<pc>530,2<k1>nalacampU
  <s1 slp1="damayantI-kaTA">Damayantī-kathā</s1>. -> <ls>Damayantī-kathā</ls>.
  
restore 02:41 in temp_tooltip_4.txt as
02:41	Damayantī-kathā	A poem, also called Nalacampū	Title

------------------------------------------------------------
00000	04:31 :: Khaṇḍapr. :: Khaṇḍapraśasti :: Title
0 matches for "Khaṇḍap"
2 matches for "Khaṇḍa-praśasti" in buffer: temp_mw_2.txt
#  <s1 slp1="KaRqa-praSasti">Khaṇḍa-praśasti</s1>  ->
#  <ls>Khaṇḍa-praśasti</ls>
python make_change_regex.py 1h temp_mw_2.txt temp_change_regex_1h.txt
2 cases written to temp_change_regex_1h.txt
# insert temp_change_regex_1h.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1388 change transactions from change_2.txt

in temp_tooltip_4.txt, add 
93.41 :: Khaṇḍa-praśasti :: Khaṇḍapraśasti, name of a poem attributed to Hanūmat [Cologne Addition] :: Title
------------------------------------------------------------
00000	04:59 :: MāghaMāh. :: Māgha-māhātmya in the Padma-purāṇa :: subtitle
2 matches for "Māghamāhātmya" in buffer: temp_mw_2.txt
#  <s1 slp1="mAGamAhAtmya">Māghamāhātmya</s1>
#  <ls>Māghamāhātmya</ls>
python make_change_regex.py 1i temp_mw_2.txt temp_change_regex_1i.txt
2 cases written to temp_change_regex_1i.txt
# insert temp_change_regex_1i.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1390 change transactions from change_2.txt

add to temp_tooltip_4.txt
93.42 :: Māghamāhātmya :: name of a chapter in the Padma-purāṇa [Cologne Addition] :: subtitle

------------------------------------------------------------
00000	04:61 :: MahānārāyaṇaUp.. :: Mahānārāyaṇa-upaniṣad see Nārāyaṇa-upaniṣad :: Title
None found but 2 instances of MahānārUp.
05:44x	MahānārUp.	Nārāyaṇa-upaniṣad	Title
No changes
------------------------------------------------------------
00000	05:48 :: Nid,Sch.. :: Nidāna,Sch.i.e.Vācaspati's Comm. :: Title
4 matches for "<ls>Nid.</ls> <ab>Sch.</ab>" in buffer: temp_mw_2.txt
#  <ls>Nid.</ls> <ab>Sch.</ab>
#  <ls>Nid., Sch.</ls>
python make_change_regex.py 1j temp_mw_2.txt temp_change_regex_1j.txt
4 cases written to temp_change_regex_1j.txt
# insert temp_change_regex_1j.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1394 change transactions from change_2.txt

add to temp_tooltip_4.txt
05:48 :: Nid., Sch. :: Nidāna, Sch. i.e. Vācaspati's Comm. :: Title
------------------------------------------------------------

06:06 :: Pañcadaśī, see Bhpañcad. :: Bhāratītīrtha's Pañcadaśī :: Title
2 matches for "Pañcadaśī" in buffer: temp_mw_2.txt
# <s1 slp1="paYcadaSI">Pañcadaśī</s1> ->
# <ls>Pañcadaśī</ls>
python make_change_regex.py 1k temp_mw_2.txt temp_change_regex_1k.txt
4 cases written to temp_change_regex_1k.txt
# insert temp_change_regex_1k.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1394 change transactions from change_2.txt

add to temp_tooltip_4.txt
06:06 :: Pañcadaśī :: see Bhāratītīrtha's Pañcadaśī :: Title

------------------------------------------------------------
00000	06:15 :: Paraśur. :: Paraśurāma-prakāśa :: Title
1 match for "Paraśurāma-prakāśa" in buffer: temp_mw_2.txt
# <s1 slp1="paraSurAma-prakASa">Paraśurāma-prakāśa</s1>
# <ls>Paraśurāma-prakāśa</ls>
python make_change_regex.py 1l temp_mw_2.txt temp_change_regex_1l.txt
1 cases written to temp_change_regex_1l.txt
# insert temp_change_regex_1l.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1394 change transactions from change_2.txt

insert into temp_tooltip_4.txt
06:15 :: Paraśurāma-prakāśa :: Paraśurāma-prakāśa :: Title

------------------------------------------------------------
00000	06:26 :: Pradyumn. :: Pradyumna-vijaya :: Title

# <s1 slp1="pradyumna-vijaya">Pradyumna-vijaya</s1>
# <ls>Pradyumna-vijaya</ls>
python make_change_regex.py 1m temp_mw_2.txt temp_change_regex_1m.txt
1 cases written to temp_change_regex_1m.txt
# insert temp_change_regex_1m.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1394 change transactions from change_2.txt

insert into temp_tooltip_4.txt
06:26 :: Pradyumna-vijaya :: Pradyumna-vijaya :: Title


------------------------------------------------------------
09:35 :: Uṇ,Sch.. :: Uṇādi-sūtra,Sch.i.e.Ujjvaladatta :: Author
53 matches for "<ls>Uṇ.</ls>[,]? <ab>Sch" in buffer: temp_mw_2.txt

# <ls>Uṇ.</ls> <ab>Sch.</ab>
# <ls>Uṇ., Sch.</ls>
python make_change_regex.py 1n temp_mw_2.txt temp_change_regex_1n.txt
53 cases written to temp_change_regex_1n.txt
# insert temp_change_regex_1n.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1451 change transactions from change_2.txt

insert into temp_tooltip_4.txt
09:35 :: Uṇ., Sch. :: Uṇādi-sūtra, Scholiast, i.e.Ujjvaladatta :: Author

------------------------------------------------------------
09:39 :: Upap. :: Upapurāṇa :: Literary category
20 matches for "Upapurāṇa" in buffer: temp_mw_2.txt
# <s1 slp1="upapurARa">Upapurāṇa</s1>
# <ls>Upapurāṇa</ls>
python make_change_regex.py 1o temp_mw_2.txt temp_change_regex_1o.txt
20 cases written to temp_change_regex_1o.txt
# insert temp_change_regex_1o.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1471 change transactions from change_2.txt

insert into temp_tooltip_4.txt as
09:39 :: Upapurāṇa :: a minor Purāṇa :: Literary category
------------------------------------------------------------
10:36 :: Yājñ.,Sch. :: Vijñāneśvara's Mitākṣarā, commentary on Yājñavalkya's Dharma-śāstra :: Title
169 matches for "<ls>Yājñ.</ls>,? <ab>Sch.</ab>" in buffer: temp_mw_2.txt

# <ls>Yājñ.</ls>, <ab>Sch.</ab>
# <ls>Yājñ., Sch.</ls>
python make_change_regex.py 1p temp_mw_2.txt temp_change_regex_1p.txt
169 cases written to temp_change_regex_1p.txt
# insert temp_change_regex_1p.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1640 change transactions from change_2.txt

insert into temp_tooltip_4.txt as
10:36 :: Yājñ., Sch. :: Vijñāneśvara's Mitākṣarā, commentary on Yājñavalkya's Dharma-śāstra :: Title
------------------------------------------------------------
10:32X	Vṛṣabhân.	Vṛṣabhānujā-nāṭikā, by Mathurā-dāsa	Title
# Vṛṣabhân.
# Vṛṣabhān.   (This is 10:32 tooltip)
python make_change_regex.py 1q temp_mw_2.txt temp_change_regex_1q.txt
9 cases written to temp_change_regex_1q.txt
# insert temp_change_regex_1q.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1640 change transactions from change_2.txt

Remove 10:32X from temp_tooltip_4.txt

------------------------------------------------------------
00000	11:16 :: Śiva. :: ŚivaSūtra [Cologne Addition] :: Title
python make_change_regex.py 1r temp_mw_2.txt temp_change_regex_1r.txt
9 cases written to temp_change_regex_1r.txt
# manual adjust temp_change_regex_1r.txt
# insert temp_change_regex_1r.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1654 change transactions from change_2.txt

Śivasūtra (4), Śivas. (1) (tooltip 92.27)
Not changed: <s1 slp1="Siva-sUtra">Śiva-sūtra</s1>s (4)

insert into temp_tooltip_4.txt as
93.43 :: Śivasūtra :: ŚivaSūtra, the first 14 Sūtras of Pāṇini's grammar [Cologne Addition] :: subtitle
------------------------------------------------------------
12:16 :: Ind.Ant. :: Indian Antiquary [Cologne Addition] :: Title

One instance 'Ind. Ant.'
Since we have 92.24	Ind. Ant.	Indian Antiquary [Cologne Addition]	Title,
no need for 12:16.
------------------------------------------------------------
12:23 :: Zachariae :: Theodor Zachariae,  Die indischen Wörterbücher
93.02	Zachariae, Beiträge	Zachariae, Beiträge Zur Indischen Lexicographie

One instance <L>26118<pc>150,1<k1>AramBa
<ls>Zachariae, Beiträge, p. 20, l. 9</ls>

12:23 not needed.

------------------------------------------------------------
12:25 :: Bn. :: ? [Cologne Addition] :: Author
2 matches for "Bn\." in buffer: temp_monier_dump_20071130.txt
Each instance appears Not to be a 'Bn. ls.

1. <L>94428<pc>487,2<k1>durga
2007 version:
<p><lex>m.</lex>~<c>only</c>~<ls>Pan5c._v_,_76</ls>~;~<c>Bn.</c></p>
2022 version:
(<lex type="hwalt">m.</lex> only <ls>Pañc. v, 76</ls>; <ab n="Bombay?">B</ab> <ab>n.</ab>)

2. <L>226631<pc>1118,1<k1>saMSuz
2007 version:
<c><to/>to_be_completely_dried_or_dried_up_,_MBn.</c>
2022 version:
to be completely dried or dried up, <ls>MBh.</ls>;

12:25 not needed.
No changes.
------------------------------------------------------------
12:26 :: Boehtlingk :: Otto von Böhtlingk [Cologne Addition] :: Author

2 matches for "Boeht" in buffer: temp_mw_2.txt
1 match for "Boeht" in buffer: temp_monier_dump_20071130.txt

mw.txt instances:
1. <L>24702<pc>141,3<k1>AntarIpaka
(<ab>fr.</ab> <s>antar-Ipa</s> <ab>g.</ab> <s>DUmA<srs/>di</s>, <ls>Pāṇ. iv, 2, 127</ls>, where [in <ls>Boehtlingk's edition</ls>] <s>antarIpa</s> is to be read instead of <s>antarIya</s>)

2. <L>75248<pc>403,2<k1>cOli
(<s>°lakAyana</s> <ab n="Boehtlingk text of Pravarādhyāya OR Bharadvāja gotra? ">B</ab>, <s>°lika</s> <ab n="Viśvāmitra gotra ?">V</ab>)

The abbreviations in 2 must come from Andhrabharati! Assume they are plausible.

12:26 unneeded.
no changes made
------------------------------------------------------------
12:31 :: Kaegi :: Adolf Kaegi [Cologne Addition] :: Author

2 matches for "Kaegi" in buffer: temp_mw_2.txt
Both instances are already in <ls>:
<ls>Kaegi, Der Ṛgveda, p. 177, l. 28 ff.</ls>
<ls>Kaegi, RV. p. 53 f.</ls>
And have tooltips in temp_tooltip_4.txt:
93.03	Kaegi, Der Ṛgveda	Adolf Kaegi, Der RigVeda: die älteste literature der Inder [Cologne Addition]	Title
93.03a	Kaegi, RV.	Adolf Kaegi, Der RigVeda: die älteste literature der Inder [Cologne Addition]	Title

12:31 is not needed.
no changes made.
------------------------------------------------------------
12:43 :: Wh. :: Whitney, W. D. (1872). [Cologne Addition] :: Author

12:52	Wh. and Ro.	Atharva Veda Sanhita, Volume 1, by  R.Roth and W.D. Whitney, 1856 [Cologne Addition]	Title

1 match for "Wh\." in buffer: temp_mw_2.txt
<L>27372<pc>157,1<k1>ASaMs
(<ab>Impv.</ab> <s>A/-SaMsaya</s>, <ls>RV. i, 29, 1</ls> and [with <ls>Wh. and Ro.</ls>] <ls>AV. xix, 64, 4</ls>)

12:43 unneeded
no changes.
------------------------------------------------------------
new abbreviation 'mystic.'
6 matches for "mystic\." in buffer: temp_mw_2.txt
# mystic. -> <ab>mystic.</ab>
python make_change_regex.py 1s temp_mw_2.txt temp_change_regex_1s.txt
5 cases written to temp_change_regex_1s.txt
# insert temp_change_regex_1s.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1660 change transactions from change_2.txt

new item for mwab_input.txt in pywork/v02/distinctfiles
mystic.	 <id>mystic.</id> <disp>mystical</disp>

------------------------------------------------------------
python ls_unknown.py temp_mw_2.txt temp_tooltip_4.txt temp_ls_unknown.txt
853 tooltips from temp_tooltip_4.txt
0 with unknown ls abbreviation

python lsextract_all.py temp_mw_2.txt temp_tooltip_4.txt lsextract_all.txt
grep '00000' lsextract_all.txt
00000   9.1 :: NUMBER :: number :: ls starts with number

Thus, each abbreviation in temp_tooltip_4.txt has at least 1 instance in
temp_mw_2.txt.

------------------------------------------------------------
------------------------------------------------------------
THIS ENDS WORK WITH TOOLTIP_2_UNUSED.TXT
------------------------------------------------------------
------------------------------------------------------------

------------------------------------------------------------
19 matches for "</ls>(<ab" in buffer: temp_mw_2.txt
insert a space:
# "</ls>(<ab" -> "</ls> (<ab"
python make_change_regex.py 1t temp_mw_2.txt temp_change_regex_1t.txt
19 cases written to temp_change_regex_1t.txt
# insert temp_change_regex_1t.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1660 change transactions from change_2.txt

------------------------------------------------------------
57 matches for "<ls>R.</ls> (<ab>B.</ab>)" in buffer: temp_mw_2.txt
# "<ls>R.</ls> (<ab>B.</ab>)" -> "<ls>R. (B.)"

python make_change_regex.py 1u temp_mw_2.txt temp_change_regex_1u.txt
57 cases written to temp_change_regex_1u.txt
# manual adjustments to temp_change_regex_1u.txt
# insert temp_change_regex_1u.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1738 change transactions from change_2.txt

------------------------------------------------------------
4 matches for "<ls>R.</ls> (<ab>ed.</ab> <ab>Bomb.</ab>)" in buffer: temp_mw_2.txt
# "<ls>R.</ls> (<ab>ed.</ab> <ab>Bomb.</ab>)" ->
# "<ls>R. (ed. Bomb.)</ls>"
python make_change_regex.py 1v temp_mw_2.txt temp_change_regex_1v.txt
4 cases written to temp_change_regex_1v.txt
# manual adjustments to temp_change_regex_1v.txt
# insert temp_change_regex_1v.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1742 change transactions from change_2.txt

insert into temp_tooltip_4.txt
93.11	R. (ed. Bomb.)	Rāmāyaṇa (Bombay edition) [Cologne Addition]	Title

------------------------------------------------------------
5 matches for "<ls>R.</ls> (<ab>ed.</ab> <ab>Gorr.</ab>)" in buffer: temp_mw_2.txt

# "<ls>R.</ls> (<ab>ed.</ab> <ab>Gorr.</ab>)" ->
# "<ls>R. (ed. Gorr.)</ls>"
python make_change_regex.py 1w temp_mw_2.txt temp_change_regex_1w.txt
5 cases written to temp_change_regex_1w.txt
# manual adjustments to temp_change_regex_1w.txt
# insert temp_change_regex_1w.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1747 change transactions from change_2.txt

insert into temp_tooltip_4.txt
93.44	R. (ed. Gorr.)	Rāmāyaṇa (Gorresio edition) [Cologne Addition]	Title

------------------------------------------------------------
15 matches for "<ls>MBh.</ls> (<ab>B.</ab>)" in buffer: temp_mw_2.txt
# "<ls>MBh.</ls> (<ab>B.</ab>)" ->
# "<ls>MBh. (B.)</ls>"
python make_change_regex.py 1x temp_mw_2.txt temp_change_regex_1x.txt
15 cases written to temp_change_regex_1x.txt
# manual adjustments to temp_change_regex_1x.txt
# insert temp_change_regex_1x.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1762 change transactions from change_2.txt

insert into temp_tooltip_4.txt
04:58b	MBh. (B.)	Mahābhārata, Bombay edition	Title

------------------------------------------------------------
4 matches for "Mbh" in buffer: temp_mw_2.txt

python make_change_regex.py 1y temp_mw_2.txt temp_change_regex_1y.txt
4 cases written to temp_change_regex_1y.txt
# manual adjustments to temp_change_regex_1y.txt
# insert temp_change_regex_1y.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1762 change transactions from change_2.txt

3 of the 4 are print changes.
Document in csl-corrections/dictionaries/mw/mw_printchange.txt

remove from temp_tooltip_4.txt
04:60x	Mbh.	Mahābhārata	Title

------------------------------------------------------------
7 matches for "<ls>MBh.</ls> (<ab>ed" in buffer: temp_mw_2.txt
various solutions
python make_change_regex.py 1z temp_mw_2.txt temp_change_regex_1z.txt
7 cases written to temp_change_regex_1z.txt
# manual adjustments to temp_change_regex_1z.txt
# insert temp_change_regex_1z.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1773 change transactions from change_2.txt


add to temp_tooltip_4.txt
04:58c	MBh. ed. Bombay	Mahābhārata, Bombay edition	Title
04:58d	MBh. (ed. Bombay)	Mahābhārata, Bombay edition	Title
04:58e	MBh. (ed. Calc.)	Mahābhārata, Calcutta edition	Title

------------------------------------------------------------
12 matches for "<ls>R. <ab>G.</ab>" in buffer: temp_mw_2.txt
# <ls>R. <ab>G.</ab>  -> <ls>R. G.
python make_change_regex.py 2a temp_mw_2.txt temp_change_regex_2a.txt
12 cases written to temp_change_regex_2a.txt
# manual adjustments to temp_change_regex_2a.txt
# insert temp_change_regex_2a.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1785 change transactions from change_2.txt

------------------------------------------------------------
15 matches in 12 lines for "<ls[^<]*<ab>ed\." in buffer: temp_mw_2.txt

python make_change_regex.py 2b temp_mw_2.txt temp_change_regex_2b.txt
12 cases written to temp_change_regex_2b.txt
# manual adjustments to temp_change_regex_2b.txt
# insert temp_change_regex_2b.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1798 change transactions from change_2.txt

add to temp_tooltip_4.txt
93.14a	R. ed. Gorresio	Rāmāyaṇa (Gorresio edition) [Cologne Addition]	Title
93.11a	R. ed. Bomb.	Rāmāyaṇa (Bombay edition) [Cologne Addition]	Title

------------------------------------------------------------
51 matches in 50 lines for "<ls[^<]*<ab>[a-z]" in buffer: temp_mw_2.txt
A few of these should be changed.
python make_change_regex.py 2c temp_mw_2.txt temp_change_regex_2c.txt
50 cases written to temp_change_regex_2c.txt
# manual adjustments to temp_change_regex_2c.txt
# insert temp_change_regex_2c.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1830 change transactions from change_2.txt

Still have
24 matches in 23 lines for "<ls[^<]*<ab>[a-z]" in buffer: temp_mw_2.txt

------------------------------------------------------------
7 matches for "<ls>R. <ab>B.</ab>" in buffer: temp_mw_2.txt
# "<ls>R. <ab>B.</ab>" -> "<ls>R. B."
python make_change_regex.py 2d temp_mw_2.txt temp_change_regex_2d.txt
7 cases written to temp_change_regex_2d.txt
# insert temp_change_regex_2d.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1837 change transactions from change_2.txt

add to temp_tooltip_4.txt
93.11b	R. B.	Rāmāyaṇa (Bombay edition) [Cologne Addition]	Title

------------------------------------------------------------
307 matches in 305 lines for "<ls[^<]*<ab>" in buffer: temp_mw_2.txt
# examine all of these. Only a few will be changed
python make_change_regex.py 2e temp_mw_2.txt temp_change_regex_2e.txt
305 cases written to temp_change_regex_2e.txt
# insert temp_change_regex_2e.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1902 change transactions from change_2.txt

add to temp_tooltip_4.txt
07:02a	Ragh. (C)	Raghuvaṃśa, Calcutta edition	Title
07:03a	Rājat. (C)	Rājataraṃgiṇī, Calcutta edition [Cologne Addition]	Title
93.14b	R. (G)	Rāmāyaṇa (Gorresio edition) [Cologne Addition]	Title
93.14c	R. [G]	Rāmāyaṇa (Gorresio edition) [Cologne Addition]	Title
93.10a	R. (B)	Rāmāyaṇa (Bombay edition) [Cologne Addition]	Title
93.12a	R. [B]	Rāmāyaṇa (Bombay edition) [Cologne Addition]	Title
93.38a	BhP. (B)	Bhāgavata-purāṇa, by Eugène Burnouf, 1844 [Cologne Addition]	Title
93.37a	Pañc. (B)	Pañcatantra, Bombay edition [Cologne Addition]	Title
04:58g	MBh. [B.]	Mahābhārata, Bombay edition	Title

------------------------------------------------------------
19 matches in 18 lines for ">(" in buffer: temp_mw_2.txt
python make_change_regex.py 2f temp_mw_2.txt temp_change_regex_2f.txt
18 cases written to temp_change_regex_2f.txt
# manually examine
# insert temp_change_regex_2f.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1918 change transactions from change_2.txt

------------------------------------------------------------
39 matches in 34 lines for "</ab><ab>" in buffer: temp_mw_2.txt
</ab><ab> -> </ab><ab>
python make_change_regex.py 2g temp_mw_2.txt temp_change_regex_2g.txt
34 cases written to temp_change_regex_2g.txt
# manually examine
# insert temp_change_regex_2g.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1952 change transactions from change_2.txt

------------------------------------------------------------
21 matches for "</ab><s>" in buffer: temp_mw_2.txt
</ab><s> -> </ab> <s>
python make_change_regex.py 2h temp_mw_2.txt temp_change_regex_2h.txt
21 cases written to temp_change_regex_2h.txt
# manually examine
# insert temp_change_regex_2h.txt into change_2.txt
python updateByLine.py temp_mw_1.txt change_2.txt temp_mw_2.txt
1973 change transactions from change_2.txt

------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
add to temp_tooltip_4.txt
------------------------------------------------------------

 
---------------------------------------------------------------------------

---------------------------------------------------------------------------
---------------------------------------------------------------------------
# install temp_tooltip_4.txt
cp temp_tooltip_4.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt

---------------------------------------------------------------------------
# install of temp_mw_2.txt to check xml
cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135



==========================================================================
temp_mw_3.txt
cp temp_mw_2.txt temp_mw_3.txt
change number of lines by introducing new entry.
1.
OLD
<L>211541<pc>1047,2<k1>SaNKa<k2>SaNKa/<e>1B
¦ a kind of metre, <ls>Ked.</ls>; <ab>N.</ab> of one of <s1 slp1="kubera">Kubera</s1>'s treasures and of the being presiding over it, <ls>MBh.</ls>; <ls>Kāv.</ls> &c.<info lex="inh"/>
<LEND>

NEW
<L>211541<pc>1047,2<k1>SaNKa<k2>SaNKa/<e>1B
¦ a kind of metre, <ls>Ked.</ls>;<info lex="inh"/>
<LEND>
<L>211541.1<pc>1047,2<k1>SaNKa<k2>SaNKa/<e>1B
¦ <ab>N.</ab> of one of <s1 slp1="kubera">Kubera</s1>'s treasures and of the being presiding over it, <ls>MBh.</ls>; <ls>Kāv.</ls> &c.<info lex="inh"/>
<LEND>
# install temp_tooltip_4.txt
cp temp_tooltip_4.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt

2. <L>165691<pc>823,2<k1>mumUrzA  <s>°zu</s> [to be expanded as a HW (mumūr°ṣu)]

OLD:
<L>165691<pc>823,2<k1>mumUrzA<k2>mumUrzA<h>a<e>1
<s>mumUrzA</s> <hom>a</hom> ¦, <s>°zu</s>. See <pcol>p. 827, col. 2</pcol>.
<LEND>
NEW:
<L>165691<pc>823,2<k1>mumUrzA<k2>mumUrzA<h>a<e>1
<s>mumUrzA</s> <hom>a</hom> ¦See <pcol>p. 827, col. 2</pcol>.
<LEND>
<L>165691.1<pc>823,2<k1>mumUrzu<k2>mumUrzu<h>a<e>1
<s>mumUrzu</s> <hom>a</hom> ¦See <pcol>p. 827, col. 2</pcol>.
<LEND>

OLD:
<L>166609<pc>827,2<k1>mumUrzu<k2>mumUrzu<e>2
<s>mumUrzu</s> ¦ <lex>mfn.</lex> wishing or being about to die, moribund, <ls>ib.</ls><info lex="m:f:n"/>
<LEND>
NEW:
<L>166609<pc>827,2<k1>mumUrzu<k2>mumUrzu<h><b><e>2
<s>mumUrzu</s> <hom>b</hom> ¦ <lex>mfn.</lex> wishing or being about to die, moribund, <ls>ib.</ls><info lex="m:f:n"/>
<LEND>

<L>190038<pc>937,1<k1>vAgdevatAguru
    <ls>Piṅg. <ab>Sch.</ab> (in a quot.)</ls>
    <ls>Piṅg. <ab>Sch.</ab> (in a <ab>quot.</ab>)</ls>

------------------------------------------------------------
python ls_unknown.py temp_mw_3.txt temp_tooltip_4.txt temp_ls_unknown.txt
870 tooltips from temp_tooltip_4.txt
0 with unknown ls abbreviation

python lsextract_all.py temp_mw_3.txt temp_tooltip_4.txt lsextract_all.txt
grep '00000' lsextract_all.txt
00000   9.1 :: NUMBER :: number :: ls starts with number

---------------------------------------------------------------------------
# install of temp_mw_3.txt 
cp temp_mw_3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwauthorities/ls/issue135

-------------------------------------------------------------------------
Push repositories to Github.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/135 (change_2)
 csl-pywork  commit e6e4082998e53d799f17207738263f1ba52e218e
 csl-orig  commit 70ba9b9d422f95bbf357a327c140572e5050fb7d
 csl-apidev  commit 10e5d2b336e7978b24b37eac4622d24c5aac56d0
 csl-websanlexicon  commit 8411f022650b776f64f85dd90e5827dbac4da69c
 csl-corrections  commit a81b5a7ed8cb498b27054f879ce0e41c624dee38
 mws 
and update the correspondents at Cologne web site.
DONE with this batch of corrections.


End change_2

==========================================================================
ae -> æ, oe -> œ  (as in Lyrae).  
Reasons: not current usage in English; not amenable to Advanced Search

Remaining unresolved ls tooltips
11:42	TaṇḍināmUp.	NONE	Title
11:43	TśUp.	NONE	Title
11:49	Vallabh.	NONE	Author
90.83	RLM.	Unknown reference [Cologne Addition]	Title

*********************************************************************
Begin change_4
Note: There is no 'change_3'.
touch change_4.txt
cp temp_mw_3.txt temp_mw_4.txt
cp temp_tooltip_4.txt temp_tooltip_5.txt

*********************************************************************
corrections to tooltip_5:
OLD
90.54	Kṛṣṇaj.	Weber's Kṛṣṇajanma ?? [Cologne Addition]	Title
12:21	Beames	? [Cologne Addition]	Author
12:22	Hunter	? [Cologne Addition]	Author
NEW
90.54	Kṛṣṇaj.	Über die Kṛishṇajanmâshṭamî (Kṛishṇa's Geburtsfest), 1867, by Albrecht Weber (English translation: 1874) [Cologne Addition]	Title
12:21	Beames	John Beames (1837-1902), English civil servant and linguistics scholar [Cologne Addition]	Author
12:22	Hunter	William Wilson Hunter (1840-1900)  [Cologne Addition]	Author

NOTE: See later, where BhP. (B) and (B.) are revised further
OLD:
93.38	BhP. (B.)	Bhāgavata-purāṇa, by Eugène Burnouf, 1844 [Cologne Addition]	Title
93.38a	BhP. (B)	Bhāgavata-purāṇa, by Eugène Burnouf, 1844 [Cologne Addition]	Title
NEW:
93.38	BhP. (B.)	Bhāgavata-purāṇa, Bombay edition [Cologne Addition]	Title
93.38a	BhP. (B)	Bhāgavata-purāṇa, Bombay edition [Cologne Addition]	Title
------------------------------------------------------------
addition to change_4.txt
; <L>128945<pc>648,2<k1>petva
434344 old ¦ a small part, W<info lex="inh"/>
434344 new ¦ a small part, <ls>W.</ls><info lex="inh"/>

; <L>204509<pc>1010,1<k1>vftti   print change
683321 old ¦ wages, hire, <ls>Pañcar.</ls><info lex="inh"/>
683321 new ¦ wages, hire, <ls>Pañcat.</ls><info lex="inh"/>

; <L>75248<pc>403,2<k1>cOli
255424 old <s>cOli</s> ¦ <lex>m.</lex> = <s>cOqi</s>, <ls n="Pravar.">vi, 1</ls> (<s>°lakAyana</s> <ab n="Boehtlingk text of Pravarādhyāya OR Bharadvāja gotra? ">B</ab>, <s>°lika</s> <ab n="Viśvāmitra gotra ?">V</ab>). <info lex="m"/>
255424 new <s>cOli</s> ¦ <lex>m.</lex> = <s>cOqi</s>, <ls n="Pravar.">vi, 1</ls> (<s>°lakAyana</s> <ab n="Boehtlingk text of Pravarādhyāya">B</ab>, <s>°lika</s> <ab n="Vaśiṣṭha gotra">V</ab>). <info lex="m"/>
-------------------------------
Ref: https://github.com/sanskrit-lexicon/MWS/issues/135#issuecomment-1204935174
change to temp_tooltip_5
OLD
11:42	TaṇḍināmUp.	NONE	Title
11:42	TāṇḍBr.	TāṇḍyaBrāhmaṇa [Cologne Addition]	Title


; <L>83755<pc>441,3<k1>tARqin
; TaṇḍināmUp. -> TāṇḍBr.  print change
283195 old ¦ <ab>pl.</ab> (<ls>Pravar. ii, 2, 2</ls>) <ab>N.</ab> of a school of the <ls>SV.</ls> (founded by a pupil of <s1 slp1="vESampAyana">Vaiśampāyana</s1>, <ls>Pāṇ. iv, 3, 104</ls>, <ls>Kāś.</ls>; <ab>cf.</ab> <ls n="Pāṇ. iv,">2, 66</ls>, <ls>Kāś.</ls>) <ab>Sch.</ab> on <ls>Bādar. iii, 3, 24</ls>-<ls n="Bādar. iii, 3,">28</ls> and (<ls>TaṇḍināmUp.</ls> = <ls>ChUp.</ls>), <ls n="Bādar. iii, 3,">36.</ls><info lex="inh"/>
283195 new ¦ <ab>pl.</ab> (<ls>Pravar. ii, 2, 2</ls>) <ab>N.</ab> of a school of the <ls>SV.</ls> (founded by a pupil of <s1 slp1="vESampAyana">Vaiśampāyana</s1>, <ls>Pāṇ. iv, 3, 104</ls>, <ls>Kāś.</ls>; <ab>cf.</ab> <ls n="Pāṇ. iv,">2, 66</ls>, <ls>Kāś.</ls>) <ab>Sch.</ab> on <ls>Bādar. iii, 3, 24</ls>-<ls n="Bādar. iii, 3,">28</ls> and (<ls>TāṇḍBr.</ls> = <ls>ChUp.</ls>), <ls n="Bādar. iii, 3,">36.</ls><info lex="inh"/>

--------------------------------
Ref: https://github.com/sanskrit-lexicon/MWS/issues/135#issuecomment-1204952191
 tooltip_5:
Delete
11:43	TśUp.	NONE	Title
Assume print error, in place of
03:38	ĪśUp.	Īśa-upaniṣad	Title

mw.txt change
; <L>94911<pc>489,2<k1>dUre
; TśUp. -> ĪśUp.  print change
319870 old <s>dUre/</s> <hom>a</hom> ¦ <lex>ind.</lex> (<ls>Pāṇ. ii, 3, 36</ls>, <ls>Kāś.</ls>) in a distant place, far, far away, <ls>RV. i, 24, 9</ls>; <ls n="RV.">iv, 4, 3</ls> (<ab>opp.</ab> <s>a/nti</s>) &c., <ls>AV.</ls>; <ls>ŚBr.</ls>; <ls>TśUp. 5</ls> (<ab>opp.</ab> <s>antike</s>), <ls>Mn.</ls>; <ls>MBh.</ls> &c.<info lex="ind"/>
;
319870 old <s>dUre/</s> <hom>a</hom> ¦ <lex>ind.</lex> (<ls>Pāṇ. ii, 3, 36</ls>, <ls>Kāś.</ls>) in a distant place, far, far away, <ls>RV. i, 24, 9</ls>; <ls n="RV.">iv, 4, 3</ls> (<ab>opp.</ab> <s>a/nti</s>) &c., <ls>AV.</ls>; <ls>ŚBr.</ls>; <ls>ĪśUp. 5</ls> (<ab>opp.</ab> <s>antike</s>), <ls>Mn.</ls>; <ls>MBh.</ls> &c.<info lex="ind"/>
;
----------------------------------
tooltip_5 change
OLD
11:49	Vallabh.	NONE	Author
NEW
11:49	Vallabh.	Vallabhadeva's Subhāshitāvali	Title

----------------------------------
6 matches for "Rev\." in buffer: temp_mw_4
All matches are of form:  <ls>ŚivaP. <ab>Rev.</ab></ls>

# <ls>ŚivaP. <ab>Rev.</ab></ls> -> <ls>SkandaP. Rev.</ls>
python make_change_regex.py 4a temp_mw_4.txt temp_change_regex_4a.txt
6 cases written to temp_change_regex_4a.txt
# insert temp_change_regex_4a.txt into change_4.txt
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
11 change transactions from change_4.txt

Document mw_printchange.txt for these 6.
add ls tooltip
93.45	SkandaP. Rev.	SkandaPurāṇa Revākhaṇḍa [Cologne Addition]	Title

Notes:
What are the ls refs in PWG for these 6?
Answer:  Verz. D. Oxf. H.
<L>15785<pc>90,2<k1>arjuneSvaratIrTa
<L>19685<pc>114,1<k1>aSokeSvaratIrTa
<L>19925.1<pc>115,1<k1>aSvaparRI   
<L>20083<pc>115,3<k1>aSvAvatI
<L>21784<pc>125,1<k1>ahalyeSvaratIrTa
<L>22849<pc>131,2<k1>ANgiraseSvaratIrTa

33 matches in 30 lines for "RevāKh\." in buffer: temp_mw_4.txt


The PWG entries for at least some of these mention Śiva-P.
jayavArAhatIrTa: N. eines Tīrtha Śiva-P.  in Verz. D. Oxf. H. 66,b,4.    
jaweSvaratIrTa : N. eines Tīrtha Śiva-P.  in Verz. D. Oxf. H. 66,a,30.
trilocaneSvaratIrTa: N. eines Tīrtha Śiva-P.  in Verz. D. Oxf. H. 66,b,26.

-------------------------------------------
tooltip resolved:
90.83	RLM.	Unknown reference [Cologne Addition]	Title
90.83	RLM.	RājendraLālaMitra's Notices of Sanskrit MSS. ? [Cologne Addition]	Title

-------------------------------------------
Further revision re BhP. (B.)
First, consider these two entries in mw:

<L>184163<pc>910,1<k1>vaMSa<k2>vaMSa/<e>1A
¦ the back-bone, spine, <ls>VarBṛS.</ls>; <ls>BhP.</ls><info lex="inh"/>
<LEND>
<L>184164<pc>910,1<k1>vaMSa<k2>vaMSa/<e>1A
¦ a hollow or tubular bone, <ls>BhP. (B.)</ls>, <ab>Sch.</ab><info lex="inh"/>
<LEND>

Compare these to the extraction from PWG at
 this [link above](https://github.com/sanskrit-lexicon/MWS/issues/135#issuecomment-1204460837).
Conclude:  MW is 'following' PWG.
Note Rückgrat = backbone  (so this corresponds to 184163)
Note Röhrknochen = long bones (corresponding to 184164
Thus, we can infer that the 184164 'BhP. (B.)' reference was erroneously
taken from 'Comm. in der ed. Bomb.  zu 5, 35, 19.'
Conclude:
'BhP. (B.)' is a print error, to change to 'R. (B.)' in 184165

python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
12 change transactions from change_4.txt

Now there is no instance of <ls>BhP. (B.)</ls>, so we may delete 93.38
in temp_tooltip_5.txt.
93.38	BhP. (B.)	Bhāgavata-purāṇa, Bombay edition [Cologne Addition]	Title
93.38a	BhP. (B)	Bhāgavata-purāṇa, Bombay edition [Cologne Addition]	Title
Note We keep 93.38a, since it is used at <L>71762.1<pc>387,2<k1>candramasA,
 and is consistent with PW at candramasa.

---------------------------------------------------------------------------
# install temp_tooltip_5.txt
cp temp_tooltip_5.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt

# install of temp_mw_4.txt 
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
 
-------------------------------------------------------------------------
Push repositories to Github.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/135 (change_4)
 csl-pywork  commit 6b0b99de7ff2532f9f92689c282eef1f2b9b12a2
 csl-orig  commit e833504ff4d316cc7a94b426ba1cd07de13e2483
 csl-corrections  commit 67acf14a1703d7bb0c6f0d135e54a174bad74369
and update the correspondents at Cologne web site.

 push this MWS repository to Github.

DONE with this batch of corrections.

End change_4  (part a)

=========================================================
change_4, part b
A few additional changes, based on issue comments starting at
https://github.com/sanskrit-lexicon/MWS/issues/135#issuecomment-1206255854
=========================================================

00001 90.16 :: Bṛ. :: Śatapatha-brāhmaṇa ? [Cologne Addition] :: Title
02:16	Br.	Brāhmaṇa	Literary category

<L>117598<pc>595,1<k1>pariṇī
The PWG references after 'agram' are to three Brāhmaṇas. We conclude
that the MW text 'Bṛ.' is print error for 'Br.'
397080 old <div n="to"/>to lead forward to, put or place anywhere (<s>agram</s>, at the head), <ls>Bṛ.</ls>;
397080 new <div n="to"/>to lead forward to, put or place anywhere (<s>agram</s>, at the head), <ls>Br.</ls>;

python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt

delete 90.16 from temp_tooltip_5.

---------------------------------------------
02:32	Car.	Caraka	Author
90.24	Cār.	(possibly) Caraka [The context indicates that a work related to some herb, so some medical treatise is intended.] [Cologne Addition]	Title

<L>93383<pc>483,2<k1>duHsparSa<k2>duH—sparSa<e>3B
<s>duH—sparSa</s> ¦ <lex>m.</lex> <bot>Alhagi Maurorum</bot> (also <s>°Saka</s>, <ls>Cār.</ls>)<info lex="m"/>

From pw (duHsparSaka), Cār.  should be 'Carakasaṃhitā'
in L=93383,  print change Car. to Cār.
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
15 change transactions from change_4.txt


delete 90.24 from temp_tooltip_5
revise 02:32 to
02:32	Car.	Carakasaṃhitā 	Title

---------------------------------------------
3 'unknown tips' from lsextract_all.txt
unknown tip at <L>120735<pc>612,2<k1>paScAdbadDapuruza
lstxt = <ls><ab>ib.</ab> [Pi.]</ls>, elt="<ab>ib.</ab> [Pi.]"

unknown tip at <L>120736<pc>612,2<k1>paScAdbAhubadDa
lstxt = <ls><ab>ib.</ab> [Pi.]</ls>, elt="<ab>ib.</ab> [Pi.]"

unknown tip at <L>187338<pc>924,3<k1>varRatAla
lstxt = <ls>Vār., <ab>Introd.</ab></ls>, elt="Vār., <ab>Introd.</ab>"

solutions: remove 'ab' markup in first two.
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
18 change transactions from change_4.txt

Vār. -> Vās. in L=187338 (print change)
We already have the tooltip for Vās.
10:16	Vās.	Vāsavadattā	Title

python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
32 change transactions from change_4.txt

---------------------------------------------
space is missing between the title and the citation
python make_change_regex.py 4b temp_mw_4.txt temp_change_regex_4b.txt
12 cases written to temp_change_regex_4b.txt
# manual adjustment
#  one additional mentioned in issue comment: KātyŚr.,xxv)
# insert temp_change_regex_4b.txt into change_4
python updateByLine.py temp_mw_3.txt change_4.txt temp_mw_4.txt
31 change transactions from change_4.txt

---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------
---------------------------------------------------------------------------
python ls_unknown.py temp_mw_4.txt temp_tooltip_5.txt temp_ls_unknown.txt
869 tooltips from temp_tooltip_5.txt
0 with unknown ls abbreviation
0 cases written to temp_ls_unknown.txt

python lsextract_all.py temp_mw_4.txt temp_tooltip_5.txt lsextract_all.txt
grep '00000' lsextract_all.txt
00000   9.1 :: NUMBER :: number :: ls starts with number
00000   9.2 :: UNKNOWN :: unknown :: ls is unknown


Thus, each abbreviation in temp_tooltip_5.txt has at least 1 instance in
temp_mw_4.txt. And each marked ls abbreviation is identified by a tooltip.


---------------------------------------------------------------------------
# install temp_tooltip_5.txt
cp temp_tooltip_5.txt /c/xampp/htdocs/cologne/csl-pywork/v02/distinctfiles/mw/pywork/mwauth/tooltip.txt

# install of temp_mw_4.txt 
cp temp_mw_4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
grep 'mw ' redo_xampp_all.sh
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
# correct errors
# rerun until
 #prints 'ok'
 
-------------------------------------------------------------------------
Push repositories to Github.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/135 (change_4)
 csl-pywork  commit 6b0b99de7ff2532f9f92689c282eef1f2b9b12a2
 csl-orig  commit e833504ff4d316cc7a94b426ba1cd07de13e2483
 csl-corrections  commit 67acf14a1703d7bb0c6f0d135e54a174bad74369
and update the correspondents at Cologne web site.

 push this MWS repository to Github.

DONE with this batch of corrections.

End change_4

*********************************************************************
*********************************************************************
