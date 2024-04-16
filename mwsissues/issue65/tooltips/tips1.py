#-*- coding:utf-8 -*-
""" tips1.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')  
 print(len(lines),"written to",fileout)

class Tip:
 def __init__(self,line):
  self.line = line
  self.ab,self.data = line.split('\t')
  m = re.search(r'<disp>.*?</disp>',self.data)
  self.tip = m.group(0)
  self.tagcounts = {} # filled in later
  
def init_tips(filein):
 lines = read_lines(filein)
 tips = [Tip(line) for line in lines]
 print(len(tips),"tips read from",filein)
 d = {}
 for tip in tips:
  if tip.ab in d:
   print('duplicate abbrev at',tip.line)
  d[tip.ab] = tip
 return tips,d

def update_tips(lines,tags,tips,dtips):
 regexes = ['<%s>(.*?)</%s>' %(tag,tag) for tag in tags]
 dbg = True
 for line in lines:
  for itag,tag in enumerate(tags):
   regex = regexes[itag]
   a = re.findall(regex ,line)
   if a == []:
    continue
   for ab in a:
    if ab not in dtips:
     newtipline = '%s\t<disp>?</disp>' % ab
     #print(newtipline)
     #exit(1)
     newtip = Tip(newtipline)
     dtips[ab] = newtip
     tips.append(newtip)
    tip = dtips[ab]
    if tag not in tip.tagcounts:
     tip.tagcounts[tag] = 0
    tip.tagcounts[tag] = tip.tagcounts[tag] + 1

def write_tips(fileout,tips):
 outarr = []
 for tip in tips:
  a = []
  for tag in tip.tagcounts:
   n = tip.tagcounts[tag]
   a.append('%s,%s' %(tag,n))
  b = ' '.join(a)
  out = '%s\t%s <count>%s</count>' %(tip.ab,tip.tip,b)
  outarr.append(out)
 write_lines(fileout,outarr)

def sort_tips(tips):
 tips1 = []
 for tip in tips:
  if 'lang' in tip.tagcounts:
   tips1.append(tip)
 tips1a = sorted(tips1,key = lambda tip: tip.ab.lower())
 tips2 = []
 for tip in tips:
  if 'lang' not in tip.tagcounts:
   tips2.append(tip)
 tips2a = sorted(tips2,key = lambda tip: tip.ab.lower())
 return tips1a + tips2a

if __name__=="__main__":
 tags = sys.argv[1].split(',')
 filein = sys.argv[2] #  xxx.txt
 filein1 = sys.argv[3] # mwab_input old
 fileout = sys.argv[4] # mwab_input new
 lines = read_lines(filein) # xxx.txt
 print(len(lines),"read from",filein)
 tips,dtips = init_tips(filein1)
 # changes tips and dtips
 update_tips(lines,tags,tips,dtips)
 tips1 = sort_tips(tips)
 write_tips(fileout,tips1)
