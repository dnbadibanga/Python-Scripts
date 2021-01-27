##
#Assignment 6 - RecurFrequency.py
#This program counts the number of times a certain integer, determined by the
#user, occurs in a randomly generated list
#
#By Divine Ndaya Badibanga - 201765203
#

#set the lcv
#i, to keep track of the numbers in the list
i = 0
#count, to store the frequency of a given number
count = 0

#import random function to generate list of ten random integers
import random
#define the function that will generate the list of twenty random numbers
def createList():
    #create an empty list
    listONumbers = []
    #generate a list of twenty random numbers and store in the list created
    for integer in range(20):  
        listONumbers.append(random.randint(1,10))
    return listONumbers

#define the recursive function that will count the number of times a given
#number, theNumber, appears in the randomly generated list
def frequency(theNumber, count, i, aList):
    #base case that will end the recursive function once all twenty numbers
    #have been looked over
    if i == 20:
        #print the list of twenty numbers
        print('The list of random numbers is: \n', aList)
        print()
        #print the number of times a given number, theNumber,
        #occurs in the list
        print(theNumber, ' occurs ', count, ' times in the given list.')
    #recursive case to look over and count the frequency of theNumber
    else:
        #update the count if the item accessed in the list is equal
        #to theNumber
        if aList[i] == theNumber:
            #invoke the function to repeat with the next item in the list
            return frequency(theNumber, count+1, i+1, aList)
        #invoke the function to repeat without updating the count if the item
        #is not equal to theNumber, with the next item in the list
        else:
            return frequency(theNumber, count, i+1, aList)

#define the function that will prompt the user for the number they want
#the frequency of and will call the two previously defined functions
def main():
    theNumber = int(input('Enter an integer (1 to 10) to count its frquency in a '\
                  'random list: '))
    print() #blank line
    #invoke the functions to compute the frequency
    listONumbers = createList()
    frequency(theNumber, count, i, listONumbers)
    
#invoke the main function
main()    

#FIN
