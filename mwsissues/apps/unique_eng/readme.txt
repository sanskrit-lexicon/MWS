
cp  ../../unique_section-wise_entries_Andhrabharati/'unique words extracted.txt' temp_unique_words.txt


 51297 lines
 each line is a 'word' from mw.txt, got by unknown means.

temp_words_00.txt
 Manually remove Arabic words. 
python remove_arabic.py temp_unique_words.txt temp_words_00.txt words_arabic.txt words_nonascii.txt
51188 written to temp_words_00.txt
3 written to words_arabic.txt
107 written to words_nonascii.txt

temp_words_01.txt
 Words with only letters, except for possible ending punctuation [.,;:?!]
   The ending punctuation dropped.
 words_other.txt  other words, including ending punctuation.
python remove_punct.py temp_words_00.txt words_01.txt words_other.txt
51188 lines from temp_words_00.txt
24305 written to words_01.txt
7825 written to words_other.txt

(+ 24305 7825) = 32130  (non-duplicates after removing ending punctuation.)

===================================================================

Search for words in MW, but first reduce xml-elements to space character ' '
 <ab.*?<ab>, <s>X</s>, <ls>X</ls>, <info.*?/>,
 <bot>X</bot>,<hom>X</hom>, <etym>X</etym>, <lang.*?</lang>
 <lex.*?</lex>

# Takes about 4 minutes
python check_instance.py words_01.txt temp_mw.txt words_mw.txt words_notmw.txt
24305 words from temp_words_01.txt
880576 lines read from temp_mw.txt
287627 entries found
23744 written to words_mw.txt
561 written to words_notmw.txt

# test version
python check_instance.py temp.txt temp_mw.txt temp_words_mw.txt temp_words_notmw.txt

===================================================================
## english/nonenglish
words_02_english.txt
words_02_nonenglish.txt
Use dictionary 'en_US' and 'en_GB' from enchant.

python detect_english.py words_mw.txt words_mw_US.txt words_mw_GB.txt words_mw_noneng.txt
23744 lines from words_mw.txt
21954 written to words_mw_US.txt
281 written to words_mw_GB.txt
1509 written to words_mw_noneng.txt


python find_instance.py words_mw_noneng.txt temp_mw.txt instance_mw_noneng.txt

# test version
python find_instance.py temp.txt temp_mw.txt instance_mw_noneng.txt


; ----------------------------------------------
; Not very useful
try api at https://dictionaryapi.dev/
python dictionaryapi.py words_nonenglish.txt words_english1.txt words_nonenglish1.txt
; ----------------------------------------------
Search for words found outside of 

