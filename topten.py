
array = [5, 4, 2, 87, 54, 25, 65, 35, 47, 81, 52, 59, 22, 14, 87, 47, 47]

tenlist = []

for i in range(0, 10):
    tenlist.append(max(array))
    array.remove(max(array))
print(tenlist)
