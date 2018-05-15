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

listsegfull = [Segmented(path+cds+'gold.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', 'unit', 'gold', 'cds')]

print("daddy : ",listsegfull[0]._freq_words['daddy'])
print("daediy : ", listsegfull[0]._freq_top['daediy'])
print("mommy : ",listsegfull[0]._freq_words['mommy'])
print("maamiy : ", listsegfull[0]._freq_top['maamiy'])
