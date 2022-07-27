#-*- coding:utf-8 -*-
"""make_change_ls.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,newline,idx):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.newline = newline
  self.idx = idx 

def compute_newpart(part,changedata):
 for idata,data in enumerate(changedata):
  old,new = data
  newpart = part.replace(old,new)
  if newpart != part:
   return newpart,idata  # apply first change 
 return part,-1 # no changes apply

def compute_newline(line,changedata):
 parts = re.split(r'(<ls[^<]*</ls>)',line)
 newparts = []
 idxnew = -1
 for part in parts:
  if part.startswith('<ls'):
   newpart,idx = compute_newpart(part,changedata)
   if idx != -1:
    # part was changed
    if False: # dbg
     change = changedata[idx]
     print(change)
    if idxnew != -1:
     # hard to handle multiple changes in a line
     print('compute_newline multiple:',line)
    idxnew = idx
  else:
   newpart = part
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline,idxnew

def init_cases(lines,changedata):
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   continue 
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  newline,changeidx = compute_newline(line,changedata)
  if newline == line:
   continue
  # generate a case
  cases.append(Case(metaline,iline,line,newline,changeidx))

 print(len(cases),'lines modified')
 return cases

def write_cases(fileout,cases,changedata):
 n = 0
 nchg = 0
 outrecs = []
 for idx,data in enumerate(changedata):
  oldtxt,newtxt = data
  idxcases = [c for c in cases if c.idx == idx]
  ncases = len(idxcases)
  # section title
  outarr = []
  outarr.append('; ======================================================')
  outarr.append('; %s -> %s (%s instances)' %(oldtxt,newtxt,ncases))
  outarr.append('; ======================================================')
  outrecs.append(outarr)
  # each case
  #print(idx,oldtxt,newtxt,ncases)
  nchg = nchg + ncases
  for case in idxcases:
   outarr = []
   n = n + 1
   outarr.append(r'; -------------------------------------------------------')
   metaline = re.sub(r'<k2>.*$','',case.metaline)
   outarr.append('; %s' % metaline)
   #outarr.append('; %s ' % case.match)
   iline = case.iline
   lnum = iline + 1
   line = case.line
   newline = case.newline
   outarr.append('%s old %s' %(lnum,line))
   outarr.append('%s new %s' %(lnum,newline))
   outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(nchg,'changes written to',fileout)

changedata = [
 ('AAnukr.' , 'AV.Anukr.'),
 ('AitrAnukr.' , 'ĀtrAnukr.'),
 ('Burnell.' , 'Burnell*'),
 ('Divyâs.' , 'Divyâv.'),
 ('Jam.' , 'Jaim.'),
 ('Kop.' , 'Vop.'),
 ('Kāvy.' , 'Kāv. '),
 ('Naith.' , 'Naiṣ.'),
 ('Nastar.' , 'Hastar.'),
 ('NādapUp.' , 'NādabUp.'),
 ('Parāś.' , '*Parāś.'),
 ('Pallcat.' , 'Pañcat.'),
 ('Pariś.' , 'ĀśvGṛ.Pariś.'),
 ('Parvad.' , 'Sarvad.'),
 ('Pañcav.' , 'Pañcar.'),
 ('PhP.' , 'BhP.'),
 ('Prasamar.' , 'Prasannar.'),
 ('Pālār.' , '*Pālār.'),
 ('Rasav.' , 'Rasar.'),
 ('Rudraj.' , 'Rudray.'),
 ('SaṃjUp.' , 'SaṃnyUp.'),
 ('SāmarBr.' , 'SāmarBr.'),
 ('Anir.' , '*Anir.'),
 ('VaṛB-S.' , 'VarBṛS.'),
 ('VB.' , 'VP.'),
 ('ŚāṅgS.' , ' ŚārṅgS.'),
 ('Śāṅkh.' , 'ŚāṅkhBr.'),
 ('Kāth.' , 'Kath. mw.txt'),
 ('Mantram' , 'Mantram.'),
 ('Krauñca' , '*Krauñca'),
 ('Bañc.' , 'Pañc.'),
 ('Manu' , 'Manu.'),
 ('(B)' , '(B.)'),
 ]

if __name__=="__main__":

 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines,changedata) 
 print(len(cases),'cases')
 write_cases(fileout,cases,changedata)
  
