from collections import Counter
from xlingcorrelation import Segmented, Reports, ListModels, Model
# import numpy as np

path = '/Users/gladysbaudet//Desktop/PFE/'
# cds = 'CDS/english/Brent/Brent/'
cds = 'CDS/english/Brent/full_corpus/'
# cds = "CDS/french/Lyon/"
size = 'full_corpus/'
algos = ['ag/', 'dibs/', 'puddle/','baseline/', 'tp/relativeforward/', 'tp/absoluteforward/']
unit = 'syllable/'

# import random
# print(hash(np.random.get_state()))
#rs = random.getstate()
#print(hash(rs))
#
# random.seed(2)
# np.random.seed(2)

# listsegfull = [Segmented("tests/data/segmented.txt", "tests/data/gold.txt", "tests/data/ortholines.txt", "unit", "algo", "cds")]
# listsegfull = [Segmented(path+'Results/'+size+algo+unit+'segmented.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', unit, algo, cds) for algo in algos]
listsegfull = [Segmented(path+cds+'gold.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', 'unit', 'gold', 'cds')]
# listsegfull = [Segmented(path+cds+'gold.txt', path+cds+'gold.txt', path+cds+'ortholines-limited-updated.txt', 'unit', 'gold', 'cds')]



print("daddy : ",listsegfull[0]._freq_words['daddy'])
print("daediy : ", listsegfull[0]._freq_top['daediy'])

# rep = Reports("tests/data/reports.csv")
rep = Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")

# listortho=Counter()
ortho=open(path+cds+"ortholines.txt",'r').read()
rep_ortho=rep.get_reports(13)
seg_ortho=Counter(ortho.split())
mod_ortho=Model(seg_ortho,rep_ortho)
mod_ortho.compute()
mod_ortho.plot()

# models = ListModels(listsegfull, rep)
#
# models.compute()
# models.plot_regression(5,0)
# print(models._df)
# print(models.)


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
