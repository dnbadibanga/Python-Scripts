##
#This program computes Marvin's coins
#

#Conversion Chart
TAR_TO_MAR = 4
CAR_TO_MAR = 2
PAR_TO_MAR = 24

#Input variables
Mar = int(input('Please enter the number of Maruvians: '))
Car = int(input('Please enter the number of Caruvians: '))
Tar = int(input('Please enter the number of Taruvians: '))
Par = int(input('Please enter the number of Paruvians: '))

#input friends
friends = int(input('Please enter the number of friends: '))
#include Marvin
shareHolders = friends + 1

#compute
total_Mar = Mar + (Car // CAR_TO_MAR) + (Tar // TAR_TO_MAR) + (Par // PAR_TO_MAR)
shared_Coins = total_Mar // shareHolders
rem_Mar = total_Mar % shareHolders
rem_Coins = (((Car % CAR_TO_MAR)*CAR_TO_MAR) + ((Tar % TAR_TO_MAR)*TAR_TO_MAR) + ((Par % PAR_TO_MAR)*PAR_TO_MAR)) // PAR_TO_MAR

#display output
print('Marvin has ', total_Mar, ' Maruvian(s) in total')
print('He gives ', shared_Coins, ' Maruvian(s) to himself and to each of his ', friends, ' friends.')
print('Marvin puts back ', rem_Mar, ' Maruvian(s) and ', rem_Coins, ' Paruvian(s) back in his jar.')
