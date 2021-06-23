# Create a static firework
# Update firework colors
# Update background color
# Change firework location
# Create multiple fireworks

import turtle
import random

background = turtle.Screen()
background.bgcolor("black")

for i in range(5):
  #Declare the object and set speed
  star = turtle.Turtle()
  star.speed(10)

  #Set the position
  x = random.randint(-250,250)
  y = random.randint(-250,250)
  star.setposition(x,y)

  #Set the color
  red = random.randint(0, 255)
  green = random.randint(0,255)
  blue = random.randint(0,255)
  star.pencolor(red,green,blue)

  #Set the size
  size = random.randint(10,35)

  # Draw the star
  for i in range(size):
    star.forward(i*8)
    star.right(144)









