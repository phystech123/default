import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/home/oleg/Desktop/лаба_2.4.1/plots')
def f1():
    plt.title('Зависимость log(P) от 1/T')
    plt.ylabel('log(P)')
    plt.xlabel('1/T')


    # Загрузка данных из файла "МНК"
    data = np.loadtxt('coord.txt')
    data_r=np.loadtxt('coord_r.txt')
    # Разделение данных на х и у

    y = data[:, 1]
    x = data[:, 0]


    yr = data_r[:, 1]
    xr = data_r[:, 0]
    sumx = 0
    for i in x:
        sumx += i**2
    sumy = 0
    for i in y:
        sumy += i**2
    print(sumy/sumx)
    for i in xr:
        sumx += i**2
    sumy = 0
    for i in yr:
        sumy += i**2
    print(sumy/sumx)
    #  Построение графика набора значений
    plt.scatter(x, y, label='нагрев', color='red')
    plt.scatter(xr, yr, label='охлаждение', color='blue')
    # Построение графика интерполяции функции
    p = np. polyfit(x, y, deg=1)
    pr = np. polyfit(xr, yr, deg=1)

    x_interp = np. linspace(x.min(), x.max(), 1000)
    y_interp = np. polyval(p, x_interp)
    plt.plot(x_interp, y_interp, color='red' )

    xr_interp = np. linspace(xr.min(), xr.max(), 1000)
    yr_interp = np. polyval(pr, xr_interp)
    plt.plot(xr_interp, yr_interp, color='blue')
    print(p, pr)

    plt.legend()
    plt.show()

def f2():
    plt.title('Зависимость T от P')
    plt.xlabel('T')
    plt.ylabel('P')


    data = np.loadtxt('coord1.txt')
    data_r=np.loadtxt('coord1_r.txt')
    print(data)
    x = data[:, 0]
    y = data[:, 1]

    xr = data_r[:, 0]
    yr = data_r[:, 1]

    #  Построение графика набора значений
    plt.scatter(x, y, label='нагрев', color='red')
    plt.scatter(xr, yr, label='охлаждение', color='blue')

    plt.legend()
    plt.show()

def f3():
    plt.title('Зависимость P1+P2 от P')
    plt.xlabel('P')
    plt.ylabel('P1+P2')

    data = np.loadtxt('pp.txt')

    x = data[:, 0]
    y1 = data[:, 1]
    y2 = data[:, 2]
    

    #  Построение графика набора значений
    plt.scatter(x, y1, label='нагрев', color='red')
    plt.scatter(x, y2, label='охлаждение', color='blue')

    plt.legend()
    plt.show()

f1()
f2()
# f3()