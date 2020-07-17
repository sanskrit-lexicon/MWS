echo "verbs1_merge0.txt"
python verbs1_merge.py 0 verbs1_merge0.txt ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt
echo "verbs1_merge1_1v.html"
python verbs1_merge.py 1h,1v verbs1_merge1_1v.html ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt
echo "verbs1_merge2.txt"
python verbs1_merge.py 2 verbs1_merge2.txt ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt
echo "copying html file(s) to sanskrit-lexicon.github.io"

echo "verbs1_merge1_1vmw.html (links to dalglob1"
python verbs1_merge.py 1hmw,1v verbs1_merge1_1vmw.html ../mwverbs/mwverbs2.txt ap90,ben,bur,cae,ccs,gra,krm,md,pwg,pw,skd,stc,vcp,wil,shs,yat ../../ > verbs1_merge_log.txt

cp verbs1_merge1_1v.html ../../sanskrit-lexicon.github.io/verbs/verbs01/

cp verbs1_merge1_1vmw.html ../../sanskrit-lexicon.github.io/verbs/verbs01/
