import turtle
from random import randint
screen = turtle.getscreen()
t = turtle.Turtle()
class DrawShape:
    def draw(self,f = 0,v = 0, color = 'red'):
        t.penup()
        t.goto(f,v)
        t.pendown()
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()

class Rect(DrawShape):
    def __init__(self,size,fill = False):
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill  = fill



class Triangle(DrawShape):
    def __init__(self,size,fill = False) :
        self.size = size
        self.sides = 3
        self.angle = 120
        self.fill = fill

class Circle():
    def __init__(self,size,fill = True) :
        self.size = size
        self.fill = fill
    def draw(self,x,y,color = 'yellow'):
        t.penup()
        t.goto(x,y)
        t.pendown()
        if self.fill:
            t.color(color)
            t.begin_fill()
        t.circle(self.size)
        if self.fill:
            t.end_fill()



       

a = Circle(size = 200,fill = True) 
a.draw(0,-200)   

v = Rect(size=10,fill = True)
d = Triangle(size=10,fill=True)
c = Circle(size=10,fill = True)
for i in range(10):
    v.draw(randint(-150,150),randint(-150,150),color='green')
    d.draw(randint(-150,150),randint(-150,150),color='blue')
    c.draw(randint(-150,150),randint(-150,150),color='red')

screen.mainloop()