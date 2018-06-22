import pandas as pd

class Reports(object):
    """
    Reading from an already built prop_ cdi file
    Afterwards, from whole CDI to get age distribution, known by, no_knowledge ?
    """
    def __init__(self, path_cdi_prop, path_cdi_all=None):
        self._reports = pd.read_csv(path_cdi_prop, sep=None, engine='python')
        self._nouns = []
        self._verbs = []

        self._age_min = 0
        self._age_max = 0
        self._age_range = self.age_range()

        # self._function_words = self.select_function_words()
        # self._content_words = self.select_content_words()
        # # self._func_0 = self.modif_func_0()
        #
        # self._reports_by_age = [self.select_df(age)[['Type', 'prop', 'lexical_classes']] for age in self.age_range()]
        self._reports_by_age = [self.select_df(age)[['Type', 'prop']] for age in self.age_range()]
        # self._reports_by_age_function = [self.select_df(age,self._function_words)[['Type', 'prop', 'lexical_classes']] for age in self.age_range()]
        # self._reports_by_age_content = [self.select_df(age,self._content_words)[['Type', 'prop', 'lexical_classes']] for age in self.age_range()]
        # self._dict_word_freq = {} # really going from dataframe to dict to dataframe ? or dataframe from beginning ?
        self._word_freq = self._reports[['Type', 'prop']]
        # self._reports_by_age_func_0 = [self.select_df(age, self._func_0)[['Type', 'prop', 'lexical_classes']] for age in self.age_range()]

        self._form = path_cdi_prop.split('_')[1] #WG, WS
        self._type = path_cdi_prop.split('_')[2] #understands, produces

    def select_function_words(self):
        rep = self._reports

        return rep[rep['lexical_classes']=="function_words"]

    def select_content_words(self):
        rep = self._reports

        return rep[rep['lexical_classes']!="function_words"]

    def modif_func_0(self, prop):
        rep = self._reports

        rep.loc[rep.lexical_classes=="function_words", "prop"] = prop
        return rep

    def select_df(self, age, rep=None):
        # selection = self._reports[self._reports['age']==age]
        if rep is None:
            rep = self._reports
        return rep[rep['age']==age]

    def index_age(self, age):
        #error if < to age_min, error if > age_max
        return age-self._age_min


    def get_reports(self, age):
        return self._reports_by_age[self.index_age(age)]

    def get_reports_function(self, age):
        return self._reports_by_age_function[self.index_age(age)]

    def get_reports_content(self, age):
        return self._reports_by_age_content[self.index_age(age)]

    def get_modif_func_0(self, age, prop):
        self._func_0 = self.modif_func_0(prop)
        self._reports_by_age_func_0 = [self.select_df(age, self._func_0)\
        [['Type', 'prop', 'lexical_classes']] for age in self.age_range()]
        return self._reports_by_age_func_0[self.index_age(age)]

    def get_reports_by_age(self):
        return self._reports_by_age

    def get_form(self):
        return self._form

    def get_type(self):
        return self._type

    def get_age_min(self):
        return self._age_min

    def get_age_range(self):
        return self._age_range

    # def get_word_freq(self):
    #     return self._word_freq

    def distribution(self):
        return

    def age_range(self):
        mini = min(self._reports['age'])
        self._age_min = mini
        # print(mini)
        maxi = max(self._reports['age'])
        self._age_max = maxi
        # print(maxi)
        return list(range(mini, maxi+1))

    def known_by(self, word):
        return

    def no_knowledge(self):
        return
