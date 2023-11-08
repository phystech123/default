from tkinter import *
from random import randint
from tkinter import ttk

WIDTH = 1200
HEIGHT = 600
color=['green','red','pink','black','brown','purple','yellow']
pol=['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'center']
class MATAN:
    def __init__(self):
        self.x = 0
        self.y = 10
        self.dx, self.dy = 10, 8 
        self.id = canvas.create_image(WIDTH/6, HEIGHT/6,image=photo) 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + 400 > WIDTH or self.x < 0: 
            self.dx = -self.dx
        if self.y +200 > HEIGHT or self.y-10 < 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.id, self.dx, self.dy)

class Ball:
    def __init__(self,event):
        self.R = randint(10, 50) 
        self.x = event.x 
        self.y = event.y
        self.dxx, self.dyy = randint(-10, 10),randint(-10, 10)
        self.dx=self.dxx
        self.dy=self.dyy
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill=color[randint(0,6)])

    def move(self):
        if self.x - self.R >= WIDTH: 
            self.dx = -WIDTH-2*self.R
        elif self.x + self.R < 0:
            self.dx = WIDTH+2*self.R
        else:
            self.dx=self.dxx
        self.x+=self.dx
        if self.y - self.R >= HEIGHT: 
            self.dy = -HEIGHT-2*self.R
        elif self.y + self.R < 0:
            self.dy = HEIGHT+2*self.R
        else:
            self.dy=self.dyy
        self.y+=self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

class heart:
    def __init__(self,event):
        self.x = event.x
        self.y = event.y
        self.dx, self.dy = randint(-10, 10), randint(-10, 10) 
        self.id = canvas.create_image(self.x,self.y, image=phot[randint(0,len(phot)-1)])

    def move(self):
        if self.dx>0:
            self.dx+=0.1
        else:
            self.dx-=0.1
        if self.dy>0:
            self.dy+=0.1
        else:
            self.dy-=0.1
        self.x += self.dx
        self.y += self.dy
        if self.x + 50 > WIDTH or self.x <= 0: 
            self.dx = -self.dx
        if self.y + 50 > HEIGHT or self.y <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.id, self.dx, self.dy)

class prise:
    def __init__(self,event):
        self.x = 600
        self.y = 300
        self.id = canvas.create_image(self.x,self.y, image=pho)

    def show(self):
        canvas.move(self.id)

class Infa:
    def __init__(self,event):
        self.x = 600
        self.y = 300
        self.dx=0
        self.dy=0
        self.id = canvas.create_image(self.x,self.y, image=photog)

    def move(self):
        self.x+=self.dx
        self.y+=self.dy

    def show(self):
        canvas.move(self.id,self.dx,self.dy)

class text:
    def __init__(self):
        self.id=canvas.create_text(WIDTH-50,0,
            text=f'Shift: {Time.Title1}\nBackspace: {Time.Title2}',
            anchor='ne'
            )
        self.dx,self.dy=0,0
    def show(self):
        canvas.delete(self.id)
        self.id=canvas.create_text(WIDTH-50,0,
            text=f'Shift: {Time.Title1}\nBackspace: {Time.Title2}',
            anchor='ne'
            )
        canvas.move(self.id,self.dx,self.dy)

if __name__=='__main__':
#........................
    list1=[]
    def cl_Ball(event):
        list1.append(Ball(event))

    list2=[]
    def cl_heart(event):
        list2.append(heart(event))

    list3=[]
    def cl_prise(event):
        list3.append(prise(event))

    list4=[]
    def cl_Infa(event):
        list4.append(Infa(event))
#.........................
    class time: #performer
        def __init__(self):
            self.i=0
            self.s=0
            self.Title1='отжато'
            self.Title2='отжато'

        def shift(self,event):
            self.i+=1
            if not self.i%2:
                self.Title1='отжато'
            else:
                self.Title1='нажато'

        def backspace(self,event):
            self.s+=1
            if not self.s%2:
                self.Title2='отжато'
            else:
                self.Title2='нажато'

        def choice(self,event):
            if self.i%2:
                if not self.s%2:
                    cl_heart(event)
                else:
                     for hear in list2:
                        if (hear.x-event.x)**2+(hear.y-event.y)**2<=50**2:
                            list2.remove(hear)
            else:
                if not self.s%2:
                    cl_Ball(event)
                else:
                    for ball in list1:
                        if list3:
                            o=list3.pop()
                            canvas.delete(o.id)
                        elif list4:
                            o=list4.pop()
                            canvas.delete(o.id)
                        elif (ball.x-event.x)**2+(ball.y-event.y)**2<=ball.R**2:
                            list1.remove(ball)
                            canvas.delete(ball.ball_id)
        def dell(self,event):
            canvas.delete("all")

#main part inition
    Time=time()
#Canvas, tkinter
    root = Tk()
    root.title(f'Проект по информатике.')
    root.geometry(f'{WIDTH}x{HEIGHT}')
    canvas = Canvas(root,width=WIDTH, height=HEIGHT)
    canvas.pack(anchor=CENTER)
#tick
    def tick():
        for i in list0:
            i.move()
            i.show()
        for i in list1:
            i.move()
            i.show()
        for i in list2:
            i.move()
            i.show()
        for i in list3:
            i.move()
            i.show()
        for i in list4:
            i.move()
            i.show()    
        for i in range(1):
            tex.show()
        root.after(50, tick)
#photo
    photo=PhotoImage(file='ovch.png').subsample(3, 3)
    phot=[PhotoImage(file='h.png').subsample(10, 10),
        PhotoImage(file='man.png').subsample(10, 10),
        PhotoImage(file='dick1.png').subsample(10, 10)]
    photog=PhotoImage(file='infop.png').zoom(2,1)
    pho=PhotoImage(file='kk.png').zoom(2,2)
#main photo put
    list0 = [MATAN()]
    tex=text()
#bind
    canvas.bind('<Button-3>',cl_prise)
    canvas.bind('<Double-Button-1>',cl_Infa)
    canvas.bind('<Button-1>', Time.choice)
    root.bind('<Shift_L>',Time.shift)
    root.bind('<space>',Time.backspace)
    root.bind('<BackSpace>',Time.dell)
#loop,tick
    tick()
    root.mainloop()