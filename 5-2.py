#Сделанно и Работает в GoogleColab
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
G = np.random.normal(500, 2, 1000)
plt.hist(G, bins=20, color='blue')
plt.show()