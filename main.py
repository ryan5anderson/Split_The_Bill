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
p2 = Person("Jack", 76.91, "electric")
p3 = Person("Riley", 202.85, "gas")
p4 = Person ("Ed",  0, "nothing")
p5 = Person("Ash", 135, "water")
p6 = Person("Wang", 0, "nothing")

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
        print(obj.name, " ", obj.price, "(", obj.item, ")")
    print("\n")    



#average out price for equall payment (sum / amount of people)
average_price = sum_prices() / len(OGlist)


print ("------money spent------")
print_list(OGlist)


#subtract each peoples price from average price, if negative means they must pay more
for obj in OGlist:
    obj.price -= average_price
    obj.price = round(obj.price, 2)
    
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
    owelist[i].price = round(owelist[i].price, 2)
    #needlist[i].price = round(needlist[i].price, 2)
    put_to_end_of_list(needlist, i)

#when person that owes equals the person who needs amount, so they both go to zero
def even_transaction(owelist, needlist, i):
    needlist[i].price -= needlist[i].price
    owelist[i].price -= owelist[i].price
    #owelist[i].price = round(owelist[i].price, 2)
    #needlist[i].price = round(needlist[i].price, 2)
    put_to_end_of_list(owelist, i)
    
#when person that owes pays all of their debt    
def owe_pays_all(owelist, needlist, i):
    needlist[i].price += owelist[i].price
    owelist[i].price -= owelist[i].price
    #owelist[i].price = round(owelist[i].price, 2)
    needlist[i].price = round(needlist[i].price, 2)
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
    transactoins = []
    done = False

    while sum_pricesV2() != 0.0:
        i = 0
        if abs(owesMoneyList[i].price) < needsMoneyList[i].price:
            string1 = (owesMoneyList[i].name +  " pay " + needsMoneyList[i].name + "  " + str(abs(owesMoneyList[i].price)) + "  " + "dollars")
            print(string1)
            transactoins.append(string1)
            owe_pays_all(owesMoneyList, needsMoneyList, i)
            print_both_MoneyLists()
            i += 1
            print("rest", sum_pricesV2())
        
        elif abs(owesMoneyList[i].price) > needsMoneyList[i].price:
            string2 = (owesMoneyList[i].name + " pay " + needsMoneyList[i].name + "  " + str(needsMoneyList[i].price) + "  " + "dollars")
            print(string2)
            transactoins.append(string2)
            owe_pays_not_all(owesMoneyList, needsMoneyList, i)
            print_both_MoneyLists()
            i += 1
            print("rest", sum_pricesV2())

        else:
            string3 = (owesMoneyList[i].name + " pay " + needsMoneyList[i].name + "  " + str(abs(owesMoneyList[i].price)) + "  " + "dollars")
            print(string3)
            transactoins.append(string3)
            even_transaction(owesMoneyList, needsMoneyList, i)
            print_both_MoneyLists()
            i += 1
            print("rest", sum_pricesV2())

        #user_i = input("are you done? (y/n)")
        #if user_i == "y":
            #done = True

        #if sum_pricesV2() == 0.0:
            #done = True
        
    print(*transactoins, sep = "\n")


comparebalanceV2()

print("all money was disbursted evenly, total:", sum_pricesV2())