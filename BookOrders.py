##
#Assignment 6 - BookOrders
#This program reads a text file, Books.txt, displays the information
#and writes the information into a new text file
#
#By Divine Ndaya Badibanga - 201765203
#

#define the recursive function that will read each line from the input file
def recurs(line, t):
    #base case to end function when line is empty and there is no more data
    if line == '':
        #print the total with appropriate labelling
        print('The total of all orders is: $%.2f' % t)
    #recursive case to print data and write new lines in the output file
    else:
        #remove \n from the lines
        line = line.rstrip()
        #split the content in each line into a list for easy access
        line = line.split(',')
        #assign separate values in the list to variables
        first = line[0]
        second = line[1]
        third = line[2]
        #calculate the total cost in each line
        total = float(second)*float(third)
        #print the data calculated from the input file
        print('%-15s $%-9s %-10s $%-9s' %\
              (first, second, third, format(total,'.2f')) )
        #write data onto the output file
        outfile.write(str(first) + str(',') + str(third) + str(',' )\
                      + str(total) + str('\n'))
        #move onto the next line
        line = infile.readline()
        #invoke the function again with an updated total and the next line
        return recurs(line, t= t + total)

#open the text files to read information from and write information to
try:
    #open the file named by the user to read data from
    infile = open(input("Enter filename: "), 'r')
    #open the output file to write into
    outfile = open("YourOrders.txt", 'w')
    #print appropriate headings for the data
    print( '%-15s %-10s %-10s %-10s' % ('ISBN', 'Cost', 'Copies', 'Total Cost'))
    #set a variable to keep track of the total
    t = 0
    #read the first line in the input file
    line = infile.readline()
    #invoke the function to read each line and process data
    recurs(line, t)
    #close both files after processing has been done
    infile.close()
    outfile.close()
#create an exception error
except IOError:
    #assign an error message
    print("Error: File not found.")

#FIN

