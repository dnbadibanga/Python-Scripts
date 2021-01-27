
array = [0, 1, 2, 3, 4, 5, 6, 8, 9]

counter = 0
lenlist = len(array)
while counter < lenlist:
    if counter not in array:
        print(counter)
        break
    else counter += 1
