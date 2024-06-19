# coding=utf-8
""" 
diffs_separate.py
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def write_lines(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
 print(len(outarr),"lines written to",fileout)

def k2_to_k1(k2):
 # Is this complete?
 k1 = re.sub(r'[^aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzshL|~]','',k2)
 return k1

def get_diffs_1(lines):
 ans = []
 for line in lines:
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>(.*?)<',line)
  if m == None:
   print('metaline invalid format:\n%s' % line)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  k2 = m.group(4)
  k1a = k2_to_k1(k2)
  if k1 == k1a:
   continue
  Lpc = '<L>%s<pc>%s' %(L,pc)  
  a = (Lpc,k1,k2,k1a)
  b = '\t'.join(a)
  ans.append(b)
 return ans

def get_diffs_2(lines):
 ans = []
 for line in lines:
  if not line.startswith('<L>'):
   continue
  m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<k2>(.*?)<',line)
  if m == None:
   print('metaline invalid format:\n%s' % line)
  L = m.group(1)
  pc = m.group(2)
  k1 = m.group(3)
  k2 = m.group(4)
  k2s = k2.split(',')  # list of alternate k2s
  k2ok = True
  for k2a in k2s:
   k1a = k2_to_k1(k2a)
   if k1 != k1a:
    k2ok = False
  if k2ok:
   continue
  Lpc = '<L>%s<pc>%s' %(L,pc)  
  a = (Lpc,k1,k2,k1a)
  b = '\t'.join(a)
  ans.append(b)
 return ans

def separate_copilot(A, B):
    # code courtesy of copilot (06-17-2024)
    # Find common elements
    common_elements = list(set(A) & set(B))
    
    # Find unique elements in A
    unique_A = list(set(A) - set(B))
    
    # Find unique elements in B
    unique_B = list(set(B) - set(A))
    
    return common_elements, unique_A, unique_B
"""
# Example usage:
A = [1, 2, 3, 4]
B = [1, 11, 22, 33, 44, 3, 4]
result = separate(A, B)
print(result)  # Output: ([1, 3, 4], [2], [33, 11, 22, 44])
"""


def separate(A, B):
    # preserves ordering
    # Initialize dictionaries to store the indices of elements in A and B
    # copilot put these two un-needed lines in the answer.
    # while the 
    #index_A = {elem: i for i, elem in enumerate(A)}
    #index_B = {elem: i for i, elem in enumerate(B)}
    # This code works, but is quite inefficient as it
    # does list-traversal.
    # Find common elements and preserve their order
    common_elements = [elem for elem in A if elem in B]
    
    # Find unique elements in A and preserve their order
    unique_A = [elem for elem in A if elem not in B]
    
    # Find unique elements in B and preserve their order
    unique_B = [elem for elem in B if elem not in A]
    
    return common_elements, unique_A, unique_B
"""
# Example usage:
A = [1, 2, 3, 4]
B = [1, 11, 22, 33, 44, 3, 4]
result = separate(A, B)
print(result)  # Output: ([1, 3, 4], [2], [11, 22, 33, 44])
"""
def test():
 A = [1, 2, 3, 4]
 B = [1, 11, 22, 33, 44, 3, 4]
 result = separate(A, B)
 print(result)  # Output: ([1, 3, 4], [2], [11, 22, 33, 44])
 exit(1)
#test()

def check_diffs(lines1,lines2):
 A = [re.sub(r'<pc>.*$','',line) for line in lines1]
 B = [re.sub(r'<pc>.*$','',line) for line in lines2]
 both,cdsl,ab = separate(A,B)
 print(len(both),len(cdsl),len(ab))
 
if __name__=="__main__":
 filein1 = sys.argv[1] # cdsl diff file
 filein2 = sys.argv[2] # ab diff file
 fileout1 = sys.argv[3]  # both
 fileout2 = sys.argv[4]  # cdsl unique
 fileout3 = sys.argv[5]  # ab unique
 
 lines1 = read_lines(filein1)
 print(len(lines1),"read from",filein1)
 lines2 = read_lines(filein2)
 print(len(lines2),"read from",filein2)
 (both,cdsl,ab) = separate(lines1,lines2)
 write_lines(fileout1,both)
 write_lines(fileout2,cdsl)
 write_lines(fileout3,ab)
 # as a check, do the same for <L>
 check_diffs(lines1,lines2)
 
