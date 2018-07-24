
import sys
from collections import Counter

c = Counter(open(sys.argv[1],'r').read().lower().split())
f = open(sys.argv[2]+"/gold_freq_words.csv", 'w')
for double in c.most_common() :
    f.write(str(double[1])+" "+ str(double[0])+'\n')
f.close()
