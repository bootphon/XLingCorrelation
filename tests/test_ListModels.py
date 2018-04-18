import sys
sys.path.insert(0, 'xlingcorrelation/')
import Segmented, Reports, ListModels
import numpy as np

path = '/Users/gladysbaudet//Desktop/PFE/'
cds = 'CDS/english/Brent/Brent/'
size = 'full_corpus/'
algos = ['ag/', 'dibs/', 'puddle/','baseline/', 'tp/relativeforward/', 'tp/absoluteforward/']
unit = 'syllable/'

import random
# print(hash(np.random.get_state()))
#rs = random.getstate()
#print(hash(rs))

random.seed(2)
np.random.seed(2)
# listsegfull = [Segmented.Segmented(path+'Results/'+size+algo+unit+'segmented.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', unit, algo, cds) for algo in algos]
listsegfull = [Segmented.Segmented(path+cds+'gold.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', 'unit', 'gold', 'cds')]
#listsegfull = [Segmented.Segmented(path+'Results/'+size+'ag/'+unit+'segmented.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', unit, 'ag/', cds)]
# seg1 = Segmented.Segmented(path+'Results/20k/dibs/syllable/segmented0.txt', path+'CDS/english/Brent/20k/gold0.txt', path+'CDS/english/Brent/sub_corpus/20k/ortholines0.txt')

# listseg = [listsegfull[0]]
# listsegfull=[Segmented.Segmented('../package/test/segmented.txt', '../package/test/gold.txt', '../package/test/ortholines.txt', 'unit', 'algo', 'corpus')]
# listsegfull = [Segmented.Segmented('../Results/Providence/tp/relativeforward/syllable/segmented.txt', '../CDS/english/Providence/gold.txt', '../CDS/english/Providence/ortholines.txt', 'syllable','tp','providence')]
rep = Reports.Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")


models = ListModels.ListModels(listsegfull, rep)

models.compute()
print(models._df)


# listsegfull = [Segmented.Segmented(path+'Results/'+size+algo+unit+'segmented.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', unit, algo, cds) for algo in algos]
# # seg1 = Segmented.Segmented(path+'Results/20k/dibs/syllable/segmented0.txt', path+'CDS/english/Brent/20k/gold0.txt', path+'CDS/english/Brent/sub_corpus/20k/ortholines0.txt')
#
# # listseg = [listsegfull[0]]
#
# rep = Reports.Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")
# models2 = ListModels.ListModels(listsegfull, rep)
#
# # print('intersect', models._results[0,0]._data)
# models2.compute()
# print(models2._df.head(5))
# print(models._df[models._df['age']==13])
# print(models2._df[models2._df['age']==13])
