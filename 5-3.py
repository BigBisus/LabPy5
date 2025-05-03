#Сделанно и Работает в GoogleColab
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
M= np.random.randint(1, 11, (5, 5))
average = np.mean(M)
Max = np.max(M)
Min = np.min(M)
SumCol= np.sum(M,axis=0)
print(M)
print(average)
print(Max)
print(Min)
print(SumCol)
