cd rev1a

Examine ../rev1/temp_rev1_cdsl.txt.
Constructing displays yields some other inconsistencies.

cp ../rev1/temp_rev1_ab_iast.txt temp_rev1a_ab_iast.txt

Correct these in temp_rev1a_ab_iast.txt
see rev1a/change_notes_rev1a.txt

# construct temp_rev1a_cdsl.txt  from temp_rev1a_ab_iast.txt
sh convert_rev1a_ab_cdsl.sh

# check lnum uniquenss and ordering
python ../code1/check_lnum.py temp_rev1a_cdsl.txt
# check_lnum finds 0 problems

#construct local version based on temp_rev1_cdsl.txt

cd rev1a
sh redo_mw.sh
-----------------------------------------
All looks ok.
-------------
End of rev1a

