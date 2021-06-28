import turtle

star = turtle.Turtle()

star.color("blue","red")

for i in range(4):
  star.begin_fill()
  star.forward(100)
  star.left(90)
  star.end_fill()


turtle.done()