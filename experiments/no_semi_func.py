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

listsegfull = [Segmented(path+'Results/'+size+algo+unit+'segmented.txt', path+cds+'gold.txt', path+cds+'ortholines.txt', unit, algo, cds) for algo in algos]

rep = Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")
rep_func_0 = rep.get_modif_func_0(13, 0.8)
rep_content = rep.get_reports_content(13)

for seg in listsegfull:
    print(seg._algo)
    mod_ortho = Model(seg._freq_words, rep_content)
    mod_ortho.compute()
    mod_ortho.plot()

for seg in listsegfull:
    print(seg._algo)
    mod_ortho = Model(seg._freq_words, rep_func_0)
    mod_ortho.compute()
    mod_ortho.plot()
# plt.show()

print("gold")
ortho=open(path+cds+"ortholines.txt",'r').read()
seg_ortho=Counter(ortho.lower().split())
mod=Model(seg_ortho, rep.get_reports(13))
mod.compute()
mod2=Model(seg_ortho, rep_content)
mod2.compute()
mod3=Model(seg_ortho, rep_func_0)
mod3.compute()
