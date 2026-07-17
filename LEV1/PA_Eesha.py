import turtle
t  =  turtle.Turtle()
ts = t.getscreen()

def draw_line(x0,y0,x1,y1):
  t.penup()
  t.goto(x0,y0)
  t.pendown()
  t.goto(x1,y1)

def draw_rectangle(x0,y0,len,hgt,clr):
  t.fillcolor(clr)
  t.begin_fill()
  draw_line(x0,y0,x0+len,y0)
  draw_line(x0+len,y0,x0+len,y0+hgt)
  draw_line(x0+len,y0+hgt,x0,y0+hgt)
  draw_line(x0,y0+hgt,x0,y0)
  t.end_fill()

n_cols  = 24
n_rows  =  31
x_val = -150
y_val = 190

ts.tracer(0)

for kk in range(n_rows) :
  if kk == 0 or kk == 1  :
    colour_list  = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
  elif kk == 2 :
    colour_list  = [ 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1 ]
  elif  kk == 3 :
    colour_list  = [ 1, 1, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 1 ]
  elif  kk == 4 :
   colour_list  = [ 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1 ]
  elif  kk == 5 :
     colour_list  = [ 1, 1, 3, 3, 3, 3, 3, 3, 3, 1, 7, 7, 8, 1, 1, 3, 3, 3, 3, 3, 3, 3, 1, 1 ]
  elif  kk == 6 :
    colour_list  = [ 1, 1, 4, 4, 3, 3, 3, 3, 1, 7, 7, 7, 7, 8, 1, 3, 3, 3, 3, 3, 3, 3, 1, 1 ]
  elif  kk == 7 :
    colour_list  = [ 1, 1, 5, 4, 4, 4, 4, 4, 1, 7, 7, 7, 7, 8, 1, 1, 4, 4, 4, 3, 4, 4, 1, 1 ]
  elif  kk == 8 :
    colour_list  = [ 1, 1, 5, 4, 4, 5, 4, 4, 1, 7, 7, 7, 7, 8, 1, 1, 5, 5, 4, 4, 4, 5, 1, 1 ]
  elif  kk == 9 :
    colour_list  = [ 1, 1, 5, 5, 5, 5, 5, 5, 1, 7, 7, 7, 7, 8, 1, 1, 5, 5, 4, 4, 4, 5, 1, 1 ]
  elif  kk == 10 :
    colour_list  = [ 1, 1, 5, 5, 5, 5, 2, 2, 1, 7, 7, 7, 7, 8, 1, 1, 2, 2, 2, 2, 2, 5, 1, 1 ]
  elif  kk == 11 :
    colour_list  = [ 1, 1, 5, 5, 5, 2, 2, 2, 1, 1, 7, 7, 8, 1, 1, 1, 5, 2, 5, 5, 5, 5, 1, 1 ]
  elif  kk == 12 :
    colour_list  = [ 1, 1, 2, 2, 2, 2, 2, 5, 1, 1, 1, 8, 8, 8, 1, 1, 5, 5, 2, 2, 5, 5, 1, 1 ]
  elif  kk == 13 :
    colour_list  = [ 1, 1, 5, 8, 8, 6, 5, 5, 1, 1, 7, 7, 7, 7, 1, 1, 10, 5, 5, 5, 2, 5, 1, 1 ]
  elif  kk == 14 :
    colour_list  = [ 1, 1, 6, 6, 5, 8, 6, 5, 1, 7, 7, 7, 7, 7, 1, 6, 1, 10, 5, 6, 8, 5, 1, 1 ]
  elif  kk == 15 :
    colour_list  = [ 1, 1, 6, 5, 5, 6, 6, 10, 1, 7, 7, 7, 7, 7, 6, 1, 9, 1, 10, 6, 6, 8, 1, 1 ]
  elif  kk == 16 :
    colour_list  = [ 1, 1, 8, 6, 6, 6, 10, 10, 8, 8, 7, 7, 7, 6, 1, 9, 10, 10, 10, 5, 6, 6, 1, 1 ]
  elif  kk == 17 :
    colour_list  = [ 1, 1, 6, 8, 6, 10, 10, 1, 6, 6, 8, 8, 8, 1, 9, 10, 10, 9, 10, 10, 5, 6, 1, 1 ]
  elif  kk == 18 :
    colour_list  = [ 1, 1, 5, 6, 5, 10, 10, 1, 1, 6, 6, 6, 1, 9, 10, 10, 10, 9, 9, 10, 5, 5, 1, 1 ]
  elif  kk == 19 :
    colour_list  = [ 1, 1, 5, 5, 6, 10, 10, 1, 1, 1, 1, 1, 1, 10, 10, 10, 9, 9, 9, 10, 5, 5, 1, 1 ]
  elif  kk == 20 :
    colour_list  = [ 1, 1, 5, 5, 10, 10, 10, 10, 1, 1, 1, 1, 9, 10, 10, 9, 10, 10, 9, 10, 10, 5, 1, 1 ]
  elif  kk == 21 :
    colour_list  = [ 1, 1, 5, 10, 10, 9, 1, 10, 10, 9, 1, 9, 10, 10, 10, 10, 10, 9, 10, 10, 10, 5, 1, 1 ]
  elif  kk == 22 :
    colour_list  = [ 1, 1, 5, 10, 9, 1, 1, 9, 10, 9, 1, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 1, 1 ]
  elif  kk == 23 :
    colour_list  = [ 1, 1, 5, 10, 1, 6, 6, 7, 7, 7, 1, 10, 10, 10, 10, 10, 9, 9, 9, 10, 10, 5, 1, 1 ]
  elif  kk == 24 :
    colour_list  = [ 1, 1, 10, 10, 9, 1, 1, 8, 8, 7, 7, 7, 1, 10, 10, 9, 9, 9, 9, 9, 10, 10, 1, 1 ]
  elif  kk == 25 :
    colour_list  = [ 1, 1, 10, 10, 10, 10, 9, 7, 7, 8, 8, 7, 7, 6, 6, 6, 1, 10, 9, 9, 10, 10, 1, 1 ]
  elif  kk == 26 :
    colour_list  = [ 1, 1, 10, 10, 10, 10, 7, 8, 1, 9, 9, 6, 1, 1, 9, 10, 10, 10, 10, 10, 10, 5, 1, 1 ]
  elif  kk == 27 :
    colour_list  = [ 1, 1, 10, 10, 10, 10, 9, 9, 10, 10, 10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 5, 1, 1 ]
  elif  kk == 28 :
    colour_list  = [ 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 1, 1 ]
  else :
    colour_list  = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]

  for   jj in range(n_cols) :
    if colour_list[jj] == 1 :
      draw_rectangle(x_val,y_val,15,15,"#361a0c")
    elif colour_list[jj] == 2 :
      draw_rectangle(x_val,y_val,15,15,"#0d855e")
    elif colour_list[jj] == 3 :
      draw_rectangle(x_val,y_val,15,15,"#818f56")
    elif colour_list[jj] == 4 :
      draw_rectangle(x_val,y_val,15,15,"#cfd6a8")
    elif colour_list[jj] == 5 :
      draw_rectangle(x_val,y_val,15,15,"#5b623d")
    elif colour_list[jj] == 6 :
      draw_rectangle(x_val,y_val,15,15,"#843f1b")
    elif  colour_list[jj] == 7 :
      draw_rectangle(x_val,y_val,15,15,"#c6be6f")
    elif  colour_list[jj] == 8 :
      draw_rectangle(x_val,y_val,15,15,"#7e5f32")
    elif  colour_list[jj] == 9 :
      draw_rectangle(x_val,y_val,15,15,"#1f2328")
    elif  colour_list[jj] == 10 :
      draw_rectangle(x_val,y_val,15,15,"#000000")

    x_val = x_val + 15
  x_val  = -150
  y_val  = y_val - 15

ts.update()