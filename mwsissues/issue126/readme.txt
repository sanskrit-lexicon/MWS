MWS/mwsissues/issue126

Ref: https://github.com/sanskrit-lexicon/MWS/issues/126

The aim is to make links for the Dhatup references.

Want to get the possible forms that must be parsed.

Some corrections
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt  temp_mw_1.txt

python dhatup.py temp_mw_1.txt dhatup.txt
 Dhāt. or Dhātup.
2084 dhatupada cases
49 cases with non-standard form
2084 cases written to dhatup.txt

Changes to temp_mw_1.txt
---
<L>37131<pc>217,1<k1>uBayatoBAza :
old: <ls>Dhātup. xxx</ls> <ab>B.</ab>
new:  <ls>Dhātup. xxx, B.</ls>
---
<L>60863<pc>335,1<k1>Kac : 
old : <ls n="Dhātup.">xxvi</ls>
new: <ls n="Kathās.">xxvi</ls>
---
<L>69165<pc>374,3<k1>glep
old: and <ls n="Dhātup.">8</ls>
new: & <ls n="Dhātup. x,">8</ls>
---
<L>75700<pc>405,2<k1>Camp
old: <ls>Dhātup. xxxiii.</ls>
new: <ls>Dhātup. xxxii.</ls>
---
<L>92228<pc>478,2<k1>div
old: <ls>Dhātup. xxxiii, 51, 32.</ls>
new: <ls>Dhātup. xxxiii, 51</ls>, <ls n="Dhātup. xxxiii,">32.</ls>
---
<L>101932<pc>519,3<k1>Dfj
old: <ls>Dhātup. vii, 42, 43</ls>
new: <ls>Dhātup. vii, 42</ls>, <ls n="Dhātup. vii,">43</ls>
---
<L>101932.1<pc>519,3<k1>DfYj
old: <ls>Dhātup. vii, 42, 43</ls>
new: <ls>Dhātup. vii, 42</ls>, <ls n="Dhātup. vii,">43</ls>
---
<L>102937<pc>524,3<k1>naK
old: <ls>Dhātup. v, 20, 21.</ls>
newL <ls>Dhātup. v, 20</ls>, <ls n="Dhātup. v,">21.</ls>
---
<L>102937.1<pc>524,3<k1>naNK
old: <ls>Dhātup. v, 20, 21.</ls>
new: <ls>Dhātup. v, 20</ls>, <ls n="Dhātup. v,">21.</ls>
---
<L>115169<pc>582,3<k1>pad
old: <ls>Dhātup. iii, 1, 4</ls>
new: <ls>Dhātup. iii, 1</ls>, <ls n=">Dhātup. iii,">4</ls>
---
<L>142890<pc>721,3<k1>bamb
old: <ls>Dhātup. xi, 24, 25.</ls>
new: <ls>Dhātup. xi, 24</ls>, <ls n="Dhātup. xi,">25.</ls>
---
<L>165301<pc>821,3<k1>muj
old: <ls>Dhātup. vii, 76, 77</ls>
new: <ls>Dhātup. vii, 76</ls>, <ls n="Dhātup. vii,">77</ls>
---
<L>165301.1<pc>821,3<k1>muYj
old: <ls>Dhātup. vii, 76, 77</ls>
new: <ls>Dhātup. vii, 76</ls>, <ls n="Dhātup. vii,">77</ls>
---
<L>205298<pc>1013,3<k1>vekz
old: <ls>Dhātup. xxxv, 84, 6</ls>
new: ?? problem with '6'  see 'further corrections' below
---
<L>210272<pc>1040,3<k1>vyuz
old: <ls n="Dhātup. xxvi,">xxxii, 92.</ls>
new: <ls n="Dhātup.">xxxii, 92.</ls>
---
<L>210345<pc>1041,2<k1>vye
old: <ls>Dhātup. xxili, 38</ls>
new: <ls>Dhātup. xxiii, 38</ls>
---
<L>226481<pc>1117,1<k1>saMvezwana
old: (<ls n="Dhātup.">iii</ls> explaining √ <s>mur</s>)
new: (in explaining √ <s>mur</s>)
---
<L>263399<pc>1300,3<k1>hillolaya
old:  <ls>Dhātup. xxxv, 84, 6.</ls>
new:  UNCHANGED  COULD NOT FIND REF. to hillolaya in
  '6'.?? see 'further corrections' below

-----------------------------------------------
Rerun after changes to temp_mw_1.txt
python dhatup.py temp_mw_1.txt dhatup_1.txt
31 cases with non-standard form
2084 cases written to dhatup_1.txt

-----------------------------------------------
install temp_mw_1.txt in csl-orig
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt  
-----------------------------------------------
01-30-2024
2 further corrections courtesy 
 https://github.com/sanskrit-lexicon/MWS/issues/126#issuecomment-1916078204
 (ref pwg)
Due to intervening changes to csl-orig/v02/mw/mw.txt
cp /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt  temp_mw_2.txt 
---
<L>205298<pc>1013,3<k1>vekz
old: <ls>Dhātup. xxxv, 84, 6</ls>
new: <ls>Dhātup. xxxv, 84, b</ls>
print change
---
<L>263399<pc>1300,3<k1>hillolaya
old: <ls>Dhātup. xxxv, 84, 6.</ls>
new: <ls>Dhātup. xxxv, 84, h.</ls>
print change
-----------------------------------------------
install temp_mw_2.txt in csl-orig

cp temp_mw_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt  
etc.
sync csl-orig to github, install at Cologne
-------------------------------------------------------
revise basicadjust.php (csl-websanlexicon) to link to Westergaard Dhātup.
for MW.
Also for PW, and PWG.
Copy basicadjust and basicdisplay to csl-apidev repo (for simple-search).
Change DHĀTUP ls tooltip for MW.
sync csl-websanlexicon, csl-pywork to github, then sync cologne.
remake displays for pw, pwg, mw at cologne.
------------------------------------------------------------------
01-31-2021
pwg: look for markup errors re <ls>DHĀTUP. XX</ls>
csl-orig at commit ff1180e0e05b2845d997cdc9fc1df8f62fca5b48
cp /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt  temp_pwg_1.txt

cp dhatup.py dhatup_pwg.py

python dhatup_pwg.py temp_pwg_1.txt dhatup_pwg_1.txt tempchange_pwg_2.txt
2626 dhatupada cases
2626 cases
392 cases with non-standard form
2626 cases written to dhatup_pwg_1.txt
392 change cases written to tempchange_pwg_2.txt
188 programmatic changes


cp tempchange_pwg_2.txt change_pwg_2.txt
edit change_pwg_2.txt

---
Question: Should 'v. l.' be within scope of <ls> ?
e.g. <ls>DHĀTUP. 32, 115, v. l.</ls> 
I choose to move v. l. out of ls
e.g. <ls>DHĀTUP. 32, 115</ls>, v. l.

---
TODO: v. l. -> <ab>v. l.</ab>  add to pwgab_input.txt if needed (csl-pywork)


---
L>24850<pc>2-0948<k1>cam
<ls>53.</ls> — {#camno/ti#} ved.
---
Note:
<is>Kār.</is> 2 aus <ls>SIDDH. K.</ls> zu <ls>P. 7, 2, 10.</ls>
---
; <L>51129<pc>4-1173<k1>preNKolay
;  <ls>DHĀTUP. 379,a.</ls> -> ??
504702 old <ls>WEST.</ls> im <ls>DHĀTUP. 379,a.</ls> {#preNKolita#} {%geschwungen, geschaukelt%} 
 379 looks like page number (last page),
  but don't see reference to preNKolay


----------------------------------------------------------------------
Have finished editing change_pwg_2.txt.
apply changes
python updateByLine.py temp_pwg_1.txt change_pwg_2.txt temp_pwg_2.txt
1149413 records written to temp_pwg_2.txt
394 change transactions from change_pwg_2.txt

rerun analysis on pwg_2
python dhatup_pwg.py temp_pwg_2.txt dhatup_pwg_2.txt temp_change_pwg_2a.txt
35 cases with non-standard form
2607 cases written to dhatup_pwg_2.txt
33 change cases written to temp_change_pwg_2a.txt

A few edits of change_pwg_2.txt, including
---
<L>86154<pc>6-0521<k1>laS
old: DHĀTUP. 36, 55
new: DHĀTUP. 33, 55
PRINT CHANGE

============================================================
02-01-2024
Have finished editing change_pwg_2.txt.
apply changes again
python updateByLine.py temp_pwg_1.txt change_pwg_2.txt temp_pwg_2.txt
1149413 records written to temp_pwg_2.txt
394 change transactions from change_pwg_2.txt

rerun analysis on pwg_2
python dhatup_pwg.py temp_pwg_2.txt dhatup_pwg_2.txt change_pwg_2_unused.txt
25 cases with non-standard form
2607 cases written to dhatup_pwg_2.txt
25 change cases written to change_pwg_2_unused.txt

change_pwg_2_unused.txt has the non-standard forms that remain.
They are deemed ok, even though they differ from the current
meaning of 'standard form' per program dhatup_pwg.py.
-----------------------------------------------------------
Install the changes:
1) in local csl-orig/v02/pwg/pwg.txt
cp temp_pwg_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/pwg/pwg.txt
update local installation for csl-orig
push to github
install at cologne and regenerate pwg displays.
2) csl-corrections
install the print change noted above.
----------------------------------------------------------
02-02-2024  dhatup links in schmidt.


csl-orig at commit 47c9b8f974e7aaa175663b47a4bdb286e579cec3
cp /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt  temp_sch_1.txt

'Dhātup.' is the spelling in SCH for references to Westergaard dhatupatha
13 instances found.

Here the change to sch.txt  is to include the 'numbers' within the ls.
I'll do this manually.
cp temp_sch_1.txt temp_sch_2.txt
edit temp_sch_2.txt

</ls> <ls n="Dhātup.">
cp dhatup_pwg.py dhatup_sch.py
python dhatup_sch.py temp_sch_2.txt dhatup_sch_2.txt temp_change_sch_2.txt

These two may be wrong (there is no subsection 960 or 840 in section 1
 of Westergaard).
 ??
<L>11832<pc>162-3<k1>Kadana : Dhātup. 1, 960.
<L>13009<pc>179-2<k1>can : Dhātup. 1, 840.
-------------------------------------------------------
install temp_sch_2.txt in local csl-orig
cp  temp_sch_2.txt /c/xampp/htdocs/cologne/csl-orig/v02/sch/sch.txt 


revise csl-websanlexicon so westergaard is a link target for Dhātup.
change basicadjust.php as needed.
copy also to csl-apidev

sync csl-orig, csl-websanlexicon, csl-apidev at Github and cologne.
Regenerate sch displays at Cologne.

DONE!
