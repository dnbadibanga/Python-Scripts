
thislist = [5, 2, 6, 9, 14, 5]

counter = 0
lowest = thislist[0]
highest = thislist[0]
while counter < len(thislist):
    if thislist[counter] <= lowest:
        lowest = thislist[counter]
    elif thislist[counter] >= highest:
        highest = thislist[counter]
    counter += 1

print(highest, lowest)
                         
