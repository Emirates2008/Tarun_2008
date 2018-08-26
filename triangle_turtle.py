import turtle
screen = turtle.Screen()
t=turtle.Turtle()
l=["green","purple","red"]
l=l*100
t.color("white")
t.begin_fill()
for i in range(3):
    t.pencolor(l[i])
    t.pensize(100)
    t.forward(60)
    t.left(120)
t.end_fill()
