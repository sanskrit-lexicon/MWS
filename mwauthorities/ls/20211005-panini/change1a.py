#-*- coding:utf-8 -*-
"""change1a.py 
 
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
  
def change1(line):
 reason = 'DUMMY'
 #newline = re.sub(r'{%([mfn])%}',r'{%\1.%}',line)
 newline = re.sub(r'(<ls[^<]*)<ab>Sch',r'\1<abx>Sch',line)
 m = re.search(r'<ls>Pāṇ.</ls> *\(<ls>',line)
 
 return reason,newline

def change2(line):
 reason = ''
 newline = line.replace('{#(#}','(')
 newline = newline.replace('{#)#}',')')
 return reason,newline

def change3(line):
 reason = '{%S.%} -> Ś.'
 newline = line.replace('{%S.%}','Ś.')
 return reason,newline

def reasons_update(reasons,reason):
 if reason not in reasons:
  reasons[reason] = 0
 reasons[reason] = reasons[reason] + 1
 
def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 page = None
 #change_fcns = [change1]
 #reasons = {} # counts
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
  #lnum = iline+1
  m = re.search(r'<ls>Pāṇ.</ls> *\(<ls>',line)
  if m == None:
   continue
  # generate change
  newline = oldline
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
 outarr.append('; ' + ident)
 lnum = change.iline + 1
 outarr.append('%s old %s' % (lnum,change.old))
 outarr.append(';')
 outarr.append('%s new %s' % (lnum,change.new))
 outarr.append(';')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)

def sortF(suggest):
 nold = len(suggest.botold_recs)
 nnew = len(suggest.botnew_recs)
 return nnew - nold

def write_suggest_stats(fileout,suggests):
 suggests1 = sorted(suggests,key = sortF, reverse=True)
 ntodo = 0
 ndone = 0
 with codecs.open(fileout,"w","utf-8") as f:
  for suggest in suggests1:
   nold = len(suggest.botold_recs)
   nnew = len(suggest.botnew_recs)
   ndiff = nnew - nold
   if (nnew == 0) or (ndiff < 0):
    note = 'TODO'
    ntodo = ntodo + 1
   else:
    note = 'DONE'
    ndone = ndone + 1
   out = '%03d %s %s\t%s %s (%s)' %(ndiff,nold,suggest.botold,nnew,suggest.botnew,note)
   f.write(out+'\n')
 print(ndone,'Records marked DONE')
 print(ntodo,'Records marked TODO')
 
def replace_tag_like_emacs(x,y,z):
 """
  Example: 
  x = nardottachys jatamansi
  y = nardostachys jatamansi
  z = Nardottachys Jatamansi
  Return w = Nardostachys Jatamansi
  (Emacs does such 'case preservation' when the 'ignore case' option is
   set.)
 """
 # x is 'old', y is 'new', lower case
 # x = <bot>a</bot> and y similar
 a = x.replace('<bot>','')
 a = a.replace('</bot>','')
 b = y.replace('<bot>','')
 b = b.replace('</bot>','')
 c = z.replace('<bot>','')
 c = c.replace('</bot>','')
 awords = a.split(' ')
 bwords = b.split(' ')
 cwords = c.split(' ')
 if (len(awords) != len(bwords)) or (len(awords)!= len(cwords)):
  return False,z  # False indicates no change made
 warr = []
 for i,aw in enumerate(awords):
  bw = bwords[i]
  cw = cwords[i]
  if cw.capitalize() == cw:  # this word in z is capitalized
   ww = bw.capitalize()
  else:
   ww = bw
  warr.append(ww)
 w = ' '.join(warr)
 if False: # dbg
  print(awords)
  print(bwords)
  print(cwords)
  print(warr)
  exit(1)
 return True,'<bot>%s</bot>' %w

def suggest_instances_out(suggest,icase):
 oldrecs = suggest.botold_recs
 nold = len(oldrecs)
 newrecs = suggest.botnew_recs
 nnew = len(newrecs)
 ndiff = nnew - nold
 outarr = []
 if nnew == 0:
  return outarr
 if ndiff < 0:
  return outarr
 #
 oldtag = suggest.botold_tag
 newtag = suggest.botnew_tag
 outarr.append('; old: %s occurs %s times' %(oldtag,nold))
 outarr.append('; new: %s occurs %s times'  %(newtag,nnew))
 #outarr.append('; Here are changes from %s to %s' %(oldtag,newtag))
 outarr.append(';')
 for rec in oldrecs:
  metaline,lnum,line,taginstance = rec
  if False: # dbg
   print('taginstance=',taginstance)
   print('line=',line)
  flag,newtaginstance = replace_tag_like_emacs(oldtag,newtag,taginstance)
  m = re.search(r'<L>(.*?)<',metaline)
  L = m.group(1)
  m = re.search(r'<k1>(.*?)<',metaline)
  k1 = m.group(1)
  told = re.sub('</?bot>','',taginstance)
  tnew = re.sub('</?bot>','',newtaginstance)
  outarr.append('; %s : %s : %s : %s : typo or print change?=' %(L,k1,told,tnew))
  #outarr.append('; print change? ')
  outarr.append('; %s' %metaline)
  outarr.append('%s old %s' %(lnum,line))
  #newline = line.replace(oldtag,newtag)
  if not flag:
   outarr.append('; Warning: new line not fixed!')
  newline = line.replace(taginstance,newtaginstance)
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append(';')
 outarr.append('; ------------------------------------------------------')
 return outarr
 
def write_suggest_instances(fileout,suggests):
 suggests1 = sorted(suggests,key = sortF, reverse=True)
 with codecs.open(fileout,"w","utf-8") as f:
  for i,suggest in enumerate(suggests1):
   outarr = suggest_instances_out(suggest,i+1)
   for out in outarr:
    f.write(out+'\n')

def get_words(x):
 x = x.strip() # remove whitespace at ends
 words = re.split(r' +',x)
 return words

class Suggest(object):
 dold = {}
 dnew = {}
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.botold,self.botnew = line.split('\t')
  self.botold_words = get_words(self.botold)
  self.botnew_words = get_words(self.botnew)
  self.botold_recs = []
  self.botnew_recs = []
  self.botold_tag = '<bot>'+self.botold.strip() + '</bot>'
  self.botnew_tag = '<bot>'+self.botnew.strip() + '</bot>'
  if self.botold_tag not in Suggest.dold:
   Suggest.dold[self.botold_tag] = []
  else:
   print('old dup',self.botold_tag)
  Suggest.dold[self.botold_tag].append(self)
  if self.botnew_tag not in Suggest.dnew:
   Suggest.dnew[self.botnew_tag] = []
  else:
   print('new dup',self.botnew_tag)
  Suggest.dnew[self.botnew_tag].append(self)
  
  #Suggest.dold[self.botold_tag.strip()] = self
  #Suggest.dnew[self.botnew_tag.strip()] = self
  
def init_suggests(filein):
 with codecs.open(filein,"r","utf-8") as f:
  suggests = [Suggest(x) for x in f]
 print(len(suggests),'Suggestions from',filein)
 return suggests
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes = init_changes(lines)
 write_changes(fileout,changes)

