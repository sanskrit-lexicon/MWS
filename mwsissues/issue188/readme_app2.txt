
=================================================
app2
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vikramor
local url:
localhost/sanskrit-lexicon-scans/vikramor/app2/N,N


Github url:
https://sanskrit-lexicon-scans.github.io/vikramor/app2/?N,N

https://sanskrit-lexicon-scans.github.io/vikramor/
shows README.md  (with markdown converted to html)

----------------
# app2 is similar to app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor
cp -r app0 app2

-------------------------------------
TITLE = Vikramorvasī by Kālidāsa, ed. F. Bollensen, 1846
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor/app2

# Edit index.html
--- head/title: vikramor
--- body/title: TITLE

# Edit info.html
--- head/title: vikramor info
--- body/title: TITLE
--- app2

# Edit main.js
# pdfpages:  vikramor_001.pdf

# vp is of form NNN

# --------------------
When local debugging done, upload to github

