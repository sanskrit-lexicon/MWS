This 'homophone' folder describes work to improve the homophone markup in 
the Cologne digitization of the Monier-Williams Sanskrit-English Dictionary of
1899 (MW).
Jim Funderburk, April 2015.
June 25, 2015
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

Corrections made
----------------
About 200 homophone corrections were made in April. 
See the updlogs folder (https://github.com/sanskrit-lexicon/MWS/tree/master/homophone/updlogs).  The 'log' files represent updates to monier on Cologne.
The 'notes' files provide some context to the log files.
See also the readme_corrections.txt file in this repository.

Removehom corrections (June 16, 2015)
---------------------
Assume a copy of monier.xml from Cologne. 
The removeHom program removes homophone codes for those records whose
Hierarchy codes are `<Hx[ABC]>`.  It starts with a copy of monier.xml 
and generates a modified version, monier_pg2.xml.

python removeHom.py monier.xml monier_pg2.xml

A similar program, removeHomUpd.py, generates a 'log' and 'notes' file for
the modified homophones.
python removeHomUpd.py monier.xml updlogs/log_20150616-01.txt updlogs/notes_20150616-01.txt


6555 changes were made here.

Artificial Homophones (June 16, 2015)
---------------------
Using the version of monier.xml after making the changes of removeHom.py
 (e.g., monier_pg2.xml),  a multi-step process assigns artificial homophones
to 10,913 records.
Here are the steps:

1. Create a (temporary) version of monier.xml, called monier_pg2a.xml, in 
   which some of the Hierarchy codes are adjusted to have an extra 'a' letter.
   Slightly more specifically, certain `<Hx[BC]>` hierarchy codes are changed
   to `<Hx[BC]a>`  (e.g. H2B becomes H2Ba).  These are cases where the
   headword for a 'B' or 'C' record is a repeat of a previous record.  In the
   next step, the records so marked are excluded as artificial homophone
   candidates.  About 35000 records are so marked.
python python hierMod.py  monier_pg2.xml  monier_pg2a.xml

2. Generate a file 'extract_keys_b.txt' from monier.xml.  The essential
   feature of this file is that it gathers ALL the records which have a
   given headword as key1.  For instance, for the headword 'akza', we have
   H2,424,431.1;H2,455,463;H2,517,525;H2,535,535;H2,660,660
   which means that akza is the headword 
    - H2 for record numbers, L, in the range 424 to 431.1
    - H2 for 455<=L<=463
    - H2 for 517<=L<=525
    - H2 for 535<=L<=535  (i.e. L=535)
    - H2 for L=660
Here is how extract_keys_b.txt is generated:
python extract_keys.py monier.xml extract_keys.txt
python extract_keys_a.py extract_keys.txt extract_keys_a.txt
python extract_keys_b.py extract_keys_a.txt extract_keys_b.txt

3. Create a new version of monier.xml by assigning artificial homophones.
   The inputs are the version of monier which has the modified hierarchy
   codes AND extract_keys_b.txt.  This is done by the newHom.py program:
python  newHom.py extract_keys_b.txt monier_pg2a.xml mod_hom.txt monier_pg3.xml > newHom_log.txt
  The modified MW is monier_pg3.xml.  The two files mod_hom.txt and 
  newHom_log.txt provide information on records that were changed.

  The general idea is to process the headwords as presented in extract_keys_b.
  For such a headword,  the first record in each of the 'groups'  is 
  examined. In our 'akza' example, this would be records 424, 455,517,535
  and 660.  If there is already a unique (numeric) homophone code for one of
  these records, it is left unchanged (e.g. 424, 455, and 517 with homophone
  codes of 1,2 and 3).   If there remain multiple records for duplicate (or 
  missing) homophone codes, then these records are assigned artificial 
  alphabetical homophone codes, in order of L number.  In our akza case,
  records 535 and 660 have the same homophone code '4' assigned by MW, so these
  are modified to 4a and 4b for L=535, 660.
  The more usual case is where there are multiple records with no homophone
  code. For example, headword akzaja has two groups in extract_keys_b, 
  H3,434,436;H3,469,470;  and record L= 434 and 469 have no homophone code
  assigned by Monier-Williams. In this case artificial homophone codes of
  'a' and 'b' are assigned to L=434 and 469, respectively.

4. newHom correction records
The newHom.py program was modified to newHomUpd.py, to generate an update
of monier.xml at Cologne for installing the artificial hom codes.
Here is the program invocation:
python newHomUpd.py extract_keys_b.txt monier_pg2a.xml  log_20150616-03.txt notes_20150616-03.txt
The first two run-time arguments (extract_keys_b.txt and monier_pg2a.xml) are
the same as for newHom.  log_20150616-03.txt is the file of update records.
notes_20150616-03.txt is a record of the 'old' and 'new' form for each of the
modified records.  There are 10,913 records that are changed.
These two output files are in the homophone/updlogs directory of this repository

The corrections of log_20150616-03.txt have been applied to Cologne edition
of monier.xml.

