from xlingcorrelation import Segmented
import sys, os
# taking ortho, gold and segmented
# output freq_words.txt

segmented = sys.argv[1]
gold = sys.argv[2]
ortho = sys.argv[3]


print(segmented, "\n", gold, "\n",  ortho, "\n")

res = os.path.dirname(segmented)+"/freq_words.csv" #should be computed w/ segmented (and put in the same dir automatically)

seg = Segmented(segmented, gold, ortho, "", "", "")

seg.write_freq_words(res)
