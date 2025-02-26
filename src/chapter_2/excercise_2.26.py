"""
(Turtle: draw a circle) Write a program that prompts the user to enter the
center and radius of a circle, and then displays the circle and its area, as shown
in Figure 2.5.
"""

import turtle

PI = 3.142

x, y, radius = eval(input("Enter center and radius of circle separated by comma eg (x, y, r):")) #gets the center and radius

area = PI * (radius**2)

turtle.showturtle()  #show the current location of turtle

#draw circle
turtle.penup()
turtle.goto(x, y-radius)
turtle.pendown()
turtle.circle(radius)

# write the area at the center
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(area, align="left", font=("Verdana", 10, "normal"))

turtle.mainloop() #makes the screen still pop up until u quit() manually
