from collections import defaultdict

file=open("./test.txt","r+")
r=file.read()
print(r)
file.close()
# wordcount={}
wordcount = defaultdict(int)
# print(file.read())
for word in r.split():
    wordcount[word]+=1
    # if word not in wordcount:
    #     wordcount[word] = 1
    # else:
    #     wordcount[word] += 1
# print (wordcount)
# file.close();
