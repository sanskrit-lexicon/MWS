# coding=utf-8
""" lsfix2.py
  2 nparm values
"""
from __future__ import print_function
import sys, re,codecs
import digentry
from lsfix2_parm import targetobj2

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
   for out in outarr:
    f.write(out+'\n')  
 print(len(outarr),"lines written to",fileout)

def get_regexes_all(lscode):
 # lscode = targetparms['lscode']
 lscode1 = lscode.replace('.','[.]')
 a = []
 a.append(r'<ls>%s (.*?)</ls>' % lscode1)
 a.append(r'<ls n="%s(.*?)">(.*?)</ls>' % lscode1)
 return a

class REGEX1:
 def __init__(self,n,S):
  self.n = n  # a number 
  self.S = S
  self.W = self.reg_help(self.n)
  self.regex = '^' + self.W + self.S
  
 def reg_help(self,n):
  a = []
  for i in range(n):
   a1 = '([0-9]+)'
   a.append(a1)
  ans = ','.join(a)
  return ans

def get_REGEXes_next(nparm):
 sfxes = ['\.' , '', '\. fg\.', '\. fgg\.', ', v\. l\.']
 a = []
 for n in range(1,nparm+1):
  for S in sfxes:
   a.append(REGEX1(n,S))
 b = sorted(a,key = lambda x: len(x.regex), reverse=True)
 return b

class REGEX:
 def __init__(self,X,nY,nZ,S):
  """   
   generate regex from parameters
  """
  self.X = X
  self.nY = nY
  self.nZ = nZ
  self.S = S
  self.Z = self.reg_help(self.nZ)
  self.Y = None
  if self.nY == None:
   self.regex = r'<ls>%s %s%s</ls>' %(self.X,self.Z,self.S)
   self.nparm = self.nZ
   #print(self.regex)
  elif self.nY == 0:
   self.Y = ''
   self.regex = r'<ls n="%s">%s%s</ls>' %(self.X,self.Z,self.S)
   self.nparm = self.nZ
  else: # nY a pos. integer
   self.Y = self.reg_help(self.nY)
   # note comma : ,">
   self.regex = r'<ls n="%s %s,">%s%s</ls>' %(self.X,self.Y,self.Z,self.S)
   self.nparm = self.nY + self.nZ
   #print(self.regex)
  self.regex_first = self.regex.replace('</ls>',' (.*)</ls>')
 def reg_help(self,n):
  a = []
  for i in range(n):
   a1 = '([0-9]+)'
   a.append(a1)
  ans = ','.join(a)
  return ans
 def toStr(self):
  if self.Y == None:
   ans = '<ls>%s %s%s</ls>' %(self.X,self.Z,self.S)
  else:
   ans = '<ls n="%s%s">%s%s</ls>' %(self.X,self.Y,self.Z,self.S)
  return ans
 
def get_REGEXes_standard(lscode,nparm):
 # lscode = targetparms['lscode']
 lscode1 = lscode.replace('.','[.]')
 # nparm = targetparms['nparm']
 sfxes = ['\.' , '', '\. fg\.', '\. fgg\.', ', v\. l\.']
 aREGs = []
 for S in sfxes:
  aREGs.append(REGEX(lscode1,None,nparm,S))
 for nY in range(nparm):
  nZ = nparm - nY
  for S in sfxes:
   aREGs.append(REGEX(lscode1,nY,nZ,S))
 return aREGs

class Instance:
 def __init__(self,m,entry,iline,regexes_standard,nparm):
  self.m = m
  self.entry = entry
  self.iline = iline
  self.status = None
  self.matchstr = m.group(0)
  self.nparm = nparm
  for regex in regexes_standard:
   if re.search(regex,self.matchstr):
    self.status = True
    break
  self.expansions = []

def skip_instance(str,starts):
 for start in starts:
  if str.startswith(start):
   return True
 return False

def get_instances_all(entries, regexes_all,regexes_standards,skip_starts,
                      skip1_starts):
 regs = [re.compile(regex) for regex in regexes_all]
 instances = []
 nparms = list(regexes_standards.keys())
 for entry in entries:
  for iline,line in enumerate(entry.datalines):
   for reg in regs:
    for m in re.finditer(reg,line):
     matchstr = m.group(0) # <ls..</ls>
     if skip_instance(matchstr,skip_starts):
      continue
     if skip_instance(matchstr,skip1_starts):
      continue
     instanced = {}
     for nparm in nparms:
      regexes_standard = regexes_standards[nparm]
      instanced[nparm] = Instance(m,entry,iline,regexes_standard,nparm)
     instances.append(instanced)
 return instances

def ABC(A,C):
 """ A and C are strings
  C is the end of A.  Find B so A = B + C
  Solution from Copilot
 """
 if A.endswith(C):
  return A[:-len(C)]   # string slicing
 else:
  raise ValueError("String %s does not end with string %s" % (A,C))

def fix_instance_rest_ls(lscode,parms1,rest1):
 if parms1 == []:
  ans = '<ls n="%s">%s</ls>' %(lscode,rest1)
 else:
  Y = ','.join(parms1)
  ans = '<ls n="%s %s,">%s</ls>' %(lscode,Y,rest1)
 return ans
def fix_instance_rest(lscode,parms,rest,REGEXES_next,dbg=False):
 #dbg = True
 if dbg:
  print('fix  input:')
  print('    lscode:',lscode)
  print('     parms:',parms)
  print('      rest:"%s"' % rest)
 #if dbg: print('fix input: parms=%s, rest=%s' %(parms,rest))
 REG_next = None
 for r in REGEXES_next:
  m = re.search(r.regex,rest)
  if m != None:
   REG_next = r
   break
 if REG_next == None:
  if dbg:
   print('ERROR in INPUT')
  return None
 parms_rest = list(m.groups())
 rest1 = m.group(0)
 newrest = rest[len(rest1):]
 n = len(parms)
 n2 = len(parms_rest)
 assert n2 <= n
 n1 = n - n2
 parms1 = parms[0:n1]
 newparms = parms1 + parms_rest
 newls = fix_instance_rest_ls(lscode,parms1,rest1)
 if dbg:
  print('fix output:')
  print('     newls:',newls)
  print('  newparms:',newparms)
  print('   newrest:"%s"' % newrest)
 return (newls,newparms,newrest)

def fix_instance_rest_all(lscode,parms,rest,REGEXES_next,dbg=False):
 result = []
 newparms = parms
 newrest = rest
 status = False
 while True:
  lastfix = fix_instance_rest(lscode,newparms,newrest,REGEXES_next,dbg=dbg)
  if lastfix == None:
   break
  (newls,newparms,newrest1) = lastfix
  # trim spaces from left of newrest1
  newrest = newrest1.lstrip()
  result.append(newls)
  if newrest == '':
   status = 'fixed'
   break
 if dbg:
  print('result:')
  for i,x in enumerate(result):
   print('   ',i,x)
 return status,result

def test_fix():
 lscode = 'X'
 nparm = 3
 REGEXES_next = get_REGEXes_next(nparm)
 parms = ['3', '14', '19']
 rest = '15,65. fg. 66.'
 rest = '15,65. fg. 66. 2,3,4'
 #rest = '15,65. fg.'
 # rest = ',a. fg.'
 rest = '2,3,4.'
 rest = '10. 2,3,4.'
 rest = '10. 2,3.'
 status,result = fix_instance_rest_all(lscode,parms,rest,REGEXES_next,dbg=False)
 
#test_fix()

def fix_instance_main(lsstr,REG,REGEXES_next):
 dbg = False
 reg = REG.regex_first
 m = re.search(reg,lsstr)
 assert m != None
 lscode = REG.X
 if REG.nY == None:
  nparm = REG.nZ
 else:
  nparm = REG.nY + REG.nZ
 expansions = []
 parms = [m.group(i+1) for i in range(nparm)]
 rest = m.group(nparm+1)
 C =' ' + rest + '</ls>'
 B = ABC(lsstr,C)
 exp1 = B + '</ls>'
 expansions.append(exp1)
 if dbg:
  print('lscode=',lscode,'nparm=',nparm)
  print('lsttr=',lsstr)
  print('exp1 =',exp1)
  print('parms=',parms)
  print('rest =',rest)
 # Now need to parse rest.
 status,result = fix_instance_rest_all(lscode,parms,rest,REGEXES_next)
 for x in result:
  expansions.append(x)
 return status,expansions
 
def fix_instance(lsstr,REGS_standard):
 REGS_first = sorted(REGS_standard,key = lambda x: len(x.regex_first),
                     reverse=True)
 for REG in REGS_first:
  reg = REG.regex_first
  m = re.search(reg,lsstr)
  if m != None:
   break
 if m != None:
  status = 'fixable'
  REG_first = REG
  nparm = REG.nparm
  REGEXES_next = get_REGEXes_next(nparm)
  status,expansions = fix_instance_main(lsstr,REG_first,REGEXES_next)
 else:
  status = None
  expansions = []
 return status,expansions

def write_instances_temp(fileout,instances):
 outarr = []
 statd = {}
 
 for instanced in instances:
  for nparm in instanced:
   instance = instanced[nparm]
   parse = ' '.join(instance.expansions)
   parse = parse.replace('[.]','.')
   iline = instance.iline
   entry = instance.entry
   lnum = entry.linenum1 + iline + 1
   status = instance.status
   out = '%s\t%s\t%s\t%s\t%s' % (status,lnum,nparm,instance.matchstr,parse)
   outarr.append(out)
   #if status not in statd:
   # statd[status] = 0
   #statd[status] = statd[status] + 1
  outarr.append('')
 write_lines(fileout,outarr)
 #for status in statd:
 # print(status,statd[status])

def write_instances(fileout,instances):
 outarr = []
 statd = {}
 
 for instance in instances:
  parse = ' '.join(instance.expansions)
  parse = parse.replace('[.]','.')
  iline = instance.iline
  entry = instance.entry
  lnum = entry.linenum1 + iline + 1
  status = instance.status
  nparm = instance.nparm
  out = '%s\t%s\t%s\t%s\t%s' % (status,nparm,lnum,instance.matchstr,parse)
  outarr.append(out)
  stat1 = (status,nparm)
  if stat1 not in statd:
   statd[stat1] = 0
  statd[stat1] = statd[stat1] + 1
 write_lines(fileout,outarr)
 for stat1 in statd:
  print(stat1,statd[stat1])


def init_skip_starts(targetobj2):
 ans = []
 #print('init_skip_starts', targetobj2)
 if not ('skip' in targetobj2):
  return ans
 skips = targetobj2['skip'] # array of string
 for skip in skips:
  ans.append('<ls>%s' % skip)
  ans.append('<ls n="%s' % skip)
 if False: # dbg
  print('skip starts',ans)
 return ans

def init_skip1_starts(targetobj2):
 ans = []
 if 'skip1' in targetobj2:
  ans = targetobj2['skip1']
 #print('init_skip1_starts: ',ans)
 return ans

if __name__=="__main__":
 code = sys.argv[1]
 filein = sys.argv[2]  # xxx.txt kosha
 fileout = sys.argv[3] # output file
 if code not in targetobj2:
  print('Unknown code:',code)
  exit(1)
 targetparms = targetobj2[code]
 skip_starts = init_skip_starts(targetparms)
 skip1_starts = init_skip1_starts(targetparms)
 lscode = targetparms['lscode']
 regexes_all = get_regexes_all(lscode)
 nparms = targetparms['nparms']
 REGEXes_standard = {}
 regexes_standard = {}
 for nparm in nparms:
  REGEXes_standard[nparm] = get_REGEXes_standard(lscode,nparm)
  a = [reg.regex for reg in REGEXes_standard[nparm]]
  regexes_standard[nparm] = sorted(a,key = lambda x: len(x),reverse=True)
  
 entries = digentry.init(filein)
 instances_all = get_instances_all(entries,
                                   regexes_all, regexes_standard,
                                   skip_starts, skip1_starts)
 for instanced in instances_all:
  for nparm in instanced:
   instance = instanced[nparm]
   if instance.status == None:
    status,expansions = fix_instance(instance.matchstr,REGEXes_standard[nparm])
    instance.expansions = expansions
    instance.status = status
   
 instances_all_select = []
 for instanced in instances_all:
  nparm_select = None
  nparms = list(instanced.keys())
  for nparm in nparms:
   instance = instanced[nparm]
   if instance.status in [True,'fixed']:
    nparm_select = nparm
    break
  if nparm_select == None:
   nparm_select = nparms[0]  # arbitrary
  instance_select = instanced[nparm_select]
  instances_all_select.append(instance_select)
 write_instances(fileout,instances_all_select)
 exit(1)

