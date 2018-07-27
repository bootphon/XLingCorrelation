import sys
from collections import Counter

## python clean_jap.py ortho.txt tags.txt

# 1. Read file
# 2. Split on spaces (by word)
# 3. Split each word at each consonant not preceded by another consonant (except if q)
#   - start i at 1 (if exists)
#   - if i consonant
#       - if i-1 not consonant
#           - split right before i

# f = open("test_jap.txt", "r")
f = open(sys.argv[1], "r")
# toprocess = f.read().lower().replace("_",'').replace("?","").split()
to_process = f.readlines()
to_process = [line.lower().replace("_","").replace("?","") for line in to_process]
f.close()

# f = open(sys.argv[2], "r")
# toprocess = toprocess + f.read().lower().replace("?","").replace("_",'').split()
# f.close()

consonants = ["z", "r", "t", "y", "p", "s", "d", "f", \
    "g", "h", "k", "j", "l", "m", "w", "x", "c", "v", "b", "n", "y"]

morae = []

syll = open("temp.txt", 'w')
for line in to_process:
    for word in line.split():
        to_add = word[0]
        i=1
        w = word
        while (i<=len(word)):
            try:
                if word[i] in consonants:
                    if word[i-1] not in consonants:
                        morae.append(to_add)
                        # syll.write(to_add+" ;esyll ")
                        syll.write(to_add+" ")
                        to_add = word[i]
                        i+=1
                    else :
                        to_add += word[i]
                        i+=1
                else :
                    to_add += word[i]
                    i+=1
                # syll.write(word[i])
                # print(word[i])


            except Exception as e:
                morae.append(to_add)
                # syll.write(to_add+" ;esyll ")
                syll.write(to_add+" ")
                i+=1
        syll.write(" ;eword ")
    syll.write("\n")
syll.close()
###### SYLLABIFICATION OK, STARTING PHONES SEP
syll = open("temp.txt", 'r').readlines()
pho = open("temp2.txt", "w")
for line in syll:
    for s in line.split():
        i=1
        while(i<len(s)):
            if (s[i-1] in consonants and s[i] not in consonants and s != ";eword"):
                pho.write(s[:i]+"_"+s[i:])
                break
            i+=1
        else:
            pho.write(s)
        pho.write(" ")
    pho.write("\n")
pho.close()
pho = open("temp2.txt", "r").read().replace(" "," ;esyll ").replace(";eword ;esyll",";eword").replace("_"," ")
# print(pho)
open(sys.argv[2],'w').write(pho)





# f = open("test_morae.txt", "w")
# f.write(str(Counter(morae)))
# f.close()
# print(len(list(set(morae))))
