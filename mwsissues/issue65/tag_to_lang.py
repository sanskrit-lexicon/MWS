#-*- coding:utf-8 -*-
"""tag_to_lang.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def change_lines(lines,d,tag):
 
 newlines = []
 nchg = 0 # number of lines changed
 regex = r'<%s>(.*?)</%s>' % (tag,tag)
 regexa = re.compile(regex) # for efficiency
 
 for iline,line in enumerate(lines):
  """
re.findall return"
   If the pattern has one capturing group, 
     the function returns a list of strings that match that group.
   If the pattern has multiple capturing groups, 
     the function returns tuples of strings corresponding to those groups.
  """
  abs = re.findall(regexa,line)
  if abs == []:
   newlines.append(line)
   continue
  newline = line
  for x in abs:
   if x in d:
    old = '<%s>%s</%s>' % (tag,x,tag)
    new = '<lang>%s</lang>' % x
    newline = newline.replace(old,new)
    # update d
    d[x] = d[x] + 1
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
  if False: # dbg
   if newline != line:
    print('old:',line)
    print('new:',newline)
    exit()
 print('%s lines changed' % nchg)
 return newlines

def change_lines_1(lines,d,tag):
 newlines = []
 nchg = 0 # number of lines changed
 regex = r'<%s ([^<]*?)>(.*?)</%s>' % (tag,tag)
 regexa = re.compile(regex) # for efficiency
 
 for iline,line in enumerate(lines):
  """
re.findall return"
   If the pattern has one capturing group, 
     the function returns a list of strings that match that group.
   If the pattern has multiple capturing groups, 
     the function returns tuples of strings corresponding to those groups.
  """
  abs = re.findall(regexa,line)
  if abs == []:
   newlines.append(line)
   continue
  newline = line
  for attr,x in abs:  
   if x in d:
    old = '<%s %s>%s</%s>' % (tag,attr,x,tag)
    new = '<lang>%s</lang>' % x
    newline = newline.replace(old,new)
    # update d
    d[x] = d[x] + 1
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
  if False: # dbg
   if newline != line:
    print('old:',line)
    print('new:',newline)
    exit()
 print('%s lines changed' % nchg)
 return newlines

replacements_2 = [
  ('<s1 slp1="prAkf">Prākṛ</s1>.' , '<lang>Prākṛ.</lang>'),
  ('<ns>Gaël</ns>.' , '<lang>Gaël.</lang>'),
  (' Gaelic ' , ' <lang>Gaëlic</lang> '),
  ('Irish' , '<lang>Irish</lang>'),
  ('<ab>Mod.</ab> <lang>Eng.</lang>' , '<lang>Mod. Eng.</lang>'),
  ('<s1 slp1="jEna">Jaina</s1> <lang>Prākṛt</lang>' , '<lang>Jaina Prākṛt</lang>'),
  ('<ab>O.E.</ab>' , '<lang>O. E.</lang>'),
  ('<ab>O.N.</ab>' , '<lang>O. N.</lang>'),
  ('<ab>O.Pr.</ab>' , '<lang>O. Pr.</lang>'),
  ('<ab>O.</ab> <lang>Pruss.</lang>' , '<lang>O. Pruss.</lang>'),
  ('<ab>O.</ab> <lang>Slav.</lang>' , '<lang>O. Slav.</lang>'),
  #('<lang>Sanskṛt</lang>-Persian' , '<lang>Sanskṛt</lang>-<lang>Persian</lang>'),
  ('<lang>Sanskṛt</lang>-Persian' , '<lang>Sanskṛt-Persian</lang>'),
  (' Persian ' , ' <lang>Persian</lang>'),
  ('Sinhalese' , '<lang>Sinhalese</lang>'),
  ('<lang>class.</lang> <lang>Sanskṛt</lang>' , '<lang>class. Sanskṛt</lang>'),
  ('<lang>Class.</lang> <lang>Sanskṛt</lang>' , '<lang>Class. Sanskṛt</lang>'),
  ('classical <lang>Sanskṛt</lang>' , '<lang>classical Sanskṛt</lang>'),
  ('later <lang>Sanskṛt</lang>' , '<lang>later Sanskṛt</lang>'),
  ('later <ab>Skr.</ab>' , '<lang>later Skr.</lang>'),
  ('medieval <lang>Lat.</lang>' , '<lang>medieval Lat.</lang>'),
  ('modern <lang>Sanskṛt</lang>' , '<lang>modern Sanskṛt</lang>'),
  ('old <lang>Prākṛt</lang>' , '<lang>old Prākṛt</lang>'),
  ('English' , '<lang>English</lang>'),
  ('French' , '<lang>French</lang>'),
  (' Arabic ' , ' <lang>Arabic</lang> '),
  ('new <ab>Sax.</ab>' , '<lang>Old Sax.</lang>'),
  ('<ab>Goth. Old S.</ab>' , '<lang>Goth.</lang> <lang>Old S.</lang>'),
]

def change_lines_2(lines,d,tag):
 # misc
 newlines = []
 nchg = 0 # number of lines changed
 
 for iline,line in enumerate(lines):
  if line.startswith(('<L>','<LEND>')):
   newlines.append(line)
   continue
  if line.strip() == '':   
   newlines.append(line)
   continue
  newline = line
  for oldtext,newtext in replacements_2:
   newline = newline.replace(oldtext,newtext)
  newlines.append(newline)
  if newline != line:
   nchg = nchg + 1
 print('%s lines changed' % nchg)
 return newlines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)
 
def init_langtags(filein):
 lines = read_lines(filein)
 d = {}
 for line in lines:
  # <lang>X</lang>
  m = re.search(r'<lang>([^<]*)</lang>',line)
  if m == None:
   print('init_langtags error: %s' % line)
   exit(1)
  x = m.group(1)
  if x in d:
   print('init_langtags duplicate',line)
   exit(1)
  d[x] = 0  # count of instances
 print(len(lines),"lang tags read from",filein)
 return d

def write_unused_tags(fileout,d):
 outarr = []
 # write tags that are not found
 for x in d:
  val = d[x]
  if val == 0:
   y = '<lang>%s</lang>' % x
   outarr.append(y)
 write_lines(fileout,outarr)
 
def update_langtags_dict(d,lines):
 z = [('<lang>%s</lang>' % k,k) for k in d]
 for iline,line in enumerate(lines):
  # skip metalines and empty lines
  if line.startswith(('<L>','<LEND>')):
   continue
  if line.strip() == '':   
   continue
  for elt,k in z:
   nelt = line.count(elt)
   if nelt != 0:
    d[k] = d[k] + nelt
 return d

if __name__=="__main__":
 oldtag = sys.argv[1]
 langtagfile = sys.argv[2]
 filein = sys.argv[3] #  xxx.txt 
 fileout = sys.argv[4] #
 filetodo = sys.argv[5]
 langtags_dict = init_langtags(langtagfile)
 lines = read_lines(filein)
 print(len(lines),"lines read from",filein)
 if oldtag in ['ab','ns']:
  newlines = change_lines(lines,langtags_dict,oldtag)
 elif oldtag in ['s1']:
  newlines = change_lines_1(lines,langtags_dict,oldtag)
 elif oldtag == 'misc':
  newlines = change_lines_2(lines,langtags_dict,oldtag)
 write_lines(fileout,newlines)
 update_langtags_dict(langtags_dict,newlines)
 write_unused_tags(filetodo,langtags_dict,)

