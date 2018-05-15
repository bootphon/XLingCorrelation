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

listsegfull = [Segmented(path+cds+'gold.txt', path+cds+'gold.txt', \
path+cds+'ortholines.txt', 'unit', 'gold', 'cds')]

# Retrieve corresponding tags
corpus = Corpus.Corpus(path+cds+"tags.txt")
# Get monosyllabic words in phono form
mono_w_phono = corpus.get_monosyllabic_words().keys()
# Get dictionary phono to ortho (from gold here)
# (should this dictionary be the one for all segmented from same cds?)
phono_ortho = listsegfull[0].dict_phono_ortho
# Get monosyllabic words in orthographic form
mono_w = [phono_ortho.get(w) for w in mono_w_phono]

# Open + count the number of occurrences of each word in corpus (in ortho form)
ortho=open(path+cds+"ortholines.txt",'r').read()
seg_ortho=Counter(ortho.lower().split())

# Dictionary that will contain monosyllabic words + nb of occurrences
seg_ortho_mono=Counter()
# Dictionary that will contain polysyllabic words + nb of occurrences
seg_ortho_poly=seg_ortho.copy()
# Build these two dictionaries
for w in mono_w:
    # if seg_ortho[w]<100: #
    seg_ortho_mono[w] = seg_ortho[w]
    del seg_ortho_poly[w]


# CDI
rep = Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")
rep_ortho = rep.get_reports(13)
rep_content = rep.get_reports_content(13)
rep_function = rep.get_reports_function(13)

""" REGULAR CDI : MONO VS POLY """

# Regular model
mod_ortho=Model(seg_ortho,rep_ortho)
mod_ortho.compute()
# mod_ortho.write_data("~/Desktop/PFE/table.csv")

# Model with only monosyllabic words
print("mono\n")
mod_ortho_mono=Model(seg_ortho_mono,rep_ortho, "prop ~ np.log(word_freq)"+\
" + lexical_classes + np.log(word_freq) * lexical_classes")
mod_ortho_mono.compute()

# Model with only polysyllabic words
print("poly\n")
mod_ortho_poly=Model(seg_ortho_poly, rep_ortho, "prop ~ np.log(word_freq)"+\
" + lexical_classes  + np.log(word_freq) * lexical_classes")
mod_ortho_poly.compute()

# Display parameters of both models
print("Nb words mono : ", len(mod_ortho_mono._data))
print(mod_ortho_mono._lin_reg)
print("Nb words poly : ", len(mod_ortho_poly._data))
print(mod_ortho_poly._lin_reg)

# Display both models
mod_ortho_mono.plot("r")
mod_ortho_poly.plot("b")
plt.show()

""" CONTENT CDI : MONO VS POLY """

# Mono vs poly for content words
mod_ortho_mono=Model(seg_ortho_mono,rep_content)
mod_ortho_mono.compute()

mod_ortho_poly=Model(seg_ortho_poly, rep_content)
mod_ortho_poly.compute()

print("Nb words mono : ", len(mod_ortho_mono._data))
print(mod_ortho_mono._lin_reg)
print("Nb words poly : ", len(mod_ortho_poly._data))
print(mod_ortho_poly._lin_reg)
mod_ortho_mono.plot("r")
mod_ortho_poly.plot("b")
plt.show()
#
""" FUNCTION CDI : MONO VS POLY """

# Mono vs poly for content words
mod_ortho_mono=Model(seg_ortho_mono,rep_function)
mod_ortho_mono.compute()

mod_ortho_poly=Model(seg_ortho_poly, rep_function)
mod_ortho_poly.compute()

print("Nb words mono : ", len(mod_ortho_mono._data))
print(mod_ortho_mono._lin_reg)
print("Nb words poly : ", len(mod_ortho_poly._data))
print(mod_ortho_poly._lin_reg)
mod_ortho_mono.plot("r")
mod_ortho_poly.plot("b")
plt.show()
