import random
import time
import turtle


screen = turtle.Screen()
screen.setup(500, 500)
t = turtle.Turtle()
t.color('green')
t.speed(0)
ts = turtle.Screen()
ts.bgcolor('light green')
s = t.screen
t.hideturtle()


def up():
  if t.heading() != 270:
    t.setheading(90)


def down():
  if t.heading() != 90:
    t.setheading(-90)


def left():
  if t.heading() != 0:
    t.setheading(180)


def right():
  if t.heading() != 180:
    t.setheading(0)


pos = []
length = 30
speed = 4
size = 21
playing = True
collect = 5
fruits = []
eaten, posx, posy, dir, steps = 0, 0, 0, 0, 0


def draw_fruit():

  t.pendown()
  t.dot(20, 'red2')
  t.setheading(90)
  t.penup()
  t.sety(t.ycor() + 5)
  t.pendown()
  t.circle(-8, 60)
  t.penup()


def draw_grass():

  g.pendown()
  g.color('green2')
  g.setheading(110)
  g.forward(10)
  g.setheading(260)
  g.forward(10)
  g.penup()


t.penup()
for i in range(collect):
  t.goto(random.randint(-230, 230), random.randint(-230, 230))
  fruits.append(t.pos())

t.goto(0, 0)

g = turtle.Turtle()
g.hideturtle()
g.color('green2')
g.speed(0)
for i in range(random.randint(10, 15)):
  g.penup()
  g.goto(random.randint(-250, 250), random.randint(-250, 250))
  for j in range(random.randint(3, 5)):
    draw_grass()
  g.color('Black')
  g.goto(0, 0)
  g.pendown()
  g.dot(5)
  g.penup()
g.goto(0, 0)

while True:
  t.clear()
  ts.tracer(0)

  if playing:
    posx = t.xcor()
    posy = t.ycor()
    dir = t.heading()

    for i in range(len(fruits)):
      t.goto(fruits[i])
      draw_fruit()
      t.goto(posx, posy)
      t.setheading(dir)

    s.onkey(up, 'Up')
    s.onkey(down, 'Down')
    s.onkey(left, 'Left')
    s.onkey(right, 'Right')
    s.listen()

    t.penup()
    t.forward(speed)

    pos.append(t.pos())
    if len(pos) > length + 1:
      pos.pop(0)

    for i in range(len(pos) - 1):

      t.goto(pos[len(pos) - i - 1])
      t.pendown()
      t.dot(size)
      t.penup()

    t.goto(pos[len(pos) - 1])
    for i in range(len(fruits)):
      if i < len(fruits) and t.distance(fruits[i]) < 20:
        length += 5
        fruits.pop(i)
        eaten += 1

    if eaten == collect and t.distance(g.pos()) < 10:
      playing = False
      t.clear()
      g.clear()
      t.hideturtle()
      g.write("Steps Taken: " + str(steps),
              align="center",
              font=('arial', 26, 'normal'))

    steps += 1
    time.sleep(0.05)
  ts.update()