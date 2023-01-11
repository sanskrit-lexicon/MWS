import sys
import codecs
import re
from indic_transliteration import sanscript

def add_slp1_data(text):
	text = text.lstrip('<s1>')
	text = text.rstrip('</s1>')
	sl = sanscript.transliterate(text, 'iast', 'slp1')
	return '<s1 slp1="' + sl + '">' + text + '</s1>'

if __name__ == "__main__":
	filein1 = 'MW_corrected_by_AB.txt'
	filein2 = 'trailing_info_tags.txt'
	fileout = 'MW_new.txt'
	fin1 = codecs.open(filein1, 'r', 'utf-8')
	fin2 = codecs.open(filein2, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	lins1 = fin1.readlines()
	lins1 = [x.rstrip() for x in lins1]
	lins2 = fin2.readlines()
	lins2 = [x.rstrip() for x in lins2]
	counter = 0
	for lin1 in lins1:
		m = re.findall('(<s1>.*?</s1>)', lin1)
		if m:
			for iast_itm in m:
				slp1_rep = add_slp1_data(iast_itm)
				lin1 = lin1.replace(iast_itm, slp1_rep)
		# print(lin1 + lins2[counter])
		fout.write(lin1 + lins2[counter] + '\n')
		counter += 1
	fin1.close()
	fin2.close()
	fout.close()


