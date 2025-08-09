
=================================================
app1  by anka,verse
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw
local url:
localhost/sanskrit-lexicon-scans/vikramor_mw/app1/?N,N


Github url:
https://sanskrit-lexicon-scans.github.io/vikramor_mw/app1/?N,N

https://sanskrit-lexicon-scans.github.io/vikramor_mw/
shows README.md  (with markdown converted to html)

----------------
# app1 is similar to vikramor/app1
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw
cp -r ../vikramor/app1 .

# get the index

cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188/index.txt app1/pywork/
# get the program to convert index.txt to index.js
cp /c/xampp/htdocs/sanskrit-lexicon/MWS/mwsissues/issue188/make_js_index.py app1/pywork/
# generate index.js
cd app1/pywork
python make_js_index.py index.txt index.js

# copy index.js to app0
cp index.js ../

-------------------------------------
TITLE = Vikramorvasī by Kālidāsa, ed. Shankar P. Pandit, 1879

cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw/app1

# Edit index.html
--- head/title: vikramor_mw
--- body/title: TITLE

# Edit info.html
--- head/title: vikramor_mw info
--- body/title: TITLE
--- app1

# Edit main.js
# pdfpages:  vikr1879_mw_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `vikram_${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

