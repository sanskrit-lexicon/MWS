12-29-2022
Replacement of scanned images for MW (1899) dictionary

mw_color.pdf  colored pages 1-1333 From Andhrabharati
mw_grey.pdf   greyscale pages 1-1333 From Andhrabharati
Objective:
Replace current MWScan/NWScanpdf files with new pdfs.
File name problem:
Current file names in MWScanpdf
  mw0001-a.pdf through mw1308-hvala.pdf  main section
  mw1309.pdf through mw1333.pdf  addendum
  mw010001.pdf through mw010036.pdf  front matter
  mw171504.pdf unused: 'printed in great britain ...'
Similar filenames in MWScanjpg:
 mw0001-a.jpg through mw1308-hvala.jpg main section

MWScan/mwfiles.txt:
mw0001-a
mw0002-akarman
...
these file names are used in MWScan/form.php' which is used
by MWScan/index.php which is referenced by the 'S1', 'S2' links on homepage.

ALSO
csl-websanlexicon/distinctfiles/mw/web/webtc/pdffiles is used for
  displays of mw.

0001:mw0001-a.pdf:0001 a
0002:mw0002-akarman.pdf:0002 akarman
...
1308:mw1308-hvala.pdf:1308 hvala , Suppl.
1309:mw1309.pdf:S1309 agṛhīta
...
1333:mw1333.pdf:S1333 sarṣapa-miṣra
t01:mw010001.pdf:Title
t02:mw010002.pdf:Copyright
...
t36:mw010036.pdf:Page xxxii

--------------------------------------------------------------------
The simplest solution for file names for pages 1-1333 is
to use the old filenames:
  mw0001-a.pdf  ... mw1308-hvala.pdf  main section
  mw1309.pdf through mw1333.pdf  addendum

The new images do not include front matter, so front matter files
will be copied from the current (old) MWScanpdf directory
  mw010001.pdf through mw010036.pdf  front matter
  mw171504.pdf unused: 'printed in great britain ...'
--------------------------------------------------------------------
Adobe Acrobat 9 'Document/Extract pages' is used to extract
the 1333 pages from mw_color.pdf into folder mwcolorpages directory.
The names of the mwcolorpages files are
 'MW-main (coloured) 1.pdf' through 'MW-main (coloured) 1333.pdf'
 
Use a copy of MWScan/mwfiles.txt
curl https://sanskrit-lexicon.uni-koeln.de/scans/MWScan/mwfiles.txt -o mwfiles.txt
mkdir pdfpages
ls mwcolorpages/*.pdf > mwcolornames.txt
python make_rename_copy_main.py mwfiles.txt mwcolornames.txt rename_copy_main.sh pdfpages

sh rename_copy_main.sh pdfpages
-------------------------------------------------------------------
now pdfpages has consistently named pdfs for pages 1-1333.
-------------------------------------------------------------------
add copies of the pdfs for frontmatter and endmatter pages.

These are taken from the previous sanskrit-lexicon-scans
# 37 files
ls /c/xampp/htdocs/cologne/scans/mw/pdfpages/mw0100??.pdf > frontfiles.txt
SAMPLE /c/xampp/htdocs/cologne/scans/mw/pdfpages/mw010023.pdf
Edit frontfiles.txt, and
1.remove the prefix and suffix /c/xampp/htdocs/cologne/scans/mw/pdfpages/
  NEWSAMPLE mw010023
2. Add the 'back page' name mw171504
python make_rename_copy_front.py frontfiles.txt rename_copy_front.sh /c/xampp/htdocs/cologne/scans/mw/pdfpages pdfpages

sh rename_copy_front.sh

# check 1
ls /c/xampp/htdocs/cologne/scans/mw/pdfpages/*.pdf | wc -l
# 1370
ls pdfpages | wc -l
# 1370
# GOOD same number of files
# check 2
ls /c/xampp/htdocs/cologne/scans/mw/pdfpages > tempold.txt
ls pdfpages > tempnew.txt
diff tempold.txt tempnew.txt
# 0 GOOD! no difference

------------------------------------------------------------------------
rename repository
