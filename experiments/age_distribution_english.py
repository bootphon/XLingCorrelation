import os
from collections import defaultdict
import matplotlib.pyplot as plt

from wordseg.statistics import CorpusStatistics
from wordseg.separator import Separator

rootdir = "/Users/gladysbaudet/Desktop/PFE/CDS/english/Brent/Brent/"

res = defaultdict(int)
res_nb_files = defaultdict(int)
res_ttr = defaultdict(int)
res_utt_length = defaultdict(int)
s = 0
tot = 0

for fn in os.listdir(rootdir):


    try:
        m=fn[-4:-2]
        num_lines = sum(1 for line in open(rootdir+fn+"/ortholines.txt"))
        text = open(rootdir+fn+"/ortholines.txt", 'r').readlines()
        separator = Separator(phone='', syllable=None, word=' ')
        stats = CorpusStatistics(text, separator).describe_all()
        # print(stats)
        ttr = stats['words']['types']/stats['words']['tokens']
        utt_length = stats['words']['tokens']/stats['corpus']['nutts']

        age_in_months = int(m)
        s += num_lines * (age_in_months)
        tot += num_lines
        res_nb_files[age_in_months] += 1
        res[age_in_months] += num_lines
        res_utt_length[age_in_months] += utt_length
        res_ttr[age_in_months] += ttr
    except (ValueError, NotADirectoryError):
        continue

print(s/tot)
print(res)

for i in res_nb_files:
    res_ttr[i] /= res_nb_files[i]
    res_utt_length[i] /= res_nb_files[i]

plt.figure()
plt.bar(range(len(res)), list(res.values()), align='center')
blabl=plt.twinx()
blabl.plot(range(len(res_ttr)), list(res_ttr.values()), color='r')
# blabl.plot(range(len(res_utt_length)), list(res_utt_length.values()))

plt.xticks(range(len(res)), list(res.keys()))
# plt.plot(res_ttr)


plt.show()
