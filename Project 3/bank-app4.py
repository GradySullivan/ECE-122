print("Welcome to App4\n===============\n")
print("Ok I load your expenses from expense.txt\nI have created the budget file budget.txt")

f1 = open("expenses.txt","r") #open expenses.txt to read
f2 = open("budget.txt","w") #open budget.txt to write
f3 = open("budget-sorted.txt","w")

expenses = {} #create dictionary
total = 0

for line in f1: #do the following for each line in expenses
    expense,price=line.split() #split the string
    total += float(price) #add individual price to the total price
    if expense in expenses.keys():
        expenses.update({expense:float(price)+expenses.get(expense)}) #if expense name is already in the dictionary, update it instead of adding new entry 
    else:
        expenses.update({expense:float(price)})

for key in expenses.keys():
    f2.write(key+"--"+str(expenses.get(key))+"\n") #write costs in budget.txt
f2.write("Total--%.1f" % total) #writes total cost (rounded to tenths place)

#Bonus#

# convert the dict to a list to sort
expenseList = [] #make a list
for key in expenses.keys(): #iterating through the dict and add what we see to the list
    expenseList.append((key,expenses.get(key)));
expenseList = sorted(expenseList, key=lambda x: -x[1]) # now that we have the list version, we sort it in place
for item in expenseList: # write to file
    f3.write("%s--%.1f\n" % (item[0], item[1]))
f3.write("Total--%.1f" % total)