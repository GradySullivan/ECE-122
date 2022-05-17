from Bank import BankAccount
import math

print("Welcome to App2\n===============")

balance,rate=input("Enter initial balance and interest rate for saving account: ").split() #user inputs values for balance and interest rate

balance=float(balance) #balance and rate turned to floats for calculations later
rate=float(rate)
years=0 #variable that eventually displays how many years to triple money

acc=BankAccount("saving",balance,rate) #create a BankAccount object with inputed values for balance and rate
print(str(acc),"\n")

print("How many years will it take to triple my balance?")
while acc.balance < (3*balance): #while balance is less than triple initial amount, do the following:
    acc.balance=acc.addcompound(acc.rate) #run addcompund function
    years=years+1 #tallies up years until initial amount is tripled

acc.balance=balance*math.pow(1+(rate/12),years*12) #calculates total amount given total number of years

print("You will triple your initial balance after ",years," years!")
print(str(acc),"\n") #displays balance and rate

acc.balance=balance
years=0 #reset variable for next calculation
while acc.balance < (3*balance): #while balance is less than triple initial amount, do the following:
    acc.balance=acc.addcompound(acc.rate) #run addcompund function
    acc.deposit(balance*.05) #add additional 5% of original balance every year
    years=years+1 #tallies up years until initial amount is tripled

print("Would this be better if I keep contributing 5% of my initial amount every year?")
print("You will triple your initial balance after ",years," years!")
print(str(acc),"\n") #displays balance and rate

acc.balance=balance
years=0
while acc.balance < (3*balance): #same as part 2 until next comment
    acc.balance=acc.addcompound(acc.rate)
    acc.deposit(balance*.05)
    years=years+1
    if acc.balance < (3*balance): 
        acc.rate=acc.rate*1.005 #multiplies rate by %0.05 until amount of money is tripled

print("Would this be even better if an addition my interest rate grows up by 0.5% every year?")
print("You will triple your initial balance after ",years," years!")
print(str(acc)) #displays balance and rate