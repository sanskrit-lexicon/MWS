Jan 21, 2021.  
save local copies:  (the 'tempprev_...' files not tracked by git.
  mw.txt as tempprev_mw.txt  
  mw_iast.txt as tempprev_mw_iast.txt

Sync mw.txt with csl-orig version, in preparation for Andhrabharati's  work.
The csl-orig commit is 7c4f7779372a13cdd691faf28d9984f86069112f

reconstruct mw_iast.txt
python mw_transcode.py slp1 roman mw.txt mw_iast.txt

confirm invertibility:
python mw_transcode.py roman slp1 mw_iast.txt temp_mw_slp1.txt
diff mw.txt temp_mw_slp1.txt  (no difference)
NOTE:  mw_transcode program changed to
  manually adjust three lines in the roman-slp1 transcoding.

-----------------------------------------------------------------------


Currently (Jan 3, 2021), mw.txt agrees with version in csl-orig at
commit# 67bfbda32328317ab45f69432f58204595227609).

Folder to create versions of the base digitization of mw  (mw.txt)
where the slp1 text is transcoded.
We also check for invertibility of this transcoding.

The current transcoding results are:
 mw_iast.txt and mw_deva.txt.

These are reconstructed by:

python mw_transcode.py slp1 roman mw.txt mw_iast.txt
and
python mw_transcode.py slp1 deva mw.txt mw_deva.txt

Discussion of mw_iast.txt
-------------------------

The transcoding details are contained in transcoder/slp1_roman.xml.

python mw_transcode.py slp1 roman mw.txt mw_iast.txt

We do the inverse transcoding, from iast back to slp1.
The inverse transcoding is governed by transcoder/roman_slp1.xml.

python mw_transcode.py roman slp1 mw_iast.txt temp_mw_slp1.txt
diff mw.txt temp_mw_slp1.txt > temp.txt

The diff shows that there are 3 cases where the transcoding is NOT invertible.
Note: temp_mw_slp1.txt should == mw.txt
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


Discussion of mw_deva.txt
-------------------------

This is how we can transcode mw.txt to Devanagari.

python mw_transcode.py slp1 deva mw.txt mw_deva.txt 

python mw_transcode.py deva slp1 mw_deva.txt temp_mw_slp1.txt

Now, mw.txt and temp_mw_slp1.txt should be the same
diff mw.txt temp_mw_slp1.txt 
The files are the same!
