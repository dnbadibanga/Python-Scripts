##
#Assignment 5 -
#
#This program is an extension of the PaintCircle.py program, it calculates
#the amount of paint needed to paint a cylinder
#
#By Divine Badibanga - 201765203
#

#import the math function for functions to be used in the program
from math import *

#import PaintCircle
from PaintCircle import PaintCircle

#define the class to calculate the surface area of a cylinder
class PaintCylinder(PaintCircle):
    #define a constructor with default values for instance variables
    def __init__(self, name='', h=1, rad = 1):
        #get all instance variables from the superclass
        super().__init__()
        #initialize all instance variables
        self._name = name
        self._height = h
        self._radius = rad

    #define an accessor method to calculate and return the surface area
    def getSArea(self):
        return round((2 * pi * self._radius * self._height)\
               + (2 * pi * pow(self._radius,2)),2)

    #define a method to display the information on the cylinder
    def __str__(self):
        return str(self._name) + str(':') + '\nHeight: '\
               + str(format(self._height,'.2f')) + ' Radius: '\
               +str(format(self._radius,'.2f'))+'ft, Surface area: '\
               + str(self.getSArea()) + 'sq ft\nRequired Paint: '\
               + str(super().getReqPaint()) + ' litres, Paint Cost: $'\
               + str(super().getPaintCost())

#create objects that use the PaintCylinder class
c1 = PaintCylinder('CYLINDER1',12,5)
c2 = PaintCylinder('CYLINDER2',10,4)
#display the information on both cylinders
print()
print(c1)
print()
print(c2)

#FIN
