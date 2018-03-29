import numpy as np
import Model
import Reports

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


        self._results = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = Model.Model) # array of models ? dict ?
        self._r2 = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = float)
        self._std_err = np.empty([len(self._reports.get_age_range()), len(self._segmented_list)], dtype = float)

        self._df = pd.DataFrame(columns=['corpus', 'algo', 'unit', 'form', 'type', 'age', 'R2', 'std_err', 'nb_words'])

    def compute(self):
        """
        Add logistic afterwards !!! TODO

        """
        for age in self._reports.get_age_range() :
            reports = self._reports.get_reports(age)
            irep = age-self._reports.get_age_min()

            for iseg in range(len(self._segmented_list)) :
                segmented = self._segmented_list[iseg]
                # create corresponding model
                self._results[irep, iseg] = Model.Model(segmented.get_freq_words(), reports)
                # compute correlation for this very model
                self._results[irep, iseg].compute()
                self._fill_dataframe(segmented, reports, age, self._results[irep, iseg])

        # fill r2 array
        self._fill_r2_stderr_arrays()
        # TODO same with other values - std_err maybe
        self._fill_dataframe()
        return

    def _fill_r2_stderr_arrays(self):
        for i in range(len(self._results)):
            for j in range(len(self._results[0])):
                self._r2[i,j] = self._results[i,j].get_lin_reg()['r2_value']
                self._std_err[i,j] = self._results[i,j].get_lin_reg()['std_err']
        return

    def fill_dataframe(self, segmented, reports, age, model):
        corpus = segmented.get_corpus()
        algo = segmented.get_algo()
        unit = segmented.get_unit()
        form = reports.get_form()
        type = reports.get_type()
        age = age #//
        R2 = model.get_lin_reg()['r2_value']
        std_err = model.get_lin_reg()['std_err']
        nb_words = len(model.get_intersect()) #TODO check nrow
        # 
        # serie = pd.Series()


    def get_r2(self):
        return self._r2
