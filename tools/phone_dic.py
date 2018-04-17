# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:45:32 2017

@author: elinlarsen
"""

import sys
from collections import Counter

def create_counter_phone(tags_file):
    phones=Counter()

    with open(tags_file,'r') as f:
        filedata = f.read()
        filedata = filedata.replace(';eword', '')
        # filedata = filedata.replace(' ', '')
        filedata = filedata.replace(';esyll', '')

        list_lines=filedata.split()

        for pho in list_lines:
                phones.update([pho])
    return phones, list_lines


def generate_unigram_grammar_phon_file(dic_phon, name_file):
    sorted_phones=[]
    for key,value in sorted(dic.items()):
        sorted_phones.append(key)
    with open (name_file,'w') as g:
        g.write('1 1 Sentence --> Colloc0s' + '\n')
        g.write('1 1 Colloc0s --> Colloc0'+ '\n')
        g.write('1 1 Colloc0s --> Colloc0 Colloc0s'+ '\n')
        g.write('Colloc0 --> Phonemes'+ '\n')
        g.write('1 1 Phonemes --> Phoneme'+ '\n')
        g.write('1 1 Phonemes --> Phoneme Phonemes'+ '\n')
        for syl in sorted_phones:
            g.write('1 1 Phoneme --> ' + syl + '\n')


tags=sys.argv[1]
dic, filedata=create_counter_phone(tags)
name=sys.argv[2]
generate_unigram_grammar_phon_file(dic, name)
