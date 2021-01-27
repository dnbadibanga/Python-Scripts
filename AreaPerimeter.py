##
#This program calculates the Area and Perimeter of a quadrilateral
#

#import math
from math import *

#enter variables
coordinateX1 = float(input('Enter value for x1: '))
coordinateY1 = float(input('Enter value for y1: '))
coordinateX2 = float(input('Enter value for x2: '))
coordinateY2 = float(input('Enter value for y:  '))

#calculate perimeter
length = abs(coordinateX2 - coordinateX1)
width = abs(coordinateY2 - coordinateY1)
perimeter = length + length + width + width

#calculate area
area = length * width

#calculate length of diagonal
diagonal = sqrt(pow(length,2) + pow(width,2))

#display data
print('The perimeter of the rectangle is ', '%.2f' %perimeter)
print('The area of the rectangle is ', '%.2f' %area)
print('The length of the diagonal is: ', '%.2f' %diagonal)
