##This program sorts a text file of countries by their country code using radix sort

#create a method for Radix sort
"""I used a user-define method, not a class as I'm not very comfortable with classes. 
I hope that's okay"""
def RadixSort(filename):
    #open the file
    fil = open(filename, 'r')
    f1 = fil.readlines()

    #create parameters
    asc = 65
    alphabet = 26

    #create 3 bucket lists, one for each character in the country code
    def buckets(lis, index):
        #sort by the third character
        buckets = [[] for _ in range(alphabet)]
        for line in range(len(lis)):
            char = ord(lis[line][index]) - asc
            buckets[char].append(lis[line])
     
        #sort by the second character
        buckets2 = [[] for i in range(alphabet)]
        for i in range(len(buckets)):
            for j in range(len(buckets[i])):
                char = ord(buckets[i][j][index-1]) - asc
                buckets2[char].append(buckets[i][j])

        #sort by the third character
        buckets3 = [[] for _ in range(alphabet)]
        for i in range(len(buckets2)):
            for j in range(len(buckets2[i])):
                char = ord(buckets2[i][j][index-2]) - asc
                buckets3[char].append(buckets2[i][j])

        #write the sorted list in a new text file
        f = open("countries_sorted.txt", "w+")
        for i in range(len(buckets3)):
            for j in range(len(buckets3[i])):
                f.write(buckets3[i][j])

        #close the files
        fil.close()
        f.close()

    #call the method
    here = 2
    buckets(f1, here)

#call the method
m = RadixSort('country.txt')

#check her
OG = open('country.txt', 'r')
copy = open('countries_sorted.txt', 'r')
OG = OG.readlines()
copy = copy.readlines()
for i in range(len(OG)):
    if OG[i] != copy[i]:
        x = False
    else:
        x = True
if x == True:
    print("You messed up")
else:
    print("Stephen Anthony could never")



