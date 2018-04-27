import argparse
from xlingcorrelation import Corpus

parser=argparse.ArgumentParser(description="Compute corpus info")
parser.add_argument("-t", "--tags",help="path to tags")

args=parser.parse_args()

corpus = Corpus.Corpus(args.tags)
corpus.display_basic_info()
# corpus.plot_syllables()
# print(corpus.get_monosyllabic_words().most_common(100))
