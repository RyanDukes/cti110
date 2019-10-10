# Creates an increasing rectangle.
# 10/10/2019
# CTI-110 P4T1a - Squares
# Ryan Dukes
#

# The variables sq and e are assigned values.
# Using a while function a rectangle is drawn and increases in size because it is increased by 5 each time.
# Displays increasing squares as the while loop runs until sq runs 50 times.

import turtle

sq = 0
e = 10


while sq < 50:
    for x in range(4):
        turtle.speed(100)
        turtle.left(90)
        turtle.forward(e)

    sq = sq + 1
    e = e + 5

turtle.hideturtle()
exitonclick()
