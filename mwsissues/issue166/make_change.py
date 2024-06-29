# coding=utf-8
""" 
make_change.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def write_changes(fileout,changes):
 # changes is array of Dotrec objects
 outrecs = []
 for change in changes:
  lnum = change.lnum
  metaline = change.metaline
  text = change.text
  line = change.line
  newline = change.newline
  outarr = []
  meta = re.sub(r'<k2>.*$','',metaline)
  outarr.append('* ; %s' % meta)
  outarr.append('; text:" %s"' % text)
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('; ')
  newline1 = newline.replace(' }}','}} ') # for easier reading
  outarr.append('%s new %s' %(lnum,newline1))
  outarr.append('; ---------------------------------------------')
  outrecs.append(outarr)
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"records written to",fileout)

class Dotrec:
 def __init__(self,line):
  a,b = line.split('\t')  # two tab-delimited fields
  # a:  (N):   where N is digit sequence (lnum in mw.txt)
  m = re.search(r'^\(([0-9]+)\):$',a)
  if m == None:
   print('Dotrec ERROR:',line)
   exit(1)
  self.lnum = int(m.group(1))
  self.text = b
  self.metaline = None # filled in later
  self.oldline = None 
  
def init_dotrecs(lines):
 recs = [Dotrec(line) for line in lines]
 d = {}
 for rec in recs:
  iline = rec.lnum - 1
  d[iline] = rec
 return recs,d

def get_prev_metaline(iline0,lines):
 iline = iline0
 while iline >= 0:
  line = lines[iline]
  if line.startswith('<L>'):
   return iline
  iline = iline - 1
 print('get_prev_metaline ERROR: iline0=',iline0)
 exit(1)
 
def marklines(dotrecsdict,lines):
 newlines = []
 for iline,line in enumerate(lines):
  if iline not in dotrecsdict:
   newlines.append(line)
   continue
  dotrec = dotrecsdict[iline]
  text = dotrec.text
  lnum = dotrec.lnum
  newtext = '{{%s}}' % text
  newline = line.replace(text,newtext)
  if newline == line:
   print('"%s" not found at line# %s' %(text,lnum))
   newline = '{{}}%s' % line
  newlines.append(newline)
  # get metaline
  ilinemeta = get_prev_metaline(iline,lines)
  metaline = lines[ilinemeta]
  dotrec.metaline = metaline
  dotrec.line = line
  dotrec.newline = newline
  newlines[ilinemeta] = '* ' + metaline  # for Emac org mode
 return newlines

if __name__=="__main__":
 filein = sys.argv[1] # e.g., mw.txt
 filein1 = sys.argv[2] # dot.corrections.txt
 fileout = sys.argv[3] # text output -
 fileout1 = sys.argv[4]  # mw.txt  for easier cross-reference
 # read all the entries of the dictionary.
 lines = read_lines(filein)
 print(len(lines),"read from",filein)
 lines1 = read_lines(filein1)
 dotrecs,dotrecsdict = init_dotrecs(lines1)
 print(len(dotrecs),"inputs from",filein1)
 # marklines also adds metaline attribute of dotrec
 newlines = marklines(dotrecsdict,lines)
 write_changes(fileout,dotrecs)
 # temporary copy of filein
 write_lines(fileout1,newlines)
