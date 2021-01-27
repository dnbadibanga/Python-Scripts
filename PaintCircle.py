##
#Assignment 5
#
#This program computes the cost of paint to be used to paint a circle with
#a given radius
#
#By Divine Ndaya Badibanga - 201765203
#

#import the math function for functions to be used in the program
from math import *

#define the class with information on the circle to be processed
class PaintCircle():
    #set constant class variables
    COVERAGE = 11
    PAINTCOST = 15

    #define the constructor method with a default radius and other instance
    #variables
    def __init__(self, name='', rad=1):
        self._name = name
        self._radius = rad

    #define accessors for each instance variable, along with their calculations
    def getRadius(self):
        return self._radius

    def getSArea(self):
        return round(pi * pow(self._radius,2),2)

    def getReqPaint(self):
        return ceil(self.getSArea() / PaintCircle.COVERAGE)

    def getPaintCost(self):
        return '%.2f' %(PaintCircle.PAINTCOST * self.getReqPaint())

    #define a method to display the information in an appropriate format
    def __str__(self):
        return (str(self._name) + str(':') + '\nRadius: '\
                +str(format(self._radius,'.2f')) + 'ft, Surface Area : '\
                + str(self.getSArea()) +  ' sq ft \nRequired Paint: '\
                +str(self.getReqPaint()) + ' litres, Paint Cost: $'\
                +str(self.getPaintCost()))

#access the class with objects
circle1 = PaintCircle('CIRCLE1', 5)
circle2 = PaintCircle('CIRCLE2', 10)
circle3 = PaintCircle('CIRCLE3', 15)
#display the information of the different circles
print(circle1)
print()
print(circle2)
print()
print(circle3)

#FIN
