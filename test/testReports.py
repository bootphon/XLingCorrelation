import sys
sys.path.insert(0, '../src/')
import Reports

rep = Reports.Reports("~/Desktop/PFE/CDI/english/Prop_WS_produces_16_30.csv")
print(rep.get_type(), rep.get_form())
# print(rep._word_freq.columns)
print(rep.age_range())
