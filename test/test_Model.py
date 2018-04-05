import sys
sys.path.insert(0, 'src/')
import Model


#get first dico from Segmented
dic1 = {'baa baa':5, 'mummy':8, 'baby':5, 'hello':120, 'yes':13, 'I':1, 'you':1, 'him':1}
#get second dico from Reports (which is not here yeeeet)
dic2 = {'baa baa':0.2, 'mummy':0.9, 'hello':0.5, 'no':0.7, 'I':1.0, 'you':1.0, 'him':1.0}

mod = Model.Model(dic1, dic2)

print(mod.get_intersect())

reg = mod.compute()

print(reg['r2_value'])
print(mod._test_size) #should error somehow
