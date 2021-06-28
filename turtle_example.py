import turtle

star = turtle.Turtle()

star.color("blue","red")

star.begin_fill()
for i in range(4):
  star.forward(100)
  star.left(90)

star.end_fill()


turtle.done()