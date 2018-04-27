import matplotlib.pyplot as plt
import numpy as np


def linear(a,b):
  x = np.linspace(0,12, 1000)
  plt.plot(x, x*a+b)


linear(0.02, 0.2)
linear(0.05, 0.2)
linear(0.02, 0.5)
plt.show()
