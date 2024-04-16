#-*- coding:utf-8 -*-
""" tips2.py
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

def clean_lex(x):
 y = x
 y = re.sub(r'\(.*?\)','',y)
 y = re.sub(r'\[.*?\]','',y)
 y = re.sub(r'<ab>.*?</ab>','',y)
 y = re.sub(r'<ls.*?</ls>','',y)
 y = re.sub(r'<s>.*?</s>','',y)
 y = re.sub(r' and','',y)
 y = re.sub(r' or','',y)
 y = re.sub(r'[,;.]','',y)
 y = y.replace(r'])','')
 y = y.replace(' ','')
 y = y + '.'
 return y

def update_tips_helper_lex(a):
 b = []
 for x in a:
  #<lex>x</lex>
  y = clean_lex(x)
  b.append(y)
 return b

def update_tips(lines,tags,tips,dtips):
 regexes = ['<%s>(.*?)</%s>' %(tag,tag) for tag in tags]
 dbg = True
 for line in lines:
  for itag,tag in enumerate(tags):
   regex = regexes[itag]
   a = re.findall(regex ,line)
   if a == []:
    continue
   # for lex tag, we try to get rid of non-gender stuff
   if tag == 'lex':
    a = update_tips_helper_lex(a)
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

def unused_sort_tips(tips):
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

def sort_tips(tips,tags):
 tips1 = sorted(tips,key = lambda tip: tip.ab.lower())
 # separate tips into those that are found or not found
 tips_f =  [tip for tip in tips1 if tip.tagcounts != {}]
 tips_nf = [tip for tip in tips1 if tip.tagcounts == {}]
 tg = {}
 for tag in tags:
  tg[tag] = []
 for tip in tips_f:
  for tag in tags:
   if tag in tip.tagcounts:
    tg[tag].append(tip)
    # tip to appear with only one tag, the first tag found
    break
 # finally, revise tips_f
 tips_f1 = []
 for tag in tags:
  for tip in tg[tag]:
   tips_f1.append(tip)
 # And add tips_nf at the end
 ans = tips_f1 + tips_nf
 return ans

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
 tips1 = sort_tips(tips,tags)
 write_tips(fileout,tips1)
