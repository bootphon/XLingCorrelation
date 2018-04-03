# XLingCorrelation

## TODO

- assert in tests
- documentation

## Goal

To have an easy to use package to compute correlation between algorithms segmentation and CDI reports
_describe project_

## Files

### Corpus.py
Handles .cha (or other ? or nothing at all, just clean ortho file ? or just tags.txt ?)
Can (or can't) phonologize and syllabify (which languages ? -none for now, except for English some time soon)

+ Get nb of words, phones, syllables in corpus
+ Get nb of single word utterances
+ Get stats on corpus

+ Store+stats ortho, gold

### Segmented.py
_Given segmented, ortho, gold_
+ Get dict from phono to ortho (build it rather from CDI ? Cheating lil bit)

+ Nb/list of words, syllables, phones
+ Freq_top, freq_words, write these in files
+ True pos and all
+ Evaluation (f-score &cie)

+ Correct words
+ Incorrect words

+ POS tagging ?


### Model.py


### translate.py
