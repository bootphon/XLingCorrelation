
import unittest
from xlingcorrelation import Reports


"""

To test in reports :
- right range of ages -- what if ages with no reports in between ?
- age selection ok
- then what ?

"""

class test_Reports(unittest.TestCase):

    def setUp(self):
        # self.rep = Reports("tests/data/report_cdi.csv")
        pass

    def test_age_range(self):
        pass

rep = Reports("~/Desktop/PFE/CDI/english/Prop_WS_produces_16_30.csv")
print(rep.get_type(), rep.get_form())
# print(rep._word_freq.columns)
print(rep.age_range())
# ind_age = lambda x : x-rep.get_age_min()
# print(rep.get_reports_by_age()[ind_age(21)].head(5))
print(rep.get_reports(21).head(5))
