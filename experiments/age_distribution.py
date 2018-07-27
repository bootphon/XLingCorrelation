import os
from collections import defaultdict
import matplotlib.pyplot as plt

from wordseg.statistics import CorpusStatistics
from wordseg.separator import Separator
'''
# load the input text file
text = open(sys.argv[1], 'r').readlines()

# compute some statistics on the input text (text tokenized at phone
# and word levels)
separator = Separator(phone=' ', syllable=None, word=';eword')
stats = CorpusStatistics(text, separator).describe_all()
'''

# /!\ different for English !! age not written the same /!\

# rootdir = "/Users/gladysbaudet/Desktop/PFE/CDS/french/Lyon/"
# children = ["Anais/", "Marie/", "Theotime/", "Nathan/"]

# rootdir = "/Users/gladysbaudet/Desktop/PFE/CDS/spanish/OreaPine/"
# children = ["Juan/", "Lucia/"]
#
# rootdir = "/Users/gladysbaudet/Desktop/PFE/CDS/swedish/Lund/"
# children = ["Anton/", "Bella/", "Harry/", "Markus/", "Tea/"]

rootdir = "/Users/gladysbaudet/Desktop/PFE/CDS/danish/Plunkett/"
children = ["Anne/", "Jens/"]

res = defaultdict(int)
res_nb_files = defaultdict(int)
res_ttr = defaultdict(int)
res_utt_length = defaultdict(int)
s = 0
tot = 0
for child in children:
    d = rootdir+child

    for fn in os.listdir(d):
        # if os.path.isfile(fn):
            # print (fn)
        if (fn[-1]=='e'):
            continue
        age=fn.split("-ortholines")
        if (len(age)>1):


            # FOR FRENCH/LYON ##
            # a = int(age[0][0])
            # ## FOR OTHERS
            a = int(age[0][1])
            # print(age, a)
            if (a<4):
                # m = int(age[0][1]+age[0][2])
                m = int(age[0][2]+age[0][3])

                num_lines = sum(1 for line in open(d+fn))
                try:
                    text = open(d+fn, 'r').readlines()
                    separator = Separator(phone='', syllable=None, word=' ')
                    stats = CorpusStatistics(text, separator).describe_all()
                    # print(stats)
                    ttr = stats['words']['types']/stats['words']['tokens']
                    utt_length = stats['words']['tokens']/stats['corpus']['nutts']

                    age_in_months = 12*a+m
                    s += num_lines * (age_in_months)
                    tot += num_lines
                    res_nb_files[age_in_months] += 1
                    res[age_in_months] += num_lines
                    res_utt_length[age_in_months] += utt_length
                    res_ttr[age_in_months] += ttr
                except (ValueError):
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
