##
#Assignment 5 - Medals.py
#
#This class defines an object with the name of a country and the number of
#gold, silver and bronze medals which that country won at the last Olympics.
#
#By Divine Ndaya Badibanga - 201765203
#

#define the Medals class
class Medals():
    #create a class variable to store the total number of medals
    allMedals = 0
    
    #define a constructor with default values for all instance variables
    def __init__(self, country='', gold=0, silver=0, bronze=0):
        #initialize all private instance variables
        self._name = country
        self._goldMedals = gold
        self._silverMedals = silver
        self._bronzeMedals = bronze
        #update the total medals won so far
        Medals.allMedals += gold + silver + bronze

    #define an accessor to return the name of the country
    def getName(self):
        return self._name

    #define an accessor to return the number of gold medals from each country
    def getGoldMedals(self):
        return self._goldMedals

    #define an accessor to return the number of silver medals from each country
    def getSilverMedals(self):
        return self._silverMedals

    #define an accessor to return the number of bronze medals from each country
    def getBronzeMedals(self):
        return self._bronzeMedals

    #define an accessor to return the total number of medals won
    def getMedals(self):
        return 'Total medals awarded: ' + str(Medals.allMedals)

    #define a mutator to add medals to countries
    def addMedals(self, gold=0, silver=0, bronze=0):
        self._goldMedals += gold
        self._silverMedals += silver
        self._bronzeMedals += bronze
        #update the total medals won so far
        Medals.allMedals += bronze + silver + gold

    #define an accessor to display the information for each country in an
    #appropriate manner
    def __str__(self):
        return 'Country: ' + str(self._name) + '\nGold : ' + \
               str(self._goldMedals) + ' Silver: ' + str(self._silverMedals)\
               + ' Bronze: ' + str(self._bronzeMedals)

#define the main function to access the class
def main():
    #create a list with the names of the countries
    countries = ['Canada', 'Sweden', 'Norway', 'Germany', 'France']
    #create objects to access the class with the countries
    country1 = Medals(str(countries[0]),6,8,10)
    country2 = Medals(str(countries[1]),7,6,1)
    country3 = Medals(str(countries[2]),14,14,11)
    country4 = Medals(str(countries[3]),14,10,7)
    country5 = Medals(str(countries[4]),5,4,6)

    #create an object to  access the total number of medals
    totalMedals = Medals()

    #display the processed information
    print(country1)
    print() #blank line
    print(country2)
    print() #blank line
    print(country3)
    print() #blank line
    print(country4)
    print() #blank line
    print(country5)
    print() #blank line
    print(totalMedals.getMedals())
    print() #blank line for formatting
    #add five medals to the first countriy's number of gold medals
    country1.addMedals(gold=5)
    #display the total number of medals
    print(country1)
    print() #blank line
    #display the total number of medals after updating one country's totals
    print(totalMedals.getMedals())

#invoke the main function  
main()

#FIN
