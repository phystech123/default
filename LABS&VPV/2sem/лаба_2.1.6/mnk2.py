import numpy as np
import matplotlib.pyplot as plt
# # Загрузка данных из файла "МНК"
# data = np.loadtxt( 'MHK.txt')
# # Разделение данных на х и у
# x = data[:, 0]
# y = data[:, 1]
#  Построение графика набора значений
plt.scatter(x, y, label='Набор значений')
# Построение графика интерполяции функции
p = np. polyfit(x, y, deg=2)

x_interp = np. linspace(x.min(), x.max(), 1000)
y_interp = np. polyval(p, x_interp)
plt.plot(x_interp, y_interp, label=f'Интерполяция\n{p}' )
print(p)

plt.legend()
plt.show()