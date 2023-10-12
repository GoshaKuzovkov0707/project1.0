import turtle


class DS:
    def draw(self, nana, color='red'):
        if self.fill:
            nana.color(color)
            nana.begin_fill()
        for _ in range(self.sides):#кол-во сторон
            nana.forward(self.size)#длина стороны
            nana.left(self.angle)#угол(градусы)
        if self.fill:
            nana.end_fill()

class RE(DS):
    def __init__(self, size, fill = False) -> None:
        self.size = size
        self.sides = 4 
        self.angle = 90 
        self.fill = fill


if __name__ == '__main__':
    screen = turtle.getscreen()
    nana = turtle.Turtle()
    crlf = RE(60, True)
    crlf.draw(nana)
    screen.mainloop()