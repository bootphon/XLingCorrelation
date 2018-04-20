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

    def __init__(self, path, syll_sep=";esyll", word_sep=";eword"):

        self._path = path
        self._syll_sep = syll_sep
        self._word_sep = word_sep

        f = open(path, 'r')
        self._tags = f.read()
        f.close()

        self._words = compute_words() # (dictionary with word : nb_occurences)
        self._syll = compute_syll() # same with syll
        self._phon = compute_phon() # same with phones

        self._mono_words = compute_mono_words() # same w/ monosyllabic words
        self._iso_words = compute_iso_words() # same w/ isolated words

        return

    def compute_words(self):
        blop=self._tags.replace("\n", '')
        blop=blop.replace(" ", '')
        blop=blop.replace(self._syll_sep, '')
        blop=blop.replace(self._word_sep, ' ')[:-1] # getting words alright

        return (Counter(blop.split()))

    def compute_syll(self):
        blop2 = self._tags.replace("\n", '')
        blop2 = blop2.replace(" ", "")
        blop2 = blop2.replace(self._word_sep, "")
        blop2 = blop2.replace(self._syll_sep, " ")

        return (Counter(blop2.split()))

    def compute_phon(self):
        blop3 = self._tags.replace("\n", '')
        blop3 = blop3.replace(self._word_sep, "")
        blop3 = blop3.replace(self._syll_sep, "")

        return (Counter(blop3.split()))

    def compute_iso_words(self):
        iso=[]
        blop4 = blop_init.split("\n")
        for b in blop4:
            if b.count(self._word_sep)==1:
                iso.append(b.replace(self._word_sep,"").replace(self._syll_sep,"").replace(" ",""))
        return (Counter(iso))

    def compute_mono_words(self):
        mono = []
        blop5 = blop_init.split(self._word_sep)
        for b in blop5 :
            if b.count(self._syll_sep)==1:
                mono.append(b.replace(self._word_sep,"").replace(self._syll_sep,"").replace(" ","").replace("\n",""))
        return (Counter(mono))


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

    def get_nb_word_types(self):
        return len(list(self._words.keys()))

    def get_words(self):
        return self._words

    def get_phones(self):
        return self._nb_phon

    def get_syllables(self):
        return self._nb_syll


    # def get_stats(self):
    #     """ Using wordseg.stats (?)"""
    #     return
