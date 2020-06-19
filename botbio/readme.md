Extract list of bot, bio tags from MW, using digitization mw.txt

We extract from digitization csl-orig/v02/mw/mw.txt
Assume we are in local installation:
* sanskrit-lexicon
  * mws
    * botbio  # directory containing this readme
* cologne
  * csl-orig

relative path to mw.txt from here is ../../../cologne/csl-orig/v02/mw/mw.txt
python tagunique.py bot ../../../cologne/csl-orig/v02/mw/mw.txt mw_bot.txt
python tagunique.py bio ../../../cologne/csl-orig/v02/mw/mw.txt mw_bio.txt
