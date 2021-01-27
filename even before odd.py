numbers = [5, 4, 21, 15, 18, 16, 9, 8, 7, 1, 6, 3, 2, 88]
numbers = [1, 5, 8, 7, 6, 4, 2, 1, 3, 9]
length = len(numbers)

for i in range(0, length):
    if numbers[i] % 2 == 0:
        hold = numbers[i]
        numbers.remove(hold)
        numbers.insert(0, hold)

print(numbers)
