import turtle
import math

wn = turtle.Screen()
aTurtle = turtle.Turtle()

x0,y0 = eval(input('Please enter the coordinated for the first point, separated by comma: '))
x1,y1 = eval(input('Please enter the coordinates for the second point, separated by comma: '))
x2,y2 = eval(input('Please enter the coordinates for the third point, separated by comma: '))

aTurtle.penup()
aTurtle.goto(x0,y0)
aTurtle.pendown()
aTurtle.goto(x1,y1)
aTurtle.penup()
aTurtle.goto(x2,y2)
aTurtle.pendown()
aTurtle.write("X")
aTurtle.penup()
aTurtle.goto(x2+10,y2+10)
aTurtle.pendown()
if x0 == x1:
    if x2 > x0 and x2 > x1:
        aTurtle.write('p2 is on the right of the line')
    if x2 < x0 and x2 < x1:
        aTurtle.write('p2 is on the left of the line')
    else:
        aTurtle.write('p2 is on the line')
elif y0 == y1:
    if y2 > y0 and y2 > y1:
        aTurtle.write('p2 is on above the line')
    if y2 < y0 and y2 < y1:
        aTurtle.write('p2 is below the line')
    else:
        aTurtle.write('p2 is on the line')
else:
    slope = (y1-y0)/(x1-x0)
    intercept = y0 -x0 * slope
    xNew = (y2 - intercept) / slope
    if x2 > xNew:
        aTurtle.write('p2 is on the right of the line')
    elif x2 < xNew:
        aTurtle.write('p2 is on the left of the line')
    else:
        aTurtle.write('p2 is on the line')
