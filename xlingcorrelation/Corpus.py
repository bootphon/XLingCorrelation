# import all you need

from collections import defaultdict
import subprocess
import wordseg #(?) #TODO

class Corpus(object):

    """
    For given path to tags.txt, blabla

    """

    def __init__(self, path):

        self._path = path
        # self.cha_all = ''

        self._nb_words = 0 # compute nb words
        self._nb_syll = 0 # compute nb syll after syllabification
        self._nb_phon = 0 # compute nb phon after phonologize

        self._words = defaultdict(int) # (dictionary with word : nb_occurences)
        self._syll = defaultdict(int) # same with syll
        self._phon = defaultdict(int) # same with phones

        self._single_words = 0

        self._ortho = []
        self._tags = []

        self.compute_all_cha()

        return

    # def compute_all_cha(self):
    #
    #     # call script that finds all .cha files in path and concatenates them into self.cha_all
    #     # raise error if no such path or no cha file in path
    #     subprocess.call(['./write_cha.sh', self._path]) # creates path/all_cha.txt
    #
    #
    # def clean_annotations(self, cha='/all_cha.txt', sel='/ortho_sel.txt', ortho='/ortholines.txt', ling_clean=None):
    #     # call script that selects lines
    #     subprocess.call(['./cha2sel.sh', self._path+cha, self._path+sel]) # creates path/ortho_sel.txt
    #
    #     # call script that cleans lines
    #     subprocess.call(['./selcha2clean.sh', self._path+sel, self._path+ortho]) # creates path/ortholines.txt
    #
    #     # if extraclean => whaddaya / what do you, you're => you are etc
    #     if ling_clean:
    #         subprocess.call([ling_clean, self._path+ortho])
    #     # read and fill right attribute with ortholines.txt
    #     f=open(self._path+ortho,"r+")
    #     self._ortho = f.readlines()
    #     f.close()
    #
    #     self.compute_words()
    #     return

    # def phonologize(self, language='en-us-festival', ortho='/ortholines.txt', tags='/tags.txt'):
    #     """
    #     LIST AVAILABLE LANGUAGES IN HELP
    #     call script w/
    #     module load espeak
    #     phonemize -l $language -p ' ' -w ';eword' path+file > path+tags
    #     """
    #     subprocess.call(['./phono.sh', language, self._path+ortho, self._path+tags])
    #
    #     # read and return tags
    #     return

    # def syllabify(self, onsets_file, vowels_file): #change parameters so that only take the language in which the file is written (onsets and vowels already in the package somewhere)
    #     """
    #     TODO
    #     """
    #     onsets = open(onset_file, 'r').readlines()
    #     vowels = open(vowels_file, 'r').readlines()
    #
    #     self._syll = syllabify(self._ortho, onsets, vowels)
    #     return

    def compute_words(self):
        for line in self._ortho :
            curr_line = 0
            for word in line.split():
                self._words[word]+=1
                self.nb_words += 1
                curr_line += 1
            if (curr_line==0) :
                self._single_words += 1

    def count_words(self):
        return self._nb_words

    def get_word_tokens(self):
        return self._words.keys()

    def get_word_types(self):
        return self._words

    def count_phone(self):
        return self._nb_phon

    def get_phon(self):
        return self._phon.keys()

    def count_syll(self):
        return self._nb_syll

    def get_syll(self):
        return self._syll.keys()

    def get_stats(self):
        """ Using wordseg.stats """
        return

    # TODO distribution words by length of syllable
