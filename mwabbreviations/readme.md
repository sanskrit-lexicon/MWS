
## MW abbreviations

### mwabbreviations.png
This is a scan of the page of the MW dictionary that describes the abbreviations used by the author within the dictionary.

### mwab_input.txt
This file provides abbreviations and definitions used within the Cologne digitization of the MW dictionary.

Each line contains the abbreviation, then (in the `<disp>` tag), the abbreviation definition. 

The abbreviations include
* The abbreviations shown in the mwabbreviations.png above.
* Other abbreviations which we have thus far identified within the Cologne digitization of the dictionary.  These types are indicated by the `<INFER/>` tag.
For these we have *made up* an abbreviation definition since a defintion was not explicitly provided by the text.
* 108 cases marked as DEF=NODEF.  These all involve the abbreviation
  'Va1rtt' (AS coding) or Vārttika.  They are currently (2017-11-07) improperly
  coded and under investigation for coding improvement.

### work/compare.txt
This file provides a useful summary of the actual abbreviation markings of the Cologne digitization along with the abbreviation definitions.
Each entry shows the 
* the abbreviation
* the frequency with which the abbreviation is marked in the digitization
* the definition according to the mwab_input
* A NOTE: of extra information appearing in mwab_input (such as `<INFER/>`
* Those entrys tagged as `<UNMARKED>` and or `<UNUSED/>` (27 currently) 
  represent cases where an entry X in the printed Abbreviations does not have
  any instances marked as abbreviations `<ab>X</ab>` in the digitization.
* There are a few cases (such as mfn, cl., P., etc.) where the abbreviation
  of the text is implied by some other markup than `<ab>` in the digitization.

### abbr.html
This file is a copy of file from Cologne server at
docs/monier/abbr.html.

It has no current use.

### The current *official* list of mw abbreviations
The abbreviations for MW that are used for tooltips in the displays
is in csl-pywork repository. Namely:
https://github.com/sanskrit-lexicon/csl-pywork/blob/master/v02/distinctfiles/mw/pywork/mwab/mwab_input.txt.

