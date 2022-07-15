#-*- coding:utf-8 -*-
"""make_change_regex1.py 
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

def get_line_in_context(regex1,regex2,context,line):
 # assume context = 'out'
 parts = re.split(r'(<ls.*?</ls>)|(<ab>.*?</ab>)|(<s>.*?</s>)|(&c)|(<info.*?/>)|(<i>.*?</i>)',line)
 newparts = []
 for part in parts:
  if part == None:
   continue
  elif part.startswith(('<ls','<ab>','<s>','&c','<info','<i>')):
   newpart = part
  else:
   newpart = re.sub(regex1,regex2,part)
  newparts.append(newpart)
 newline = ''.join(newparts)
 if False: #True:
  if newline != line:
   print('old: %s' % line)
   print('new: %s' % newline)
   #for ipart,part in enumerate(parts):
   # print('%d: %s' %(ipart+1,part))
   exit(1)
 return newline

def init_cases(lines,regex1,regex2,context):
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
   continue  # can't adjust metaline
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  m = re.search(regex1,line)
  if m == None:
   continue
  match = m.group(0)
  if match in ['ill','cl','l','x','c','v']:
   continue
  newline = get_line_in_context(regex1,regex2,context,line)
  #newline = re.sub(regex1,regex2,line)
  if newline != line:
   # generate a case
   cases.append(Case(metaline,iline,line,match,newline))

 print(len(cases),'changes of %s'%regex1)
 return cases

def write_cases_regex(fileout,cases,regex1,regex2,context):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(cases)))
 outarr.append('; regex1 = /%s/,  regex2 = /%s/' %(regex1,regex2))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; %s ' % case.match)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  if previline == iline:
   # in case we change same line more than once
   line = prevline
  outarr.append('%s old %s' %(lnum,line))
  nchg = nchg + 1
  newline = case.newline
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
  previline = iline
  prevline = newline

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)

interpret_option = {
  '1': (r'\b([ivxcl]+)\b',
        r'<ls n="">\1'),
  '1a': (r'\b([ivxcl]+) ([0-9])',
        r'<ls n="">\1, \2'),

 }

if __name__=="__main__":
 # Problem with input of regexes into command line
 # python make_change_regex.py ', </ls>' '</ls>, ' temp_mw_3.txt temp.txt
 # The 2nd paramenter '</ls>, ' is not intepreted properly
 # It prints as "<C:/Program Files/Git/ls>, "
 # Thus, use an option number
 contextcode,option = sys.argv[1].split(',')
 context = contextcode
 regex1,regex2 = interpret_option[option]

 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines,regex1,regex2,context) 
 print(len(cases),'cases')
 write_cases_regex(fileout,cases,regex1,regex2,context)
  
