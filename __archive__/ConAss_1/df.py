# import pandas as pd
# import matplotlib.pyplot as plt
# import mpl_toolkits
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns
# import numpy as np
# import math
# import os
# import matplotlib.animation as animation

# N = 100000
# h = 0.001*1000
# nu=1000
# l=10
# a=0.1
# g=9.81
# m=2
# df1 = pd.read_csv("datas/data_phi.csv", sep=";")
# df2 = pd.read_csv("datas/data_omega.csv", sep=";")
# X = l*np.sin(df1[" x"])
# Y = l*np.cos(df1[" x"]) + a*np.cos(nu*df1['t'])


# fig, ax = plt.subplots()



# line2 = ax.plot(X[0], Y[0])[0]
# ax.set(xlim=[min(X), max(X)], ylim=[min(Y), max(Y)], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()


# def update(frame):
#     # for each frame, update the data stored on each artist.
#     x = X[:frame]
#     y = Y[:frame]
#     # update the line plot:
#     line2.set_xdata(X[:frame])
#     line2.set_ydata(Y[:frame])
#     return (line2)


# ani = animation.FuncAnimation(fig=fig, func=update, frames=N, interval=h)
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import json
import pandas as pd
import time
import pygame

df1 = pd.read_csv("datas/data_l.csv", sep=";")[" x"]
# df2 = pd.read_csv("datas/data_l_.csv", sep=";")[" x"]
df2 = pd.read_csv("datas/data_phi.csv", sep=";")[" x"]
# df4 = pd.read_csv("datas/data_phi_.csv", sep=";")[" x"]
df3 = pd.read_csv("datas/data_psi.csv", sep=";")[" x"]
# df6 = pd.read_csv("datas/data_psi_.csv", sep=";")[" x"]
df4 = pd.read_csv("datas/data_x.csv", sep=";")[" x"]
df5 = pd.read_csv("datas/data_y.csv", sep=";")[" x"]
df6 = pd.read_csv("datas/data_z.csv", sep=";")[" x"]

with open('configs/RK4.json', 'r') as json_file:
    data = json.load(json_file)
m1 = data["m1"]
m2 = data["m2"]
mu = data["m"]
k = data["k"]
l0 = data["l0"]





# Создаем фигуру и 3D-ось
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Параметры шара
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

# Инициализация поверхности шара
ball1 = ax.plot_surface(x, y, z, color='b', alpha=0.8)
ball2 = ax.plot_surface(x, y, z, color='r', alpha=0.8)

# Начальные координаты шара
pos_x1= data["x"] + m2/(m1+m2)*data["l"]*np.cos(data["psi"])*np.cos(data["phi"])
pos_y1= data["y"] + m2/(m1+m2)*data["l"]*np.cos(data["psi"])*np.sin(data["phi"])
pos_z1= data["z"] +  m2/(m1+m2)*data["l"]*np.sin(data["psi"])

pos_x2= data["x"] - m1/(m1+m2)*data["l"]*np.cos(data["psi"])*np.cos(data["phi"])
pos_y2= data["y"] - m1/(m1+m2)*data["l"]*np.cos(data["psi"])*np.sin(data["phi"])
pos_z2= data["z"] -  m1/(m1+m2)*data["l"]*np.sin(data["psi"])
# Функция обновления анимации
i = 1
def update(frame):
    global pos_x1, pos_y1, pos_z1, pos_x2, pos_y2, pos_z2, i
    # Смещаем шар в пространстве
    pos_x1 += -pos_x1 + df4[i] + m2/(m1+m2)*df1[i]*np.cos(df3[i])*np.cos(df2[i])
    pos_y1 += -pos_y1 + df5[i] + m2/(m1+m2)*df1[i]*np.cos(df3[i])*np.sin(df2[i])
    pos_z1 += -pos_z1 + df6[i] + m2/(m1+m2)*df1[i]*np.sin(df3[i])
    
    pos_x2 += -pos_x2 + df4[i] - m1/(m1+m2)*df1[i]*np.cos(df3[i])*np.cos(df2[i])
    pos_y2 += -pos_y2 + df5[i] - m1/(m1+m2)*df1[i]*np.cos(df3[i])*np.sin(df2[i])
    pos_z2 += -pos_z2 + df6[i] -  m1/(m1+m2)*df1[i]*np.sin(df3[i])
    
    ax.clear()

    # Обновляем координаты шара
    new_x = x + pos_x1
    new_y = y + pos_y1
    new_z = z + pos_z1
    # Удаляем старый шар и рисуем новый
    ax.plot_surface(new_x, new_y, new_z, color='b', alpha=0.8)
   
    # Обновляем координаты шара
    new_x = x + pos_x2
    new_y = y + pos_y2
    new_z = z + pos_z2
    # Удаляем старый шар и рисуем новый
    ax.plot_surface(new_x, new_y, new_z, color='r', alpha=0.8)
    
    # Устанавливаем границы осей
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    ax.set_zlim([-100, 100])
    i += 1
# Создаем анимацию
ani = FuncAnimation(fig, update, frames=np.arange(0, data["N"]), interval=1)

# Отображаем анимацию
plt.show()





# import pygame
# import numpy as np
# import json
# import pandas as pd

# # Загрузка данных
# df1 = pd.read_csv("datas/data_l.csv", sep=";")[" x"]
# df2 = pd.read_csv("datas/data_phi.csv", sep=";")[" x"]
# df3 = pd.read_csv("datas/data_psi.csv", sep=";")[" x"]
# df4 = pd.read_csv("datas/data_x.csv", sep=";")[" x"]
# df5 = pd.read_csv("datas/data_y.csv", sep=";")[" x"]
# df6 = pd.read_csv("datas/data_z.csv", sep=";")[" x"]

# with open('configs/RK4.json', 'r') as json_file:
#     data = json.load(json_file)
# m1 = data["m1"]
# m2 = data["m2"]
# mu = data["m"]
# k = data["k"]
# l0 = data["l0"]

# # Инициализация pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# # Начальные координаты шаров
# pos_x1 = data["x"] + m2 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.cos(data["phi"])
# pos_y1 = data["y"] + m2 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.sin(data["phi"])
# pos_z1 = data["z"] + m2 / (m1 + m2) * data["l"] * np.sin(data["psi"])

# pos_x2 = data["x"] - m1 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.cos(data["phi"])
# pos_y2 = data["y"] - m1 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.sin(data["phi"])
# pos_z2 = data["z"] - m1 / (m1 + m2) * data["l"] * np.sin(data["psi"])

# # Масштабирование координат для отображения на экране
# scale = 10  # Масштабный коэффициент

# # Основной цикл
# running = True
# i = 0
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Обновление координат шаров
#     if i < len(df1):
#         pos_x1 = df4[i] + m2 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.cos(df2[i])
#         pos_y1 = df5[i] + m2 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.sin(df2[i])
#         pos_z1 = df6[i] + m2 / (m1 + m2) * df1[i] * np.sin(df3[i])

#         pos_x2 = df4[i] - m1 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.cos(df2[i])
#         pos_y2 = df5[i] - m1 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.sin(df2[i])
#         pos_z2 = df6[i] - m1 / (m1 + m2) * df1[i] * np.sin(df3[i])

#         i += 1

#     # Очистка экрана
#     screen.fill((0, 0, 0))

#     # Отрисовка шаров
#     pygame.draw.circle(screen, (0, 0, 255), (int(pos_x1 * scale + 400), int(pos_y1 * scale + 300)), 10)
#     pygame.draw.circle(screen, (255, 0, 0), (int(pos_x2 * scale + 400), int(pos_y2 * scale + 300)), 10)

#     # Обновление экрана
#     pygame.display.flip()

#     # Установка частоты обновления (например, 60 FPS)
#     clock.tick(60)

# pygame.quit()