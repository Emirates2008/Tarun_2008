import turtle
screen = turtle.Screen()
i = 0
a = "green"
b = "red"
c = "purple"

screen.bgcolor(a)

screen.bgcolor(b)

screen.bgcolor(c)
    
line = turtle.Turtle()
for i in range(4):
    line.forward(90)
    line.right(90)
