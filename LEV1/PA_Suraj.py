"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
ts = turtle.getscreen()


def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)


clr = t.color


def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0 + len, y0)
    draw_line(x0 + len, y0, x0 + len, y0 + hgt)
    draw_line(x0 + len, y0 + hgt, x0, y0 + hgt)
    draw_line(x0, y0 + hgt, x0, y0)
    t.end_fill()


n_cols = 30
n_rows = 30
x_val = -300
y_val = 365

ts.tracer(0)

for kk in range(n_rows):
  for jj in range(n_cols):

    if kk == 0 or kk == 1 or kk == 2:
      draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 3:
      if jj < 10 or jj > 20:
          draw_rectangle(x_val, y_val, 15, 15, 'white')
      else:
          draw_rectangle(x_val, y_val, 15, 15, 'black')

    elif kk == 4:
      if jj < 8:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj > 8 and jj < 9:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj > 10 and jj < 20:
        draw_rectangle(x_val, y_val, 15, 15, 'sky blue')
      elif jj > 22:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'black')

    elif kk == 5:
      if jj < 8:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif (jj > 10 and jj < 20) or jj > 22:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'black')

    elif kk == 6:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj > 9 and jj < 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj > 23 and jj < 31:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 7:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj > 8 and jj < 22:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 8:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj > 9 and jj < 12:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj < 12 and jj > 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 9:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'yellow')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'yellow')
      elif jj == 21:
          draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 10:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'yellow')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'yellow')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 11:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 12:
      if jj < 6:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 13:
      if jj < 6:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 14:
      if jj < 5:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 15:
      if jj < 5:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 16:
      if jj < 4:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 4:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 26:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 17:
      if jj < 4:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 4:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 26:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 18:
      if jj < 4:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 4:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 26:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 19:
      if jj < 4:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 4:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 26:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 20:
      if jj < 4:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 4:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 26:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 21:
      if jj < 4:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 4:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 26:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 22:
      if jj < 5:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 23:
      if jj < 5:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
        

    elif kk == 24:
      if jj < 5:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 5:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 25:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 25:
      if jj < 6:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')


              
    elif kk == 26:
      if jj < 6:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 6:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 24:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 27:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      elif jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 28:
      if jj < 7:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
      if jj == 7:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 9:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 10:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 11:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 12:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 13:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 14:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 16:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 17:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 18:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj == 19:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj == 20:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 21:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj == 22:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj == 23:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')

    elif kk == 29:
      if jj <8:
        draw_rectangle(x_val, y_val, 15, 15, 'white') 
      elif jj== 8:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj==9:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj==10:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj==11:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj==12:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj==13:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj==14:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj==15:
        draw_rectangle(x_val, y_val, 15, 15, 'light blue')
      elif jj==16:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')  
      elif jj==17:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj==18:
        draw_rectangle(x_val, y_val, 15, 15, 'blue')
      elif jj==19:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj==20:
        draw_rectangle(x_val, y_val, 15, 15, 'silver')
      elif jj==21:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      elif jj==22:
        draw_rectangle(x_val, y_val, 15, 15, 'black')
      else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')


    else:
        draw_rectangle(x_val, y_val, 15, 15, 'white')
        
    
    x_val = x_val + 15
  x_val = -300
  y_val = y_val - 15


ts.update()
