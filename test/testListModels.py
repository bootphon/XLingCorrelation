import sys
sys.path.insert(0, 'src/')
import Segmented, Reports, ListModels

path = '/Users/gladysbaudet//Desktop/PFE/'

seg1 = Segmented.Segmented(path+'Results/20k/dibs/syllable/segmented0.txt', path+'CDS/english/Brent/20k/gold0.txt', path+'sub_corpus/20k/ortholines0.txt')

listseg = [seg1]

rep = Reports.Reports(path+"CDI/english/Prop_WG_understands_8_18.csv")


models = ListModels.ListModels(listseg, rep)

models.compute()

print(models._r2)
