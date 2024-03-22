from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import filedialog as fd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import mean


def coefficients():
    f = filepath.get()
    df = pd.read_csv(f)
    params = [col for col in df.columns]
    if params[0] == 'Unnamed: 0':
        params = params[1:]

    df = df.sort_values(by=params[0])

    x = np.array(df[params[0]])
    y = np.array(df[params[1]])
    xy = x * y
    xx = x * x
    k = (mean(xy) - mean(x) * mean(y)) / (mean(xx) - mean(x) ** 2)
    b = mean(y) - k * mean(x)

    return k, b, x, y, params


def open_file():
    filepath.set(fd.askopenfilename(filetypes=[("CSV-файлы", ".csv")]))
    f = filepath.get()
    if f:
        file = f.split('/')[-1]
        open_btn['text'] = file


def graph():
    if filepath.get() == '':
        coefficient_label['text'] = 'Ошибка.\nОтсутствует файл'
        res_label['text'] = ''
        return
    if filepath.get()[-4:] != '.csv':
        coefficient_label['text'] = 'Ошибка.\nТребуется .csv-файл'
        res_label['text'] = ''
        return
    round_parameter = 2
    try:
        k, b, x, y, ax = coefficients()
    except (Exception,):
        coefficient_label['text'] = 'Ошибка!'
        res_label['text'] = ''
        return
    k = round(k, round_parameter)
    b = round(b, round_parameter)
    sign = '+' if b > 0 else '-'
    x_max = 1.1 * max(x)
    y_max = 1.1 * max(y)

    coefficient_label['text'] = f'Коэффициенты:\nk = {k}, b = {b}'
    res_label['text'] = f'Аппроксимирующая прямая:\ny = {k}x {sign} {abs(b)}'

    plt.plot([0, x_max], [b, k * x_max + b], zorder=0)
    plt.scatter(x, y, color='black', s=15, zorder=1)
    # plt.title('График по лабе')
    plt.xlabel(ax[0])
    plt.ylabel(ax[1])
    plt.xlim([0, x_max])
    plt.ylim([0, y_max])

    f = fd.asksaveasfilename(initialfile='graph.png', defaultextension='.png',
                             filetypes=(("PNG-файл", "*.png"), ("JPG-файл", "*.jpg"), ("Все файлы", "*.*")))
    if f != "":
        plt.savefig(f, dpi=300)
        plt.close()


width = 930
height = 600

root = Tk()
root.title('У меня лабки')
root.geometry(f'{width}x{height}')
root.minsize(930, 400)

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=5)
root.rowconfigure(index=2, weight=5)

filepath = StringVar(value='')
btn_font = tkfont.Font(size=30)
info_font = tkfont.Font(size=50)

btn_style = ttk.Style().configure('btn.TButton', font=btn_font)

coefficient_label = ttk.Label(font=info_font, justify=LEFT)
coefficient_label.grid(row=1, columnspan=2, padx=20, sticky=NSEW)
res_label = ttk.Label(font=info_font, justify=LEFT)
res_label.grid(row=2, columnspan=2, padx=20, sticky=NSEW)

open_btn = ttk.Button(text='Загрузить .csv файл', style='btn.TButton', command=open_file)
open_btn.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)
graph_btn = ttk.Button(text='Построить график', style='btn.TButton', command=graph)
graph_btn.grid(row=0, column=1, ipadx=6, ipady=6, padx=4, pady=4, sticky=NSEW)

root.mainloop()
