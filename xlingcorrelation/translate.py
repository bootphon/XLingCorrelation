# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:45:59 2016

@author: elinlarsen
"""

import collections
try:
    # Python 2
    from itertools import izip
except ImportError:
    # Python 3
    izip = zip
import pandas as pd




def build_phono_to_ortho(gold, ortho, debug=True):
    """
    Dictionnary from phono text to ortho text
    # open ortho and gold file and check if in each line, the number of words match
    # if not, skip the line and count the error,
    # then create a dictionarry with key each phono token and value a dictionary  of ortho token with their occurence
    """
    count_errors = 0
    d=collections.defaultdict(dict)
    i=0
    for line_phono_init, line_ortho_init in izip(gold, ortho):
        i+=1
        line_phono = line_phono_init.lower().split()
        line_ortho = line_ortho_init.lower().split()
        if len(line_phono) != len(line_ortho):
            count_errors += 1
            if debug:
                print("Error at line "+str(i)+" :")
                print("phono: "+line_phono_init+"ortho: "+line_ortho_init)
        else:
            for word_phono, word_ortho in izip(line_phono, line_ortho):
                count_freq = d[word_phono]
                try:
                    count_freq[word_ortho] += 1
                except:
                    count_freq[word_ortho] = 1
    print("There were {} mismatches between gold and orthographic lines.".format(count_errors))
    return d


def build_phono_to_ortho_representative(d):
    """
    list of two dictionaries:
    # 1. one of phono token and the most representative ortho token
    # 2. one linking token to their freqency
    """
    res ={}
    token_freq={}
    for d_key,d_value in d.items():
        value_max=0
        key_max = 'undefined'
        value_max, key_max = max((value, key) for key, value in d_value.items())
        # for key, value in d_value.items():
        #     print(key)
        #     if value > value_max:
        #         value_max = value
        #         key_max = key
        res[d_key] = key_max
        token_freq[value_max]=key_max
    #freq_token = {v: k for k, v in token_freq.iteritems()}
    freq_res=sorted(token_freq.items(),reverse=True)
    return res,freq_res
