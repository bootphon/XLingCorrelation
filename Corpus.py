# import all you need

from collections import defaultdict
import subprocess
import

class Corpus(object):

    """
    From given path, containing all .cha files needed, retrieves CDS data,
    gets statistics about te corpus and cleans/phonologizes/syllabifies it.
    """

    def __init__(self, path):


        self.cha_all = ''



        self._nb_words = 0 # compute nb words
        self._nb_syll = 0 # compute nb syll after syllabification
        self._nb_phon = 0 # compute nb phon after phonologize

        self.words = defaultdict(int) # (dictionary with word : nb_occurences)
        self.syll = defaultdict(int) # same with syll
        self.phon = defaultdict(int) # same with phones

        """ Question : do we phono/syllabify at init ?"""
        """ Question : do we store data in datastruct or in file"""
        self.ortho = ""
        self.tags = ""

        return

    def compute_all_cha(self, path):

        # call script that finds all .cha files in path and concatenates them into self.cha_all
        # raise error if no such path or no cha file in path
        subprocess.call(['./write_cha.sh', path]) # creates path/all_cha.txt


    def clean_annotations(self):
        # call script that selects lines
        subprocess.call(['./cha2sel.sh', path]) # creates path/ortho_sel.txt

        # call script that cleans lines
        subprocess.call(['./selcha2clean.sh', path]) # creates path/ortholines.txt
        return

    def phonologize(self):
        return

    def syllabify(self):
        return

    def count_words(self):
        return self._nb_words

    def count_phone(self):
        return self._nb_phon

    def count_syll(self):
        return self._nb_syll
