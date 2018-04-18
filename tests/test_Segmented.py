import sys
import unittest
# sys.path.insert(0, 'src/')
import Segmented

class test_Segmented(unittest.TestCase):

    def test(self):
        self.assertTrue(True)
#
#     @classmethod
#     def setUpClass(cls): # once before everything #populate database for example
#         pass
#
#     @classmethod
#     def tearDownClass(cls): # once after everything
#         pass
#
    def setUp(self): # will run before each test
        self.seg = Segmented.Segmented('tests/data/segmented.txt', 'tests/data/gold.txt', 'tests/data/ortholines.txt', 'unit', 'algo', 'corpus')

        pass #could set up  new directroy in which to work+create objects needed

    def tearDown(self): # will run after each test
        pass #could erase that directory

    def test_freqtop(self):
        # for element in self.seg.freq_top():
        #     self.assert
        self.assertCountEqual(self.seg.freq_top().most_common(), [('luhk', 2), ('siydhaxlayt', 1), ('layt', 1), ('dhaetsaxkaemerax', 1), ('yuwwaanaxsihtahp', 1), ('yuwwaanaxsiydhaxkaemerax', 1), ('yuwwaanaxsihtwihdhmaamiy', 1), ('dherzaxlihtaxlrehdlayt', 1), ('siy', 1), ('ehmeychehmyuwwaanaxsiy', 1)])
        # run python -m unittest test_Segmented.py

    def test_freqwords(self):
        self.assertCountEqual(self.seg.freq_words().most_common(),[('look', 2), ('light', 1), ('see', 1)])
# # TODO : assert
#
#
# if __name__=='__main__':
#     unittest.main() # use python test_Segmented.py

    # edge cases


# seg = Segmented.Segmented('test/segmented.txt', 'test/gold.txt', 'test/ortholines.txt', 'unit', 'algo', 'corpus')
# # print('freqtop ',seg.freq_top().most_common())
# # print('freqtop2', seg.freq_top())
# # print('freqwords ', seg.freq_words().most_common())
# print('compute',list(seg.compute_words()))
# print(seg._nb_words)
