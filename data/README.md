# Data

Basically, what is done here is in three steps :
1. the .cha files a retrieved and cleaned, so that we get only adult utterances with no annotation, only orthographic transcription which gives a ortholines.txt file
2. this file is phonologized, using a wrapper of eSpeak available on bootphon (phonemizer) given the orthographic transcription, the language and the output file
3. this new output file is then syllabified. To do so :
  - the vowels and consonants of the language are retrieved on Wikipedia
  - the onsets are retrieved from word beginnings of the corpus
  - wordseg-syll is run using the file to syllabify, the vowels and the onsets files
    - at each error, either a vowel or consonant is missing (ex: word from another language), an onset is missing, encoding problems for special characters, or there might be a problem in the phonologized corpus (only consonants word, ...)
    - no more error => success ! A syllabified corpus !
  - still some cleaning to do due to syll script (add ;eword, ;esyll, ...)


## Summary of corpora and CDI data

https://docs.google.com/spreadsheets/d/1glaH9zcTbcX9FOCBt2N55-Paj8YpvJLzWosgG8Bcpco/edit?usp=sharing

## From .cha file
- Cleaning - using cha2sel2clean.sh
  - cha2sel.sh
  - selcha2clean.sh
- Get nb of utterances (optional)
  - wc res.txt

## Phonologize file

Using bootphon/phonemize (eSpeak)

Command :

(qsub) ./phono.sh file/to/process.txt language-marker phonologized/file.txt

To check for language markers, phonemize --help. The script just loads the espeak module, and runs the phonemize command.

## Cleaning phonologized file

Command :

wordseg-syll -p '\_' -w ' ' phono.txt onsets.txt vowels.txt > syllabified.txt

- Using getOnsets.py (to upload) and wordseg-syll
- Building basis language_onsets.txt using getOnsets.py (get consonants and build language_vowels.txt from wiki:IPAlanguage)
- Run wordseg-syll / update language_onsets.txt when necessary/when error/...
  - When error on word, wordseg-syll fails - should leave error word as it is+list (word,line)
