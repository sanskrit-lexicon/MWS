
# list all commits of csl-orig where v02/mw/mw.txt was changed
cd /c/xampp/htdocs/cologne/csl-orig

git log --follow --pretty=format:"%H %an %ad %s" --date=short -- v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue190/mw_commits.txt

# mw_commits.txt is in reversed date order

# find the commit hashes of csl-orig where the text string '164587' appears
# or disappears in v02/mw/mw.txt.  '164587' is the 'L-code' of missing headword
/c/xampp/htdocs/cologne/csl-orig
git log -S'164587' --follow -- v02/mw/mw.txt

OUTPUT:
commit f677a655c4876c7adf668df631317b449d5c2100    
Author: funderburkjim <funderburkjim@gmail.com>
Date:   Sun Aug 11 16:05:57 2024 -0400

    MW: and/or group standardization.
    Ref: https://github.com/sanskrit-lexicon/MWS/issues/175

commit 6f45dd5ce45d79f36cc16ef7ecaaaf6db8800254
Author: drdhaval2785 <drdhaval2785@gmail.com>
Date:   Sat Jul 20 10:20:29 2019 +0530

    csl-orig initial commit 

-----------------
The problem occurs in commit f677a655c4876c7adf668df631317b449d5c2100
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue190
# edit mw_commits.txt to find the previous commit
# here is the lost_parent commit:
8a35c84b0c3b3ba9bbb56db324b38e636defe162
  funderburkjim 2024-08-03
  MW: supplement placement.
    Ref: https://github.com/sanskrit-lexicon/MWS/issues/171
-----------------

# This is not very interesting as diff is too big
https://github.com/sanskrit-lexicon/csl-orig/commit/f677a655c4876c7adf668df631317b449d5c2100

--------------------------------------------
Get local copies of mw.txt at the two commits
-- the 'lost' commit  (where headword is lost)
cd /c/xampp/htdocs/cologne/csl-orig
git show f677a655c4876c7adf668df631317b449d5c2100:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue190/temp_mw_lost.txt

-- the parent of lost commit
cd /c/xampp/htdocs/cologne/csl-orig
git show 8a35c84b0c3b3ba9bbb56db324b38e636defe162:v02/mw/mw.txt > /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue190/temp_mw_lostparent.txt

====================================================
# begin examination of the changes of this commit
cd /c/xampp/htdocs/sanskrit-lexicon/mws/mwsissues/issue190

# some discussion in issue 175
https://github.com/sanskrit-lexicon/MWS/issues/175

# crude differences of th'lost' commit
 wc -l temp_mw_lost*.txt
   878258 temp_mw_lost.txt
   880411 temp_mw_lostparent.txt
 (- 880411 878258) 2153 fewer lines in temp_mw_lost.txt

---------------
diff temp_mw_lostparent.txt temp_mw_lost.txt > diff_lost.txt

Search for our lost l-number <L>164587 in diff_lost.txt
