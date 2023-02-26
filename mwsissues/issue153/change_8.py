# coding=utf-8
""" 
change_8.py  See readme.txt
"""
from __future__ import print_function
import sys, re,codecs
import digentry

class Change(object):
 # attribute of entry
 def __init__(self,iline,newline,linegchanges):
  self.iline = iline
  self.newline = newline
  # CoggroupChange objects that generate
  # changes to this line
  self.linegchanges = linegchanges
  
class CoggroupChange(object):
 def __init__(self,gold,gnew,gnote,entrychanges):
  self.gold = gold
  self.gnew = gnew
  self.gnote = gnote
  self.entrychanges = entrychanges
  self.nfound = 0
  
class Coggroup(object):
 def __init__(self,glines,gtype,gnum,gcomment,gchanges):
  self.glines = glines
  self.gtype = gtype
  self.gnum = gnum
  self.gcomment = gcomment.strip()
  self.gchanges = gchanges

def groupgen(lines):
 group = []
 igroup = 0
 for iline,line in enumerate(lines):
  # ignore lines starting with ;
  if line.startswith(';'):
   continue
  # ignore blank lines
  line = line.strip()
  if line == '':
   continue
  group.append(line)
  if line.startswith('---'):
   # end of group. Prepare Group object
   
   m = re.search(r'^[*] ([^ ]+) \(([0-9]+)\) (.*$)',group[0])
   if m == None:
    print('problem 1 at line',iline+1)
    print(group[0])
    exit()
   gtype = m.group(1) # code identifying this group
   gnum = m.group(2)  # number of items in group
   gcomment = m.group(3) # text describing group
   if int(gnum) != (len(group) - 2):
    print('problem 2 at line',iline+1)
    exit()
   gchanges = []
   for i,gline in enumerate(group):
    if (i == 0) or ((i+1) == len(group)):
     continue
    parts = gline.split('\t')
    gold = parts[0].strip()
    if not (len(parts) in [2,3]):
     print('problem 3 at line',iline+1)
     print('gline=',gline)
     exit(1)
    gnew = parts[1].strip()
    if len(parts) == 3:
     gnote = parts[2]
    else:
     gnote = ''
    entrychanges = [] # entries with this change
    gchange = CoggroupChange(gold,gnew,gnote,entrychanges)
    gchanges.append(gchange)
   rec = Coggroup(group,gtype,gnum,gcomment,gchanges)
   igroup = igroup + 1
   if True: # dbg
    if igroup == 0:
     for x in rec.lines:
      print('coggroup check',x)
   yield rec
   group = []
   
def init_coggroups(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Group objects
 n = 0
 for rec in groupgen(lines):
  recs.append(rec)
  n = n + 1
  if False: # dbg
   if n < 10:
    print('init_coggroups: lnum=%s, msg=%s' % (rec.lnum,rec.msg))
 print(len(recs),"Coggroups read from",filein)
 return recs


def etyminfo(coggroups):
 for i,coggroup in enumerate(coggroups):
  a = []
  for m in re.finditer(r'<etym>(.*?)</etym>',coggroup.old):
   a.append(m.group(1))
  b = []
  for m in re.finditer(r'<etym>(.*?)</etym>',coggroup.new):
   b.append(m.group(1))
  coggroup.oldetym = a
  coggroup.newetym = b
  na = len(a)
  nb = len(b)
  if True:
   if len(a) != len(b):
    print(coggroup.lnum, '# old etym = %s, # new etym = %s' %(len(a),len(b)))

def select(entries):
 nfound = 0
 for entry in entries:
  coggroup = entry.coggroup
  if coggroup == None:
   continue
  coggroup.iline = None
  lnumg = int(coggroup.lnum)
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1 + iline + 1
   if lnum == lnumg:
    coggroup.iline = iline
    c = []
    #for m in re.finditer(r'<etym>(.*?)</etym>',coggroup.old):
    for m in re.finditer(r'<etym>(.*?)</etym>',line):
     c.append(m.group(1))
    coggroup.entryetym = c

def make_new(oldline,newetyms):
 # check same number of <etym>X</etym> in oldline as in newetyms
 oldetyms = re.findall(r'(<etym>.*?</etym>)',oldline)
 if len(newetyms) != len(oldetyms):
  return None  # error condition that caller must handle
 parts = re.split(r'(<etym>.*?</etym>)',oldline)
 newparts = []
 iety = 0
 for part in parts:
  if not part.startswith('<etym>'):
   newpart = part
  else:
   newpart = '<etym>%s</etym>' %newetyms[iety]
   iety = iety + 1
  newparts.append(newpart)
 newline = ''.join(newparts)
 return newline

def make_outarr(entry,change):
 outarr = []
 outarr.append('; ------------------------------------------------------')
 meta = re.sub(r'<k2>.*$','',entry.metaline)
 outarr.append('; %s' % meta)
 iline = change.iline
 lnum = entry.linenum1 + iline + 1
 oldline = entry.datalines[iline]
 outarr.append('%s old %s' %(lnum,oldline)) 
 outarr.append(';')
 # gchange items used
 for gchange in change.linegchanges:
  outarr.append(';   %s  =>  %s %s' % (gchange.gold,gchange.gnew,gchange.gnote))
  gchange.nfound = gchange.nfound + 1
 outarr.append(';')
 outarr.append('%s new %s' %(lnum,change.newline))
 outarr.append(';')
 return outarr

def write(fileout,entries):
 numlineschanged = 0
 outrecs = []
 # title
 outarr = []
 outarr.append('; *****************************************************')
 outarr.append('; %s %s' % (fileout, coggroup.glines[0]))
 outarr.append('; *****************************************************')
 outrecs.append(outarr)
 for entry in entries:
  changes = entry.changes
  if changes == []:
   continue
  for change in changes:
   outarr = make_outarr(entry,change)
   numlineschanged = numlineschanged + 1
  outrecs.append(outarr)   
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print('%s line changes written to %s' %(numlineschanged,fileout))
 
def find_changes(coggroup,entries):
 option = coggroup.gtype
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   linegchanges = [] # 
   newline = line
   for gchange in coggroup.gchanges:
    gold = gchange.gold
    gnew = gchange.gnew
    newline1 = newline.replace(gold,gnew)
    if newline1 != newline: 
     newline = newline1
     linegchanges.append(gchange)
   if newline != line:
    change = Change(iline,newline,linegchanges)
    entry.changes.append(change)
   
if __name__=="__main__":
 option = sys.argv[1]
 options = ['etym_s','s_etym','s_etym1','misc','misc1',
            'untag','diac','hyph','indic',
            'cog', 'cog_s','cog_nots']
 assert option in options

 filein = sys.argv[2] # xxx.txt
 filein1 = sys.argv[3] # e.g., AB.CDSL_cognates.corrections_slp1.txt
 fileout = sys.argv[4] # prototype change transactions
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 # read the corrections file
 coggroups_all = init_coggroups(filein1)
 # consider only the group matching option
 a = [x for x in coggroups_all if x.gtype == option]
 if len(a) != 1:
  print('error matching option',option)
 coggroup = a[0]
 find_changes(coggroup,entries)
 write(fileout,entries)
 print('Working on %s' % coggroup.glines[0])
 print('# Cases :')
 for g in coggroup.gchanges:
  gold = g.gold.ljust(20)
  gnew = g.gnew
  if g.nfound != 1:
   status = '?'
  else:
   status = ' '
  if status == '?':
   out = ' %s %s "%s"  =>  "%s" %s' % (status,g.nfound, gold, gnew, g.gnote)
   print(out)
