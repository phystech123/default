import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import json
import pandas as pd

# Загрузка данных
df1 = pd.read_csv("datas/data_l.csv", sep=";")[" x"]
df2 = pd.read_csv("datas/data_phi.csv", sep=";")[" x"]
df3 = pd.read_csv("datas/data_psi.csv", sep=";")[" x"]
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

# Начальные координаты шаров
pos_x1 = data["x"] + m2 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.cos(data["phi"])
pos_y1 = data["y"] + m2 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.sin(data["phi"])
pos_z1 = data["z"] + m2 / (m1 + m2) * data["l"] * np.sin(data["psi"])

pos_x2 = data["x"] - m1 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.cos(data["phi"])
pos_y2 = data["y"] - m1 / (m1 + m2) * data["l"] * np.cos(data["psi"]) * np.sin(data["phi"])
pos_z2 = data["z"] - m1 / (m1 + m2) * data["l"] * np.sin(data["psi"])

# Инициализация pygame и OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Настройка камеры в OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 500.0)
glTranslatef(0.0, 0.0, -200.0)  # Смещение камеры назад

# Функция для отрисовки сферы
def draw_sphere(x, y, z, radius, color):
    quadric = gluNewQuadric()
    glColor3f(*color)
    glPushMatrix()
    glTranslatef(x, y, z)
    gluSphere(quadric, radius, 32, 32)
    glPopMatrix()

# Основной цикл
i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление координат шаров
    if i < len(df1):
        pos_x1 = df4[i] + m2 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.cos(df2[i])
        pos_y1 = df5[i] + m2 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.sin(df2[i])
        pos_z1 = df6[i] + m2 / (m1 + m2) * df1[i] * np.sin(df3[i])

        pos_x2 = df4[i] - m1 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.cos(df2[i])
        pos_y2 = df5[i] - m1 / (m1 + m2) * df1[i] * np.cos(df3[i]) * np.sin(df2[i])
        pos_z2 = df6[i] - m1 / (m1 + m2) * df1[i] * np.sin(df3[i])

        i += 1

    # Очистка экрана
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Отрисовка первого шара
    draw_sphere(pos_x1, pos_y1, pos_z1, 5, (0, 0, 1))  # Синий шар

    # Отрисовка второго шара
    draw_sphere(pos_x2, pos_y2, pos_z2, 5, (1, 0, 0))  # Красный шар

    # Обновление экрана
    pygame.display.flip()
    pygame.time.wait(10)  # Задержка для контроля FPS

pygame.quit()