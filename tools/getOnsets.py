

import sys
import re

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]
CONSONANTS = sys.argv[3]

# readlines CONSONANTS to get a string cons =  "a|l|l|c|o|n|s|o|n|a|n|t|s"

l = open(CONSONANTS).readlines()
l = [item.split()[0] for item in l if len(item.split())>0]
cons = ''
for item in l :
    cons += '|'+item
cons = cons[1:]
print(l)
print(cons)

onsets_all = set()

f = open(INPUT)
for line in f:
    onsets = re.findall(r"\;eword\s(["+cons+"]*)",line)
    for item in onsets :
        onsets_all.add(item)
    onsets_all.discard('')

    onsets = re.findall(r'^(['+cons+']*)',line)
    for item in onsets :
        onsets_all.add(item)
    onsets_all.discard('')

bla = list(onsets_all)
print(bla[:5])

outfile = open(sys.argv[2], "w")
outfile.write("\n".join(str(i) for i in onsets_all))
outfile.close()
