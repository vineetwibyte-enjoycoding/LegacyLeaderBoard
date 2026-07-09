import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.penup()
t.speed(3)
t.shape('arrow')
t.pen(pensize=5)

s.bgcolor('sky blue')

def arch(length,size,fill,outl):

  t.fillcolor(fill)
  t.pencolor(outl)
  t.begin_fill()
  t.penup()
  t.setheading(180)
  t.forward(size/2)
  t.pendown()
  t.setheading(90)
  t.forward(length)
  t.circle(size/-2,180)
  t.forward(length)
  t.setheading(180)
  t.forward(size)
  t.setheading(0)
  t.forward(size/2)
  t.end_fill()
  t.penup()

def rectangle(length,width,fill,outl):

  t.fillcolor(fill)
  t.pencolor(outl)
  t.begin_fill()
  t.penup()
  t.setheading(180)
  t.forward(width/2)
  t.pendown()
  t.setheading(90)
  for i in range(2):
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
  t.setheading(0)
  t.forward(width/2)
  t.end_fill()
  t.penup()

def column():

  rectangle(80,20,'PeachPuff3','black')
  t.sety(-20)
  rectangle(10,22,'gold','black')
  t.sety(-10)
  rectangle(50,18,'PeachPuff2','black')
  t.sety(40)
  rectangle(10,20,'gold','black')
  t.sety(50)
  arch(30,14,'PeachPuff1','black')

def box(number):
  
  if number == 1:
    rectangle(115,40,'PeachPuff2','black')
    arch(30,20,'PeachPuff4','black')
    t.sety(-40)
    arch(20,20,'PeachPuff4','black')
  
  if number == 2:
    rectangle(100,30,'PeachPuff3','black')
    arch(20,16,'PeachPuff4','black')
    t.sety(-50)
    arch(15,16,'PeachPuff4','black')

t.goto(0,-354)
rectangle(250,1500,'green','dark green')

t.pen(pensize=3)
t.goto(0,-110)
rectangle(10,400,'gold','black')

t.goto(0,-100)
arch(120,110,'peach puff','black')
rectangle(105,110,'gold','black')
rectangle(100,110,'peach puff','black')
rectangle(90,70,'PeachPuff3','black')
rectangle(80,70,'PeachPuff2','black')
arch(40,50,'PeachPuff4','black')

t.goto(-18,72)
t.begin_fill()
t.fillcolor('gold')
t.pendown()
t.setheading(25)
t.forward(20)
t.setheading(-25)
t.forward(20)
t.goto(-18,72)
t.end_fill()
t.penup()


t.goto(75,-100)
box(1)
t.goto(-75,-100)
box(1)

t.goto(110,-100)
box(2)
t.goto(-110,-100)
box(2)

t.goto(155,-100)
column()
t.goto(-155,-100)
column()

t.goto(180,120)
t.pendown()
t.pencolor('orange')
t.fillcolor('gold')
t.begin_fill()
t.circle(30)
t.end_fill()
t.setheading(90)

t.pencolor('yellow')
t.penup()
t.goto(180,150)
t.pendown()
t.dot(48)
t.pencolor('orange2')
t.pen(pensize=4)
for i in range(12):
  t.penup()
  t.goto(180,150)
  t.right(30)
  t.forward(37)
  t.pendown()
  if i%2 == 1:
    t.forward(5)
  else:
    t.forward(7)

t.ht()

turtle.done()