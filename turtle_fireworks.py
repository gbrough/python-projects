# Create a static firework
# Update firework colors
# Update background color
# Change firework location
# Create multiple fireworks
# draw multiple starts at once 
# remove nested for loops

import turtle
import random
from tkinter import *


background = turtle.Screen()
background.bgcolor("green")

#Declare star object and set speed

star = turtle.Turtle()
star.shape("turtle")
star.speed(10)

# Draw the star
for i in range(1):
  #Set the position
  x = random.randint(-150,150)
  y = random.randint(-150,150)
  star.setposition(x,y)

  #Set the size
  size = random.randint(5,11)
  
  #Set the color
  
  # red = random.randint(0, 255)
  # red = str("#FF0000")
  # green = str("#00FF00")
  # blue = str("#0000FF")
  # star.pencolor(red,green,blue)

  for i in range(size):
    star.forward(i*8)
    star.right(144)


mainloop()