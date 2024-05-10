import numpy as np
import math
import os

os.chdir('/home/oleg/Desktop/лаба_2.4.1/plots')

def foo(fin, fout):
    data = np.loadtxt(fin)
    x = list(data[:, 0])
    y1 = list(data[:, 1])
    y2 = list(data[:, 2])
    xx=[]
    yy=[]
    for i in range(len(x)):
        xx.append(1/(x[i] + 273))
        yy.append(math.log(abs(y1[i] - y2[i]) * 133,3))
        

    with open(fout, 'w') as f:
        for i in range(len(xx)):
            f.write(f'{xx[i]:.7f}\t{yy[i]:.3f}\n')

def foo1(fin, fout):
    data = np.loadtxt(fin)
    x = list(data[:, 0])
    y1 = list(data[:, 1])
    y2 = list(data[:, 2])
    xx=[]
    yy=[]
    for i in range(len(x)):
        xx.append(x[i]+ 273)
        yy.append(abs(y1[i] - y2[i])*133.3)
        

    with open(fout, 'w') as f:
        for i in range(len(xx)):
            f.write(f'{xx[i]:.3f}\t{yy[i]:.3f}\n')

def p(fin1, fin2, fout):
    data = np.loadtxt(fin1)
    x = list(data[:, 0])
    y1 = list(data[:, 1])
    y2 = list(data[:, 2])
    x,y1,y2 = x[::2], y1[::2], y2[::2]
    xx1=[]
    yy1=[]
    for i in range(len(x)):
        xx1.append(y1[i])
        yy1.append(y1[i] + y2[i])
        

    data = np.loadtxt(fin2)
    x = list(data[:, 0])
    y1 = list(data[:, 1])
    y2 = list(data[:, 2])
    xx2=[]
    yy2=[]
    for i in range(len(x)):
        xx2.append(y1[i])
        yy2.append(y1[i] + y2[i])
        

    with open(fout, 'w') as f:
        for i in range(len(xx2)):
            f.write(f'{xx1[i]:.3f}\t{yy1[i]:.3f}\t{yy2[i]:.3f}\n')

p('data.txt', 'data_r.txt', 'pp.txt')

foo('data.txt', 'coord.txt')
foo('data_r.txt', 'coord_r.txt')

foo1('data.txt', 'coord1.txt')
foo1('data_r.txt', 'coord1_r.txt')        
