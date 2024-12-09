# coding=utf-8
""" link_expand.py for MW
"""
from __future__ import print_function
import sys, re,codecs
#import digentry  

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_recs(fileout,recs):
 # recs an array of Inrec objects
 outarr = []
 for irec,rec in enumerate(recs):
  out = '\t'.join(rec.parts)
  outarr.append(out)
 write_lines_simple(fileout,outarr)

def write_recs2_ok(fileout,recs):
 # recs an array of Inrec objects
 print('write_recs2_ok temporary')
 outarr = []
 for irec,rec in enumerate(recs):
  out = '\t'.join(rec.parts)
  outarr.append(out)
  if True: # dbg
   for out in rec.dbgarr:
    outarr.append(out)

 write_lines_simple(fileout,outarr)

def write_outrecs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outrecs),"cases written to",fileout)

def write_lines(fileout,outarr,printFlag=False):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    if out == None:
     out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def write_lines_simple(fileout,outarr,printFlag=True):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    #if out == None:
    # out = '?'
    f.write(out+'\n')
 if printFlag:
  print(len(outarr),"lines written to",fileout)

def check_standard(ls,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  if re.search(sreg,ls):
   used.append((ireg,sreg))
 return (len(used) == 1)

def check_standarda(ls,sregs):
 used = []
 for ireg,sreg in enumerate(sregs):
  m = re.search(sreg,ls)
  if m:
   used.append((m,ireg))
 flag = (len(used) == 1)
 if flag:
  m,ireg = used[0]
 else:
  m,ireg = None,-1
 return flag,m,ireg

def get_standard_regexes(X):
 d1 = "([ivx]+)"  # MW has lower-case roman numerals for skandha in BhP
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "(\.| fg\.| fgg\.|\. fg\.|\. fgg\.)?"
 regexraws = [
  r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

X = r'BhP\.'
X1 = 'BhP.'
#X = 'Z'
sregs, sregraws = get_standard_regexes(X)

def get_test1_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "( fg\.| fgg\.|\. fg\.|\. fgg|\.|)?"
 regexraws = [
  r'<ls>%s %s,%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
 ]

 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws

def test1(filein,fileout):
 # python link_change.py 
 lines_all = read_lines(filein)
 nok1 = 0
 ntodo1 = 0
 sregs,sregsraw = get_standard_regexes(X)
 ilinestodo1 = []
 for iline,line in enumerate(lines_all):
  used = []
  for ireg,sreg in enumerate(sregs):
   sregraw = sregraws[ireg]
   if re.search(sreg,line):
    used.append((ireg,sregraw))
  if len(used) == 1:
   nok1 = nok1 + 1
  else:
   ntodo1 = ntodo1 + 1
   ilinestodo1.append(iline)
 print('test1 nok1=%s, ntodo1=%s' % (nok1,ntodo1))
 sregs2,raws2 = get_test1_regexes(X)
 nok2 = 0
 ntodo2 = 0
 data2 = []
 nomatch2 = 0
 for iline in ilinestodo1:
  line = lines_all[iline]
  used = []
  for ireg,sreg in enumerate(sregs2):
   m = re.search(sreg,line) 
   if m != None:
    used.append((iline,ireg,m))
  if len(used) == 1:
   nok2 = nok2 + 1
   data2.append(used[0])
  elif len(used) == 0:
   #print('no match2: %s' %line)
   nomatch2 = nomatch2 + 1
  else:
   print('chk:',line)
   print(used)
   #exit(1)
 print('test1 nok2=%s, ntodo2=%s, nomatch2=%s,' % (nok2,ntodo2,nomatch2))
 #assert ntodo2 == 0
 # debug output for ireg=0 type:
 # r'<ls>%s %s,%s,%s%s (.*)</ls>' %(X,d1,d2,d3,Y),
 outarr = []
 #print(len(data2),' data2 length')
 iregcount = {}
 for data in data2:
  iline,ireg,m = data
  if ireg not in iregcount:
   iregcount[ireg] = 0
  iregcount[ireg] = iregcount[ireg] + 1
  #if ireg != 0:
  # continue
  line = lines_all[iline]
  (d1,d2,d3,y,rest) = m.groups()
  if (ireg == 0):
   x = '<ls>%s' % X
  else:
   x = '<ls n="%s' % X
  if y == None:
   y = ''
  #part1 = '%s,%s,%s%s' %(d1,d2,d3,y)
  part1 = '<ls>%s %s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
  part2 = '<ls n="%s">%s</ls>' %(X1,rest)
  #outarr.append('*%s' % line)
  #outarr.append(' ' + part1)
  #outarr.append(' ' + part2)
  outarr.append('%s\t%s\t%s' %(line,part1,part2))

 print(iregcount)
 write_lines_simple(fileout,outarr)

def construct_outdata(data,iregcount):
 iline,ireg,m,line = data
 #outarr = []  
 if ireg not in iregcount:
  iregcount[ireg] = 0
 iregcount[ireg] = iregcount[ireg] + 1
 #line = lines_all[iline]
 (d1,d2,d3,y,rest) = m.groups()
 if y == None:
  y = ''
 if ireg == 0: # X1 is global variable
  part1 = '<ls>%s %s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
 else:
  part1 = '<ls n="%s">%s,%s,%s%s</ls>' %(X1,d1,d2,d3,y)
 part2 = '<ls n="%s">%s</ls>' %(X1,rest)
 outarr = (line,part1,part2)
 return outarr

def get_test2_regexes(X):
 d1 = "([0-9]+)"
 d2 = "([0-9]+)"
 d3 = "([0-9]+)"
 # r"X (ABC|DEF)?"  syntax for optional matches
 # optional . OR optional fg. OR optional fgg.
 Y = "(fg\.| fgg\.|\. fg\.|\. fgg\.)?"
 # The capture groups:
 #  d1, d2, d3, Y (value none or an fg
 regexraws = [
  #r'<ls>%s</ls>' % X,
  r'<ls>%s %s,%s,%s\.%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s">%s,%s,%s\.%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,">%s,%s\.%s (.*)</ls>' %(X,d1,d2,d3,Y),
  r'<ls n="%s %s,%s,">%s\.%s (.*)</ls>' %(X,d1,d2,d3,Y),
 ]
 regexes = list(map(re.compile,regexraws))
 return regexes,regexraws


def test2_analyze(line,sregs2):
 nfound = 0 # number of regexes matching line
 ans = (-1,-1) 
 for ireg,sreg in enumerate(sregs2):
  m = re.search(sreg,line) 
  if m != None:
   ans = ireg,m
   nfound = nfound + 1
 if nfound not in (0,1):
  # multiple matches
  print('ERROR test2_analyze: no matches found for line\nline')
  exit(1)
 return ans

class Inrec:
 def __init__(self,line):
  self.line = line
  parts = line.split('\t')
  self.parts = parts
  self.L = parts[0]
  self.k1 = parts[1]
  self.lnum = parts[2] # string,
  self.ilnum = int(self.lnum)
  self.ls = parts[3]
  ##
  self.m = None
  self.ireg = None
  ##
  self.status = 'TODO'
  ##
  self.dbgarr = []  # array of strings to help debug.
  self.firstls = None # constructed in test2_parse
  
def init_inrecs(filein):
 lines = read_lines(filein)
 recs = []
 for line in lines:
  recs.append(Inrec(line))
 print(len(recs),"read from",filein)
 return recs

def test2_parse_firstls(rec):
 d1,d2,d3,y,rest = rec.m.groups()
 first = (d1,d2,d3,y)
 if y == None:
  y1 = ''
 else:
  #y1 = ' %s' % y
  y1 = y
 ireg = rec.ireg
 # X1 is global
 if ireg == 0:
  z = '<ls>%s %s,%s,%s.%s' % (X1,d1,d2,d3,y1)
 elif ireg == 1:
  z = '<ls n="%s">%s,%s,%s.%s' % (X1,d1,d2,d3,y1)
 elif ireg == 2:
  z = '<ls n="%s %s,">%s,%s.%s' % (X1,d1,d2,d3,y1)
 elif ireg == 3:
  z = '<ls n="%s %s,%s,">%s.%s' % (X1,d1,d2,d3,y1)
 else:
  print('test2_parse_firstls ERROR ireg=%s' % ireg)
  print(rec.line)
  exit(1)
 # reconstruct ls
 testls = '%s %s</ls>' %(z,rest)
 if testls != rec.ls:
  print('test2_parse_firstls FATAL ERROR')
  print('old: %s' % rec.ls)
  print('txt: %s' % testls)
  exit(1)
 firstls = '%s</ls>' % z
 rec.firstls = firstls
 return firstls


def test2_parse_inherit(prev0,cur0):
 # both prev and cur are tuples or lists of length > 0
 # the length of cur is >= length(prev)
 # Expand cur to the same length as prev
 # return the front-padding. Returns None if a problem
 newextra = ()
 prev = tuple(prev0)
 cur = tuple(cur0)
 nprev = len(prev)
 ncur = len(cur)
 if nprev == ncur:
  return newextra
 if ncur > nprev:
  # consider this to be an error
  print('test2_parse_inherit Error 1:')
  print('prev=%s, cur=%s' %(prev,cur))
  return None
 nextra = nprev - ncur
 newextra = tuple(prev[0:nextra])
 # new = newextra + cur
 return newextra

def test_test2_parse_inherit():
 data = [
  [(1,2,3),(4,5,6,7)],
  [(1,2,3),(4,5,6)],
  [(1,2,3),(4,5,)],
  [(1,2,3),(4,)],  # the comma in (4,) is python tuple syntax
  [(1,2,3),()],
 ]
 for prev,cur in data:
  new = test2_parse_inherit(prev,cur)
  print('%s + %s => %s' %(prev,cur,new))
 exit(1)
#test_test2_parse_inherit()

def test2_parse(rec):
 d1,d2,d3,y,rest = rec.m.groups()
 first = (d1,d2,d3,y)
 rest1 = re.sub(r' (fg+\.)',r'_\1',rest)
 rec.dbgarr.append(' first=%s, rest1=%s' %(first,rest1))
 parsevals = []
 firstls = test2_parse_firstls(rec)
 parsevals.append(firstls)
 # 
 rest1parts = rest1.split(' ')
 firstpart = (d1,d2,d3)
 prevpart = firstpart
 for part in rest1parts:
  a = part.split('_') #  fgg
  a1 = a[0]
  if len(a) == 1:
   a2 = ''
  elif len(a) == 2:
   a2 = a[1]
  else:
   print('test2_parse Error 1')
   exit(1)
  if a1.endswith('.'):
   b1 = a1[:-1]
   b2 = a1[-1]
  else:
   b1 = a1
   b2 = ''
  right = b1.split(',')
  left = test2_parse_inherit(prevpart,right)
  if left == None:
   print('test2_parse Error 1',rec.line)
   #exit(1)
  right1 = tuple(right)  # left is tuple
  prevpart = left + right1 # concatenate tuples
  # construct new parseval
  leftparms = ','.join(left)
  rightparms = ','.join(right)
  lsnew = '<ls n="%s' % X1 #X1 is global, the ls abbrev.
  if len(left) == 0:
   lsnew = '<ls n="%s">%s</ls>' %(X1,part)
  else:
   leftstr = ','.join(left)
   lsnew = '<ls n="%s %s,">%s</ls>' %(X1,leftstr,part)
  parsevals.append(lsnew)
 rec.parsevals = parsevals
 rec.status = 'OK'
  
def test2(filein,fileout,fileout1,fileout2 = None):
 # python link_change.py 
 recs_all = init_inrecs(filein)
 nok1 = 0
 ntodo1 = 0
 X = r'BhP\.'
 sregs,sregsraw = get_standard_regexes(X)
 ilinestodo1 = []
 sregs2,raws2 = get_test2_regexes(X)
 nok2 = 0
 ntodo2 = 0
 data2 = []
 nomatch2 = 0
 outarr = []
 iregcount = {}
 recs1 = []  # recs to further analyze
 recs_nomatch2 = []
 for irec,rec in enumerate(recs_all):
  flag = check_standard(rec.ls,sregs)  
  if flag:
   rec.status = 'STANDARD'
   continue # nothing else to do
  ireg,m = test2_analyze(rec.ls,sregs2)
  if ireg == -1:
   rec.status = 'CANTDO'
   # this line can't be analyzed by this program
   #nomatch2 = nomatch2 + 1
   #recs_nomatch2.append(rec)
   continue
  rec.ireg = ireg
  rec.m = m
  #recs1.append(rec)
  #nok2 = nok2 + 1
 # write_recs(fileout,recs1)
 #print('test2 nok1=%s, ntodo1=%s' % (nok1,ntodo1))
 #print('test2 nok2=%s, ntodo2=%s, nomatch2=%s,' % (nok2,ntodo2,nomatch2))
 #write_lines_simple(fileout2,[rec.line for rec in recs_nomatch2])

 for rec in recs_all:
  if rec.status in ['STANDARD','CANTDO']:
   pass
  else:
   # sets rec.status to OK
   test2_parse(rec)
   assert rec.status == 'OK'
 nall = len(recs_all)
 print('%05d %s' % (nall,'ALL'))
 ntot = 0
 for status in ['STANDARD','CANTDO','OK']:
  recstemp = [rec for rec in recs_all if rec.status == status]
  n = len(recstemp)
  print('%05d %s' % (n,status))
  ntot = ntot + n
 print('%05d %s' % (ntot,'TOTAL'))
 if nall == ntot:
  print('all cases accounted for')
 else:
  print('ERROR: ALL and TOTAL should be the same!')
  exit(1)
 # write prechange_records (status == OK) to fileout
 outarr = []
 for rec in recs_all:
  if rec.status != 'OK':
   continue
  parsetxt = ' '.join(rec.parsevals)
  parsetext1 = parsetxt.replace('_fg',' fg') # remove intermediate '_'
  out = '%s\t%s' %(rec.line,parsetxt)
  outarr.append(out)
 write_lines_simple(fileout,outarr)
 # write CANTDO records in similar format, but with an <lsx 
 outarr = []
 for irec,rec in enumerate(recs_all):
  if rec.status != 'CANTDO':
   continue
  lsx = rec.ls.replace('<ls','<lsx')
  out = '%s\t%s' %(rec.line,lsx)
  outarr.append(out)
 write_lines_simple(fileout1,outarr)
  
if __name__=="__main__":
 filein = sys.argv[1]  # 
 fileout = sys.argv[2] #
 fileout1 = sys.argv[3]
 X = r'BhP\.'
 test2(filein,fileout,fileout1)
