from math import sqrt
import time
import turtle
from turtle import numinput

mover = turtle.Turtle()
mover.speed(0)
initiator = "FBFBFBFB"
repeater = "AFBFA"
corner = "AFBFBFBFA"


n = numinput("Pattern Level","No. of iterations")
m = int(n)
mover.lt(45)
for counter in range(m):
        final_out = ""
        for char in initiator:
            if (char=='F'):
                final_out = final_out + char
            elif(char=='A'):
                final_out = final_out + repeater
            elif(char=='B'):
                final_out = final_out + corner
        initiator = final_out            
for ch in initiator:
    if (ch =='F'):
        mover.pencolor('red')
        mover.forward(10)
    elif (ch =='B'):
        mover.pencolor('blue')
        step = 5/sqrt(2)
        mover.forward(step)
        mover.circle(step,270)
        mover.forward(step)
    elif (ch=='A'):
        mover.pencolor('green')
        mover.circle(10,90)
    elif (ch=='R'):
        mover.right(90)
    elif (ch=='L'):
        mover.left(90)
    elif (ch=='S'):
        mover.pencolor('orange')
        mover.forward(5)
        mover.circle(5,180)
        mover.forward(5)    
    else:
        mover.pencolor('orange')
        mover.forward(5)
        mover.circle(-5,180)
        mover.forward(5)
            
mover.hideturtle()
time.sleep(5)