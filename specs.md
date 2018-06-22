# What should be done

Considering we need results for
- different CDI ages
- different sizes of the same corpus
- different children of the same corpus
- different age ranges of the same corpus
- different sizes of the same corpus
- different measures? only WG comp for now

r2_measure_unit:
- index: algos
- columns: CDI ages

## Architecture

### Data

*in lang/corpus/*
- cha_files
- full_corpus/ortholines.txt, phono.txt, gold.txt, tags.txt, prepared_phoneme.txt, prepared_syllables.txt
- by_child/child_name/*same as in full_corpus*
- by_age/age/*same as in full_corpus*

### Results
*in lang/corpus/*
- full_corpus/
  - r2_measure_unit.csv
  - ortholines.txt
  - gold.txt
  - gold_freq_words.csv
  - algo/unit/eval.txt, segmented.txt, freq_top.txt, freq_words.txt
- by_size/size/
  - same as in full_corpus
- by_child/child_name/
  - same as in full_corpus
- by_age/age/
  - same as in full_corpus

## Implementation

### Data

- script to build by-child ortholines
- script to build by-age ortholines
- script to build by-size ortholines, 5k, 10k, then by 10k

> done automatically when building the full-corpus ortholines?

### Computations

- how and where to build r2_measure_unit.csv

### Display

- script to show r2_measure_unit.csv, whether everything or just selected algo for selected age
