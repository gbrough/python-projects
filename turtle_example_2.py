import turtle
import random


star = turtle.Turtle()
star.speed(0)
star.getscreen().bgcolor("black")


def drawStar(star):
    for i in range(15):
        #Set the position
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        star.penup()
        star.setposition(x,y)
        star.pendown()

        #set color
        turtle.colormode(255)
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        star.color(red,green,blue)

        #Set the size
        size = random.randint(10,200)

        #Draw Star
        star.begin_fill()
        while True:
            star.forward(size)
            star.left(170)
            if star.heading() == 0:
                break
        star.end_fill()

drawStar(star)

turtle.done()