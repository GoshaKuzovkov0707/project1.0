import turtle

screen = turtle.getscreen()
leonardo = turtle.Turtle()
raphael = turtle.Turtle()
donatello = turtle.Turtle()
michelangelo = turtle.Turtle()


leonardo.color('grey')
raphael.color('yellow')
donatello.color('pink')
michelangelo.color('green')
for i in range(37):
    leonardo.forward(100)
    leonardo.left(175)

for i in range(4):
    raphael.forward(100)
    raphael.left(90)

donatello.forward(200)
donatello.left(90)
donatello.forward(200)

michelangelo.forward(100)
michelangelo.right(90)
michelangelo.forward(50)
    

screen.mainloop()
