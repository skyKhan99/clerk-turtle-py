import turtle


def draw_star(unit):
    for i in range(5):
        t.forward(unit)
        t.right(144)


t = turtle.Turtle()
t.penup()
t.goto(-300, 200)
t.pencolor('red')
t.fillcolor('red')
t.pendown()
t.begin_fill()
t.fd(600)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(400)
t.end_fill()
t.bk(200)
t.rt(90)
t.penup()
t.pencolor('white')
t.fd(110)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.rt(90)
t.circle(110)
t.end_fill()
t.lt(90)
t.fd(50)
t.rt(90)
t.fillcolor('red')
t.pencolor('red')
t.begin_fill()
t.circle(90)
t.end_fill()
t.lt(90)
t.penup()
t.pencolor('white')
t.fillcolor('white')
t.fd(140)
t.pendown()
t.begin_fill()
t.lt(18)
draw_star(90)
t.end_fill()

turtle.mainloop()
