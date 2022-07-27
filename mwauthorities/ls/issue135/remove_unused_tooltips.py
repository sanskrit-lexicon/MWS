#-*- coding:utf-8 -*-
"""remove_unused_tooltips.txt
"""
import sys,re,codecs

class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  # pwg has code, abbrevUpper, abbrevLower,tip
  try:
   self.code,self.abbrev,self.tipmain,self.tipcat = line.split('\t')
  except:
   print('Tooltip error:\n%s' %line)
   parts=line.split('\t')
   exit(1)
  self.keep = True  # will be modified later
  self.tip = '%s (%s)' %(self.tipmain,self.tipcat)
  
def init_tooltip(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip(x) for x in f]
 print(len(ans),'tooltips from',filein)
 return ans

class Tooltip1(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  line1 = re.sub(r'^0+ +[^ ]+','',line)
  # pwg has code, abbrevUpper, abbrevLower,tip
  try:
   self.code,self.abbrev,self.tipmain,self.tipcat = line1.split(' :: ')
  except:
   print('Tooltip1 error:\n%s' %line)
   parts=line.split('\t')
   exit(1)
  
def init_tooltip1(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip1(x) for x in f]
 print(len(ans),'tooltip1 objects from',filein)
 return ans

def mark_drop(tips,tips1):
 d1 = {}
 for tip in tips1:
  a = tip.abbrev
  if a in d1:
   print('Duplicate tip1 abbrev',a)
  d1[a] = True
 d = {}
 for tip in tips:
  a = tip.abbrev
  if a in d:
   print('Duplicate tip abbrev',a)
  d[a] = True
  if a in d1:
   tip.keep = False
   
def write_tips(fileout,tips):
 with codecs.open(fileout,"w","utf-8") as f:
  n = 0
  for tip in tips:
   if tip.keep:
    line = tip.line
    line = line.replace(' (edit)','')
    f.write(line+'\n')
    n = n + 1
 print(n,"tips written to",fileout)
 
def check_period(tips):
 """ when abbreviation has 2 periods. This may cause display problems """
 num = 0
 for tip in tips:
  a = tip.abbrev
  periods = re.findall('[.]',a)
  n = len(periods)
  if n>1:
   print(tip.code,tip.abbrev,'has %s periods' %n)
   num = num + 1
 print(num,'tooltips have more than 1 period in abbreviation')
 
if __name__=="__main__":
 filein = sys.argv[1] #  old tooltips
 filein1 = sys.argv[2] # tooltips to remove (slightly different format)
 fileout = sys.argv[3] # remaining tooltips
 tips = init_tooltip(filein)
 tips1 = init_tooltip1(filein1)
 mark_drop(tips,tips1)
 write_tips(fileout,tips)
 check_period(tips)
 
