import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/oleg/Desktop/лаба_2.1.6/plots')
def f1():
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')

    data = np.loadtxt('coord.txt')
    data_r=np.loadtxt('coord_r.txt')
    y = data[:, 0]
    x = data[:, 1]


    #  Построение графика набора значений
    plt.scatter(x, y, label='нагрев', color='red')
    p = np. polyfit(x, y, deg=1)

    x_interp = np. linspace(x.min(), x.max(), 1000)
    y_interp = np. polyval(p, x_interp)
    plt.plot(x_interp, y_interp, color='red' )

    plt.legend()
    plt.show()


f1()