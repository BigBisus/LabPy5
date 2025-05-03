#Сделанно и Работает в GoogleColab
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
M= np.random.randint(1, 11, (5, 5))

plt.imshow(M, cmap='viridis')
for i in range(5):
  for g in range(5):
    plt.text(i, g, (i , g))
plt.colorbar()
plt.show()