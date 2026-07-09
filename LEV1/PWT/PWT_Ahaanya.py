import turtle
d = turtle.Turtle()
d.speed(0)

def draw_line (x1,y1,x2,y2):
  d.penup()
  d.goto(x1,y1)
  d.pendown()
  d.goto(x2,y2)
  d.penup()


def draw_rectangle (x,y,l,b,color):
  d.penup()
  d.fillcolor(color)
  d.begin_fill()
  d.goto(x,y)
  d.pendown()
  d.goto(x+l,y)
  d.goto(x+l,y+b)
  d.goto(x,y+b)
  d.goto(x,y)
  d.end_fill()


n_cols = 20
n_rows = 15
x_val  = -150
y_val  = 100



for kk in range(n_rows): 
  for jj in range(n_cols):
    rem = jj % 3
    if rem == 0:
      draw_rectangle(x_val, y_val, 15, 15, "red")           
    elif rem == 1:
      draw_rectangle(x_val, y_val, 15, 15, "green")    
    else:
      draw_rectangle(x_val, y_val, 15, 15, "blue")
    x_val = x_val + 15
  
  x_val = -150   
  y_val = y_val -15

def ring(x,y,r,clr):
  d.setheading(90)
  d.penup()
  d.goto(x,y)
  d.pendown()
  d.fillcolor(clr)
  d.begin_fill()
  d.circle(r,180)
  d.penup()
  d.end_fill()

r = 150
x = 150
col = ['red','orange','yellow','green','blue','indigo','violet']
for i in range(7):
  ring(x,115,r,col[i])
  r = r - 10
  x = x - 15


input('Press enter to exit')