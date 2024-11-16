11-16-2024

Ref: https://github.com/sanskrit-lexicon/MWS/issues/64#issuecomment-2480603732

Ref: https://github.com/sanskrit-lexicon/MWS/issues/176#issuecomment-2307909104

Standalone environment for creating 'ab3' form from cdsl

Programs are copied from mws issue176 (Aug 2024)

convert_ab1.py
convert_ab2a.py
digentry.py

Data files from issue176
temp_mw_16_ab3_orig.txt
temp_mw_17.txt

=============================================
testrun:  convert from temp_mw_17.txt to temp_mw_17_ab2a.txt
  and confirm same as temp_mw_16_ab3_orig.txt

python convert_ab1.py cdsl,ab temp_mw_17.txt temp_mw_17_ab1.txt
# check invertibility of this step

python convert_ab1.py ab,cdsl temp_mw_17_ab1.txt temp_mw_17_chk.txt

diff temp_mw_17.txt temp_mw_17_chk.txt | wc -l
#0  So inverse function works.
rm temp_mw_17_ab1_chk.txt # not needed

----- Now for conversion to match temp_mw_16_ab3_orig.txt
python convert_ab2a.py cdsl,ab temp_mw_17_ab1.txt temp_mw_17_ab2a.txt

diff temp_mw_17_ab2a.txt temp_mw_16_ab3_orig.txt | wc -l
# 0
So temp_mw_17_ab2a.txt is same as temp_mw_16_ab3_orig.txt

--------------------------------------------------------------
# temp_mw_0.txt :  the current version of mw.txt.

csl-orig/v02/mw.txt at commit
dd3bf24682a983d3b10fc5a4a905754e37a6c3fd

cd /c/xampp/htdocs/cologne/csl-orig/
# generate temp_mw_0 .txt in this directory
  git show  dd3bf24682:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue181/temp_mw_0.txt
# return to this directory
cd /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue181
--------------------

python convert_ab1.py cdsl,ab temp_mw_0.txt temp_mw_0_ab1.txt
# check invertibility of this step

python convert_ab1.py ab,cdsl temp_mw_0_ab1.txt temp_mw_0_chk.txt

diff temp_mw_0.txt temp_mw_0_chk.txt | wc -l
#8  So inverse function almost WORKS

-------------------
temp_mw_1.txt
  correct errors uncovered by above

diff temp_mw_0.txt temp_mw_0_chk.txt
1d0  # remove blank line 
<   
3189d3187  # remove blank line 
<
271213c271211  # correct error (remove the <listinfo n="sup"/> at metaline
               # interestingly, this caused no problems in display!
< <L>80547<pc>426,3<k1>jyAyasvat<k2>jyA/yas—vat<e>3<listinfo n="sup"/>
---
> <L>80547<pc>426,3<k1>jyAyasvat<k2>jyA/yas—vat<e>3

cp temp_mw_0.txt temp_mw_1.txt
 # make the 3 corrections

python convert_ab1.py cdsl,ab temp_mw_1.txt temp_mw_1_ab1.txt
# check invertibility of this step

python convert_ab1.py ab,cdsl temp_mw_1_ab1.txt temp_mw_1_chk.txt

diff temp_mw_1.txt temp_mw_1_chk.txt | wc -l
0   So inverse function works
rm temp_mw_1_chk.txt # not needed

---------------------------
2nd step

python convert_ab2a.py cdsl,ab temp_mw_1_ab1.txt temp_mw_1_ab2a.txt

We'll have to see if this ab2a form useful (I've left the name as 'ab2a'
  rather than 'ab3'. If revision to convert_ab2a.py is required,
  I'll use the 'ab3' name.
  
============================================================

# install temp_mw_1.txt into csl-orig, and upload to Github
cp temp_mw_1.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-orig/
git add .
git commit -m "MW minor correction.
Ref: https://github.com/sanskrit-lexicon/MWS/issues/181"
#  1 file changed, 1 insertion(+), 3 deletions(-)
git push
-----------------------
sync Cologne server
and regenerate mw displays

----------------------------------------------------




