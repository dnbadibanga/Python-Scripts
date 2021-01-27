f = open('thenames.txt', 'r')
f1 = f.readlines()
for i in range(25):
    word = f1[i]
    print(word.replace('\n',''))

