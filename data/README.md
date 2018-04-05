# Data

## TODO

[x] upload data french

[x] upload clean data french

[ ] upload script used to get clean data (+steps and all)

[ ] organize in language/corpus/

## From .cha file
- Cleaning
  - cha2sel.sh
  - selcha2clean.sh
- Get nb of utterances (optional)
  - wc res.txt

## Phonologize file

Using bootphon/phonemize (eSpeak)

## Cleaning phonologized file

- Using getOnsets.py (to upload) and wordseg-syll
- Building basis language_onsets.txt using getOnsets.py (get consonants and build language_vowels.txt from wiki:IPAlanguage)
- Run wordseg-syll / update language_onsets.txt when necessary/when error/...
  - When error on word, wordseg-syll fails - should leave error word as it is+list (word,line)
