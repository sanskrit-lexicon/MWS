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
new: ?? problem with '6'
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
  '6'.??
-----------------------------------------------
Rerun after changes to temp_mw_1.txt
python dhatup.py temp_mw_1.txt dhatup_1.txt
31 cases with non-standard form
2084 cases written to dhatup_1.txt

-----------------------------------------------
install temp_mw_1.txt in csl-orig
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt  
