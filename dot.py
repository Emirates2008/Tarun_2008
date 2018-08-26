import turtle
t=turtle.Turtle()
i=0
while(i<10):
    i=i+1
    for g in range(i):
        t.dot()
        t.penup()
        t.right(90)
        t.penup()
        t.forward(10)
        t.left(90)
        t.pendown()
        t.dot()
