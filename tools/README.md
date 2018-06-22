# Tools


These tools are used to process CDS corpora. These corpora are downloaded from [CHILDES](https://childes.talkbank.org), which regroups a set of files in CHAT format; these are the files we work with.

## Preprocessing steps

1. Get all .cha in one file (all lines in one document)

    `group_cha.sh path/to/folder/containing/chafiles path/to/output/all_cha.txt`
    
    Opens only .cha files from children below 4 yo (according to current format). 
    
    TODO: 
    
    [ ] replace by all .cha, add an option to get specific ages

2. Get orthographic lines (select lines from adults, remove tags); out file: ortholines.txt

    `cha2sel.sh path/to/output/from/group_cha/all_cha.txt selected_lines.txt path/to/output/storing/folder/`
    
    Removes lines from non-adult speakers. List of names to update for each new corpus.
    
    TODO:
    
    [ ] add an option to remove a certain name, so that not hard coded?
    
    `selcha2clean.sh path/to/cha2sel/output/to_clean.txt path/to/current/output/cleaned.txt`
    
    Removes all tags and punctuation. See details in code.

3. Phonologization using eSpeak wrapper (see [eSpeak](http://espeak.sourceforge.net/languages.html) to get possible languages)

    `phono.sh path/to/file/to/phonemize.txt language path/to/output/folder/phono_transcription.txt`
    
    Uses eSpeak and bootphon/phonemizer (can be run only if right environment installed - ok on local server)
    
    TODO:
    
    [ ] make it usable by external people (?)

4. Syllabify

     - Get set of consonants phones and set of vowels phones from the languages (create language-vowels.txt and language-consonants.txt)
  
    `getVowelsConsonants.py path/to/file/from/wikipedia/IPA_language/page/consonants.txt path/to/output/folder/consonants.txt`
    
    TODO: 
    
    [ ] provide examples of files used in pipeline

     - Check that all phones of phono are in either one list or the other (/!\ NOT DONE YET /!\)
  
  

     - Build naive onset list (for now on phono, could be on dict of language; only recovers word-initial onsets)
  
    `getOnsets.py path/to/phono_transcripts.txt path/to/output/folder/onsets.txt path/to/language/consonants.txt`
    
     - Syllabify (wordseg-syllabify; incremental ie solving problems one by one -unfound onset, words composed only of consonants, unknown phone- )
  
    TODO:
    
    [ ] put here different scripts to clean the different corpora, one by corpus
    [ ] do not forget to remove word/utterance from ortholines if removed from gold !!!

5. Insert word/syllable/phoneme tags (-p ' ' -s ';esyll' -w ';eword')

   `cleaning_post_syll.sh`
  
6. Create grammars (both phone and syllable, can also be done by wordseg)

   `phone_dic.py`
  
   `syllable_dic.py`

