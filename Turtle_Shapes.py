import turtle
import math


#  Drawing the Triangle
t = turtle.Turtle()
turtle.Screen().bgcolor("Orange")
t.penup()
t.goto(-200,200)
t.pendown()
for i in range(3):
    t.lt(120)
    t.fd(100) 
turtle.Screen().bgcolor("Green")

#  Drawing the Square
t.penup()
t.goto(-200,-200)
t.lt(180)
t.pendown()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(50)
    t.lt(90)
turtle.Screen().bgcolor("Yellow")  


#  Drawing the Pentagon
t.penup()
t.goto(200,200)
t.rt(180)
t.pendown()
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(t,65,5)   
turtle.Screen().bgcolor("Light Blue")

#  Drawing the circle
t.penup()
t.goto(300,-250)
t.pendown()
def polyline(t, n, length, angle):
    for i in range (n):
        t.fd(length)
        t.lt(angle)
        


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = angle / n
    t.lt (step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

arc(t,50,360)
turtle.Screen().bgcolor("Pink")



#  Drawing the Flower
t.penup()
t.goto(0,0)
t.pendown()

def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t, 50, 90)
        t.lt(360.0/n)


flower (t,12,30,90)






turtle.done()