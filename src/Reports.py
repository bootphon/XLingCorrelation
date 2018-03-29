import pandas as pd

class Reports(object):
    """
    Reading from an already built prop_ cdi file
    Afterwards, from whole CDI to get age distribution, known by, no_knowledge ?
    """
    def __init__(self, path_cdi_prop, path_cdi_all=None):
        self._reports = pd.read_csv(path_cdi_prop, sep=None)
        self._nouns = []
        self._verbs = []

        self._dict_word_freq = {} # really going from dataframe to dict to dataframe ? or dataframe from beginning ?
        self._word_freq = self._reports[['Type', 'prop']]

        self._form = path_cdi_prop.split('_')[1] #WG, WS
        self._type = path_cdi_prop.split('_')[2] #understands, produces

    def get_form(self):
        return self._form

    def get_type(self):
        return self._type

    def get_word_freq(self):
        return self._word_freq
    def distribution(self):
        return

    def age_range(self):
        mini = min(self._reports['age'])
        # print(mini)
        maxi = max(self._reports['age'])
        # print(maxi)
        return list(range(mini, maxi+1))

    def known_by(self, word):
        return

    def no_knowledge(self):
        return
