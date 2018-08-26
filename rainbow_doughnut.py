import turtle
screen = turtle.Screen()
t=turtle.Turtle()
screen.bgcolor("snow")
l=["red","orange","yellow", "lime", "blue","indigo", "purple"]
l=l*100
t.shape('turtle')
t.color("lime")
t.begin_fill()
for i in range(100):
    t.pencolor(l[i])
    t.pensize(40)
    t.forward(200)
    t.left(145)
t.end_fill()
