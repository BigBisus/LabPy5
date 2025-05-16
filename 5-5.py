#Сделанно и Работает в GoogleColab
import numpy as np
import matplotlib.pyplot as plt

# Создаём 3 области
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Три типа графиков')

# 1. Линейный график y = x^2
x = np.linspace(0, 100, 100)
y = x ** 2
ax1.plot(x, y, color='blue')
ax1.set_title('Линейный график y = x²')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

# 2. Точечный график случайных точек
np.random.seed(42)  # Для воспроизводимости
x_rand = np.random.rand(50) * 10
y_rand = np.random.rand(50) * 100
ax2.scatter(x_rand, y_rand, color='green', alpha=0.6)
ax2.set_title('Случайные точки')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

# 3. Столбчатая диаграмма для категориальных данных
categories = ['A', 'B', 'C']
values = [3, 7, 2]
ax3.bar(categories, values, color=['red', 'green', 'blue'])
ax3.set_title('Столбчатая диаграмма')
ax3.set_xlabel('Категории')
ax3.set_ylabel('Значения')


# Показываем график
plt.show()
'''from numpy import random
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
'''