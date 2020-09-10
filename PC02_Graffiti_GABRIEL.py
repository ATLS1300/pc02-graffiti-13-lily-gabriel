#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:56:19 2020

@author: lilygabriel
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lily Gabriel
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

Turtle()
colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

penup() #lifts pen

forward(25) #goes forward 25
left(90) #rotate 90 degrees
forward(80) #move forward (up) 100

pendown() #puts pen down

color("red") #changes color to red
dot(50) #puts a dot down

penup() #lifts pen

backward(327) #goes back 327
right(90)
forward(80)
left(90)

color("blue")

pensize(10)

pendown()

forward(70) #this bar is how much amazon workers make in a year (bar)
right(90)
forward(75)
right(90)
forward(70)
right(90)
forward(75)

penup()

backward(90) #going to the second bar

color("purple") #make the pen purple

pendown()

right(90) #how much jeff makes in a minute (bar)
forward(350)
right(90)
forward(75)
right(90)
forward(350)
right(90)
forward(75)

#eat the rich

color("blue")

penup()

pensize(2) #adding diagonal lines cause I want to

forward(90)

pendown()

right(135)
forward(100)

penup()

right(135) #going to the second bar
forward(75)
left(90)
forward(17)

color("purple")

pendown()

left(45) #diagonal line
forward(110)

penup()

left(45) #getting to the corner
forward(200)
left(90)
forward(80)
right(90)
forward(75)
right(90)
forward(80)

pendown()

right(135) #last diagonal line
forward(110)








