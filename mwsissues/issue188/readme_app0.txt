
=================================================
app0
=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw
local url:
localhost/sanskrit-lexicon-scans/vikramor_mw/app0/N


Github url:
https://sanskrit-lexicon-scans.github.io/vikramor_mw/app0/?N

https://sanskrit-lexicon-scans.github.io/vikramor_mw/
shows README.md  (with markdown converted to html)

----------------
# app0 is similar to that of /vikramor/app0
cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw
cp -r ../vikramor/app0 .


# get the index (before revision)

Edit parameters in app0/pywork/make_js_index.py
# generate index.js
cd app0/pywork
python make_js_index.py index.js

# copy index.js to app0
cp index.js ../

-------------------------------------
TITLE = Vikramorvasī by Kālidāsa, ed. Shankar P. Pandit, 1879

cd /c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw/app0

# Edit index.html
--- head/title: vikramor_mw
--- body/title: TITLE

# Edit info.html
--- head/title: vikramor_mw info
--- body/title: TITLE
--- app1 

# Edit main.js
# pdfpages:  vikr1879_001.pdf

# vp is of form NNN
--- get_pdfpage_from_index
 let vp = indexobj['vp'];
 let pdf = `vikr1879_${vp}.pdf`;
--- display_ipage_id
 let ipage = indexcur['ipage']; // an int
 
# --------------------
When local debugging done, upload to github

