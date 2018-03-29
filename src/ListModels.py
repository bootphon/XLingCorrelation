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


    def compute(self):
        """
        Add logistic afterwards !!! TODO

        """
        for rep in self._reports.get_age_range() :
            reports = self._reports.get_reports(rep)
            irep = rep-self._reports.get_age_min()

            for iseg in range(len(self._segmented_list)) :
                segmented = self._segmented_list[iseg]
                # create corresponding model
                self._results[irep, iseg] = Model.Model(segmented.get_freq_words(), reports)
                # compute correlation for this very model
                self._results[irep, iseg].compute()

        # fill r2 array
        self.fill_r2_array()
        # TODO same with other values - std_err maybe
        return

    def fill_r2_array(self):
        for i in range(len(self._results)):
            for j in range(len(self._results[0])):
                self._r2[i,j] = self._results[i,j].get_lin_reg()['r2_value']
        return

    def get_r2(self):
        return self._r2
