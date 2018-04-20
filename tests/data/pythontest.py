from collections import Counter
f= open("tags.txt",'r')
blop_init = f.read()
f.close()

print(blop_init)
print('\n')
# blop = [e.replace("\n", '') for e in blop]
# blop = [e.replace(" ", '') for e in blop]
# blop = [e.replace(";esyll", '') for e in blop]
# blop = [e.replace(";eword", ' ')[:-1] for e in blop]
#
# blop = [e.split() for e in blop]

""" WORDS """
blop=blop_init.replace("\n", '')
blop=blop.replace(" ", '')
blop=blop.replace(";esyll", '')
blop=blop.replace(";eword", ' ')[:-1] # getting words alright

print("Words")
print(blop)
print(len(blop.split()))

""" SYLLABLES """

blop2 = blop_init.replace("\n", '')
blop2 = blop2.replace(" ", "")
blop2 = blop2.replace(";eword", "")
blop2 = blop2.replace(";esyll", " ")

print("Syllables")
print(blop2)
print(len(blop2.split()))

""" PHONES """

blop3 = blop_init.replace("\n", '')
blop3 = blop3.replace(";eword", "")
blop3 = blop3.replace(";esyll", "")

print("Phones")
print(blop3)
print(len(blop3.split()))

""" ISOLATED WORDS """
iso=[]
blop4 = blop_init.split("\n")
for b in blop4:
    if b.count(";eword")==1:
        iso.append(b)
print(iso)

c = Counter(blop3.split())
print(c)
