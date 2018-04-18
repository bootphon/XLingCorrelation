
import unittest
from xlingcorrelation import Segmented

class test_Segmented(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls): # once before everything #populate database for example
#         pass
#
#     @classmethod
#     def tearDownClass(cls): # once after everything
#         pass
#
    def setUp(self): # will run before each test
        self.seg = Segmented('tests/data/segmented.txt', 'tests/data/gold.txt', 'tests/data/ortholines.txt', 'unit', 'algo', 'corpus')
        pass #could set up  new directroy in which to work+create objects needed

    def tearDown(self): # will run after each test
        pass #could erase that directory

    def test_freqtop(self):
        answer=[('luhk', 2), ('siydhaxlayt', 1), ('layt', 1), ('dhaetsaxkaemerax', 1), ('yuwwaanaxsihtahp', 1), ('yuwwaanaxsiydhaxkaemerax', 1), ('yuwwaanaxsihtwihdhmaamiy', 1), ('dherzaxlihtaxlrehdlayt', 1), ('siy', 1), ('ehmeychehmyuwwaanaxsiy', 1)]
        self.assertCountEqual(self.seg.freq_top().most_common(), answer)
        # run python -m unittest test_Segmented.py

    def test_freqwords(self):
        answer=[('look', 2), ('light', 1), ('see', 1)]
        self.assertCountEqual(self.seg.freq_words().most_common(), answer)

    def test_compute_words(self):
        answer=['dherzaxlihtaxlrehdlayt', 'layt', 'dhaetsaxkaemerax', 'luhk', 'yuwwaanaxsihtahp', 'siydhaxlayt', 'ehmeychehmyuwwaanaxsiy', 'yuwwaanaxsihtwihdhmaamiy', 'yuwwaanaxsiydhaxkaemerax', 'siy']
        self.assertCountEqual(self.seg.compute_words(), answer)

    # add edge cases
    # add homophones !!

if __name__=='__main__':
    unittest.main() # use python test_Segmented.py
