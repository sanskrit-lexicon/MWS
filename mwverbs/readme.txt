
* mwverbs
python mwverb.py mw ../../../../cologne/csl-orig/v02//mw/mw.txt mwverbs.txt
each line has 5 fields, colon delimited:
 k1
 L
 verb category: genuinroot, root, pre,gati,nom
 cps:  classes and/or padas. comma-separated string
 parse:  for pre and gati,  shows x+y+z  parsing prefixes and root

* mwverbs1.txt
python mwverbs1.py mwverbs.txt mwverbs1.txt
Merge records with same key (headword)
Also  use 'verb' for categories root, genuineroot, nom
and 'preverb' for categories pre, gati.
Format:
 5 fields, ':' separated
 1. mw headword
 2. MW Lnums, '&' separated
 3. category (verb or preverb)
 4. class-pada list, ',' separated. 
    P -> 'a' (parasmaipada -> active voice)
    Ā -> 'm' (atmanepada -> middle voice)
 5. parse. Empty for 'verb' category. For preverb category U1+U2+...+root

* mwverbs2.txt
python mwverbs2.py mwverbs1.txt mwverbs2.txt
Minor changes to mwverbs1:
- Change from pada to voice in class-pada list
    P -> 'a' (parasmaipada -> active voice)
    Ā -> 'm' (atmanepada -> middle voice)
- Separate Lnums list separator from '&' to ','

Example:
OLD: aMh:107&114:verb:1Ā,10P:
NEW: aMh:107,114:verb:1m,10a:
