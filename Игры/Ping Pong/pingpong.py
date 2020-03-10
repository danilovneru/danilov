import turtle
from random import choice, randint


window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')

border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.setheading(270)
for i in range(25):
  if i%2==0:
    border.forward(24)
  else:
    border.up()
    border.forward(24)
    border.down()  
border.hideturtle()
border.goto(0, -300)


roket_a = turtle.Turtle()
roket_a.color('white')
roket_a.shape('square')
roket_a.shapesize(stretch_len=1, stretch_wid=5)
roket_a.penup()
roket_a.goto(-450, 0)

roket_b = turtle.Turtle()
roket_b.color('white')
roket_b.shape('square')
roket_b.shapesize(stretch_len=1, stretch_wid=5)
roket_b.penup()
roket_b.goto(450, 0)

def move_up_a():
  y = roket_a.ycor() + 10
  if y > 250:
    y = 250
  roket_a.sety(y)

def move_down_a():
  y = roket_a.ycor() - 10
  if y < -250:
    y = -250
  roket_a.sety(y)  



def move_up_b():
  y = roket_b.ycor() + 10
  if y > 250:
    y = 250
  roket_b.sety(y)

def move_down_b():
  y = roket_b.ycor() - 10
  if y < -250:
    y = -250
  roket_b.sety(y)


ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('red')
ball.dx = 3
ball.dy = -3
ball.penup()


window.listen()
window.onkeypress(move_up_a, 'w')
window.onkeypress(move_down_a, 's')
window.onkeypress(move_up_b, 'Up')
window.onkeypress(move_down_b, 'Down')

while True:

  window.update()
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  if ball.ycor() >= 290:
    ball.dy = -ball.dy
  
  if ball.ycor() <= -290:
    ball.dy = -ball.dy

  if ball.xcor() >= 490:
    ball.goto(0, randint(-150, 150))
    ball.dx = choice([-4, -3, -2, 2, 3, 4])
    ball.dy = choice([-4, -3, -2, 2, 3, 4])

  if ball.xcor() <= -490:
    ball.goto(0, randint(-150, 150))
    ball.dx = choice([-4, -3, -2, 2, 3, 4])
    ball.dy = choice([-4, -3, -2, 2, 3, 4])


  if ball.ycor() >= roket_b.ycor()-50 and ball.ycor() <= roket_b.ycor()+50 \
    and ball.ycor() >= roket_b.xcor() -5 and ball.ycor() <= roket_b.xcor() + 5:
    ball.dx = -ball.dx
  if ball.ycor() >= roket_a.ycor()-50 and ball.ycor() <= roket_a.ycor()+50 \
    and ball.ycor() >= roket_a.xcor() -5 and ball.ycor() <= roket_a.xcor() + 5:
    ball.dx = -ball.dx


window.mainloop()



