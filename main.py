from operator import ne
import django
from pickle import OBJ
import random

import tabulate
# creating class for person entry



class Person:
    def __init__ (self, name,  price, item):
        self.name = name
        self.price = price
        self.item = item

#adding values to people objects
p1 = Person("Ryan",  86, "wifi")
p2 = Person("Jack", 155, "water")
p3 = Person("Riley", 50, "gas")
p4 = Person ("Ed",  0, "nothing")
p5 = Person("Ash", 0, "nothing")
p6 = Person("Wang", 0, "nothin")

#creating list of people objects
OGlist = [p1, p2, p3, p4, p5, p6]


#Sum totall amount of prices
def sum_prices():
    sum_price = 0
    for obj in OGlist:
        sum_price += abs(obj.price)
    print("total:", sum_price)
    return sum_price
#prints list
def print_list(generalList):
    for obj in generalList:   
        print(obj.name, " ", obj.price)
    print("\n")    



#average out price for equall payment (sum / amount of people)
average_price = sum_prices() / len(OGlist)

print ("------money spent------")
print_list(OGlist)


#subtract each peoples price from average price, if negative means they must pay more
for obj in OGlist:
    obj.price -= average_price 
    
#sort list by price high to low
OGlist.sort(key=lambda x: x.price, reverse=True)
print ("-----money after subtracting average price: ", average_price, "-----")
print_list(OGlist)
owesMoneyList = []
needsMoneyList = []

#putting people into correct lists 
for obj in OGlist:
    if obj.price < 0:
        owesMoneyList.append(Person(obj.name, obj.price, obj.item))
    else:
        needsMoneyList.append(Person(obj.name, obj.price, obj.item))

#sorting list
owesMoneyList.sort(key=lambda x: x.price, reverse=False)
needsMoneyList.sort(key=lambda x: x.price, reverse=True)

#sum up prices of owe and need lists
def sum_pricesV2():
    sum_price = 0
    for obj in needsMoneyList:
        sum_price += abs(obj.price)
    for obj in owesMoneyList:
        sum_price += abs(obj.price)
    return sum_price


print("people that owe money")
print_list(owesMoneyList)
print("people that need money")
print_list(needsMoneyList)

        



#when person that owes pays some of their debt
def owe_pays_not_all(owelist, needlist, i):
    owelist[i].price += needlist[i].price
    needlist[i].price -= needlist[i].price
    put_to_end_of_list(needlist, i)

#when person that owes equals the person who needs amount, so they both go to zero
def even_transaction(owelist, needlist, i):
    needlist[i].price -= needlist[i].price
    owelist[i].price -= owelist[i].price
    put_to_end_of_list(owelist, i)
    
#when person that owes pays all of their debt    
def owe_pays_all(owelist, needlist, i):
    needlist[i].price += owelist[i].price
    owelist[i].price -= owelist[i].price
    put_to_end_of_list(owelist, i)


#moves person to end of list after their balance is zero
def put_to_end_of_list(list, i):
    list.append(list.pop(list.index(list[i])))  

#prints both moneylists
def print_both_MoneyLists():
    print("people that owe money")
    print_list(owesMoneyList)
    print("people that need money")
    print_list(needsMoneyList)

#transaction magic below
def comparebalanceV2():

    while sum_pricesV2() != 0:
        i = 0
        if abs(owesMoneyList[i].price) < needsMoneyList[i].price:
            print(owesMoneyList[i].name,  "paid" , needsMoneyList[i].name, abs(owesMoneyList[i].price), "dollars\n")
            owe_pays_all(owesMoneyList, needsMoneyList, i)
            print_both_MoneyLists()
            i += 1
        
        
        elif abs(owesMoneyList[i].price) > needsMoneyList[i].price:
            print(owesMoneyList[i].name,  "paid" , needsMoneyList[i].name, needsMoneyList[i].price, "dollars\n")
            owe_pays_not_all(owesMoneyList, needsMoneyList, i)
            print_both_MoneyLists()
            i += 1

        else:
            print(owesMoneyList[i].name,  "paid" , needsMoneyList[i].name, abs(owesMoneyList[i].price), "dollars\n")
            even_transaction(owesMoneyList, needsMoneyList, i)
            print_both_MoneyLists()
            i += 1


comparebalanceV2()



print("all money was disbursted evenly, total:", sum_pricesV2())
