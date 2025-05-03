#Сделанно и Работает в GoogleColab
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from random import randint
data = np.random.rand(10, 10)
def p_function(x: float) -> float:
    return x**2
x = [1, 2, 3, 4, 5]
y = [p_function(t) for t in x]
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

M= randint(-4, 4) % 100
B= randint(-4, 4) % 100
x = np.arange(M, B, 0.5)
y = np.cos(x)
plt.subplot(1, 3, 2)
plt.title("2")
plt.scatter(x, y)

plt.show()