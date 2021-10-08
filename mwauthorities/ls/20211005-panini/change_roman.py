#-*- coding:utf-8 -*-
"""change_roman.py change transactions re panini links. Conversion to roman numerals
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason

lsregex_rawarr = [
  r'^<ls>Pāṇ[.]</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+) [f]+[.]</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)-([0-9]+), ([0-9]+)</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)-([0-9]+)</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)-([0-9]+), ([0-9]+) [f]+[.]</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)-([0-9]+), ([0-9]+)[.]</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)-([0-9]+), ([0-9]+)</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)-([0-9]+), ([0-9]+)[.]</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)-([0-9]+), ([0-9]+) [f]+[.]</ls>$',
  r'^<ls n="Pāṇ[.] ([0-9])">([0-9]+), ([0-9]+)</ls>$',
  r'^<ls n="Pāṇ[.] ([0-9]-[0-9]+)">([0-9]+)</ls>$',
  r'^<ls n="Pāṇ[.] ([0-9]-[0-9]+)">([0-9]+) [f]+[.]</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)</ls>$',
]
lsregex_arr = [re.compile(regex) for regex in lsregex_rawarr]
regexraw = r'(<ls n="Pāṇ[.][^"]*">.*?</ls>)|(<ls>Pāṇ[.].*?</ls>)'
#regexraw = r'(<ls n="Pāṇ[.][^"]*">.*?</ls>)|(<ls>Pāṇ[.].*?</ls>)'

regex = re.compile(regexraw)

regexromans_raw = [
  r'<ls>Pāṇ[.] ([0-9]+-?)[0-9]+',
 
  r'^<ls>Pāṇ[.] ([0-9]+)</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+) [f]+[.]</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)-[0-9]+</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)-[0-9]+, [0-9]+ [f]+[.]</ls>$',
  r'^<ls>Pāṇ[.] ([0-9]+)([0-9]+, [0-9]+[.]</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)-[0-9]+, [0-9]+</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)-[0-9]+, [0-9]+[.]</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)-[0-9]+, [0-9]+ [f]+[.]</ls>$',
  r'^<ls n="Pāṇ[.] ([0-9])">[0-9]+, [0-9]+</ls>$',
  r'^<ls n="Pāṇ[.] ([0-9])-[0-9]+">[0-9]+</ls>$',
  r'^<ls n="Pāṇ[.] ([0-9])-[0-9]+">[0-9]+ [f]+[.]</ls>$',
  r'^<ls n="Pāṇ[.]">([0-9]+)</ls>$',
]
toroman = {'1':'i', '2':'ii', '3':'iii', '4':'iv',
           '5':'v', '6':'vi', '7':'vii', '8':'viii'}

def subroman(m):
 # m is from regex above
 # convert first numerical argument from arabic number to roman numeral lower-case
 x = m.group(0)
 # replace 1st number (if any) with its roman numeral.
 # also replace '-' (if any) with ',
 def roman(m1):
  # m1.group is a digit string
  return toroman[m1.group(0)]
 z = re.sub(r'[1-8]',roman,x,count=1)
 w = z.replace('-',', ')
 return w

def init_changes(lines):

 changes = [] # array of Change objects
 metaline = None
 page = None
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  if line.startswith('<L>'):
   metaline = line
   continue
  if line == '<LEND>':
   metaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  oldline = line  
  newline = re.sub(regex,subroman,line)
  if newline == oldline:
   continue
  reason = None
  change = Change(metaline,page,iline,oldline,newline,reason)
  changes.append(change)
 print(len(changes),'potential changes found')
 return changes

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 ident = change.metaline
 if ident == None:
  ident = change.page
 if ident == None:
  ident = 'None'
 outarr.append('; ' + ident)
 lnum = change.iline + 1
 outarr.append('%s old %s' % (lnum,change.old))
 outarr.append(';')
 outarr.append('%s new %s' % (lnum,change.new))
 outarr.append('; -------------------------')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt
 fileout = sys.argv[2] # 
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = init_changes(lines)
 write_changes(fileout,changes)
