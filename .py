from random import randint
from treygolniki_i_pramoygolniki import DS
import turtle

screen = turtle.getscreen()
nana = turtle.Turtle()

class Polygon(DS):
    def __init__(self, size, fill = False) -> None:
        self.size = size
        self.sides = 6
        self.angle = 60
        self.fill = fill

class Tr(DS):
    def __init__(self, size, fill = False) -> None:
        self.size = size
        self.sides = 3
        self.angle = 120
        self.fill = fill

nana.penup()
nana.pensize(12)
nana.goto(0, -200)
nana.pendown()
nana.color('brown')
nana.fillcolor('yellow')
nana.begin_fill()
nana.circle(200)
nana.end_fill()


nana.pensize(0)
python1 = Polygon(10, True)
python2 = Tr(15, True)
for j in range(15):
    nana.penup()
    nana.goto(0, 0)
    nana.left(randint(0, 359))
    nana.forward(randint(1, 187))
    python1.draw(nana)

    nana.penup()
    nana.goto(0, 0)
    nana.left(randint(0, 359))
    nana.forward(randint(1, 187))
    python2.draw(nana, color='violet')
    

screen.mainloop()