import numpy as np
import Model

class ListModels(object):
    """
    Input :
        - list of segmented [Segmented.Segmented]
        - list of reports [Reports.Reports]

    TODO add age ofc
    """

    def __init__(self, segmented_list, reports_list):

        self._reports_list = reports_list
        self._segmented_list = segmented_list


        self._results = np.empty([len(reports_list), len(segmented_list)], dtype = Model.Model) # array of models ? dict ?
        self._r2 = np.empty([len(reports_list), len(segmented_list)], dtype = float)

    def compute(self):
        """
        Add logistic afterwards !!! TODO

        """
        for irep in range(len(self._reports_list)) :
            reports = self._reports_list[irep]
            for iseg in range(len(self._segmented_list)) :
                segmented = self._segmented_list[iseg]
                # create corresponding model
                self._results[irep, iseg] = Model.Model(segmented.get_freq_words(), reports.get_word_freq())
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
