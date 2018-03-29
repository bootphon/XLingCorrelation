import sys
sys.path.insert(0, '../src/')
import Segmented

# TODO : assert
seg = Segmented.Segmented('segmented.txt', 'gold.txt', 'ortholines.txt')
print('freqtop ',seg.freq_top())
print('freqtop2', seg.freq_top())
print('freqwords ', seg.freq_words())
print(seg.compute_words())
print(seg._nb_words)
