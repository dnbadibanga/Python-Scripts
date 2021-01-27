
class family():
    lname = 'Mukengeshayi'

    def __init__(self, fname, age, sex):
        self.name = fname
        self.age = age
        self.sex = sex

    def getName(self):
        return self.name + self.lname

    def setName(self, fname, lname):
        self.name = fname
        self.lname = family().lname

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getSex(self):
        return self.sex

    def setSex(self, sex):
        self.sex = sex

    def __str__(self):
        return 'Name: ' + str(self.name)+str(' ') + str(family.lname) + '\nAge: ' + str(self.age)\
               + str(' Sex: ') + str(self.sex)

dad = family('William', 55, 'M')
mom = family('Wilma', 54, 'F')
firstborn = family('Jackie-Anne', 22, 'F')
secondborn = family('Kenya', 19, 'F')

print(dad)
print(mom)
mom.setName('Wilma','Gerara')
print(mom.getName)
print(firstborn)
print(secondborn)
