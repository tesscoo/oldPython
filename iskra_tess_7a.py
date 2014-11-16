#This program draws an equilateral polygon with a user-specified number of sides.

import turtle

side_number = int(input('How many sides should the polygon have? '))

window = turtle.Screen()
window.title('User Polygon Drawing')
draw = turtle.Turtle()

draw.color('pink')
draw.pensize(4)

angle = 360/side_number

for i in range (side_number):
    draw.forward(100)
    draw.right(angle)

window.mainloop()
