#-*- coding:utf-8 -*-
"""bbar2.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,match,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.newline = newline
  
def init_cases(lines,recd):
 metaline = None
 imetaline = None
 page = None
 prevls = None
 ndata = 0 # number of lines between <L> and <LEND>
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline = iline
   continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   continue
  if metaline == None:
   continue # not in an entry
  if iline != (imetaline + 1):
   continue
  m = re.search(r'^<L>(.*?)<pc>',metaline)
  L = m.group(1)
  if L not in recd:
   continue
  rec = recd[L]
  rec.mwmetaline = metaline
  rec.mwheadline = line
  rec.imetaline = imetaline  

def write_recs_helper(rec):
 outarr = []
 meta = rec.mwmetaline
 meta = re.sub(r'<k2>.*$','',meta)
 outarr.append('; %s' % meta)
 L = rec.L
 iline = rec.imetaline+1
 lnum = iline + 1 # lnum of mwheadline
 old = rec.mwheadline
 # make change if rec.headline (with bbar removed) is same as rec.mwheadline
 ABline = rec.headline  # headline from AB
 ABline1 = ABline.replace('¦','')
 ABline2 = ABline.replace('¦',' ¦')
 if ABline1 == old:
  # add space before ¦
  new = ABline2
 elif ABline2 == old:
  outarr[0] = '%s TODONE' %outarr[0]
  new = old
 else:
  outarr[0] = '%s TODO' %outarr[0]  # identify need for manual change
  # write ABline, for referece
  outarr.append('; cf: %s' % ABline)
  new = old
 if ABline2 != old:
  outarr.append('%s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,new))
  outarr.append('; ------------------------------------------------------')
 else: # comment out changes
  outarr.append('; %s old %s' %(lnum,old))
  outarr.append(';')
  outarr.append('; %s new %s' %(lnum,new))
  outarr.append('; ------------------------------------------------------')
 return outarr

def write_recs(fileout,recs):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(recs)))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for rec in recs:  
  outarr = write_recs_helper(rec)
  outrecs.append(outarr)

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(recs),'recs written to',fileout)

class Rec:
 d = {}
 def __init__(self,metaline,headline):  
  m = re.search(r'^<L>(.*?)<pc>',metaline)
  L = m.group(1)
  self.L = L
  self.metaline = metaline
  self.headline = headline
  # next filled in later in init_cases
  self.mwmetaline = None
  self.imetaline = None
  self.mwheadline = None
  if L in Rec.d:
   print('Rec: duplicate L=',L)
  Rec.d[L] = self
  
def generate_recs(f):
 # 
 reclines = []
 irec = 0
 for line in f:
  line = line.rstrip('\r\n')
  if line == '':
   pass
  elif line.startswith('<L>'):
   reclines.append(line)
  elif line == '<LEND>':
   assert len(reclines) == 2
   yield Rec(reclines[0],reclines[1])
   reclines = []
  else:
   reclines.append(line)
  
def init_recs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = list(generate_recs(f))
 print(len(recs),"recs from",filein)
 return recs

if __name__=="__main__":
 filein1 = sys.argv[1]  # AB insertion of bbar in 'and' rec
 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 recs = init_recs(filein1)
 recd = Rec.d
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 init_cases(lines,recd) # modifies recs
 write_recs(fileout,recs)
  
