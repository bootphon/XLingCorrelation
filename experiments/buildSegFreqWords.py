import tqdm as tqdm
from xlingcorrelation import Segmented
from collections import defaultdict, Counter


path = '/Users/gladysbaudet//Desktop/PFE/'
cds = 'CDS/'
results = 'Results/'
# corpora = ['french/Lyon/', 'danish/Plunkett/', 'swedish/Lund/', 'spanish/OreaPine/']
corpora = ['french/lyon-50k/', 'swedish/lund-50k/']
# algos = ['ag/', 'dibs/', 'puddle/', 'tp/relativeforward/', 'tp/absoluteforward/', 'tp/relativebackward/', 'tp/absolutebackward/', 'baseline0/', 'baseline1/']
algos = ['baseline0/', 'baseline1/']
units = ['syllable/', 'phoneme/']

# for corpus in tqdm.tqdm(corpora) :
#     ortho=open(path+cds+corpus+"ortholines.txt",'r').read()
#     seg_ortho=Counter(ortho.lower().split())
#     f = open(path+results+corpus+"gold_freq_words.csv", 'w')
#     for double in seg_ortho.most_common() :
#         f.write(str(double[1])+" "+ str(double[0])+'\n')
#     f.close()
#
# ortho=open(path+cds+"english/Brent/full_corpus/"+"ortholines.txt",'r').read()
# seg_ortho=Counter(ortho.lower().split())
# f = open(path+results+"English/Brent/"+"gold_freq_words.csv", 'w')
# for double in seg_ortho.most_common() :
#     f.write(str(double[1])+" "+ str(double[0])+'\n')
# f.close()

ortho=open(path+cds+"english/Brent/50K0/"+"ortholines.txt",'r').read()
seg_ortho=Counter(ortho.lower().split())
f = open(path+results+"English/Brent/50k/"+"gold_freq_words.csv", 'w')
for double in seg_ortho.most_common() :
    f.write(str(double[1])+" "+ str(double[0])+'\n')
f.close()


# for corpus in tqdm.tqdm(corpora) :
#     for unit in units :
#         listsegfull = [Segmented(path+results+corpus+algo+unit+'segmented.txt', \
#         path+cds+corpus+'gold.txt', path+cds+corpus+'ortholines.txt', \
#         unit, algo, cds) for algo in algos]
#
#         for seg in listsegfull :
#             seg.write_freq_words(path+results+corpus+seg._algo+seg._unit+"freq_words.csv")

# for unit in units :
#     listsegfull = [Segmented(path+results+"English/Brent/50K0/"+algo+unit+'segmented.txt', \
#     path+"CDS/"+"english/Brent/50K0/"+'gold.txt', path+"CDS/"+"english/Brent/50K0/"+'ortholines.txt', \
#     unit, algo, cds) for algo in algos]
#
#     for seg in listsegfull :
#         seg.write_freq_words(path+results+"English/Brent/50K0/"+seg._algo+seg._unit+"freq-words.txt")
