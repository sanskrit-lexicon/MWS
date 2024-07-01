MWS/mwsissues/issue167

Ref: https://github.com/sanskrit-lexicon/MWS/issues/167

Related to https://github.com/sanskrit-lexicon/csl-orig/issues/1645#issuecomment-2198054242
# this directory in local file system
/c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue167/

# -------------------------------------------------------------
Start with a copy of csl-orig/v02/mw/mw.txt at commit
7e7a5efff69a80cecb7a9b9d68ee1886db6d38a7

# change to csl-orig repository on local installation
cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0.txt in this directory
git show  7e7a5efff6:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue167/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue167/

# -------------------------------------------------------------
Start Andhrabharati list in issue 167:
(1603): `<s>/kṣa—dhur</s>`	`<k2>`akṣa—dhur	;;  "/" for "a"
(53835): `<s>ayas—m/yā<srs/>di</s>`	`<k2>`ayas—mayādi	;;  "/" for "a"
(126144): `<s>up/riṣṭād—vātá</s>`	`<k2>`upariṣṭād—vātá	;;  "/" for "a"
(128751): `<s>upa-sth/na—sāhasrī</s>`	`<k2>`upa-sthāna—sāhasrī	;;  "/" for "ā"
(357380): `<s>nāvy/</s>`	`<k2>`nāvyā	;;  "/" for "ā"
(467080): `<s>pra-°hār/ya</s>`	`<k2>`pra-hā́rya	;; "ār/" for "ā́r"
(553166): `<s>mukha—/taḥ-kāram</s>`	`<k2>`mukha—/taḥ-kāram	;; no "/" in print at all; k2 should also change
(696441): `<s>vyathā—r/hita</s>`	`<k2>`vyathā—rahita	;;  "/" for "a"
(729608): `<s>śukr/—danta</s>`	`<k2>`śukra—danta	;;  "/" for "a"
(731560): `<s>śunā-s/°ryâ</s>`	`<k2>`śunā-sīryâ	;;  "/" for "ī"
(762092): `<s>s/khi—vigraha</s>`	`<k2>`sakhi—vigraha	;;  "/" for "a"

# -------------------------------------------------------------
cp temp_mw_0.txt temp_mw_1.txt
# manual changes in mw_1 based on above AB list
11 changes -- also 1 change to metaline (553166)

# generate change file
python diff_to_changes_dict.py temp_mw_0.txt temp_mw_1.txt change_1.txt
12 changes written to change_1.txt

*********************************************************************
install temp_mw_1.txt in csl-orig
------------------------------------------------------------------------
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw

cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git add mw.txt
git commit -m "MW stray errors :
Ref: https://github.com/sanskrit-lexicon/MWS/issues/167"

git push
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue167

------------------------------------------------------------------------
