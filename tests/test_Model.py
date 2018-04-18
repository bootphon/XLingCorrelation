
import unittest
from xlingcorrelation import Model

class test_Model(unittest.TestCase):

    def setUp(self):
        self.seg = {'baa baa':5, 'mummy':8, 'baby':5, 'hello':120, 'yes':13, 'I':1, 'you':1, 'him':1}
        self.rep = {'baa baa':0.2, 'mummy':0.9, 'hello':0.5, 'no':0.7, 'I':1.0, 'you':1.0, 'him':1.0}
        self.mod = Model(self.seg, self.rep)

    def test_intersect(self):
        answer = ['hello', 'him', 'I', 'mummy', 'you', 'baa baa']
        self.assertCountEqual(list(self.mod.get_intersect()["type"]), answer)

    def test_compute(self):
        reg = self.mod.compute()
        self.assertEqual(int(1000000*(reg['r2_value'])),356806)



if __name__=='__main__':
    unittest.main() # use python test_Segmented.py


# #get first dico from Segmented
# dic1 = {'baa baa':5, 'mummy':8, 'baby':5, 'hello':120, 'yes':13, 'I':1, 'you':1, 'him':1, }
# #get second dico from Reports (which is not here yeeeet)
# dic2 = {'baa baa':0.2, 'mummy':0.9, 'hello':0.5, 'no':0.7, 'I':1.0, 'you':1.0, 'him':1.0}
#
# mod = Model(dic1, dic2)
#
# print("inter \n", list(mod.get_intersect()["type"]), "inter \n")
#
# reg = mod.compute()
#
# print('r2 ', reg['r2_value'])
# print(mod._test_size) #should error somehow
