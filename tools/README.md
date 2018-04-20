# Tools

## Preprocessing steps

blabla

- Get .cha in one file

    **group_all_cha.sh**

- Select+clean good lines => ortho

    **cha2sel.sh**
    
    **selcha2clean.sh**

- Phonologization => phono

    **phono.sh**

- Syllabify

  - Create language-vowels.txt and language-consonants.txt
  
    **getVowelsConsonants.py**

  - Check that all phones of phono are in either one list or the other
  
  

  - Build onsets (on phono ? on dict of language ?)
  
    **getOnsets.py**

- Insert right tags (-p ' ' -s ';esyll' -w ';eword')

  **cleaning_post_syll.sh**
  
- Create grammars (both phone and syllable)

  **phone_dic.py**
  
  **syllable_dic.py**

