# Writes my initials with turtle graphics.
# 10/10/2019
# CTI-110 P4T1b - Initials
# Ryan Dukes
#

# Turtle is assigned a color and size.
# Directions for writing initials given to turtle to draw.
# Drawn turtle graphic is shown displaying RD initials.

import turtle

#formatting turtle

turtle.color('red')
turtle.pensize(10)

#Instructions for turtle to draw "R"

turtle.penup()
turtle.left(180)
turtle.forward(50)

turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)

turtle.circle(30, 180, 10)
turtle.forward(25)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(25)
turtle.right(60)
turtle.forward(58)

#Instructions for turtle to draw "D"

turtle.penup()
turtle.left(60)
turtle.forward(50)
turtle.pendown()

turtle.circle(55, 180)
turtle.left(90)
turtle.forward(110)
