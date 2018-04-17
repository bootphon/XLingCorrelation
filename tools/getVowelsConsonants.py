
import sys, re

VOWELS = sys.argv[1]
OUTPUT = sys.argv[2]

l = open(VOWELS).readlines()
print(l)
l = [item.split('\t')[0] for item in l]
outfile = open(sys.argv[2], "w")
outfile.write("\n".join(str(i) for i in l))
outfile.close()
