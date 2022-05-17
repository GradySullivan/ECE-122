import math

class BankAccount: #creates BankAccount Class

    def __init__(self,name=None,balance=None,rate=None):
        self.name=name #instance variables created
        self.balance=balance
        self.rate=rate
        
    def deposit(self,amount=None,recorded=False,rate=None): #amount is how much is added, recorded determines if info will display 

        self.balance=self.balance+amount #add amount to account
        if recorded is True:
            print("Checking deposit requested " + str(amount)) #displays amount requested
            print("\tNew Checking balance " + str(self.balance)) #displays amount after transaction
            return amount
        else:
            return self.balance #no info displayed on screen
        
    def withdraw(self,amount,recorded=False,rate=None): #amount is how much is removed, recorded determines if info will display
        self.balance=self.balance-amount #subtract amount from account
        if recorded is True:
            print("Checking withdrawal requested " + str(amount)) #displays amount requested for withdrawal
            if self.balance >= 0: #if amount requested is less than amount in account
                print("\tNew Checking balance " + str(self.balance)) #displays amount after transaction
            else: #if amount requested is more than the contents of the account
                self.balance=self.balance+amount
                print("\tSorry your withdrawal is limited to " + str(self.balance))
                self.balance=0
        else:
            return self.balance #no info displayed on screen
    
    def addcompound(self,rate=None):
       self.balance=(self.balance*math.pow(1+rate/12,12)) #equation for compound interest
       return self.balance
        
        
    def __str__(self): #for printing "Checking balance"
        if self.rate is None:
            return "Checking balance %s" % (self.balance)
        else:
            return "Saving balance %s" % str(self.balance) + "; rate %s" % str(self.rate) #runs if rate is given
    
    @staticmethod
    def main():
        #create a bank account named checking with $1000
        acc1=BankAccount("checking",1000)
        #print info about its balance
        print(acc1)
        #deposit $250
        acc1.deposit(250)
        #deposit again $250 but record the transaction (i.e print some info)
        acc1.deposit(250,True)
        #withdraw $700 and record the transaction
        acc1.withdraw(700,True)
        #try to withdraw $850
        acc1.withdraw(850,True)
        #print new info about its balance
        print(acc1)
    
if __name__ == "__main__": #executes if condition is met
    BankAccount().main()