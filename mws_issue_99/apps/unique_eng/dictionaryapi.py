
import sys,re,codecs
import requests

def write(fileout,lines):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line+'\n')
 print(len(lines),"written to",fileout)
 
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2] # found at dictionaryapi
 fileout1 = sys.argv[3] # not found at dictionaryapi
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [line.rstrip('\r\n') for line in f]
 print(len(lines),"lines from",filein)
 english = []
 other = []
 #lines = lines[0:20]
 for word in lines:
  #print('word=',word)
  r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/%s' %word)
  if r.status_code == 200:
   data = r.json()
   #print(len(data))
   data = data[0]
   meanings = data['meanings']
   meanings = meanings[0]
   definitions = meanings['definitions']
   firstdef = definitions[0]
   definition = firstdef['definition']
   out = '%s %s' %(word,definition)
   english.append(out)
  else:
   other.append(word)
   print('status = ',r.status_code)
 print(len(english),len(other))
 write(fileout,english)
 write(fileout1,other)

 
