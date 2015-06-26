This 'homophone' folder describes work to improve the homophone markup in 
the Cologne digitization of the Monier-Williams Sanskrit-English Dictionary of
1899 (MW).
Jim Funderburk, April 2015.

History
-------
Peter Scharf and Pawan Goyal developed a rational extension
of the homophone markup of MW.  This work was done in 2013.
One motivation for the work was to provide an improved 
'Hierarchical List Display' for MW. Thus, some changes were also made to
the H-codes of monier.xml, and these changes are closely related to 
the proposed changes to the <hom> tags.  Finally, they implemented an 
enhancement to the <see/> tags so that displays could implement hyperlinks
among headwords.

These changes were implemented by a sequence of Java programs,
removeHom, hierMod, newHom, and corRep. Sequential application of these
programs to a version of monier.xml results in a new version of monier.xml
with changes to the <Hx>, <hom>, and <see/> tags.  These Java programs are
in the java subdirectory herein.


At Peter Scharf's request, I am revising this work.  The first step 
consists of a Python implementation of the removeHom, HierMod and newHom
Java programs, and a verification that the Python versions are functional
replicas of the Java programs.  These Python versions are in the pywork
subdirectory.

The pywork/pykeysxml subdirectory contains Python versions of a
sequence of three PHP programs. The Python programs are extract_keys.py,
extract_keys_a.py, and extract_keys_b.py. These programs come into play
between the HierMod and newHom steps. They are also part of the normal
work flow for MW on the Cologne server.

Corrections
-----------
The next step is to make use of certain 'logging' information to identify
cases where there may be errors in the MW digitization, and to implement
appropriate corrections.  A guide to these corrections is in the
readme_corrections.txt file. 

When these corrections have run their course, I'll turn  towards
implementing the Goyal-Scharf work at Cologne.  At that time a more complete
description of that work will be provided.

