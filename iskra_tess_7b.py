#This program will draw a series of colored circles

import turtle

turtle.colormode(255)
window = turtle.Screen()
window.title('Circles')

r = 255
g = 255
b = 250

draw = turtle.Turtle()
draw.color(r,g,b)
draw.pensize(4)

for shape in range(19):
    draw.circle(100)
    r = r - 10
    g = g - 10
    b = b - 10
    draw.color(r,g,b)
    
    draw.penup()
    draw.forward(10)
    draw.pendown()
    draw.right(20)

window.mainloop()

