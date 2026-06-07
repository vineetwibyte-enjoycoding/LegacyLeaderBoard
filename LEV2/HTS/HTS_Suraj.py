"""
This is the Template Repl for Python with Turtle.
Python with Turtle lets you make graphics easily in Python.
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import random
# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

import time

t = turtle.Turtle()
t.shape('square')
t.color("red")
t.penup()
t.goto(0, 0)

ts = turtle.getscreen()
# ts.tracer(0)

n_foods = 1
list_of_foods = []

for kk in range(n_foods):
    food = turtle.Turtle()
    print(food)
    food.penup()
    food.speed(0)
    food.shape("circle")
    food.color("gold")
    food_size = 20
    list_of_foods.append(food)
    #for food in list_of_foods:
    #    food.hideturtle()
    random_x = random.choice(range(-180, 180, 20))
    random_y = random.choice(range(-180, 180, 20))
    #random_food = random.choice(list_of_foods)
    food.goto(random_x, random_y)
    #random_food.shapesize(1)
    food.showturtle()




ts.tracer(0)


def draw_grid():
    grid = turtle.Turtle()
    grid.penup()
    grid.goto(-190, -190)
    grid.speed(579)
    for i in range(20):
        for j in range(20):
            if (i + j) % 2 == 0:
                grid.color("black")
            else:
                grid.color("grey")
            grid.begin_fill()
            for _ in range(4):
                grid.forward(20)
                grid.right(90)
            grid.end_fill()
            grid.forward(20)
        grid.penup()
        grid.goto(-190, -190 + 20 * (i + 1))
        grid.pendown()


draw_grid()

ts.update()

# input()

ts.tracer(1)
'''

'''
pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color("white")
pen.ht()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("white")
report.ht()

started = 0


def right():
    if t.heading() != 180.0:
        t.setheading(0.0)


def left():
    if t.heading() != 0.0:
        t.setheading(180.0)


def up():
    if t.heading() != -90.0:
        t.setheading(90.0)


def down():
    if t.heading() != 90.0:
        t.setheading(-90.0)


steps = 0


def move():
    global steps
    #t.forward(10)

    # if t.xcor() % 20 == 0 and t.ycor() % 20 == 0:

    if True:
        if t.heading() == 0.0:
            t.setx(t.xcor() + 20)
        elif t.heading() == 180.0:
            t.setx(t.xcor() - 20)
        elif t.heading() == 90.0:
            t.sety(t.ycor() + 20)
        # elif t.heading() == -90.0:
        elif t.heading() == 270.0:
            t.sety(t.ycor() - 20)
    steps = steps + 1


ts = t.screen
ts.bgcolor("black")

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()

caught = []
for kk in range(n_foods):
    caught.append(0)

segments = []

game_over = False

foods_eaten = 0
while game_over == False:
    pen.write(foods_eaten, align="center", font=("Courier", 24, "normal"))
    for kk in range(len(list_of_foods)):
        #if t.distance(list_of_foods[kk]) < 20 and caught[kk] == 0:
        if t.distance(list_of_foods[kk]) < 20 and foods_eaten < 6:
            caught[kk] = 1
            # list_of_foods[kk].color('crimson')

            random_x = random.choice(range(-180, 180, 20))
            random_y = random.choice(range(-180, 180, 20))
            #random_food = random.choice(list_of_foods)
            list_of_foods[kk].goto(random_x, random_y)

            segment = turtle.Turtle()
            segment.shape('square')
            segment.color('green')
            segment.penup()
            segment.speed(0)
            segments.append(segment)
            foods_eaten += 1
            print('Food eaten ...', foods_eaten)
            pen.clear()

  
  
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = t.xcor()
        y = t.ycor()
        segments[0].st()
        segments[0].goto(x, y)

    move()
    print(t.xcor())
    if t.xcor() > 10:
        started = 1

    for segment in segments:
      if segment.distance(t) < 20:
        game_over = True

    if foods_eaten == 6:
        list_of_foods[0].ht()
        if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
            game_over = True
            time.sleep(1)
            t.clear()
            t.ht()
            for kk in range(len(segments)):
                segments[kk].ht()

            report.write("Steps Taken: " + str(steps),
                         align="center",
                         font=("Courier", 24, "normal"))

    time.sleep(0.1)

turtle.done()


# ts.update()
