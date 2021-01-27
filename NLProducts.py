##
#This program calculates price ish
#

#Set cost to produce per unit
ITEMA_COST = 25
ITEMB_COST = 55
ITEMC_COST = 100

#markup
MARKUPTEN = 1.1
MARKUPFIFTEEN = 1.15

#enter data
itemA_num = int(input('Please enter the number of ItemA sold: '))
itemB_num = int(input('Please enter the number of ItemB sold: '))
itemC_num = int(input('Please enter the number of ItemC sold: '))

#compute selling price
itemA_Price = ITEMA_COST * MARKUPTEN
itemB_Price = ITEMB_COST * MARKUPTEN
itemC_Price = ITEMC_COST * MARKUPFIFTEEN
#compute total cost to produce
total_Cost = (ITEMA_COST * itemA_num) + (ITEMB_COST * itemB_num) + (ITEMC_COST * itemC_num)
#compute total sales
total_Sales = (itemA_Price * itemA_num) + (itemB_Price * itemB_num) + (itemC_Price * itemC_num)
#compute profit
profit = total_Sales - total_Cost
#calculate percentage
total_Items = itemA_num + itemB_num + itemC_num
itemA_perc = itemA_num / total_Items * 100
itemB_perc = itemB_num / total_Items * 100
itemC_perc = itemC_num / total_Items * 100

#Display data
print('The selling price of ItemA is $', '%.2f' %itemA_Price)
print('The selling price of ItemB is $', '%.2f' %itemB_Price)
print('The selling price of ItemC is $', '%.2f' %itemC_Price)
print('Total Cost to Produce (all items sold) is $', '%.2f' %total_Cost)
print('Total Sales (all items sold) is $', '%.2f' %total_Sales)
print('Profit is $', '%.2f' %profit)
print('Percentage of ItemA sold is ', itemA_perc, '%')
print('Percentage of ItemB sold is ', itemB_perc, '%')
print('Percentage of ItemC sold is ', itemC_perc, '%')
