
# MWS/verbs01

In earlier work we identified verb entries for 14 dictionares, 
and developed a correspondence to verb entries in MW (Monier-William) dictionary.

The work here is to aggregate that analysis over the dictionaries.

## Inputs
In earlier work, we generated files named `xxx_verb_filter_map.txt` for
16 dictionaries xxx:
ap90, ben, bur, cae, ccs, gra, krm, md, pwg, pwk, skd, stc, vcp, wil, shs, yat

For example, for ap90, the file [ap90_verb_filter_map.txt](https://github.com/sanskrit-lexicon/AP90/blob/master/verbs01/ap90_verb_filter_map.txt) is in repository AP90.

Each of these files is a simple list of lines with at least 3 fields:
 `L=x, k1=y, mw=z`
corresponding to dictionary entries identified as verbs.

For example, the first line of the ap90 file is
`;; Case 0009: L=247, k1=aMk, k2=aMk, code=C, mw=aNk`.
This refers to an entry in the Cologne digitization ap90.txt whose
* Cologne identifier is '247'  (L=247)
* headword spelling (key1) is 'aMk'  (k1=aMk)
* whose corresponding Monier-Williams headword spelling is 'aNk' (mw=aNk)

The case number, k2 (key2) value, and code  may or may not be present
for a particular dictionary;  but these extra values are not used in the
present analysis.


## mwverbs
We are associating verbal entries of dictionary xxx with verbal entries of MW.
The particular extraction we will use is ../mwverbs/mwverbs2.txt.

This file has  5 fields, ':' separated:
* mw headword
* MW Lnums, ',' separated
* category (verb or preverb)
* class-voice list, ',' separated. 
* parse. Empty for 'verb' category. For preverb category U1+U2+...+root


## verbs1_merge.py
verbs1_merge.py provides various summaries based on the  xxx_verb_filter_map.txt files and the mwverbs2.txt file.

The summaries include only the verbs  (i.e. excludes the prefixed verbs),
and include only those verbs which have been mapped to an MW verb.



### verbs1_merge0.txt
```
python verbs1_merge.py 0 verbs1_merge0.txt ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt
```
There is a line for each mw verb X for which there is a verb Y in some dictionary which is mapped to X.

Here is a typical line of the merge0 file
```
mw=aMS;9:ap90=aMS;3:ben=aMS;2:bur=aMS;1988:pwg=aMSay;13:pwg=aMSApay;17:pw=aMSay;16:skd=aMSa;5:vcp=aMSa;4:wil=aMSa;5:shs=aMSa;4:yat=aMSa;3
```
The verbs which map onto the  mw verb AMS  (with mw Cologne id of '9'), are
* the ap90 verb aMS (cologne id=3)
* the ben  verb aMS (id=2)
* the bur  verb aMS (id=1988)
* the pwg  verb aMSay (id=13)
* the pwg  verb aMSApay (id=17)
* the pw   verb aMSay (id=16)
* the skd  verb aMSa  (id=5)
* the vcp  verb aMSa  (id=4)
* the wil  verb aMSa  (id=5)
* the shs  verb aMSa  (id=4)
* the yat  verb aMSa  (id=3)

If a dictionary doesn't appear in this list, that means that no verb in that
dictionary is mapped to aMS. For instance, there is no verb in md dictionary
that maps to mw verb aMS.

Currently, 3078 mw verbs appear in this list.

mw verb spelling has only one vowel  (so exclude nominatives and preverbs)

### verbs1_merge1_1v.html
```
python verbs1_merge.py 1h,1v verbs1_merge1_1v.html ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt
```

The '1v' is to indicate that this listing only includes mw verbs whose 
spellings include exactly one vowel.  This excludes about 1000 Denominative
verbs in mw, leaving about 1950 lines.

Each row in the html table of the merge1_1v display shows the mw verb
and, for each dictionary, the verb spelling or spellings, if any, which map to the mw verb.

This html file is best viewed when loaded into a browser window; for example,
click on  [this link](https://sanskrit-lexicon.github.io/verbs/verbs01/verbs1_merge1_1v.html).


### verbs1_merge2.txt
```
python verbs1_merge.py 2 verbs1_merge2.txt ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt

```

This is similar to the merge0 display, but simpler.
Here is the 'aMS' line:
```
aMS:mw,ap90,ben,bur aMSay:pwg,pw aMSApay:pwg aMSa:skd,vcp,wil
```
For the mw verb aMS, the dictionaries with verb entries mapping to 
* aMS are (in addition to mw) ap90, ben and bur
* aMSay are pwg and pw
* aMSApay is pwg only
* aMSa are skd, vcp, and wil.

