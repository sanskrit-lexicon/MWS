version=$1
cp temp_mw_${version}.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
cd /c/xampp/htdocs/cologne/csl-pywork/v02
sh generate_dict.sh mw  ../../mw
sh xmlchk_xampp.sh mw
cd /c/xampp/htdocs/cologne/csl-orig/v02/mw/
git restore mw.txt
