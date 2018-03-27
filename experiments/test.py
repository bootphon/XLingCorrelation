from collections import defaultdict

file=open("./test.txt","r+")
r=file.readlines()
print(r)

file.close()
# wordcount={}
wordcount = defaultdict(int)
# print(file.read())
for line in r :
    curr_line = 0
    for word in line.split():
        wordcount[word]+=1
    # if word not in wordcount:
    #     wordcount[word] = 1
    # else:
    #     wordcount[word] += 1
print (wordcount)
# file.close();
