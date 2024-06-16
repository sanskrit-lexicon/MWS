# coding=utf-8
""" 
shortlong  make_change_1.py
"""
from __future__ import print_function
import sys, re,codecs
import digentry

def select(entries):
 nfound = 0
 regexraw = r'<shortlong/>.*¦'
 
 regex = re.compile(regexraw)
 for entry in entries:
  grlines = []
  for iline,line in enumerate(entry.datalines):
   if iline != 0:
    continue
   m = re.search(regex,line)
   if m != None:
    text = m.group(0)
    grlines.append((iline,line,text))
  # add attribute to the entry
  entry.grlines = grlines
  if grlines != []:
   nfound = nfound + 1
   assert len(grlines) == 1
 print('select %s entries matching %s' %(nfound,regexraw))

def write(fileout,entries):
 outrecs = []
 for entry in entries:
  grlines = entry.grlines
  if grlines == []:
   continue
  assert len(grlines) == 1
  outarr = []
  outarr.append('; ------------------------------------------------------')
  meta = entry.metaline
  # meta = re.sub(r'<k2>.*$','',meta)
  outarr.append('; %s' % meta)
  flag = False
  for templine in entry.datalines:
   m = re.search('<info orsl=".*?"/>',templine)
   if m != None:
    orsl = m.group(0)
    outarr.append('; %s' % orsl)
    flag = True
  if flag == False:
   outarr.append('; no <info orsl="..."/>')
  iline = 0
  line = entry.datalines[0]
  lnum = entry.linenum1 + iline + 1
  outarr.append('%s old %s' %(lnum,line))
  outarr.append(';')
  # get proposed new line
  m = re.search(r'<s>(.*?)([aAiIuUfFeEoO])<shortlong/>(.*?)</s>',line)
  if m != None:
   sold = m.group(0)
   a,v,b = m.group(1),m.group(2),m.group(3)
   if v in 'aiufeo':
    w = v.upper()
   else:
    w = v.lower()
   snew1 = '<s>%s%s%s</s>' % (a,v,b)
   snew2 = '<s>%s%s%s</s>' % (a,w,b)
   snew = '%s or %s' %(snew1,snew2)
   newline = line.replace(sold,snew)
  else:
   outarr.append('; PROBLEM')
   newline = line
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 fileout = sys.argv[2] # text output
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 
 select(entries)
 write(fileout,entries)
