
Start with temp_mw2.txt and makes some additional changes.
temp_mw2.txt is copy of csl-orig/v02/mw/mw.txt at commit
2d8382ab220c52a39f79dd13976545231d87e292

----------------------------------------------
In preparation for change4a (abbreviation markup):
python filter_tag_line.py temp_mw2.txt filter_tag_line.txt
This generates line numbers in temp_mw2.txt where an xml element (always ls)
 crosses a line-break. We don't want such.
cp temp_mw2.txt temp_mw3.txt
Using the line-numbers in filter_tag_line.txt, manually adjust temp_mw3.txt
  NOTE: this editing merges and deletes lines.

----------------------------------------------
Add abbreviation markup
cp temp_mw3.txt temp_mw4.txt
touch change_4.txt
Add change transactions to change_4.txt in multiple steps.
The following gives a summary.  At each stage, we apply the
change_4.txt changes to temp_mw3.txt to get temp_mw4.txt, using updateByLine.py.

python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

Here are summaries of the steps.

python change4a.py 1 temp_mw4.txt temp_change4a_1.txt  # 1 is an option
  unmarked cf (37)  Here we add markup <ab>cf.</ab> as appropriate.
  
  Now insert temp_change4a_1.txt into bottom of change_4.txt
    Note: the analogue of this step is done in all the steps below.
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 2 temp_mw4.txt temp_change4a_2.txt 
  unmarked sc (98)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 3 temp_mw4.txt temp_change4a_3.txt 
  unmarked aor (6)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 4 temp_mw4.txt temp_change4a_4.txt 
  unmarked subj (5)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 5 temp_mw4.txt temp_change4a_5.txt 
  unmarked abstr (10)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 6 temp_mw4.txt temp_change4a_6.txt 
  unmarked gram (308)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 7 temp_mw4.txt temp_change4a_7.txt 
  unmarked irreg (34)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 8 temp_mw4.txt temp_change4a_8.txt 
  unmarked q.v. and qq.v. (45)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 9 temp_mw4.txt temp_change4a_9.txt 
  unmarked <ls>A.</ls>D. -> <ab>A.D.</ab> (19)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

So far, so good!

manual
  abl. (2)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 10 temp_mw4.txt temp_change4a_10.txt 
  unmarked acc (38)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
 [add.   (6)   << help wanted What is tooltip?
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
 cl. (5)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python change4a.py 11 temp_mw4.txt temp_change4a_11.txt 
  unmarked comp (35)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py conj,cons,dat temp_mw4.txt temp_filter_ab.txt
 conj (0)
 cons (0)
 dat  (4)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py defect,dimin,dram,du temp_mw4.txt temp_filter_ab.txt
 defect (0)
 dimin (1)
 dram (0)
 du   (12)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py 'e.g.,ed,encl'  temp_mw4.txt temp_filter_ab.txt
e.g. 0
ed 1
encl 5
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt
 (save temp_mw4_encl.txt)
 
python filter_ab.py ep,esp,etym  temp_mw4.txt temp_filter_ab.txt
ep 0
esp 5
etym 1
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
  f.  36  (feminine)
  Note f. also occurs in context of 'ls' meaning 'following (pages, verses, etc)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py fem,fig,fr,fut  temp_mw4.txt temp_filter_ab.txt
fem 29
fig 10
fr 53
fut 2
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py g,gen,gend  temp_mw4.txt temp_filter_ab.txt
g 13
gen 24
gend 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py geom,gram,ib,ibc  temp_mw4.txt temp_filter_ab.txt
geom 0
gram 1
ib 5
ibc 5
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py id,ifc  temp_mw4.txt temp_filter_ab.txt
id 76
ifc 5
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py impers,impf,impv,ind,inf  temp_mw4.txt temp_filter_ab.txt
impers 1
impf 1
impv 0
ind 13
inf 3
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py instr,inst,intens,interj,interpol,intrans  temp_mw4.txt temp_filter_ab.txt
instr 18
inst 15
intens 1
interj 0
interpol 0
intrans 52
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py irr,irreg,lat,lit  temp_mw4.txt temp_filter_ab.txt
irr 3
irreg 0
lat 0
lit 5
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py loc,log  temp_mw4.txt temp_filter_ab.txt
loc 12
log 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
 m. 88 generally changed to <ab>m.</ab>, but some lex markup might be better)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py mc,math,medic,metron,mfn  temp_mw4.txt temp_filter_ab.txt
mc 0
math 0
medic 0
metron 5
mfn 19
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py mf,mn,myth  temp_mw4.txt temp_filter_ab.txt
mf 0
mn 2
myth 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
 (n.  40
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py neg,negat,nom,obs  temp_mw4.txt temp_filter_ab.txt
neg 1
negat 0
nom 5
obs 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
<ab>opp. to</ab> -> <ab>opp.</ab> to (7)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py onomat,opp,opt,orig  temp_mw4.txt temp_filter_ab.txt
onomat 1
opp 1
opt 0
orig 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py oxyt,p.p,pp,p.p.p temp_mw4.txt temp_filter_ab.txt
oxyt 2
p.p 0
pp 21
p.p.p 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py parox,partic,patr,periphr temp_mw4.txt temp_filter_ab.txt
parox 0
partic 0
patr 0
periphr 1
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
 pass 1
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt
 
python filter_ab.py perf,perh,pers,pf,phil temp_mw4.txt temp_filter_ab.txt
perf 1
perh 0
pers 0
pf 3
phil 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
poet 0
possess 0

python filter_ab.py pl,pr,prec temp_mw4.txt temp_filter_ab.txt
pl 1
pr 1
prec 1
pres 1 (manual)
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py prep,prepos,priv,prob temp_mw4.txt temp_filter_ab.txt
prep 0
prepos 0
priv 0
prob 9
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py pron,pronom,propar,proparox,redupl temp_mw4.txt temp_filter_ab.txt
pron 0
pronom 0
propar 0
proparox 2
redupl 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py reflex,rhet,rt,rts,sc,st temp_mw4.txt temp_filter_ab.txt
reflex 0
rhet 0
rt 0
rts 0
sc 0
st 1
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py scil,seq,seqq,sev,sg,sing temp_mw4.txt temp_filter_ab.txt
scil 2
seq 0
seqq 33
sev 0
sg 144
sing 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py subst,suff,superl,surg temp_mw4.txt temp_filter_ab.txt
subst 0
suff 0
superl 151
surg 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
s.v. 6
ss.vv. 4
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py trans,vb,voc,vow temp_mw4.txt temp_filter_ab.txt
trans 62
vb 0
voc 0
vow 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

manual
intr 30
v.r. 0
w.r. 2
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

python filter_ab.py wk,wks  temp_mw4.txt temp_filter_ab.txt
wk 1
wks 0
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

-------------------------------------------------------------
capital letter abbreviations
python filter_ab.py Sept,Oct,Nov,Them,Theme,Thema,Transl,Umbr temp_mw4.txt temp_filter_ab.txt

Gorr 1
OGerm 1
Lin 7
Sl 2
Vārt 1
Sept 1
Oct 1
Nov 1
python updateByLine.py temp_mw3.txt change_4.txt temp_mw4.txt

lex problems with tamopaha (4)
lex problems with pitfyAna (2)
lex problems with sAmudrika (2)
  

-------------------------
cp temp_mw4.txt /c/xampp/htdocs/cologne/csl-orig/v02/mw/mw.txt
 and install new mw.txt
 




