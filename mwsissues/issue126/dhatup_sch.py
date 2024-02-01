#-*- coding:utf-8 -*-
"""dhatup_sch.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,dhatups,iline,line):
  self.metaline = metaline
  self.dhatups = dhatups
  self.iline = iline
  self.line = line
  
def init_cases(lines):
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
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  instances = []
  for m in re.finditer(r'<ls>(Dhātup\..*?)</ls>',line):
   instance_full = m.group(0)
   instance_inner = m.group(1)
   instance_flag = check_form(instance_inner)
   instance = (instance_full,instance_inner,instance_flag)
   instances.append(instance)
  for m in re.finditer(r'<ls n="(Dhātup\..*?)">(.*?)</ls>',line):
   instance_full = m.group(0)
   instance_inner = m.group(1) + ' ' + m.group(2)
   instance_flag = check_form(instance_inner)
   instance = (instance_full,instance_inner,instance_flag)
   instances.append(instance)
  if instances != []:
   # generate a case
   cases.append(Case(metaline,instances,iline,line))

 print(len(cases),"dhatupada cases")
 return cases

def check_form(x):
 if x == 'Dhātup.': 
  return True
 m =  re.search(r'^Dhātup\. ([0-9]+)',x)
 if m == None:
  return False
 section = int(m.group(1))
 if section < 1:
  return False
 if section > 35:
  return False
 m = re.search(r'^Dhātup\. ([0-9]+), [0-9]+\.?$',x)
 if m:
  return True
 """  
 m = re.search(r'^Dhātup\. ([0-9]+), [0-9]+, v\. l\.$',x)
 if m:
  return True
 """
 return False
  
def write_cases(fileout,cases):
 n = 0
 outrecs = []
 nprob = 0
 for case in cases:
  outarr = []
  n = n + 1
  #outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  #outarr.append('; %s' % metaline)
  for x in case.dhatups:
   (instance_full,instance_inner,instance_flag) = x
   if instance_flag:
    y = instance_inner
   else:
    y = instance_inner + ' ?'
    nprob = nprob + 1
   out = '%s : %s' %(metaline,y)
   outarr.append(out)
  outrecs.append(outarr)
 print(nprob,"cases with non-standard form")
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)

def make_change_instance(x):
 # <ls>X a, b, v. l.</ls> -> <ls>X a, b</ls>, v. l.
 y = re.sub(r'<ls>Dhātup\. ([0-9]+), ?([0-9]+), v. l.</ls>',
            r'ls>Dhātup. \1, \2</ls>, v. l.',
            x)
 if y != x:
  return y
 # <ls>X a, b. c, d.</ls>
 y = re.sub(r'<ls>Dhātup\. ([0-9]+), ?([0-9]+)\. ([0-9]+), ?([0-9]+\.?)</ls>',
            r'<ls>Dhātup. \1, \2.</ls> <ls n="Dhātup.">\3, \4</ls>',
            x)
 if y != x:
  return y
 return None
 # <ls>X a, b. c, d, v. l.</ls>
 y = re.sub(r'<ls>Dhātup\. ([0-9]+), ?([0-9]+)\. ([0-9]+), ?([0-9]+), v\. l\.</ls>',
            r'<ls>Dhātup. \1, \2.</ls> <ls n="Dhātup.">\3, \4, v. l.</ls>',
            x)
 if y != x:
  return y

 # <ls>X a, b. c, d. e, f.</ls>
 y = re.sub(r'<ls>Dhātup\. ([0-9]+), ?([0-9]+)\. ([0-9]+), ?([0-9]+)\. ([0-9]+), ?([0-9]+\.?)</ls>',
            r'<ls>Dhātup. \1, \2.</ls> <ls n="Dhātup.">\3, \4.</ls>  <ls n="Dhātup.">\5, \6</ls>',
            x)
 if y != x:
  return y

 return None
 
def write_changes(fileout,cases):
 n = 0
 outrecs = []
 nprob = 0
 nautochg = 0
 for case in cases:
  outarr = []
  n = n + 1
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  change_instances = [x for x in case.dhatups if not x[2]]
  if change_instances == []:
   continue
  iline = case.iline
  oldline = case.line
  outarr.append(r'; -------------------------------------------------------')
  outarr.append('; %s' % metaline)
  newline = oldline  
  for x in change_instances:
   (instance_full,instance_inner,instance_flag) = x
   # generate 
   instance_changed = make_change_instance(instance_full)
   if not instance_changed:
    outarr.append(';  %s -> ?' % instance_full)
    instance_full_marked = '??' + instance_full + '??'
    newline = newline.replace(instance_full,instance_full_marked)
   else:
    # a recognized change
    outarr.append(';  %s -> %s' % (instance_full,instance_changed))
    instance_changed_marked = '**' + instance_changed + '**'
    newline = newline.replace(instance_full,instance_changed_marked)
    nautochg = nautochg + 1
  lnum = iline + 1
  out = '%s old %s' % (lnum,oldline)
  outarr.append(out)
  outarr.append(';')
  out = '%s new %s' % (lnum,newline)
  outarr.append(out)
  outrecs.append(outarr)
 #
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),'change cases written to',fileout)
 print(nautochg,"programmatic changes")
 
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # instance list
 fileout1 = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines) 
 print(len(cases),'cases')
 write_cases(fileout,cases)
 write_changes(fileout1,cases)
 
