# Create a static star
# Update star colors
# Update background color
# Change star location
# Create multiple stars
# Customize

import turtle
import random
from tkinter import *

background = turtle.Screen()
background.bgcolor("black")

#Declare star object and set speed
star = turtle.Turtle()
star.shape("circle")
star.speed(10)

# Draw the star
for i in range(5):
  #Set the position
  x = random.randint(-150,150)
  y = random.randint(-150,150)
  star.penup()
  star.setposition(x,y)
  star.pendown()

  #Set the size
  size = random.randint(5,20)
  
  #Set the color
  turtle.colormode(255)
  red = random.randint(0,255)
  green = random.randint(0,255)
  blue = random.randint(0,255)
  star.color(red,green,blue)

  #Draw the star
  for i in range(size):
    star.forward(i*8)
    star.right(144)

mainloop()