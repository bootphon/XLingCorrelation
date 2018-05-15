# all good imports and all
from xlingcorrelation import Corpus

"""
pb imports
pb path - when calling scripts -
"""

# corpus = Corpus.Corpus("~/Desktop/PFE/package/experiments/")
c0 = Corpus.Corpus("/Users/gladysbaudet/Desktop/PFE/CDS/english/Brent/full_corpus/tags.txt")
c1 = Corpus.Corpus("/Users/gladysbaudet/Desktop/PFE/CDS/french/Lyon/tags-auto-updated-clean.txt")
c2 = Corpus.Corpus("/Users/gladysbaudet/Desktop/PFE/CDS/spanish/OreaPine/tags-auto.txt")
c3 = Corpus.Corpus("/Users/gladysbaudet/Desktop/PFE/CDS/danish/Plunkett/tags3.txt")
c4 = Corpus.Corpus("/Users/gladysbaudet/Desktop/PFE/CDS/swedish/Lund/tags.txt")

print("english")
print(c0.get_nb_isolated_words()/c0.get_nb_words())
print(c0.get_nb_monosyllabic_words()/c0.get_nb_words())
print("french")
print(c1.get_nb_isolated_words()/c1.get_nb_words())
print(c1.get_nb_monosyllabic_words()/c1.get_nb_words())
#
print("spanish")
print(c2.get_nb_isolated_words()/c2.get_nb_words())
print(c2.get_nb_monosyllabic_words()/c2.get_nb_words())
print("danish")
print(c3.get_nb_isolated_words()/c3.get_nb_words())
print(c3.get_nb_monosyllabic_words()/c3.get_nb_words())
print("swedish")
print(c4.get_nb_isolated_words()/c4.get_nb_words())
print(c4.get_nb_monosyllabic_words()/c4.get_nb_words())



# corpus.compute_all_cha()
# corpus.clean_annotations(extra="~/Desktop/PFE/package/experiments/extraclean.sh")
# words = corpus.get_word_tokens()
# print(corpus.count_words())
# corpus.phonologize()
# corpus.syllabify()
