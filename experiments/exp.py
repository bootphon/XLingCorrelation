import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

data = pd.read_csv("/Users/gladysbaudet/Desktop/PFE/Results/correlationR2_syllable.txt")

result = sm.ols(formula="dibs ~ puddle * baseline", data=data).fit()
print(result.summary())
print(result.rsquared, result.params['baseline'])

# def linear(a,b):
#   x = np.linspace(0,12, 1000)
#   plt.plot(x, x*a+b)
#
#
# linear(0.02, 0.2)
# linear(0.05, 0.2)
# linear(0.02, 0.5)
# plt.show()
