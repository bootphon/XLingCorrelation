# get all phono symbols appearing
import sys
from collections import Counter

f = open(sys.argv[1],'r')#.read()
# print(f.read().count("(en)"))
c = Counter(f.read())
count=0
for i in c:
    print(i, c[i])
    count+=1
print(count)
# print(Counter(f.read()))
f.close()

'''

({' ': 778803,
'a': 488631,    V
'n': 267600,
'\n': 222068,
'd': 200443,
'm': 198568,
'ɪ': 194742,    V
'j': 192353,
'ɯ': 184299,    V
'k': 171717,
't': 156198,
'b': 150658,
'ɛ': 139601,    V
'e': 116872,    V
'r': 112644,
's': 110733,
'ʃ': 106000,
'ʊ': 101979,    V
'i': 94707,     V
'ɫ': 90296,
'ɔ': 83922,     V
'l': 81107,
'æ': 71404,     V
'ɾ': 70052,
'h': 65382,
'ɟ': 60172,
'o': 56077,     V
'z': 48644,
'ʒ': 45526,
'u': 42200,     V
'p': 41987,
'v': 33940,
'œ': 30175,     V
'ø': 29893,     V
'y': 22016,     V
'ː': 16684,
'f': 13174,
'ɡ': 8913,
'c': 818,
'w': 241,
'ɣ': 27,
'ɹ': 7})


'''
