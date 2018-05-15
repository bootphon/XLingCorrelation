from collections import Counter
from xlingcorrelation import Segmented, Reports, ListModels, Model, Corpus
# import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

path = '/Users/gladysbaudet//Desktop/PFE/'
# cds = 'CDS/english/Brent/Brent/'
cds = 'CDS/english/Brent/full_corpus/'
# cds = 'CDS/english/Brent/sub_corpus/10k/'
# cds = 'CDS/english/Providence/'
# cds = 'CDS/english/buckeye/'
# cds = 'CDS/english/BernsteinCDS/'
# cds = 'CDS/english/Brent/10K0/'
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
listsegfull = [Segmented(path+'Results/'+size+algo+unit+'segmented.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', unit, algo, cds) for algo in algos]
''' TODO change architecture of results !!! '''

print(cds)

# rep = Reports("tests/data/reports.csv")
rep = Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")
rep_ortho = rep.get_reports(13)

models = ListModels(listsegfull, rep)

models.compute()
models.plot_regression(2,0)
print(models._df.head(5))
