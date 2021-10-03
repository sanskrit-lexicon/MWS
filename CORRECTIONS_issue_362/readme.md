# Input files

1. `MW_lang.lines.xlsx` - File received from Andhrabharati. See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/362#issuecomment-915318257.
2. `ab_lang.tsv` - Copy paste of `MW_lang.lines.xlsx`. These first two files are not altered in the whole process.
3. `ab_lang1.tsv` - Copy of `ab_lang.tsv` file in which corrections are made.

# Scripts

1. `issue_632.py` - Identify the differences between AB and Cologne data.

# Output files

1. `log.txt` - Differences between two versions. Based on this, corrections in AB or Cologne data would be made. Ultimate goal is to have log.txt blank.

