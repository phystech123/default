import numpy as np
import matplotlib.pyplot as plt

# k=6

# # Загрузка данных из файла "МНК"
# data = np.loadtxt('data/1.txt')
# # Разделение данных на х и у
# x0 = data[:, 0]
# x1=[i*1.96 for i in x0]
# x=x1[:k]
# xt=x1[k:]
# y0 = data[:, 1]
# y1=[i for i in y0]
# y=y1[:k]
# yt=y1[k:]
# #  Построение графика набора значений
# plt.scatter(x, y, label='Набор значений')
# # Построение графика интерполяции функции
# p = np. polyfit(x, y, deg=1)

# x_interp = np. linspace(min(x), max(x), 1000)
# y_interp = np. polyval(p, x_interp)
# plt.plot(x_interp, y_interp, label=f'Интерполяция\n{p}')
# plt.scatter(xt, yt)

# plt.xlabel('P1-P2')
# plt.ylabel('Q')
# print(p)

# plt.legend()
# plt.show()






# Загрузка данных из файла "МНК"
data = np.loadtxt('data/3.txt')
# Разделение данных на х и у
x = data[:, 0]
x = [i for i in x]
y = data[:, 1]
y = [52.9/11.9,
    94/30,
    70.6/40,
    88.2/50] 
#  Построение графика набора значений
plt.plot(x, y, '-or', label='Набор значений')
# Построение графика интерполяции функции
# p = np. polyfit(x, y, deg=1)

# x_interp = np. linspace(min(x), max(x), 1000)
# y_interp = np. polyval(p, x_interp)
# plt.plot(x_interp, y_interp, label=f'Интерполяция\n{p}')

plt.xlabel('x')
plt.ylabel('(P1-P2)/L')
# print(p)

plt.legend()
plt.show()