"""make_html_comments.py
"""
import sys,re,codecs,os
import requests

class Comment(object):
 def __init__(self,lines,case):
  self.lines = lines
  self.case = case
  self.images_text = []
  self.images_rev = []
 def get_k1(self):
  for line in self.lines:
   m = re.search(r'<k1>(.*?)<k2>',line)
   if m:
    return m.group(1)
  k1 = 'Could not find metaline'
  return k1
 
def init_comments(filein):
 recs = [] # array of Comment objects
 with codecs.open(filein,"r","utf-8") as f:
  c = []  # array of lines from BEGIN to END
  incase = False
  nline = 0
  for line in f:
   line = line.rstrip('\r\n')
   if line.startswith(';; END'):
    c.append(line)
    recs.append(Comment(c,case))
    c = []
    incase = False
    continue
   m = re.search(r';; BEGIN (.*)$',line)
   if m:
    case = int(m.group(1))
    #c.append(line)
    incase = True
   if incase:
    c.append(line)
 print(len(recs),"Records read from",filein)
 return recs

def init_images(filein,comments):
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   line = line.rstrip()
   if line.startswith(';'): continue
   if line == '': continue  # blank line
   parts = re.split(r' +',line)
   # case img1 img2 ...
   # ASSUME: case is index (base 1) into comments
   case = int(parts[0])
   comment = comments[case - 1]
   images = parts[1:]
   for img in images:
    if img.endswith('_rev'):
     comment.images_rev.append(img)
    else:
     comment.images_text.append(img)

def make_html_start(title):
 s = '''<!DOCTYPE html>
<head>
<title>%s</title>
<meta charset="UTF-8">
</head>
<body>
''' % title
 lines = s.splitlines()
 return lines

def make_html_end():
 s = '''</body>
</html>
'''
 lines = s.splitlines()
 return lines

def images_to_string(prefixes):
 a = []
 for p in  prefixes:
  filename = 'images/%s.png' % p
  imgelt = '<img src="%s"/>' % filename
  a.append(imgelt)
 return '\n'.join(a)

def make_html_textarea(lines):
 a = []
 for line in lines:
  if line.startswith((';; BEGIN',';; END')):
   continue
  elif line.startswith(('<L>','<Ls>')):
   a.append(' ')
   a.append(line)
  elif line.startswith('<LEND>'):
   a.append(line)
   a.append(' ')
  else:
   a.append(line)
 return '\n'.join(a)

def make_html_comment(comment):
 k1 = comment.get_k1()
 textimagestr = images_to_string(comment.images_text)
 revimagestr = images_to_string(comment.images_rev)
 textareastr = make_html_textarea(comment.lines)
 template = '''
<details><summary>%s</summary>
 <div class='image'>
  <H3>TEXT</H3>
   %s
  <H3>REV</H3>
   %s
 </div>
 <div class='comment'>
  <H3>COMMENT</H3>
  <textarea rows="20" cols="72">%s</textarea>
 </div>
</details>
'''
 htmlstr = template % (k1,textimagestr,revimagestr,textareastr)
 htmlarr = htmlstr.splitlines()
 return htmlarr

def make_html_title():
 x = '<H2>Review of revisions to MW from supplement</H2>'
 y = '<it>Refer <a href="https://github.com/sanskrit-lexicon/MWS/issues/97">Github mws issue 97</a></it>'
 return [x,y]

def make_html_body(comments):
 outarr = make_html_title()
 for c in comments:
  outarr = outarr + make_html_comment(c)
 return outarr

def make_html(comments,title):
 html1 = make_html_start(title)
 html3 = make_html_end()
 html2 = make_html_body(comments)
 return html1 + html2 + html3

def iast_ascii_lo(x):
 y = x.lower()
 replacements = [
  ('ā','a'),
  ('ṛ','ri'),
  ('ś','sh'),
  ('ṣ','sh'),
  ('ñ','n'),
  
  ('ī','i'),
  ('ṇ','n'),
  
 ]
 for old,new in replacements:
  y = y.replace(old,new)
 m = re.search(r'[^a-z]',y)
 if m:
  print('iast_ascii_lo error:',x,y)
 return y

def write_temp(comments):
 filetmp = "temp.txt"
 with codecs.open(filetmp,"w","utf-8") as f:
  for c in comments:
   k1 = c.get_k1()
   k1a = iast_ascii_lo(k1)
   f.write('%d %s %s_rev\n' %(c.case,k1a,k1a))
 print('wrote to',filetmp)

if __name__ == "__main__":
 filein = sys.argv[1] # ab_2_comments.txt
 dictlo = 'mw'
 filein1 = sys.argv[2]  # ab_2_comments_img.txt
 fileout = sys.argv[3]  # constructed html file
 title = sys.argv[4]
 comments = init_comments(filein)
 images = init_images(filein1,comments)
 htmlarr = make_html(comments,title)  # array of lines
 with codecs.open(fileout,"w","utf-8") as f:
  for out in htmlarr:
   f.write(out+'\n')

 write_temp(comments)
 
