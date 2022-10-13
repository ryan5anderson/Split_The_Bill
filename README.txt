The program I made takes in a group bill, a total amount that must be paid by a certain number of people in the large transaction. 
The program takes in input of what which user has paid towards the total amount. Computation commensises and prompts which user what to pay who in the cleanest fashion. 
This could be a feature popular among young adults who usually split large transactions among a group. Image you are living with 6 people, some of which pay for utilities 
some of which do not. However the ulitiy bill must eventually be paid eventually among all 6. The program takes the people who have paid a bill and the people who have not 
paid the bill and splits the price eventually in the quickest way possible. Say this is a feature integrated into an app like venmo or cash app. Someone would start a group 
transaction, they would invite others. The person who started would be able to enter all the amouns for all the users or have the option to let the other users enter there 
own amounts. Then the program would run and each user would be prompted with a screen on the breakdown of the transaction and what amount of money to pay who, as well as a 
“send now” button that will automatically send the amount owed to whoever needed money back. 

My next goal for this program is too refactor the code and make it look a lot better, add functions to reduce repetition, add a main function, allow for user input, etc. 

After this is done I will be using pyscript with html and css framework (if possibly paired with a react framework)  to create an interactive web app that allows as a 
demo for what could be a feature in a main stream transaction based App (venmo, cash app)



to start server- "python3 -m http.server 880"



def transaction1(i):
    OGlist[i].price -= abs(OGlist[i+1].price)
    print(OGlist[i+1].name, "paid",  OGlist[i].name, abs(OGlist[i+1].price), "dollars")
    OGlist[i+1].price -= OGlist[i+1].price
    print(OGlist[i+1].name, "now owes", OGlist[i+1].price, "dollars")
    print(OGlist[i].name,"now needs", OGlist[i].price, "dollars")
    OGlist.append(OGlist.pop(OGlist.index(OGlist[i+1])))

def transaction2(i):
    OGlist[i+1].price = OGlist[i+1].price + OGlist[i].price
    print(OGlist[i+1].name, "paid",  OGlist[i].name, OGlist[i].price, "dollars")
    OGlist[i].price -= OGlist[i].price
    print(OGlist[i+1].name, "now owes", OGlist[i+1].price, "dollars")
    print(OGlist[i].name,"now needs", OGlist[i].price, "dollars")
    OGlist.append(OGlist.pop(OGlist.index(OGlist[i+1])))



def comparebalance():
    i = 0
    if abs(OGlist[i].price) == abs(OGlist[i+1].price):
  
        if OGlist[i].price > 0:
            transaction1(i)
            print("transaction1, abs(0) == abs(1) && [0] > 0\n")
            print_list(OGlist)
            
        
        else: 
            OGlist[i], OGlist[i+1] = OGlist[i+1], OGlist[i]   
            transaction1(i)
            print("transaction1, abs(0) == abs(1) && [0] =< 0\n")
            print_list(OGlist)
            
    else:    
        if OGlist[i].price > 0 and OGlist[i+1].price > 0:
            OGlist.append(OGlist.pop(OGlist.index(OGlist[i+1])))
            print("^resorted^ \n")
            print_list(OGlist)
        
        elif OGlist[i].price > OGlist[i+1].price:
            transaction1(i)
            print("transaction1, 0 > 1\n")
            print_list(OGlist)
        
        elif OGlist[i].price < OGlist[i+1].price:
            transaction2(i)
            print("transaction2, 0 < 1\n")
            print_list(OGlist)
        