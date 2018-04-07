

The MWWorksAuthorsCurrentMarkup3.xml is the reference document for the
Cologne digitization of the List of Works of the Monier Williams Sanskrit English
Dictionary of 1899.  It was prepared under the supervision of 
Peter Scharf and Malcolm Hyman of [The Sanskrit Library](www.sanskritlibrary.org) ca. 2010.

This xml document follows the structure as specified in the Relax NG schema mw-authorities.rng; which, I think, is derived from the compact syntax form of mw-authorities.rnc.

The mwauthorities_init.txt file is a  slightly simplified version of MWWorksAuthorsCurrentMarkup3.xml.  It was originally created by an xsl transformation of
the xml file, but also includes two revisions for 

* the author Kielhorn
* the title kOzItaki-brAhmaRa


The linkmwauthorities_init.txt file contains the link between the literary
source abbreviations appearing in monier.xml and the records appearing in 
MWWorksAuthorsCurrentMarkup3.xml.
There are three tab-delimited fields:
* ls (literary source) abbreviation appearing in monier.xml
* a count (probably not maintained) of the number of instances of the
  ls abbreviation in monier.xml
* the abbreviation appearing in MWWorksAuthorsCurrentMarkup3.xml.

The correlation was established several years ago primarily on the basis
of formal similarity between the spelling of the two abbreviations.

### Images
mw010005.jpg and mw010006.jpg are images of the two pages of `LISTS OF WORKS AND AUTHORS` from MW1899.

### mwauth.txt
This is an amalgam of mwauthorities_int.txt and linkmwauthorities_init.txt,
and is intended to be the basis of further corrections and improvements regarding the literary sources in the digitized MW.  It includes the links, in the
spelling (IAST with a few MW-specific wrinkles) used in the current revision
of the MW digitization.  The first column is a record identifier, as
described [here](https://github.com/sanskrit-lexicon/Cologne/issues/219#issuecomment-379501096).
The other fields are coded in the same way as in mwauthorities_init.txt

### tooltip.txt
This is derived (by program tooltip.py) from mwauth.txt.  It contains
* record identifier
* abbreviation
* expansion of abbreviation
  * Currently uses the `<expandNorm>` tag, if available. Otherwise uses
    the `<expandMW>` tag.
  * Prints the expansion in an IAST trascoding of the `<slp>` tags according
    to the transcoding/slp_roman.xml transcoding file.
  * With some modification to tooltip.py, the expansion could be printed in
    Devanagari, or other encodings of Sanskrit words denoted by `<slp>` tag.
* type of literary source, based on the 4th field of mwauth.txt.


