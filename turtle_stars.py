# Create our star
# Change the star color
# change the background color
# change the location of star
# change the size of star
# create multiple stars

import turtle
import random

star = turtle.Turtle()
star.speed(0)
star.getscreen().bgcolor("black")

def drawStar(star):
  for i in range(7):
    #Set color
    turtle.colormode(255)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    star.color(red,green,blue)

    x = random.randint(-300,300)
    y = random.randint(-300,300)
    star.penup()
    star.setposition(x,y)
    star.pendown()

    size = random.randint(20,200)

    star.begin_fill()
    while True:
      star.forward(size)
      star.left(170)
      if star.heading() == 0:
        break
    star.end_fill()

drawStar(star)
turtle.done()