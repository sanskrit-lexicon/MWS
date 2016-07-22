

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

