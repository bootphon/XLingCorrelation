import numpy as np
from xlingcorrelation import Model, Reports
import pandas as pd

class ListModels(object):
    """
    Input :
        - list of segmented [Segmented.Segmented]
        - list of reports [Reports.Reports]

    TODO add age ofc
    TODO weird, in phono...
    """

    def __init__(self, segmented_list, reports):
        # self._reports = reports

        self._reports = reports
        self._segmented_list = segmented_list


        self._results = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = Model) # array of models ? dict ?
        self._r2 = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = float)
        # self._std_err = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = float)
        # self._p_value = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = float)
        self._columns = ['corpus', 'algo', 'unit', 'form', 'type', 'age', 'R2', 'nb_words']
        self._df = pd.DataFrame(columns=self._columns)

    def plot_regression(self, i, j):
        self._results[i,j].plot()


    def compute(self):
        """
        Add logistic afterwards !!! TODO

        """
        for age in self._reports.get_age_range() :
            # print(age)
            reports = self._reports.get_reports(age)
            irep = age-self._reports.get_age_min()

            for iseg in range(len(self._segmented_list)) :
                segmented = self._segmented_list[iseg]
                # create corresponding model
                # print(segmented.get_freq_words())
                self._results[irep, iseg] = Model(segmented.get_freq_words(), reports)
                # compute correlation for this very model
                self._results[irep, iseg].compute()
                self._fill_dataframe(segmented, age, self._results[irep, iseg])

        # fill r2 array
        # self._fill_r2_stderr_arrays()

        # TODO same with other values - std_err maybe
        # self._fill_dataframe()
        return

    def _fill_r2_stderr_arrays(self):
        for i in range(len(self._results)):
            for j in range(len(self._results[0])):
                self._r2[i,j] = self._results[i,j].get_lin_reg()['r2_value']
                self._std_err[i,j] = self._results[i,j].get_lin_reg()['std_err']
                self._p_value[i,j] = self._results[i,j].get_lin_reg()['p_value']
        return

    def _fill_dataframe(self, segmented, age, model):
        corpus = segmented.get_corpus()
        algo = segmented.get_algo()
        unit = segmented.get_unit()
        form = self._reports.get_form()
        type = self._reports.get_type()
        age = age #//
        R2 = model.get_lin_reg()['r2_value']
        # p_value = model.get_lin_reg()['p_value']
        nb_words = int(len(model.get_intersect())) #TODO check nrow
        #
        serie = pd.Series([corpus, algo, unit, form, type, age, R2, nb_words], index=self._columns)
        self._df = self._df.append(serie, ignore_index=True)

    def write_dataframe(self, name):
        # to change - ie, create (?) right archi and store according to language/corpus/algo/unit/form
        # what do we store in one single csv exactly ?
        self._df.to_csv(name)


    def get_r2(self):
        return self._r2
