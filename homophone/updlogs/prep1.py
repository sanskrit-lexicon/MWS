"""prep1.py April 9, 2015
 Read a version of monier.xml, and newhom_log.txt and
 construct preliminary versions of log_yyyymmdd-01.txt and 
 notes_yyyymmdd-01.txt.
 Read an option code to determine which records of newhom_log to use.
"""
import sys, re,codecs

def prep1(cases,mwdict,mwrecs,fileout,fileout1):
 fout = codecs.open(fileout,"w",'utf-8') # log file
 fout1 = codecs.open(fileout1,"w",'utf-8') # notes file
 for icase in xrange(0,len(cases)):
  case = cases[icase]
  fout1.write(";%s\n" %('-'*60))
  fout1.write("; Case %03d %s\n" %(icase+1,case.key))
  for i in xrange(0,case.n): # # of lnums and homs in this case
   L=case.lnums[i]
   if not (L in mwdict):
    print icase," ERROR 1 in prep1",case.key," (line=",case.line
    exit(1)
   imwrec=mwdict[L]
   mwrec = mwrecs[imwrec]
   hom = case.homs[i]
   fout1.write("hom=%s\n"%hom) 
   fout1.write("%s\n" % mwrec.line)
   # Apr 12, 2012 print cases with '0'
   if (hom == '0'):
    fout.write("Update\n")
    line = mwrec.line    
    if i==0:
     fout.write("<L>%s</L>X\n" % L)
     line = re.sub(r'</key2>','</key2><hom>%s</hom>'% 1,line)
    else:
     fout.write("<L>%s</L>?\n" % L)
    fout.write("%s\n" % line)
 fout.close()
 fout1.close()
 return

class Case(object):
 def __init__(self,line):
  line = line.rstrip() # remove trailing spaces, if any
  # line expected to have form
  # key l1 ... ln h1 ... hn
  parts = re.split(r' +',line)
  self.key = parts[0]
  m = len(parts)
  if (m % 2) != 1:
   print "Case ERROR: ",m,parts
   exit(1)
  n = (m - 1) / 2
  self.n = n
  self.lnums = parts[1:n+1]
  self.homs = parts[n+1:m]
  self.line = line
  if False: # dbg
   if (self.key == 'ezwa'):
    print line
    print self.key,self.lnums,self.homs
  
def select_cases(option,filein):
 f = codecs.open(filein,"r",'utf-8')
 #f = codecs.open(filein,"r")
 n = 0 # number of lines read
 cases = [] # array of Case objects, returned
 for line in f:
  n = n + 1
  #if (n > 5): 
  # break
  line=line.rstrip('\r\n')
  if re.search(r'-----',line):  
   continue
  if re.search(r'[.][.]',line):
   continue # first line
  case = Case(line)
  if option == '1':
   homs = case.homs
   homs1 = sorted(list(set(homs)))
   if homs1 == ['0','1']:  # this is what option 1 likes
    cases.append(case)
    #print "CHOSE: ",case.line," <--> ",case.lnums,case.homs
   continue # nothing else of interest for option 1
  elif option == '2':
   homs = case.homs
   homs1 = sorted(list(set(homs)))
   if homs1 == ['0','1']:  # these selected by option == 1
    continue
   if (len(homs1) !=2) or (not ('0' in homs1)):
    continue
   # we have the cases option 2 likes
   cases.append(case)
   continue # nothing else of interest
  else:
   print "ERROR select_cases: unknown option",option
   exit(1)
   
 f.close()
 print n,"lines from",filein
 print len(cases)," selected"
 return cases

class Mwrec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n') 
  self.line = line
  m = re.search(r'^<(.*?)>.*?<key1>(.*?)</key1>.*?<L.*?>(.*?)</L>',line)
  if not m:
   print "MWrec error\n",line.encode('utf-8')
   exit(1)
  self.H = m.group(1)
  self.key1 = m.group(2)
  self.L = m.group(3)

def init_mwrecs(filein):
 with codecs.open(filein,"r",'utf-8') as f:
  mwrecs = [Mwrec(line) for line in f if line.startswith('<H')]
 mwdict={} # 
 n = 0
 for mwrec in mwrecs:
  mwdict[mwrec.L] = n
  n = n + 1
 print len(mwrecs),"records from",filein
 return (mwdict,mwrecs)

if __name__=="__main__": 
 option = sys.argv[1]
 filein = sys.argv[2] #  monier.xml
 filein1 = sys.argv[3] #  newhom_log.txt
 fileout = sys.argv[4] # log_yyyymmdd-01.txt
 fileout1 = sys.argv[5] # notes_yyyymmdd-01.txt
 cases = select_cases(option,filein1)
 (mwdict,mwrecs) = init_mwrecs(filein)
 prep1(cases,mwdict,mwrecs,fileout,fileout1)
