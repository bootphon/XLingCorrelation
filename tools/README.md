# Tools

## Preprocessing steps

blabla

1. Get .cha in one file

    **group_all_cha.sh**

2. Select+clean good lines => ortho

    **cha2sel.sh**
    
    **selcha2clean.sh**

3. Phonologization => phono

    **phono.sh**

4. Syllabify

  - Create language-vowels.txt and language-consonants.txt
  
    **getVowelsConsonants.py**

  - Check that all phones of phono are in either one list or the other
  
  

  - Build onsets (on phono ? on dict of language ?)
  
    **getOnsets.py**

5. Insert right tags (-p ' ' -s ';esyll' -w ';eword')

  **cleaning_post_syll.sh**
  
6. Create grammars (both phone and syllable)

   **phone_dic.py**
  
   **syllable_dic.py**

