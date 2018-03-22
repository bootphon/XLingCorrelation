# import all you need

from collections import defaultdict
import subprocess
import

class Corpus(object):

    """
    For given path, containing all .cha files needed, retrieves CDS data,
    gets statistics about the corpus and cleans/phonologizes/syllabifies it.

    """

    def __init__(self, path):


        self.cha_all = ''

        self._nb_words = 0 # compute nb words
        self._nb_syll = 0 # compute nb syll after syllabification
        self._nb_phon = 0 # compute nb phon after phonologize

        self._words = defaultdict(int) # (dictionary with word : nb_occurences)
        self._syll = defaultdict(int) # same with syll
        self._phon = defaultdict(int) # same with phones

        """ Q : do we phono/syllabify at init ?"""
        """ Q : do we store data in datastruct or in file ?"""
        self.ortho = ""
        self.tags = ""

        return

    def compute_all_cha(self, path):

        # call script that finds all .cha files in path and concatenates them into self.cha_all
        # raise error if no such path or no cha file in path
        subprocess.call(['./write_cha.sh', path]) # creates path/all_cha.txt


    def clean_annotations(self, cha='/all_cha.txt', sel='/ortho_sel.txt', ortho='/ortholines.txt'):
        # call script that selects lines
        subprocess.call(['./cha2sel.sh', path+cha, path+sel]) # creates path/ortho_sel.txt

        # call script that cleans lines
        subprocess.call(['./selcha2clean.sh', path+sel, path+ortho]) # creates path/ortholines.txt

        # read and return ortholines.txt

        return

    def phonologize(self, language='en-us-festival', ortho='/ortholines.txt', tags='/tags.txt'):
        """
        LIST AVAILABLE LANGUAGES IN HELP
        call script w/
        module load espeak
        phonemize -l $language -p ' ' -w ';eword path+file > path+tags
        """
        subprocess.call(['./phono.sh', language, path+ortho, path+tags])

        # read and return tags
        return

    def syllabify(self):
        """
        TODO
        """
        return

    def count_words(self):
        return self._nb_words

    def get_words(self):
        return self._words.keys()

    def count_phone(self):
        return self._nb_phon

    def get_phon(self):
        return self._phon.keys()

    def count_syll(self):
        return self._nb_syll

    def get_syll(self):
        return self._syll.keys()
