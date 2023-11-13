import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
import random




# s=np.arange(0,5,0.05)

# plt.figure(figsize=(11,13), dpi=100)
# plt.title('fuckk',fontdict={'fontname':'sans-serif','fontsize':10})
# plt.xlabel('one')
# plt.ylabel('two')

# plt.xticks([i for i in range(26)])
# plt.yticks([i for i in range(26)])
# plt.grid()

# plt.plot(s,s**2,'r-',label='1')
# plt.legend()

# plt.show()




# a=['1','2','3']
# b=[1,2,3]
# plt.figure(figsize=(5,5),dpi=100)
# #plt.title('fuckk',fontdict={'fontname':'sans-serif','fontsize':10})
# plt.bar(a,b)
# plt.yticks([i for i in range(10)])
# plt.show()


# x = [i for i in range(50)]
# y = [j for j in range(50)]
# S = [i + j for i in x for j in y]
# plt.figure(figsize=(10,5),dpi=100)
# plt.hist(S,bins=1000)
# plt.show()



# pos = 0
# scale = 10
# size = 10000
# values = np.random.normal(pos, scale, size)
# plt.hist(values, 100)
# plt.show()






# plt.pie([10,10,1], labels = ['No','No, but in orange','Perhaps'])
# plt.title('What are the chances that I will wake up early tomorrow?')
# plt.show()




# fig = plt.figure(figsize = (16,9))
# ax1 = fig.add_subplot(111) 
# x_measured = [i for i in range(5)]
# y_measured = [i**2 for i in range(5)]
# x = [0.5, 9.0]
# y = np.interp(x, x_measured, y_measured)
# ax1.scatter(x_measured, y_measured, marker='x')
# ax1.errorbar(x_measured, y_measured, yerr=0.2, xerr = 0.1, color = 'k', linestyle = '--')
# ax1.plot(x,y, 'r')
# ax1.grid()
# plt.show()


lenn=[i for i in range(60)]
time=[i**3+(i**2)*12000-123 for i in range(60)]
plt.figure(figsize=(16,9),dpi=100)
plt.subplot(1,1,1)
plt.title('laba',fontdict={'fontname':'sans-serif','fontsize':10})
plt.xlabel('lenght')
plt.ylabel('period')
plt.xticks(np.arange(0,60,1))
plt.yticks(np.arange(0,100000000,1000000))
plt.grid()
plt.plot(lenn,time,'r--')
plt.show()