#-*- coding:utf-8 -*-
"""tabconvert.py
 python tabconvert.py <OPTION> <FILEIN> <FILEOUT>
 '<OPTION> is "totab"  or "fromtab"
 python tabconvert.py totab <FILEIN> <FILEOUT>
 python tabconvert.py fromtab <FILEIN> <FILEOUT>

"""
from __future__ import print_function
import sys, re,codecs

def convert_totab(lines):
 groups = []
 flag = False
 group = []
 for line in lines:
  if line.startswith('<L>'):
   flag = True
   group = [line]
  elif line.startswith('<LEND>'):
   group.append(line)
   groups.append(group)
   group = []
   flag = False
  elif flag:
   group.append(line)
  else:
   group = [line]
   groups.append(group)
 # 
 outlines = []
 suppflag = False
 for group in groups:
  if len(group) == 1:
   line = group[0]
   suppflag = (line == '; SUPPLEMENT')
   if suppflag:
    continue  # don't include in output    
  else:
   line = '\t'.join(group)
   if suppflag:
    line = re.sub('<L>','<Ls>',line)
   suppflag = False
  outlines.append(line)    
 return outlines

def convert_fromtab(lines):
 outlines = []
 for line in lines:
  if re.search(r'^ *$',line):
   # skip blank lines
   continue
  if not line.startswith('<L'):
   outlines.append(line)
   continue
  m = re.search('^<L(.*?)>',line)
  a = m.group(1)
  line1 = re.sub(r'^<L(.*?)>','<L>',line)
  lines1 = line1.split('\t')
  if a != '':
   outlines.append('; SUPPLEMENT %s'%a)
  outlines = outlines + lines1
 return outlines

def unused_convert_totab(lines):
 outlines = []
 tabline = ''
 suppflag = False  # is previous line ';  SUPPLEMENT' ?
 for line in lines:
  if line == '<LEND>':
   tabline = tabline + '\t' + line
   outlines.append(tabline)
   tabline = ''
   suppflag = False
  elif line.startswith('<'):
   if line.startswith('<L>') and suppflag:
    line = re.sub(r'^<L>','<Ls>',line)
   if tabline == '':
    tabline = line
   else:
    tabline = tabline + '\t' + line
   suppflag = False
  elif line.startswith('; SUPPLEMENT'):
   # exclude but set suppflag
   suppflag = True
  else:
   suppflag = False
   outlines.append(line)
 if tabline != '':
  print('END of file incomplete. tabline=\n',tabline)
 return outlines
  
if __name__=="__main__": 
 try:
  option = sys.argv[1]
  filein = sys.argv[2]
  fileout = sys.argv[3]
  assert option in ['totab','fromtab']
 except:
  print('Usage error')
  print('python tabconvert.py <OPTION> <FILEIN> <FILEOUT>')
  print('<OPTION> is "totab"  or "fromtab"')
  exit(1)
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]

 if option == 'totab':
  lines1 = convert_totab(lines)
 elif option == 'fromtab':
  lines1 = convert_fromtab(lines)
 else:
  print('tabconvert ERROR 2: unknown option=',option)
  exit(1)

 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines1:
   f.write(line+'\n')
