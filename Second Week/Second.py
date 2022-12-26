#To draw heart using turtle
import turtle   
t = turtle.Pen()
t.speed(0)
t.pencolor("red")
t.fillcolor("pink")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.end_fill()
t.hideturtle()
turtle.done()
    
