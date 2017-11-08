""" compare.py
   11-06-2017
   Use filter_abbrev.txt (marked abbreviations)
   and mwab_input.txt  (defined abbreviations)
   Compare the two
"""
import sys,re,codecs

class ABmark(object):
 # filter_abbrev
 def __init__(self,line):
  line = line.rstrip('\r\n')
  m = re.search(r'^(.*) ([0-9]+)$',line)
  self.ab = m.group(1)
  self.count = m.group(2)
  #parts = line.split(' ')
  #self.ab = ''.join(parts[0:-1])
  #self.count = parts[-1]
  self.count = int(self.count)
  self.disp = "NODEF"
  self.defined = False
  self.extra = ''

class ABdef(object):
 # mwab_input
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  try:
   (self.ab,self.data) = line.split('\t')
  except:
   print "mwab_input error. line=",line.encode('utf-8')
   exit(1)
  m = re.search(r'<disp>(.*?)</disp>(.*)$',self.data)
  if not m:
   print "mwab_input error 1. line=",line.encode('utf-8')
   exit(1)
  self.disp = m.group(1)
  self.used = False
  self.extra = m.group(2).strip()

def add_unmarked(abdefs,abmarks):
 for abdef in abdefs:
  if not abdef.used:
   line = '%s 0' %abdef.ab
   abmark = ABmark(line)
   abmark.disp = abdef.disp
   abmark.extra = abdef.extra + ' <UNUSED/>'
   abmark.defined = True
   abmarks.append(abmark)
def compare(abmarks,abdefs,fileout):
 ABdefdict = {}
 for abdef in abdefs:
  ABdefdict[abdef.ab] = abdef
 #
 ndefined = 0
 ndefined_low = 0
 for abmark in abmarks:
  ab = abmark.ab
  if ab in ABdefdict:
   abdef = ABdefdict[ab]
   abmark.disp = abdef.disp
   abmark.extra = abdef.extra
   abdef.used = True
   abmark.defined = True
   ndefined = ndefined + 1
   continue
 # Add abdefs which are not in abmarks to abmarks, for
 # purpose of display
 add_unmarked(abdefs,abmarks) # modifies abmarks
 # Generate output
 # sort abmarks alphabetical by ab (case insensitive)
 abmarks = sorted(abmarks,key = lambda x: x.ab.lower())
 with codecs.open(fileout,"w","utf-8") as f:
  for abmark in abmarks:
   extra = abmark.extra
   if extra != '': 
    extra = ' [NOTE: %s]' % extra
   out = '%s %s DEF=%s%s' %(abmark.ab, abmark.count,abmark.disp,extra)
   f.write(out + '\n')
 print ndefined,"marked abbreviations are defined"
 print ndefined_low,"additional lower case marked abbreviations are defined"
if __name__=="__main__":
 filein = sys.argv[1]  # filter_abbrev
 filein1 = sys.argv[2] # mwab_input
 fileout = sys.argv[3] # results
 with codecs.open(filein,"r","utf-8") as f:
  abmarks = [ABmark(x) for x in f if not x.startswith(';')]
 with codecs.open(filein1,"r","utf-8") as f:
  abdefs = [ABdef(x) for x in f if not x.startswith(';')]

 print len(abmarks),"records from",filein
 print len(abdefs),"records from",filein1
 compare(abmarks,abdefs,fileout)
 # unused definitions
 n = len([x for x in abdefs if not x.used])
 print ';',n,"unused definitions from",filein1
 for abdef in abdefs:
  if not abdef.used:
   out = abdef.line
   print "UNUSED:",out.encode('utf-8')
   
