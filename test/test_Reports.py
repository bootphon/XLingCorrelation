import sys
sys.path.insert(0, '../src/')
import Reports

rep = Reports.Reports("~/Desktop/PFE/CDI/english/Prop_WS_produces_16_30.csv")
print(rep.get_type(), rep.get_form())
# print(rep._word_freq.columns)
print(rep.age_range())
# ind_age = lambda x : x-rep.get_age_min()
# print(rep.get_reports_by_age()[ind_age(21)].head(5))
print(rep.get_reports(21).head(5))
