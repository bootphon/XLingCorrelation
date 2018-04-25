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


    def compute_words(self):
        word=self._tags.replace("\n", '')
        word=word.replace(" ", '')
        word=word.replace(self._syll_sep, '')
        word=word.replace(self._word_sep, ' ')[:-1] # getting words alright

        return (Counter(word.split()))

    def compute_syll(self):
        syll = self._tags.replace("\n", '')
        syll = syll.replace(" ", "")
        syll = syll.replace(self._word_sep, "")
        syll = syll.replace(self._syll_sep, " ")

        return (Counter(syll.split()))

    def compute_phon(self):
        phon = self._tags.replace("\n", '')
        phon = phon.replace(self._word_sep, "")
        phon = phon.replace(self._syll_sep, "")

        return (Counter(phon.split()))

    def compute_iso_words(self):
        iso=[]
        utt = self._tags.split("\n")
        for b in utt:
            if b.count(self._word_sep)==1:
                iso.append(b.replace(self._word_sep,"").replace(self._syll_sep,"").replace(" ",""))
        return (Counter(iso))

    def compute_mono_words(self):
        mono = []
        words = self._tags.split(self._word_sep)
        for b in words :
            if b.count(self._syll_sep)==1:
                mono.append(b.replace(self._word_sep,"").replace(self._syll_sep,"").replace(" ","").replace("\n",""))
        return (Counter(mono))

    def plot_counter(self, c, nb=100):
        labels, values = zip(*c.most_common(nb))
        indexes = np.arange(len(labels))
        width = 1

        plt.bar(indexes, values, width)
        plt.xticks(indexes + width * 0.5, labels)
        plt.show()

    def plot_phones(self, nb=100):
        self.plot_counter(self._phon, nb)

    def plot_syllables(self, nb=100):
        self.plot_counter(self._syll, nb)

    def plot_words(self, nb=100):
        self.plot_counter(self._words, nb)    

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

    def get_isolated_words(self):
        return self._iso_words

    def get_monosyllabic_words(self):
        return self._mono_words


    # def get_stats(self):
    #     """ Using wordseg.stats (?)"""
    #     return
