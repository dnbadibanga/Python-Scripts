##
#Assignment 5 - PaintCone.py
#This program is an extension of the PaintCircle.py program to calculate
#the amount of paint needed to paint a cone
#
#By Divine Ndaya Badibanga - 201765203
#

#import the math function for functions to be used in the program
from math import *
#import the PaintCircle class
from PaintCircle import PaintCircle

#define the class PaintCone to compute the surface area of a cone
class PaintCone(PaintCircle):
    #define the constructor with default values for the instance variables
    def __init__(self, name='', h=1, rad=1):
        #get instance variables from the superclass
        super().__init__()
        #initialize instance variables
        self._name = name
        self._radius = rad
        self._height = h


    #define accessor to compute and return the surface area
    def getSArea(self):
        return round(pi*self._radius * (self._radius + pow(pow(self._height,2)\
                                                + pow(self._radius,2),0.5)),2)

    #define a method to display the information on the cone
    def __str__(self):
        return str(self._name) + str(':') + '\nHeight: '\
               + str(format(self._height,'.2f')) + ' Radius: '\
               + str(format(self._radius,'.2f')) + 'ft, Surface area: '\
               + str(self.getSArea()) + 'sq ft\nRequired Paint: '\
               + str(super().getReqPaint()) +  ' litres, Paint Cost: $'\
               + str(super().getPaintCost())

#create objects to access the class
c1 = PaintCone('CONE1',10,10)
c2 = PaintCone('CONE2',12,4)

#display the processed information
print()
print(c1)
print()
print(c2)

#FIN
