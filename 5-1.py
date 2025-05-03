#Сделанно и Работает в GoogleColab
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y= np.sin(x)
z= np.cos(x)
plt.plot(x,y,'r',label='График 1')
plt.plot(x,z,'b--',label='График 2')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y or Z")
plt.show