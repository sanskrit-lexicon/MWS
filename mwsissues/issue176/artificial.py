#-*- coding:utf-8 -*-
""" artificial.py
"""
from __future__ import print_function
import sys,re,codecs,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import digentry
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 print(len(lines),"from",filein)
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in lines:
   f.write(out+'\n')  
 print(len(lines),"lines written to",fileout)

def write_recs(fileout,outrecs,printflag=True,blankflag=True):
 # outrecs is array of array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
   if blankflag:
    out = ''  # blank line separates recs
    f.write(out+'\n')
 if printflag:
  print(len(outrecs),"records written to",fileout)

def write_entries_helper(entry):
 outarr = []
 outarr.append(entry.metaline)
 for line in entry.datalines:
  outarr.append(line)
 outarr.append(entry.lend)
 return outarr

def write_entries(fileout,entries):
 outrecs = []
 for entry in entries:
  outrec = write_entries_helper(entry)
  outrecs.append(outrec)
 write_recs(fileout,outrecs,blankflag=False)

def isrealhom(h):
 m = re.search(r'^[0-9]+$',h)
 if m == None:
  realhom = False  # artificial hom
 else:
  realhom = True
 return realhom

def revise_metaline(entry):
 if 'h' not in entry.metad:
  return (None,None)
 h = entry.metad['h']
 realhom = isrealhom(h)
 return h,realhom

def remove_art_hom(text):
 n = 0
 homs = re.findall(r'<hom>(.*?)</hom>',text,re.DOTALL)
 arthoms = []
 for hom in homs:
  # we know from observation that there is usually a period
  # following a digit string for a 'real' hom
  if re.search(r'^[0-9]+\.?$', hom) == None:
   arthoms.append(hom)
 n = len(arthoms)
 if n == 0:
  return n,text
 newtext = text
 for hom in arthoms:
  # the capture group
  old = '<hom>%s</hom>' % hom
  newtext = newtext.replace(old,'')
  # extra space remove
  newtext = newtext.replace('  ',' ')
 return n,newtext

def revise_entries(entries):
 nmeta = 0 # number of metalines changed
 nhui = 0 # number of <info n="X"/> fields added (real and artificial <h>)
 nhomui = 0
 for entry in entries:
  h,realhom = revise_metaline(entry)
  if realhom == False:
   # remove artificial hom from metaline
   nmeta = nmeta + 1
   hfield = '<h>%s' % h
   newmetaline = entry.metaline.replace(hfield,'')
   entry.metaline = newmetaline
  if h != None:
   # add field hui field
   nhui = nhui + 1
   datalines = entry.datalines
   line = datalines[-1]  # last line
   hui = '<info hui="%s"/>' % h
   newline = '%s%s' %(line,hui)
   datalines[-1] = newline
   entry.datalines = datalines
  # remove '<hom>X</hom>'
  oldtext = '\n'.join(entry.datalines)
  n,newtext = remove_art_hom(oldtext)
  nhomui = nhomui + n
  if n != 0:
   entry.datalines = newtext.split('\n')
 print('nmeta=',nmeta)
 print('nhui=',nhui)
 print('nhomui=',nhomui)
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # 
 entries = digentry.init(filein)
 Ldict = digentry.Entry.Ldict;

 revise_entries(entries)
 write_entries(fileout,entries)
 print(len(entries),'entries written to',fileout)

