from tkinter import *
from random import randint

WIDTH = 1200
HEIGHT = 600
# color=['green','red','pink','black','brown','purple','yellow']
# pol=['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'center']
class Ball:
    def __init__(self):
        self.x = 10
        self.y = 0
        self.dx, self.dy = (10, 10) 
        self.ball_id = canvas.create_image(WIDTH/6, HEIGHT/6,image=photo) 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + 400 > WIDTH or self.x < 0: 
            self.dx = -self.dx
        if self.y +200 > HEIGHT or self.y-10 < 0:
            self.dy = -self.dy
            self.ball_id

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


class Hu:
    def __init__(self,event):
        self.x = event.x
        self.y = event.y
        self.dx, self.dy = (10, 10) 
        self.ball_id = canvas.create_image(self.x,self.y, image=phot[randint(0,len(phot)-1)])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + 50 > WIDTH or self.x <= 0: 
            self.dx = -self.dx
        if self.y + 50 > HEIGHT or self.y <= 0:
            self.dy = -self.dy
            self.ball_id

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

class HUY:
    def __init__(self,event):
        self.x = 600
        self.y = 300
        self.dx, self.dy = (10, 10) 
        self.ball_id = canvas.create_image(self.x,self.y, image=pho)

    # def move(self):
    #     self.x += self.dx
    #     self.y += self.dy
    #     if self.x + 50 > WIDTH or self.x <= 0: 
    #         self.dx = -self.dx
    #     if self.y + 50 > HEIGHT or self.y <= 0:
    #         self.dy = -self.dy
    #         self.ball_id

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


hu=[]
def click_handler(event):
    hu.append(Hu(event))

ho=[]
def click_r(event):
    ho.append(HUY(event))

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    for hurt in hu:
        hurt.move()
        hurt.show()
    for huy in ho:
        huy.move()
        huy.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root,width=WIDTH, height=HEIGHT)
canvas.pack(anchor=CENTER)
photo=PhotoImage(file='ovch.png').subsample(3, 3)
phot=[PhotoImage(file='h.png').subsample(10, 10),
       PhotoImage(file='man.png').subsample(10, 10),
       PhotoImage(file='dick1.png').subsample(10, 10)]
pho=PhotoImage(file='kk.png').zoom(2,2)
canvas.bind('<Button-3>',click_r)
canvas.bind('<Button-1>', click_handler)
balls = [Ball()]
tick()
root.mainloop()