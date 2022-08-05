#-*- coding:utf-8 -*-
"""make_change_regex.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,match,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.newline = newline
  
def init_cases(lines,regex1,regex2):
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   #continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  m = re.search(regex1,line)
  if m == None:
   continue
  match = m.group(0)
  newline = re.sub(regex1,regex2,line)
  if newline != line:
   # generate a case
   cases.append(Case(metaline,iline,line,match,newline))

 print(len(cases),'changes of %s'%regex1)
 return cases

def write_cases_regex(fileout,cases,regex1,regex2):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(cases)))
 outarr.append('; regex1 = /%s/,  regex2 = /%s/' %(regex1,regex2))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; %s ' % case.match)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  if previline == iline:
   # in case we change same line more than once
   line = prevline
  outarr.append('%s old %s' %(lnum,line))
  nchg = nchg + 1
  newline = case.newline
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
  previline = iline
  prevline = newline

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)

interpret_option = {
  '1': (r'<ls>RTL\.</ls> p\. *([0-9]+\.?)', r'<ls>RTL. p. \1</ls>'),
  '1a': (r' Jain\b', r' <ns>Jain</ns>'),
  '1b': (r'([^>])\binterr\.', r'\1<ab>interr.</ab>**'),
  '1c': (r'(<ls[^<]*)([0-9]),([0-9])', r'**\1\2, \3'),
  '1d': (r'<ls>Bādar\.</ls>,? <ab>Sch\.</ab>',r'<ls>Bādar., Sch.</ls>'),
  '1e': (r'HaṉsUp', r'HaṃsUp'),
  '1f': (r'<ls>Siṉhâs.',  r'<ls>Siṃhās.'),
  '1g': (r'<ls n="Siṉhâs.',  r'<ls n="Siṃhās.'),
  '1h': (r'<s1 slp1="KaRqa-praSasti">Khaṇḍa-praśasti</s1>',
         r'<ls>Khaṇḍa-praśasti</ls>'),
  '1i': (r'<s1 slp1="mAGamAhAtmya">Māghamāhātmya</s1>',
         r'<ls>Māghamāhātmya</ls>'),
  '1j': (r'<ls>Nid.</ls> <ab>Sch.</ab>',
         r'<ls>Nid., Sch.</ls>'),
  '1k': (r'<s1 slp1="paYcadaSI">Pañcadaśī</s1>',
         r'<ls>Pañcadaśī</ls>'),
  '1l': (r'<s1 slp1="paraSurAma-prakASa">Paraśurāma-prakāśa</s1>',
         r'<ls>Paraśurāma-prakāśa</ls>'),
  '1m': (r'<s1 slp1="pradyumna-vijaya">Pradyumna-vijaya</s1>',
         r'<ls>Pradyumna-vijaya</ls>'),
  '1n': (r'<ls>Uṇ.</ls>,? <ab>Sch.</ab>',
         r'<ls>Uṇ., Sch.</ls>'),
  '1o': (r'<s1 slp1="upapurARa">Upapurāṇa</s1>',
         r'<ls>Upapurāṇa</ls>'),
  '1p': (r'<ls>Yājñ.</ls>,? <ab>Sch.</ab>',
         r'<ls>Yājñ., Sch.</ls>'),
  '1q' : (r'Vṛṣabhân\.',
          r'Vṛṣabhān.'),
  '1r' : (r'(Śiva[ -]?[sS]ūtra)',
          r'**\1'),
  '1s' : (r'mystic\.',
          r'<ab>mystic.</ab>'),
  '1t' : (r'</ls>\(<ab',
          r'</ls> (<ab'),
  '1u' : (r'<ls>R.</ls> \(<ab>B.</ab>\)',
          r'<ls>R. (B.)</ls>'),
  '1v' : (r'<ls>R.</ls> \(<ab>ed.</ab> <ab>Bomb.</ab>\)',
          r'<ls>R. (ed. Bomb.)</ls>'),
  '1w' : (r'<ls>R.</ls> \(<ab>ed.</ab> <ab>Gorr.</ab>\)',
          r'<ls>R. (ed. Gorr.)</ls>'),
  '1x' : (r'<ls>MBh.</ls> \(<ab>B.</ab>\)',
          r'<ls>MBh. (B.)</ls>'),
  '1y' : (r'Mbh\.', r'MBh.'), # print change
  '1z' : (r'<ls>MBh.</ls> \(<ab>ed',
          r'**<ls>MBh.</ls> (<ab>ed'),
  '2a' : (r'<ls>R. <ab>G.</ab>',
          r'<ls>R. G.'),
  '2b' : (r'(<ls[^<]*<ab>ed\.)',
          r'**\1'),
  '2c' : (r'(<ls[^<]*<ab>[a-z])',
          r'**\1'),
  '2d' : (r'<ls>R. <ab>B.</ab>',
          r'<ls>R. B.'),
  '2e' : (r'(<ls[^<]*<ab>.*?</ls>)',
          r'**\1'),
  '2f' : (r'>\(',
          r'>**('),
  '2g' : (r'</ab><ab>',
          r'</ab> <ab>'),
  '2h' : (r'</ab><s>',
          r'</ab> <s>'),
  '4a' : (r'<ls>ŚivaP. <ab>Rev.</ab></ls>',
          r'<ls>SkandaP. Rev.</ls>'),
  '4b' : (r'(<ls>[^.]*)[.]([il])',
          r'**\1. \2'),
 
 }
if __name__=="__main__":
 # Problem with input of regexes into command line
 # python make_change_regex.py ', </ls>' '</ls>, ' temp_mw_3.txt temp.txt
 # The 2nd paramenter '</ls>, ' is not intepreted properly
 # It prints as "<C:/Program Files/Git/ls>, "
 # Thus, use an option number
 option = sys.argv[1]
 regex1,regex2 = interpret_option[option]

 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines,regex1,regex2) 
 print(len(cases),'cases')
 write_cases_regex(fileout,cases,regex1,regex2)
  
