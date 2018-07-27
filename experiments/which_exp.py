from collections import Counter
from xlingcorrelation import Segmented, Reports, ListModels, Model, Corpus
# import numpy as np
import matplotlib.pyplot as plt

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

rep = Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")
rep_ortho = rep.get_reports(13)
# rep_func_0 = rep.get_modif_func_0(13)
rep_content = rep.get_reports_content(13)

ortho=open(path+cds+"ortholines.txt",'r').read()
seg_ortho=Counter(ortho.lower().split())
