##
#Assignment 6 - Pattern.py
#This program creates a pattern of asterisks dependant on a number given
#by the user
#
#By Divine Ndaya Badibanga - 201765203
#

#define the recursive function that will write out a pattern
def repeat(a, b):
    #the base case that ensures the function ends once the pattern
    #is complete
    if abs(a) > b:
        return
    #the recursive case that continuously calls on the function
    #in order to print out the pattern
    else:
        #the condition statement the function follows to print out the
        #descending part of the pattern
        if a > 0:
            #print the number of asterisks, with each iteration, decrease
            #the number of asterisks printed
            print('*' * a)
            #call on the function again, with a decreased input number
            return repeat(a-1, b)
        #write the condition statement the function follows to print out the
        #ascending part of the pattern
        else:
            #print the number of asterisks, with each iteration, increase the
            #number of asterisks to be printed, using the absolute funtion
            #to print appropriately
            if a != 0:  
                print('*' * abs(a))
            #call on the function again, with a decreased input number
            return repeat(a-1, b)

#prompt the user for input regarding the size of the pattern to be printed
a = int(input('Please enter an integer value to start the pattern: '))
#invoke the function with the input given by the user
repeat(a, a)

#FIN


