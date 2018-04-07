# coding=utf-8
""" tooltip.py
    04-04-2018.  
"""
import sys,re,codecs
sys.path.append('../')
import transcoder
transcoder.transcoder_set_dir("transcoder/");

class Unused_Link(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  (self.linkkey,self.numinstance,self.authkey) = line.split('\t')
  self.authrec = None
  self.entry = None
 def make_entry(self):
  authrec = self.authrec
  authtype = authrec.authtype
  authdata = authrec.authdata
  self.entry = '<entry type="%s">%s</entry>' %(authtype,authdata)
 def print_type(self):
  known_types = {
   'ti':'Title',
   'au':'Author',
   'litcat':'Literary category',
   'subti':'subtitle',
  }
  authtype = self.authrec.authtype
  if authtype in known_types:
   type1 = known_types[authtype]
  else:
   print "WARNING: Unknown author type:",authtype
   type1 = authtype
  return type1
 def toString(self):
  outarr = []
  try:
   outarr.append(self.authrec.cologneid)
  except:
   print "Link.toString error:",self.line.encode('utf-8')
   exit(1)
  outarr.append(self.linkkey)
  authkey1 = self.authrec.authabbrev()
  linkkey1 = transcoder.transcoder_processString(self.linkkey,'as1','roman')
  # transcode the same way it is done for ls in 
  # correctionwork/cologne-issue-216
  linkkey2a = transcoder.transcoder_processString(self.linkkey,'asls','iast')
  linkkey2 = transcoder.transcoder_processString(linkkey2a,'iast','iast1')
  outarr.append(linkkey2)
  outarr.append(linkkey1)
  outarr.append(authkey1)
  outarr.append(self.authrec.toString())
  outarr.append(self.print_type())
  out = '\t'.join(outarr)
  return out

def applySA(s):
 s = s.replace('<slp cap="true">','{<SA>') 
 s = s.replace('<slp>','<SA>')
 s = s.replace('</slp>','</SA>')
 s = s.replace('&amp;','&')
 s = s.strip()
 return s

class Auth(object):
 def __init__(self,line):
  line = line.rstrip()
  self.line = line
  (self.cologneid,self.iastcode,self.authkey,self.authtype,self.authdata) = line.split('\t')
 def abbrv2AS(self):
  abbrv = self.authabbrev()
  abbrv1 =  transcoder.transcoder_processElements(abbrv,"slp1",'as',"SA")
  # capitalize letter after {
  abbrv2 = capitalize(abbrv1,tranout)
  #print 'CHK abbrv2AS:  %s -> %s -> %s' %(abbrv,abbrv1,abbrv2)
  abbrv2 = abbrv2 + '.'
  return abbrv2
 def authabbrev(self):
  m = re.search(r'<abbr>(.*?)</abbr>',self.authdata)
  a = m.group(1)
  a = applySA(a)
  return a
 def authdata_toString(self):
  m = re.search(r'<expandNorm>(.*?)</expandNorm>',self.authdata)
  if m:
   s = m.group(1)
  else:
   # expandMW is always present. Use it if expandNorm is not available
   m = re.search(r'<expandMW>(.*?)</expandMW>',self.authdata)
   s = m.group(1)
  # reformat this string
  s0 = s
  for tag in ['au','ti','litcat','subti']:
   regex = '</?%s>' % tag
   s = re.sub(regex,'',s)
  # put in '{' to indicate capitalization for Roman output
  s = applySA(s)
  return s
 def authtype_toString(self):
  known_types = {
   'ti':'Title',
   'au':'Author',
   'litcat':'Literary category',
   'subti':'subtitle',
  }
  authtype = self.authtype
  if authtype in known_types:
   type1 = known_types[authtype]
  else:
   print "WARNING: Unknown author type:",authtype
   type1 = authtype
  return type1

def create_authrecs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Auth(x) for x in f if x.rstrip()!= '']
 return recs
def capitalize(x,tranout):
 def cap(m):
  c = m.group(1)
  if tranout != 'roman':
   return c
  else:
   return c.upper()
 x = re.sub(r'{(.)',cap,x)
 return x


if __name__=="__main__":
 tranout = sys.argv[1]
 fileout = sys.argv[3]
 filein = sys.argv[2] # mwauth1
 authrecs = create_authrecs(filein)
 print len(authrecs),"auth records"
 outlines = []
 for ilink,authrec in enumerate(authrecs):
  outarr=[]
  outarr.append(authrec.cologneid)
  outarr.append(authrec.iastcode)
  authdata = authrec.authdata_toString()
  authdata1 =  transcoder.transcoder_processElements(authdata,"slp1",tranout,"SA")
  # capitalize letter after {
  authdata2 = capitalize(authdata1,tranout)
  outarr.append(authdata2)
  authtype = authrec.authtype_toString()
  outarr.append(authtype)
  out = '\t'.join(outarr)
  outlines.append(out)
 # print result
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outlines:
   f.write(out + '\n')
 print len(outlines),"lines written to",fileout
