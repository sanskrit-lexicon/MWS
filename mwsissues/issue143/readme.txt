Ref: https://github.com/sanskrit-lexicon/MWS/issues/143.

A simple program to count the number of DISTINCT headwords for a dictionary
in the csl format.

hwcount.py uses only the metalines of a dictionary digitization.
hwcount does not include the 'extra' headwords (e.g. mw_hwextra.txt,
which is empty for mw).

python hwcount.py /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
287587 entries found
194049 distinct k1 headwords in C:/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
