import turtle

MAX_WIDTH = 600
a=600
ckreen = turtle.getscreen
screen = ckreen()
na = turtle.Turtle()
na.shape('turtle')

class Rect:
    def __init__(self, size, fill = True) -> None:
        self.size = size
        self.sides = 4 
        self.angle = 90 
        self.fill = fill
    def draw(self, color, x = 0, y = 0):
        na.goto(x, y)
        if self.fill:
            na.color(color)
            na.begin_fill()
        for _ in range(self.sides):#кол-во сторон
            na.forward(self.size)#длина стороны
            na.left(self.angle)#угол(градусы)
        if self.fill:
            na.end_fill()

    def draw_circle(self, x, y, color, radius):
        na.penup()
        na.goto(x, y)
        na.color(color)
        na.begin_fill()
        na.circle(radius)
        na.end_fill()

b32_it = Rect(40)
# b32_it.draw(color = 'green', x = 0, y = 0 )
# b32_it.draw(color = 'yellow', x = 0, y = 40 )
# b32_it.draw(color = 'red', x = 0, y = 80 )

b32_it.draw(color = 'green', x = 0, y = 0 )
b32_it.draw(color = 'green', x = 40, y = 0 )

b32_it.draw_circle(0, -15, 'black', 15)
b32_it.draw_circle(80, -15, 'black', 15)
b32_it.draw_circle(0, -7, 'white', 7)
b32_it.draw_circle(80, -7, 'white', 7)
na.hideturtle()


screen.mainloop()