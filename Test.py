
# right_justify printing

#def right_justify(name):
#    nl = len(name)
 #   sp = 70 - nl
  #print(sp * " " + name)

#user = input("Enter name: ")
#right_justify(user)
# 
# 
# 
# 
# 
# function as object
# 
#def print_twice(a):
 #   print("\n***" + a + "***")


#
# 
# def print_spam():
#    print("spam ")
 #   print_twice("spam")
#

    
#def do_twice(print_spam):
 #    print_spam()

#
# 
# 
# do_twice(print_spam)









#Turtle

#
#import turtle
#bob = turtle.Turtle()
#for i in range(3):
#    bob.fd(100)
 #   bob.lt(120)


#bob.penup()
#bob.goto(-200,190)

#bob.pendown()

#for r in range(4):
 #   bob.fd(100)
  #  bob.lt(90)


#turtle.done()




#
# import turtle



#t = turtle.Turtle()
#bob = t
#def square(t,length):
#     for i in range(4):
 ###         t.fd(length)
    #      t.lt(90)
#square(bob,200)

#t.penup()
#t.goto(-200,100)
#t.pendown()



#def polygon(t,length,n):
#     for i in range(n):
#          t.fd(length)
#          t.lt(360/n)


#polygon(bob,50,12)         
#turtle.done()

import turtle
import math

t = turtle.Turtle()

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

#Circle

#import turtle

#t = turtle.Turtle()

#def circle(t,r,n):
#    t.penup()
 #   t.goto(10,0)
  #  t.pendown()
   # for i in range(n):
    #    t.fd(r)
     #   t.lt(360/n)
        

#circle(t,10,50)
#turtle.done()









