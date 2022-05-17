from Bank import BankAccount

print("Welcome to App3\n===============")

borrow, rate, month_pay = input("Enter amount to borrow, rate, and monthly payment: ").split() #user input for variables stated 
print("Mortgage balance",borrow)

borrow=float(borrow) #following variables changed to float for convenience
rate=float(rate)
month_pay=float(month_pay)

acc=BankAccount("saving",borrow,rate) #create new BankACcount object
balance=acc.balance #set variable balance to value inputted
months=0
int_rate=0
paid=0
added_rate=0

f1=open("Amortization.txt",'w') #opens file
f1.write("Month--Principal paid--Interest paid \n") #writes string in file

while acc.balance > 0: #the following is done until user pays off mortgage (mortgage <= 0)
    int_rate=(acc.balance*(rate/12)) #formula for interest rate
    added_rate=added_rate+int_rate
    paid=(month_pay-int_rate)+paid
    acc.balance=acc.balance+acc.balance*(rate/12)
    acc.withdraw(month_pay,False,rate) #withdraws amount calculated --> lowers amount owed
    months=months+1 #tallies up number of months
    f1.write(str(months) + "--") #writes the following string into Amortization.txt 
    f1.write(str(paid) + "--")
    f1.write(str(added_rate) + "\n")

f1.close()
   
years=months/12 #calculates years given months
paid=month_pay*months #calculates total amount paid

print("You will be paying your loan after",months,"month! (or",years,"years!)")
print("You borrowed $",borrow," but paid $",paid," (with interests)")