
Folder to create versions of the base digitization of mw  (mw.txt)
where the slp1 text is transcoded.
We also check for invertibility of this transcoding.

The only result currently installed is mw_iast.txt,  where slp1 transcoding
is changed to iast.  

This program constructs mw_iast.txt.   The input is mw.txt; and
the path '../mw.txt' was relevant where this was run on local computer.
One source for mw.txt is 
 https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/mw/mw.txt


The transcoding details are contained in transcoder/slp1_roman.xml.

python mw_transcode.py slp1 roman ../mw.txt mw_iast.txt

We do the inverse transcoding, from iast back to slp1.
The inverse transcoding is governed by transcoder/roman_slp1.xml.

python mw_transcode.py roman slp1 mw_iast.txt temp_mw_slp1.txt
diff ../mw.txt temp_mw_slp1.txt > temp.txt

The diff shows that there are 3 cases where the transcoding is NOT invertible.
Note: temp_mw_slp1.txt should == ../mw.txt
  only differs in 3 words:
slp1  <L>116525.7<pc>588,2<k1>paramahaMsopanizadhfdaya<k2>parama/—haMsopanizad-hfdaya<e>4
iast  <L>116525.7<pc>588,2<k1>paramahaṃsopaniṣadhṛdaya<k2>paramá—haṃsopaniṣad-hṛdaya<e>4
slp1a <L>116525.7<pc>588,2<k1>paramahaMsopanizaDfdaya<k2>parama/—haMsopanizad-hfdaya<e>4

slp1  <L>139372<pc>704,3<k1>prAghAra<k2>prAg—hAra<e>3
iast  <L>139372<pc>704,3<k1>prāghāra<k2>prāg—hāra<e>3
<L>139372<pc>704,3<k1>prAGAra<k2>prAg—hAra<e>3

slp1  <L>139373<pc>704,3<k1>prAghoma<k2>prAg—homa<e>3
iast  <L>139373<pc>704,3<k1>prāghoma<k2>prāg—homa<e>3
slp1a <L>139373<pc>704,3<k1>prAGoma<k2>prAg—homa<e>3


This is how we can transcode mw.txt to Devanagari.

python mw_transcode.py slp1 deva ../mw.txt mw_deva.txt 

python mw_transcode.py deva slp1 mw_deva.txt temp_mw_slp1.txt

Now, ../mw.txt and temp_mw_slp1.txt should be the same
diff ../mw.txt temp_mw_slp1.txt 
The files are the same!
