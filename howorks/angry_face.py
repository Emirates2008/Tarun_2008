from turtle import *
pencolor("red")
fillcolor("red")
begin_fill()
circle(50)
end_fill()
penup()
left(90)
forward(75)
left(90)
forward(15)
pencolor("black")
fillcolor("black")
pendown()
begin_fill()
circle(7)
end_fill()
penup()
backward(30)
pendown()
begin_fill()
circle(7)
end_fill()
penup()
forward(15)
left(90)
forward(35)
pendown()
right(90)
begin_fill()
for i in range(5):
    forward(5)
    left(90)
    forward(3)
    right(90)
backward(50)
right(90)
for i in range(5):
    forward(3)
    left(90)
    forward(5)
    right(90)
end_fill()
penup()
forward(37.5)
right(90)
forward(10)
pensize(4)
pendown()
goto(25,80)
penup()
backward(52)
pendown()
goto(-10,77)
