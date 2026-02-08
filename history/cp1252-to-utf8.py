"""
 cp1252-to-utf8.py
 Nov 16, 2015
 ejf
 Utility program to convert a file from the cp1252 encoding to the utf-8 
 encoding.  The conversion is done using the Python codecs module.
 Usage:  python cp1252-to-utf8.py <inputfile> <outputfile>
 Apr 18, 2024.  Change to python3 syntax for print
"""
import sys,codecs

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 f = codecs.open(filein,"r","cp1252")
 fout = codecs.open(fileout,"w","utf-8")
 n = 0
 for line in f:
  n=n+1
  line = line.rstrip('\r\n')  # remove possible windows-convention end-of-line
  fout.write("%s\n" % line)
 f.close()
 fout.close()
 print (n,"lines converted, and written to",fileout)
