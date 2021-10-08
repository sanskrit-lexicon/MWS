Re https://github.com/sanskrit-lexicon/csl-orig/issues/519

Start with mw.txt at commit 13f3a5489cae002726c338aa27c771fba2548806.

cp ../mw.txt temp_mw0.txt
# construct change1.txt in several steps
python change1a.py temp_mw.txt temp_change1a.txt
 
 n="Pāṇ."



#<s>X</s> is in Devanagari in pan.txt. Convert to slp1
python mw_transcode.py deva slp1 pan.txt pan_slp1.txt

# generate change transactions based on finding lines that contain
 certain strings, these strings having be extracted
 into pan1_slp1.txt from pan_slp1.txt
 
python change1b.py temp_mw0.txt pan1_slp1.txt temp_change1b.txt

python updateByLine.py temp_mw0.txt change1.txt temp_mw1.txt

Install temp_mw1.txt in csl-orig
  as commit b6d3c885f281b12b1f2c725037c7e2d9c4ad93ff


; -------------------------------------------------------------
; Prepare for changing format of Panini links in mw from
; 'x-y,z' (x,y,z Arabic numerals) to 'u,y,z'  where u is lower-case Roman.
; Begin by listing ALL panini links (along with counts)
; Forms
; <ls>Pāṇ.</ls>
; <ls>Pāṇ. x-y, z</ls>
; <ls n="Pāṇ.">x-y, z</ls>
; etc.
python panini_links0.py temp_mw1.txt panini_links_mw1.txt temp.txt




## change2.txt  constructed manually, in several steps
python updateByLine.py temp_mw1.txt change2.txt temp_mw2.txt
 - from panini_links_N errors noted
 - python change2a.py temp_mw1.txt temp_change2a.txt
   <ls>Pāṇ. x-y,z</ls> -> <ls>Pāṇ. x-y, z</ls>   (8 - space after comma)
 - python change2b.py temp_mw2.txt temp_change2b.txt  (36)
   <ls>Pāṇ. ...and</ls>
 - python change2c.py temp_mw2.txt temp_change2c.txt (54)
   <ls>Pāṇ. x-y, z and a-b, c<ls>
 - python change2d.py temp_mw2.txt temp_change2d.txt (44)
   <ls>Pāṇ. x-y, z and w<ls>
 - python change2e.py temp_mw2.txt temp_change2e.txt (16)
   <ls>Pāṇ. x-y, z and u,v<ls>  ->
   <ls>Pāṇ. x-y, z</ls> and <ls n="Pāṇ. x-">u,v<ls>
 - python change2f.py temp_mw2.txt temp_change2f.txt (30)
   The remaining panini references containing 'and'
   Have to correct these by hand.
 - python change2g.py temp_mw2.txt temp_change2g.txt (24)
   <ls>Pāṇ. ...<ab>
 - python change2h.py temp_mw2.txt temp_change2h.txt (28)
   <ls>Pāṇ. ...X   X in seq, Comm, the, or, Ka1y,?,fr,sq
 - python change2i.py temp_mw2.txt temp_change2i.txt (14)
   <ls>Pāṇ. &
 - python change2j.py temp_mw2.txt temp_change2j.txt (76)
   <ls>Pāṇ. x-y, z; a-b, c</ls>
 - python change2k.py temp_mw2.txt temp_change2k.txt (52)
   <ls>Pāṇ. x-y, z; w</ls>
 - python change2l.py temp_mw2.txt temp_change2l.txt (14)
   <ls>Pāṇ. x-y, z; u, v</ls>
 - python change2m.py temp_mw2.txt temp_change2m.txt (22 lines)
   <ls>Pāṇ. X</ls> and semicolon in X
 - python change2n.py temp_mw2.txt temp_change2n.txt (11)
   <ls>Pāṇ. x-y, z, z1</ls> and semicolon in X
 - python change2o.py temp_mw2.txt temp_change2o.txt (7)
   Contains string 'Kāś'
 - python change2p.py temp_mw2.txt temp_change2p.txt (88)
   <ls>Pāṇ. X </ls> or <ls>Pāṇ. X, </ls>


python panini_links.py temp_mw2.txt panini_links.txt panini_links_N.txt

 

python panini_links1.py temp_mw2.txt panini_links1.txt 

python change_roman.py temp_mw2.txt change_roman.txt

python updateByLine.py temp_mw2.txt change_roman.txt temp_mw3.txt


python panini_links1_roman.py temp_mw3.txt panini_links1_roman.txt 

cp temp_mw2.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt

cp temp_mw3.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
