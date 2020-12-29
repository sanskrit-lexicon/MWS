Extract supplement records, with context, from MW, using digitization mw.txt

supplement entries in mw.txt are recognized by the '<info n="sup"/>' tag.
6392 entries are marked as supplements.
There are two sub-categories: changes and additions.

Each record of mw (whether supplement or not) has a parameter 'e' in
the meta-line, related to Monier-Williams 4 lines of words.
The 'e' value is either:
a digit 1,2,3 or 4.   These we call 'parent' entries
a digit 1,2,3 or 4 followed by A,B,C or E.  These we call 'child' entries.

To analyze supplement entries, we classify them as 
supplement additions if the entry is a 'parent'
  There are 5255 supplement additions
or supplement changes if the entry is a 'child'
  There are 1137 of these  (5255 + 1137 = 6392)

Note that any 'child' entry in mw.txt  has a unique parent entry.
This is because of the ordering of records. To find the parent, we
search backwards in the list of entries until we find a parent entry.

All the children of a given parent may also be determined, by searching
forward in the entries until another parent entry is found.

We may say that two children with the same parent are siblings.
We also say that a 'family' of entries consists of a parent and all of
its children.

SUPPLEMENT CHANGES

For supplement changes, our current interest is whether the
supplement record is *properly placed* among its siblings.

The changes.py program lists each supplement change entry in the
context of its family of entries.

The program provides a listing of various 
# first parameter:
 0 = (1041) All change cases (no filtering)
 1 = ( 121) N entries and N supplement entries.
            These are additions - probably need no further analysis.
 2 = ( 416) 2 entries and 1 supplement entry
            These probably need no further analysis:
            the supplement entry is an only child of its parent entry.
 3 = ( 155) 3 entries 
            There could be 1 or 2 supplement children.
	    Repositioning could be needed.
 4 = (  67) 4 entries 
            There could be 1-3 supplement children.
	    Repositioning could be needed.
 8 = ( 238) > 4 entries and 1 supplement entry
            The single supplement entry might need repositioning
 9 = (  44) > 4 entries and > 1 supplement entry and some non-supplement entry
            The 1 or more supplement entries could need repositioning
     Check: (+ 527 163 68 238 45) = 1041

changes_3.txt and _4 and _8 and _9 need to be examined.
  Total of 514 entry families to examine.

python changes.py 0 ../mw.txt changes_0.txt
python changes.py 1 ../mw.txt changes_1.txt
python changes.py 2 ../mw.txt changes_2.txt
python changes.py 3 ../mw.txt changes_3.txt
python changes.py 4 ../mw.txt changes_4.txt
python changes.py 8 ../mw.txt changes_8.txt
python changes.py 9 ../mw.txt changes_9.txt

(+ 121 416 155 67 238 44) = 1041


SUPPLEMENT ADDITIONS
These are parent entries which are marked as supplements.
There are 5255 such entries.
These 5255 entries can be separated into two piles:

python additions.py 0 ../mw.txt additions_0.txt
 5123 cases.  Not sure why not 5255
python additions.py 1 ../mw.txt additions_1.txt
 4934 cases.  The entry family contains just the parent; there are no children.
python additions.py 2 ../mw.txt additions_2.txt
  189 cases. 

(+ 4934 189) = 5123
