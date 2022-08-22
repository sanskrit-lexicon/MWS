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
  # outarr.append('; %s ' % case.match)
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
  '1a': (r'([^ ])¦',
        r'\1 ¦'),
  '1b': (r'¦([^ ])',
        r'¦ \1'),
  '1c': (r'^([^¦]*)(<info and=)',
         r'\1**\2'),
  '1d': (r'^(<s>[^<]*?</s>) ¦ and (<s>[^<]*?</s>) ',
         r'\1 and \2 ¦ '),
  '1e': (r'^(<s>[^<]*?</s>) ¦ and (<s>[^<]*?</s>),',
         r'\1 and \2, ¦'),
  '1f': (r'</s> ¦ and <s>',
         r'</s>** ¦ and <s>'),

 '2a': (r'^(<s>[^<]*?</s>) ¦ or (<s>[^<]*?</s>) ',
         r'\1 or \2 ¦ '),
 '2b': (r'^(<hom>.*?</hom>) (<s>[^<]*?</s>) ¦ or (<s>[^<]*?</s>) ',
         r'\1 \2 or \3 ¦ '),
 '2c': (r'^(<hom>.*?</hom>) (<s>[^<]*?</s>) ¦ or (<s>[^<]*?</s>),',
         r'\1 \2 or \3, ¦ '),
 '2d': (r'</s> ¦ or <s>',
        r'</s>** or <s>'),
 '2e': (r'^(<s>[^<]*?</s> or <s>[^<]*?</s>,) ([^¦]*<info or=)',
        r'\1 ¦ \2'),
 '2f': (r'^(<s>[^<]*?</s> or <s>[^<]*?</s> or <s>[^<]*?</s>,) ([^¦]*<info or=)',
        r'\1 ¦ \2'),
 '2g': (r'^(<s>[^¦]*?</s> or <s>[^¦]*?</s>) ([^¦]*<info or=)',
        r'\1 ¦ \2'),

 '2h': (r'^<s>([^<]*)(<srs/>)?([^<]*?)</s> or <s>([^<]*)(<srs/>)?([^<]*?)</s>, ([^¦]*<info or=)',
        r'<s>\1\2\3</s> or <s>\4\5\6</s>, ¦ \7'),
 '3a': (r'^(<s>[^<]*?</s>, <lex>[^<]*?</lex>) or (<s>[^<]*?</s>, <lex>[^<]*?</lex>) or (<s>[^<]*?</s>, <lex>[^<]*?</lex>) ([^<][^¦]*<info or=)',
        r'\1 or \2 or \3 ¦ \4'),
 '3b': (r'^(<s>[^<]*?</s>, <lex>[^<]*?</lex>) or (<s>[^<]*?</s>, <lex>[^<]*?</lex>) ([^<][^¦]*<info or=)',
        r'\1 or \2 ¦ \3'),
 '3c': (r'^(<s>[^<]*?</s>) \(([^)]+)\) or (<s>[^<]*?</s>) \(([^)]+)\), <lex>',
        r'\1 (\2) or \3 (\4), ¦ <lex>'),
 '3c1': (r'^(<s>[^<]*?</s>) \(([^)]+)\) or (<s>[^<]*?</s>) \(([^)]+)\), ([^¦])([^¦]*<info or=)',
        r'\1 (\2) or \3 (\4), ¦ **\5\6 '),

 '3d': (r'^(<s>[^<]*?</s>) \[([^]]+)\] or (<s>[^<]*?</s>) \[([^]]+)\], <lex>',
        r'\1 [\2] or \3 [\4], ¦ <lex>'),

 '3e': (r'^(<s>[^<]*?</s>, <lex>[^<]*?</lex>) or (<s>[^<]*?</s>, <lex>[^<]*?</lex>) ([^<¦][^¦]*<info or=)',
        r'\1 or \2 ¦ \3'),
 '3f': (r'^(<s>[^<]*?</s>) \[([^]]+)\] or (<s>[^<]*?</s>) \[([^]]+)\], <lex>',
        r'\1 [\2] or \3 [\4], ¦ <lex>'),  # same as '3d'
 '3g': (r'(<s>[^<]*?</s>), (<s>[^<]*?</s>), (<lex[^¦]*<info or=)',
        r'\1, \2, ¦ \3'),
 '3h': (r'^(<s>[^<]*?</s>), (<lex>.*?</lex>) or (<s>[^<]*?</s>), (<lex>.*?</lex>) ([a-zA-Z][^¦]*<info or=)',
        r'\1, \2 or \3, \4 ¦ \5'),
 '3i': (r'(<s>[^<]*?</s>), (<s>[^<]*?</s>) or (<s>[^<]*?</s>), (<lex[^¦]*<info or=)',
        r'\1, \2 or \3, ¦ \4'),
 '3j': (r'(<s>[^<]*?</s>) \(([^)]+)\) or (<s>[^<]*?</s>), (<lex[^¦]*<info or=)',
        r'\1 (\2) or \3, ¦ \4'),
 '3k': (r'(<s>[^<]*?</s>), (<lex>.*?</lex>) \(([^)]+)\) or (<s>[^<]*?</s>), (<lex>.*?</lex>) \(([^)]+)\) ([^¦]*<info or=)',
        r'\1, \2 (\3) or \4, \5 (\6) ¦ \7'),
 '3l': (r'(<s>[^<]*?</s>) and (<s>[^<]*?</s>), (<lex>[^<]*</lex>) ([^¦]*<info) or=',
        r'\1 and \2, ¦ \3 \4 and='),
 '3m': (r'^(<s>[^<]*?</s>), (<lex>.*?</lex>) or (<s>[^<]*?</s>), (<lex>.*?</lex>) (<[^¦]*<info or=)',
        r'\1, \2 or \3, \4 ¦ \5'),
 '3n': (r'^(<s>[^<]*?</s>) \(([^)]+)\) or (<s>[^<]*?</s>) \(([^)]+)\), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 (\2) or \3 (\4), ¦ \5 \6'),
 '3o': (r'^(<s>[^<]*?</s>) \(or ([^)]+)\), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 (or \2), ¦ \3 \4'),

 '3p': (r'^(<s>[^<]*?</s>) \[or ([^)]+)\], (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 [or \2], ¦ \3 \4') ,

 '3q': (r'^(<s>[^<]*?</s>), (<lex>.*?</lex>) or (<s>[^<]*?</s>), (<lex>.*?</lex>,?) ([^¦]*<info or=)',
        r'\1, \2 or \3, \4 ¦ \5'),
 '3r': (r'^(<s>[^<]*?</s>), (<s>[^<]*?</s>), or (<s>[^<]*?</s>,?) (<lex>.*?</lex>,?) ([^¦]*<info or=)',
        r'\1, \2 or \3 ¦ \4 \5'),
 '3s': (r'(<s>[^<]*?</s>) \[([^]]+)\], (<lex>.*?</lex>) or (<s>[^<]*?</s>) \[([^]]+)\], (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 [\2], \3 or \4 [\5], \6 ¦ \7'),
 '3t': (r'(<s>[^<]*?</s>), (<lex>.*?</lex>) \[([^]]+)\] or (<s>[^<]*?</s>), (<lex>.*?</lex>) \[([^]]+)\] ([^¦]*<info or=)',
        r'\1, \2 [\3] or \4, \5 [\6] ¦ \7'),

 '3u': (r'(<s>[^<]*?</s>), (<lex>.*?</lex>) \(([^]]+)\), (<s>[^<]*?</s>), (<lex>.*?</lex>) \(([^)]+)\) ([^¦]*<info or=)',
        r'\1, \2 (\3), \4, \5 (\6) ¦ \7'),
 '3v': (r'(<s>[^<]*?</s>), (<s>[^<]*?</s>), (<ab>.*?</ab>) for ([^¦]*<info or=)',
        r'\1, \2, ¦ \3 for \4'),
 '3w': (r'^([^¦]*)[.] See ([^¦]*<info or=)',
        r'\1. ¦ See \2'),
 '3x': (r'(<s>[^<]*?</s>) or \(([^)]+)\) (<s>[^<]*?</s>), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 or (\2) \3, ¦ \4 \5'),
 '3y': (r'^([^¦]*)[.] (<lex>[^<]*?</lex>) ([^¦]*<info or=)',
        r'\1. ¦ \2 \3'),
 '3z': (r' and (<s>[^<]*?</s>), (<ab>.*)<info or=',
        r'and \1, ¦ \2<info and='),
 '4a': (r'(<s>[^<]*?</s>) \[([^)]+)\] or (<s>[^<]*?</s>), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 [\2] or \3 ¦ \4 \5'),
 '4b': (r', or (<s>[^<]*?</s>) \(([^)]+)\), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r', or \1 (\2), ¦ \3 \4'),
 '4c': (r'^([^¦]*) = ([^¦]*<info or=)',
        r'\1 ¦ = \2'),
 '4d': (r'^(<s>[^<]*?</s>), (<s>[^<]*?</s>), ([^¦]*<info or=)',
        r'*\1, \2, \3'),
 '4e': (r'(<s>[^<]*?</s>,?) or (<s>[^<]*?</s>), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 or \2, ¦ \3 \4'),
 '4f': (r'(<s>[^<]*?</s>,?) \[([^)]+)\], (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1 [\2], ¦ \3 \4'),
 '4g': (r'^(<s>[^<]*?</s>), (<lex>.*?</lex>) ([^¦]*<info or=)',
        r'\1, \2 ¦ \3'),
 '4h': (r'^<s>([^¦]+)<info or=',
        r'*<s>\1<info or='),
 '4i': (r'^<hom>([^¦]+)<info or=',
        r'*<hom>\1<info or='),

 '5a': (r'(<s>[^<]*?</s>) ¦ \(or (<s>[^<]*?</s>)\), (<lex>.*?</lex>)',
        r'\1 (or \2), ¦ \3'),
 '5b': (r'(<s>[^<]*?</s>) ¦ \(or (<s>[^)]*?</s>)\), (<lex>.*?</lex>)',
        r'\1 (or \2), ¦ \3'),
 '5c': (r'(<s>[^<]*?</s>) ¦ \(or (<s>[^)]*?</s>)\) (<lex>.*?</lex>)',
        r'\1 (or \2) ¦ \3'),
 '5d': (r'(<s>[^<]*?</s>) ¦ \(or ([^)]*?)\) (.*<info or=)',
        r'\1 (or \2) ¦ \3'),
 '5e': (r'(<s>[^<]*?</s>) ¦ \(or ([^)]*?)\), (.*<info or=)',
        r'\1 (or \2), ¦ \3'),
 '5f': (r'^([^¦]+¦ \(or .*<info or=)',
        r'***\1'),
 '5g': (r' ¦ (\(or [^)]*?\),?)',
        r' \1 ¦'),
 '5h': (r' √ ([1-9]\.)',
        r' √ <hom>\1</hom>'),
 '5i': (r' √ ([1-9])',
        r' √ <hom>\1.</hom>'),
 '5j': (r'^(<s>.*?</s>.*)¦ 1\. 2\.',
        r'<hom>1.</hom> <hom>2.</hom>\1 ¦'),
 '5k': (r'See under ([1-9]+\.) <s>',
        r'See under <hom>\1</hom> <s>'),
 '5l': (r'under ([1-9]+\.) <s>',
        r'under <hom>\1</hom> <s>'),
 '5m': (r'also ([1-9]+\.) <s>',
        r'also <hom>\1</hom> <s>'),
 '5n': (r'and ([1-9]+\.) <s>',
        r'and <hom>\1</hom> <s>'),
 '5o': (r' or ([1-9]+\.) <s>',
        r' or <hom>\1</hom> <s>'),
 '5p': (r' (to|for|with|<ab>cf.</ab>) ([1-9]+\.)',
        r' \1 <hom>\2</hom>'),
 '5q': (r'(<ab>g\.</ab>) ([1-9]+\.) <s>',
        r'\1 <hom>\2</hom> <s>'),
 '5r': (r'(=) ([1-9]+\.) <s>',
        r'\1 <hom>\2</hom> <s>'),
 '5s': (r' ([1-9]+\.) <s>',
        r' <hom>\1</hom> <s>'),
 '5t': (r'\(([1-9]+\.) <s>',
        r'(<hom>\1</hom> <s>'),
}
"""
  '1': (r'',
        r''),
"""
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
  
