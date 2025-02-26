"""
(Turtle: draw a rectangle) Write a program that prompts the user to enter the
center of a rectangle, width, and height, and displays the rectangle, as shown in
Figure 2.4c.
"""

import turtle

x, y = eval(input("Enter the center of the rectangle like (x, y) eg(2, 3): "))
width, height = eval(input("Enter the dimension of the rectangle like (width, height) eg (100, 200): "))

# initial turtle configuration
turtle.showturtle()
turtleXPos, turtleYPos = 0, 0
turtle.color("#888888")

# move  the  turtle position to new value for the rectangle
currentTurtleXPos, currentTurtleYPos = (turtleXPos+x) - width/2, (turtleYPos+y) - height/2
turtle.penup()
turtle.goto(currentTurtleXPos, currentTurtleYPos)
turtle.pendown()

# going right
currentTurtleXPos +=width
turtle.goto(currentTurtleXPos, currentTurtleYPos)

# going up
currentTurtleYPos +=height
turtle.goto(currentTurtleXPos, currentTurtleYPos)

# going left
currentTurtleXPos -=width
turtle.goto(currentTurtleXPos, currentTurtleYPos)

# going down
currentTurtleYPos -=height
turtle.goto(currentTurtleXPos, currentTurtleYPos)

turtle.hideturtle()
turtle.mainloop()