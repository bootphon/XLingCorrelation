# all good imports and all

"""
pb imports
pb path - when calling scripts -
"""

corpus = Corpus("~/Desktop/PFE/package/experiments/")

corpus.compute_all_cha()
corpus.clean_annotations(extra="~/Desktop/PFE/package/experiments/extraclean.sh")
words = corpus.get_word_tokens()
print(corpus.count_words())
corpus.phonologize()
corpus.syllabify()
