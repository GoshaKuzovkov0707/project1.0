import turtle 
screen = turtle.getscreen()
jane = turtle.Turtle()
jane.penup()
jane.pensize(1)
jane.shape('turtle')
jane.goto(-50, 0)
jane.pendown()
for w in range(40):
    jane.forward(100)
    jane.left(170)
# jane.color('orange')
# jane.fillcolor('yellow')
# jane.begin_fill()
# jane.circle(100)
# jane.end_fill()
# jane.hideturtle()
jane.goto(0, 0)
screen.mainloop()
