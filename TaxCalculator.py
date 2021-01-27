##
#This program calculates tax on products for you, instead of going to the
#register without knowing the total like an idiot
#
#By Divine Ndaya Mukengeshayi
#7/29/2018
#

#define the class that will calculate tax and add items to
#shopping list
class tax():
    #set tax percentage
    TAX = 1.15
    #create shopping list
    shoppingList = []
    #add your total
    checkout = 0

    #initialize variables
    def __init__(self, name, cost=0):
        self._n = name
        self._c = cost
        self._afterCost = 0

    def calcCost(self):
        self._afterCost = self._c * tax.TAX
        return self._afterCost

    def __str__(self):
        return str('Cost: ') + str(format(self.calcCost(),'.2f'))

    def shoppingCart(self, save='No'):
        if save == 'no' or save == 'No' or save == 'NO'\
                  or save == 'n':
            return
        elif save == 'y' or save == 'yes' or save == 'YES'\
                    or save == 'Yes':
            thisItem = [self._n, format(self._afterCost,'.2f')]
            tax.shoppingList.append(thisItem)
            tax.checkout = tax.checkout + self._afterCost

    def getList():
        print()
        print('Your shopping list: ')
        for eachItem in range(len(tax.shoppingList)):
            print('%-23s' %tax.shoppingList[eachItem][0], end='')
            print('$%5s' %tax.shoppingList[eachItem][1])
        print('------------------------------')
        print('Your total adds up to: $%5s' %(str(format(tax.checkout,'.2f'))))
        print()

def main():
    product = input('Enter product name: ')
    if product == 'list' or product == 'List' or product == 'LIST':
            tax.getList()
            main()
    elif len(product) > 1:
        productCost = float(input('Enter product cost: '))
        product1 = tax(product, productCost)
        print(product1)
        product1.shoppingCart(input('Save to shopping list? '))
        print()
        main()
    else: 
        tax.getList()

main()

    
