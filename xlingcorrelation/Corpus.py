# import all you need

from collections import defaultdict
import subprocess
# import wordseg #(?) #TODO

class Corpus(object):

    """
    For given path to tags.txt :
    - upload content of tags.txt in self._tags
        - no ortho or gold for now
    - get nb and list of words : words defaultdict
    - get nb and list of monosyllabic words + distribution : mono_words defaultdict
    - get nb and list of isolated words + distribution : iso_words defaultdict
    - nb+list of syllables + distribution : syllables defaultdict
    - nb+list of phonemes + distribution : phonemes defaultdict
    - distribution of words by length in syllables/phones

    """

    def __init__(self, path):

        self._path = path

        f = open(path, 'r')
        self._tags = f.readlines()
        f.close()

        self._words = defaultdict(int) # (dictionary with word : nb_occurences)
        self._syll = defaultdict(int) # same with syll
        self._phon = defaultdict(int) # same with phones

        self._mono_words = defaultdict(int) # same w/ monosyllabic words
        self._iso_words = defaultdict(int) # same w/ isolated words

        return

    def get_nb_syllables(self):
        return sum(self._syll.values())

    def get_nb_phones(self):
        return sum(self._phon.values())

    def get_nb_isolated_words(self):
        return sum(self._iso_words.values())

    def get_nb_monosyllabic_words(self):
        return sum(self._mono_words.values())

    def get_nb_words(self):
        return sum(self._words.values())

    def get_nb_unique_words(self):
        return len(list(self._words.keys()))

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

    # def compute_words(self):
    #     for line in self._ortho :
    #         curr_line = 0
    #         for word in line.split():
    #             self._words[word]+=1
    #             self.nb_words += 1
    #             curr_line += 1
    #         if (curr_line==0) :
    #             self._single_words += 1

    def count_words(self):
        return self._nb_words

    def get_word_tokens(self):
        return self._words

    def get_word_types(self):
        return self._words.keys()

    def count_phone(self):
        return self._nb_phon

    def get_phon(self):
        return self._phon.keys()

    def count_syll(self):
        return self._nb_syll

    def get_syll(self):
        return self._syll.keys()

    def get_stats(self):
        """ Using wordseg.stats (?)"""
        return
