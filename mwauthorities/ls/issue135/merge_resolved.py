#-*- coding:utf-8 -*-
"""merge_resolved
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Tooltip(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  try:
   self.code,self.abbrev,self.tipmain,self.tipcat = line.split('\t')
  except:
   print('Tooltip error:\n%s' %line)
   parts=line.split('\t')
   exit(1)
  self.total = 0
  self.tip = '%s (%s)' %(self.tipmain,self.tipcat)
  self.tipresolved = None

def init_tooltip(filein):
 with codecs.open(filein,"r","utf-8") as f:
  ans = [Tooltip(x) for x in f]
 print(len(ans),'tooltips from',filein)
 return ans

def init_tooltip1(filein):
 with codecs.open(filein,"r","utf-8") as f:
  # lines assumed to have a 5th field
  recs = []
  for iline,line in enumerate(f):
   line = line.rstrip('\r\n')
   parts = line.split('\t')
   if len(parts) != 5:
    print('problem at line # %s:  %s parts' %(iline+1,len(parts)))
    continue
   line1 = '\t'.join(parts[0:4])
   tip = Tooltip(line1)
   # edit the correction
   txt = parts[4]  
   tip.tipresolved = parts[4]
   recs.append(tip)
 print(len(recs),'tooltips from',filein)
 return recs

def write_tips(fileout,tips):
 """ 
 """
 outarr = []
 for tip in tips:
  #parts = [tip.code,tip.abbrev,tip.tipmain,tip.tipcat]
  #out = '\t'.join(parts)
  out = tip.line
  outarr.append(out)
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),'Records written to',fileout)

def update_tips(tips,tips1):
 d = {}
 for t in tips1:
  c = t.code
  if c in d:
   print('Update_tips duplicate code:',c)
  d[c] = t
 #
 newtips = []
 for tip in tips:
  if tip.code not in d:
   newtip = tip
  else:
   tip1 = d[tip.code]
   # tip1.tipresolved  replaces tipmain
   # add (edit) to tipcat
   txt = tip1.tipresolved
   txt = re.sub(r'^ *> *','',txt)
   a = '[Cologne Addition]'
   # restore/
   if (a in tip.tipmain) and (a not in txt):
    txt = txt + ' ' + a    
   newparts = [tip.code,tip.abbrev,txt,tip.tipcat+' (edit)']
   newline = '\t'.join(newparts)
   newtip = Tooltip(newline)
  newtips.append(newtip)
 return newtips
if __name__=="__main__":
 filetip = sys.argv[1] # prior version of tooltips
 fileres = sys.argv[2] # version with resolution of unknowns.
 fileout = sys.argv[3] # revised version of tooltips
 tips = init_tooltip(filetip)
 tipsresolved = init_tooltip1(fileres)
 newtips = update_tips(tips,tipsresolved)
 write_tips(fileout,newtips)
