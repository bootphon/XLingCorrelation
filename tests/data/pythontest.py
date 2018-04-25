from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series

# f= open("tags.txt",'r')
f=open("../../../CDS/french/Lyon/tags-auto.txt", 'r')
blop_init = f.read()
f.close()

# print(blop_init)
# print('\n')

""" WORDS """
blop=blop_init.replace("\n", '')
blop=blop.replace(" ", '')
blop=blop.replace(";esyll", '')
blop=blop.replace(";eword", ' ')[:-1] # getting words alright

print("Words")
# print(blop)
print(len(blop.split()))


""" SYLLABLES """

blop2 = blop_init.replace("\n", '')
blop2 = blop2.replace(" ", "")
blop2 = blop2.replace(";eword", "")
blop2 = blop2.replace(";esyll", " ")

print("Syllables")
# print(blop2)
print(len(blop2.split()))


""" PHONES """

blop3 = blop_init.replace("\n", '')
blop3 = blop3.replace(";eword", "")
blop3 = blop3.replace(";esyll", "")

print("Phones")
# print(blop3)
print(len(blop3.split()))

c = Counter(blop.split())
# print(c)
# labels, values = zip(*Counter(blop3.split()).items())
labels, values = zip(*c.most_common(100))
indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)

# s=Series(blop2.split())
# vc = s.value_counts()
# vc.plot()



plt.show()

""" ISOLATED WORDS """

iso=[]
blop4 = blop_init.split("\n")
for b in blop4:
    if b.count(";eword")==1:
        iso.append(b.replace(";eword","").replace(";esyll","").replace(" ",""))

print("Isolated words")
# print(Counter(iso))


""" Monosyllabic words """

mono = []
blop5 = blop_init.split(";eword")
for b in blop5 :
    if b.count(";esyll")==1:
        mono.append(b.replace(";eword","").replace(";esyll","").replace(" ","").replace("\n",""))

print("Monosyllabic words")
# print(Counter(mono))
