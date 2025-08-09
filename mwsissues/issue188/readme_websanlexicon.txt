
=================================================
activating links from koshas to vikramor_mw app1

koshas: mw
app2 Vikr. N,N 

=================================================
/c/xampp/htdocs/sanskrit-lexicon-scans/vikramor_mw
local urls:
localhost/sanskrit-lexicon-scans/vikramor_mw/app1/?N,N

Github url:
https://sanskrit-lexicon-scans.github.io/vikramor_mw/app1/?N,N


https://sanskrit-lexicon-scans.github.io/vikramor_mw/
shows README.md  (with markdown converted to html)


# -------------------
# edit local csl-websanlexicon ... basicadjust.php


cd /c/xampp/htdocs/cologne/csl-websanlexicon/v02
sh generate_web.sh mw  ../../mw

sh apidev_copy.sh  # simple search gets new basicadjust.php

Push csl-websanlexicon, csl-apidev to github

