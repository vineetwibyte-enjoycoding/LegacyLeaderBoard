import turtle
from datetime import datetime
import time

# Create two turtle objects for drawing,
# one for static drawing and one for the clock hands.
t = turtle.Turtle()  # Main drawing turtle


# Set the drawing speed to the fastest
t.speed(0)

# Hide the turtle objects for cleaner drawing
t.ht()


# Disable automatic screen updates for smoother animation
turtle.tracer(0)

# Set initial color and pen size for the main drawing turtle
t.color('burlywood')
t.pensize(3)

# Function to draw a rectangle centered at (x, y) with specified height, length, colors.
def rectangle(x, y, height, length, color, fillcolor):
    t.penup()
    t.color(color)
    t.goto(x - length / 2, y + height / 2)
    t.begin_fill()
    t.fillcolor(fillcolor)
    t.pendown()
    t.goto(x + length / 2, y + height / 2)
    t.goto(x + length / 2, y - height / 2)
    t.goto(x - length / 2, y - height / 2)
    t.goto(x - length / 2, y + height / 2)
    t.end_fill()

# Function to draw a regular polygon centered at (x, y)≠
def polygon(x, y, length, color, fillcolor, numsides):
    t.penup()
    t.color(color)
    t.goto(x - length/2, y - length/2)
    t.begin_fill()
    t.fillcolor(fillcolor)
    t.pendown()
    for i in range(numsides):
        t.forward(length)
        t.left(360 / numsides)
    t.end_fill()

# Draw the main structure of the clock tower
rectangle(0, -50, 350, 100, 'burlywood', 'burlywood')

# Draw the spire as an equilateral triangle
polygon(0, 175, 100, 'gray40', 'gray40', 3)

# Draw the small rectangle above the spire  
rectangle(0, 190, 40, 52, 'burlywood', 'burlywood')

# Draw black details on the roof (parallel lines)
rectangle(-18, 190, 30, 3, 'Black', 'Black')
rectangle(-9, 190, 30, 3, 'Black', 'Black')
rectangle(0, 190, 30, 3, 'Black', 'Black')
rectangle(9, 190, 30, 3, 'Black', 'Black')
rectangle(18, 190, 30, 3, 'Black', 'Black')

# draw the second spire
t.pu()
t.begin_fill()
t.color('grey40')
t.fillcolor('grey40')
t.goto(-26, 212.5)
t.pd()
t.begin_fill()
t.fillcolor('grey40')
t.goto(26, 212.5)
t.goto(0, 300)
t.goto(-26, 212.5)
t.end_fill()

# Draw the pole
t.pu()
t.color('grey34')
t.goto(0, 300)
t.pensize(5)
t.pd()
t.goto(0, 350)
t.pu()

# draw the decoration on the pole
t.goto(-7.525, 325)
t.pensize(7)
t.pd()
t.setheading(90)
t.circle(-7.525, 180)

# Draw the main clock face outside decoration
t.pu()
t.pensize(3)
polygon(0, 135, 80, 'black', 'burlywood1', 4)
t.pu()
t.goto(-30, 85)
t.dot(15, 'burlywood4')
t.goto(30, 85)
t.dot(15, 'burlywood4')
t.goto(-30, 25)
t.dot(15, 'burlywood4')
t.goto(30, 25)
t.dot(15, 'burlywood4')

# Draw a large white circle for the clock face background
t.goto(-35, 55)
t.begin_fill()
t.fillcolor('white')
t.color('white')
t.circle(35)
t.end_fill()

# Draw small black center dot for the clock's center
t.goto(0, 55)
t.dot(10, 'black')

# Draw concentric circles around the clock face
t.pd()
t.setheading(0)
y = 25
c = 30
t.pencolor('black')
t.pensize(1)
for i in range(3):
    t.pu()
    t.goto(0, y)
    t.pd()
    t.circle(c)
    y += 5
    c -= 5

# Draw decorative rectangles on the top part of clock tower
x = 35
for i in range(7):
    rectangle(x, 110, 15, 5, 'black', 'black')
    x -= 11.5

# Draw other small rectangles as details
x = 33
for i in range(4):
    rectangle(x, 0, 15, 5, 'black', 'black')
    x -= 22
    
# Draw lines at the bottom of the tower as detail
rectangle(40, -50, 30, 1, 'black', 'black')
rectangle(25, -50, 30, 1, 'black', 'black')
rectangle(-25, -50, 30, 1, 'black', 'black')
rectangle(-40, -50, 30, 1, 'black', 'black')
rectangle(-25, -100, 30, 1, 'black', 'black')
rectangle(25, -100, 30, 1, 'black', 'black')
rectangle(-40, -100, 30, 1, 'black', 'black')
rectangle(40, -100, 30, 1, 'black', 'black')
rectangle(40, -150, 30, 1, 'black', 'black')
rectangle(25, -150, 30, 1, 'black', 'black')
rectangle(-25, -150, 30, 1, 'black', 'black')
rectangle(-40, -150, 30, 1, 'black', 'black')

# Enable updates for smooth rendering
turtle.tracer(0)

# Infinite loop to continuously update the clock
while True:
    u = turtle.Turtle()  # Create a new turtle for each update to avoid conflicts
    u.speed(0)
    u.ht()
    u.pensize(7)
    u.color('black')
    u.penup()

    # Get current GMT time
    timnow = datetime.now()
    hour = timnow.hour
    minute = timnow.minute

    # Calculate angles for clock hands
    hangle = hour / 12 * 360 + (minute / 60) * 30
    mangle = minute / 60 * 360

    # Draw the hour hand
    u.goto(0, 55)
    u.setheading(90)
    u.right(hangle)
    u.pendown()
    u.forward(15)

    # Draw the minute hand
    u.penup()
    u.goto(0, 55)
    u.setheading(90)
    u.right(mangle)
    u.pendown()
    u.forward(25)

    # Update the drawing
    turtle.update()

    # Remove the turtle after drawing
    u.clear()
    u.hideturtle()

    # Wait for 60 seconds before next update
    time.sleep(60)