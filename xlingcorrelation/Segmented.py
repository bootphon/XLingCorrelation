# import all you need

from collections import defaultdict, Counter
import subprocess
import re
import wordseg #(?) #TODO
from . import translate #(?) #TODO

class Segmented(object):

    """
    For given segmented text (result of an algorithm ? gold ?) : open, get stats (?) and all
    Unit given ?
    """


    def __init__(self, path_seg, path_gold, path_ortho, unit, algo, corpus):

        self._path_seg = path_seg #ok
        self._path_gold = path_gold #ok
        self._path_ortho = path_ortho #ok

        f = open(path_seg, 'r')
        self._segmented = f.read().lower() #ok
        f.close()

        f = open(path_gold, 'r')
        self._gold = f.readlines() #ok
        f.close()

        f = open(path_ortho, 'r')
        self._ortho = f.readlines() #ok
        f.close() # function to open files ?

        self.dict_phono_ortho = {} #ok
        # print(path_seg)
        # print("strip", path_seg.split('/'))
        self._unit = unit
        self._algo = algo
        self._corpus = corpus

        self._nb_words = 0 #ok
        self._words = defaultdict(int) #ok

        self._freq_top = Counter() #ok
        self._freq_words = Counter() #ok

        self._single_words = 0 #TODO (?)
        self._correct_words = [] #TODO
        self._incorrect_words = [] #TODO

        self._TP = 0 #TODO
        self._FP = 0
        self._TN = 0
        self._FN = 0 # to put in a new object ?

        self._eval = [] # will contain different f-score, precision and recall values #TODO

        self.freq_top()
        self.freq_words()

    def get_corpus(self):
        return self._corpus
    def get_algo(self):
        return self._algo
    def get_unit(self):
        return self._unit

    def freq_top(self): #ok
        """
        Computes a dictionary of the 10k most frequent words in the segmented file, in phonological form
        The keys are the words, the values are the number of occurrences of each word
        """
        #self._freq_top = sorted(A, key=A.get, reverse=True)[:10000]

        words = re.findall(r'\w+', self._segmented)
        # print("words ", words)
        # for word in words :
        #     self._freq_top[word] += 1

        pre_res = Counter(words)
        # # print(pre_res.most_common(10000)[-1])
        # keys_to_keep = set([key for key, _ in pre_res.most_common()])
        # for key in pre_res.keys() :
        #     if key in keys_to_keep :
        #         self._freq_top[key] = pre_res[key]


        self._freq_top = pre_res

        # [key for key, _ in counter.most_common()]
        return self._freq_top

    def write_freq_top(self, name): #TODO
        """
        Write freq_top in a text file
        """
        f = open(name, 'w')
        for double in self._freq_top.most_common() :
            f.write(str(double[1])+" "+ str(double[0])+'\n')
        f.close()
        return

    def get_freq_top(self):
        return self._freq_top


    def freq_words(self): #ok
        """
        Computes a dictionary of the most frequent words in the segmented file, in orthographic form
        Keys : words ortho, values : number of occurences of each word
        The number depends on the quantity of well segmented types... [no good]
        """
        # 1. Building dictionary #
        d = translate.build_phono_to_ortho(self._gold, self._ortho)
        self.dict_phono_ortho = translate.build_phono_to_ortho_representative(d)[0]
        # 2. Using dictionary to transcribe well segmented words into ortho rpz #
        # May be improved to transcribe badly segmented words ? #TODO

        # print(self.dict_phono_ortho)

        for word in self._freq_top.keys():
            # print(word)
            if word in self.dict_phono_ortho :
                # print('found')
                self._freq_words[self.dict_phono_ortho[word]]=self._freq_top[word]

        # print(self._freq_words['you'])
        return self._freq_words

    def get_freq_words(self):
        return self._freq_words

    def write_freq_words(self, name): #TODO
        f = open(name, 'w')
        for double in self._freq_words.most_common() :
            f.write(str(double[1])+" "+ str(double[0])+'\n')
        f.close()
        return

    def compute_words(self): #ok
        for word in self._segmented.split():
            self._words[word]+=1
            self._nb_words += 1
        return self._words

    def evaluate(self): #TODO
        return

    def pos_tagging(self): #TODO
        return
