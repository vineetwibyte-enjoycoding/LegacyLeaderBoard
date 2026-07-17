"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import time

t = turtle.Turtle()

ts = t.getscreen()

def drawtheline(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)

def drawtherectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    drawtheline(x0, y0, x0+len, y0)
    drawtheline(x0+len, y0, x0+len, y0+hgt)
    drawtheline(x0+len, y0+hgt, x0, y0+hgt)
    drawtheline(x0, y0+hgt, x0, y0)
    t.end_fill()

ts.tracer(0)








ts.tracer(0)
n_rows = 30; 
n_cols = 23; 
xvalue = -150; 
yvalue = 150


for kk in range(n_rows):
    if kk==0:
        color_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif kk==1:
        color_list = [0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0]
    elif kk==2:
        color_list = [0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0]
    elif kk==3:
        color_list = [0,0,0,0,2,2,3,2,2,3,3,2,2,3,2,2,2,2,0,0,0,0,0]
    elif kk==4:
        color_list = [0,0,0,0,2,3,3,3,2,3,3,2,3,3,3,2,4,2,2,0,0,0,0]
    elif kk==5:
        color_list = [0,0,0,0,4,2,2,2,4,3,3,4,2,2,2,3,3,2,2,0,0,0,0]
    elif kk==6:
        color_list = [0,0,0,0,2,3,3,3,2,3,3,2,3,3,3,2,3,2,2,2,0,0,0]
    elif kk==7:
        color_list = [0,0,0,0,4,3,2,2,3,3,3,3,2,2,3,3,3,4,2,2,0,0,0]
    elif kk==8:
        color_list = [0,0,4,4,3,2,1,2,2,3,3,2,1,2,2,3,3,3,2,2,2,0,0]
    elif kk==9:
        color_list = [0,4,3,3,3,2,2,2,2,3,3,2,2,2,2,3,3,3,4,3,4,0,0]
    elif kk==10:
        color_list = [4,3,3,3,3,3,2,2,3,3,3,3,2,2,3,3,3,3,3,3,4,4,0]
    elif kk==11:
        color_list = [4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,0]
    elif kk==12:
        color_list = [4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4]
    elif kk==13:
        color_list = [4,3,3,3,5,5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4]
    elif kk==14:
        color_list = [0,4,3,3,5,6,5,3,3,3,3,3,3,3,3,4,4,4,3,3,3,4,0]
    elif kk==15:
        color_list = [0,0,4,4,5,6,5,3,3,3,3,3,4,4,4,6,6,5,4,4,4,0,0]
    elif kk==16:
        color_list = [0,0,0,7,5,5,4,4,4,4,4,4,6,6,6,6,6,6,6,7,0,0,0]
    elif kk==17:
        color_list = [0,0,1,7,6,6,6,6,6,6,6,6,6,6,6,7,6,6,6,7,0,0,0]
    elif kk==18:
        color_list = [0,0,7,6,6,5,6,6,6,6,6,6,6,6,6,6,7,6,6,7,0,0,0]
    elif kk==19:
        color_list = [0,0,7,6,7,6,6,6,6,6,6,6,6,6,6,6,6,7,6,7,0,0,0]
    elif kk==20:
        color_list = [0,0,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,0,0,0]
    elif kk==21:
        color_list = [0,0,4,3,7,5,5,9,9,5,5,5,9,9,9,5,5,7,3,3,4,0,0]
    elif kk==22:
        color_list = [0,0,4,3,7,5,5,9,9,5,5,5,9,9,9,5,5,7,3,3,4,0,0]
    elif kk==23:
        color_list = [0,0,0,4,11,9,9,9,9,9,9,9,9,9,9,9,9,11,4,4,0,0,0]
    elif kk==24:
        color_list = [0,0,0,0,11,11,11,11,11,11,11,11,11,11,11,11,11,11,0,0,0,0,0]
    elif kk==25:
        color_list = [0,0,0,0,4,3,3,4,0,0,0,0,0,0,4,3,3,4,0,0,0,0,0]
    elif kk==26:
        color_list = [0,0,0,0,0,4,3,4,0,0,0,0,0,0,4,3,4,0,0,0,0,0,0]
    elif kk==27:
        color_list = [0,0,0,0,0,4,3,4,0,0,0,0,0,0,4,3,4,0,0,0,0,0.0,0]
    elif kk==28:
        color_list = [0,0,10,8,8,8,8,10,0,0,0,0,0,0,10,8,8,8,8,10,0,0,0 ]
    elif kk==29:
        color_list = [0,0,10,10,10,10,10,10,0,0,0,0,0,0,10,10,10,10,10,10,0,0,0]
    else:
        color_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



    for jj in range(n_cols):

        if color_list[jj]==0:
            drawtherectangle(xvalue, yvalue, 15, 15, "green")
        elif color_list[jj]==1:
            drawtherectangle(xvalue, yvalue, 15, 15, "white")
        elif color_list[jj]==2:
            drawtherectangle(xvalue, yvalue, 15, 15, "black")
        elif color_list[jj]==3:
            drawtherectangle(xvalue, yvalue, 15, 15, "antiquewhite2")
        elif color_list[jj]==4:
            drawtherectangle(xvalue, yvalue, 15, 15, "chocolate4")
        elif color_list[jj]==5:
            drawtherectangle(xvalue, yvalue, 15, 15, "firebrick3")
        elif color_list[jj]==6:
            drawtherectangle(xvalue, yvalue, 15, 15, "red")
        elif color_list[jj]==7:
            drawtherectangle(xvalue, yvalue, 15, 15, "firebrick4")
        elif color_list[jj]==8:
            drawtherectangle(xvalue, yvalue, 15, 15, "cyan")
        elif color_list[jj]==9:
            drawtherectangle(xvalue, yvalue, 15, 15, "yellow")
        elif color_list[jj]==10:
            drawtherectangle(xvalue, yvalue, 15, 15, "cyan4")
        else:
            drawtherectangle(xvalue, yvalue, 15, 15, "goldenrod4")    
        xvalue = xvalue + 15
    xvalue = -150
    yvalue = yvalue - 15

t.goto(-150,200)
t.write('I am shin-chan I will make you laugh')

turtle.done()