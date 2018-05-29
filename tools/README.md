# Tools


These tools are used to process CDS corpora. These corpora are downloaded from [CHILDES](https://childes.talkbank.org), which regroup a set of files in CHAT format; these are the files we work with.

## Preprocessing steps

1. Get all .cha in one file (all lines in one document)

    `group_all_cha.sh`

2. Get orthographic lines (select lines from adults, remove tags); out file: ortholines.txt

    `cha2sel.sh`
    
    `selcha2clean.sh`

3. Phonologization using eSpeak wrapper (see [eSpeak](http://espeak.sourceforge.net/languages.html) to get possible languages)

    `phono.sh`

4. Syllabify

  - Get set of consonants phones and set of vowels phones from the languages (create language-vowels.txt and language-consonants.txt)
  
    `getVowelsConsonants.py`

  - Check that all phones of phono are in either one list or the other (/!\ NOT DONE YET /!\)
  
  

  - Build naive onset list (for now on phono, could be on dict of language; only recovers word-initial onsets)
  
    `getOnsets.py`
    
  - Syllabify (wordseg-syllabify; incremental ie solving problems one by one -unfound onset, words composed only of consonants, unknown phone- )
  
  (put here different scripts to clean the different corpora, one by corpus)

5. Insert word/syllable/phoneme tags (-p ' ' -s ';esyll' -w ';eword')

  `cleaning_post_syll.sh`
  
6. Create grammars (both phone and syllable, can also be done by wordseg)

   `phone_dic.py`
  
   syllable_dic.py`

