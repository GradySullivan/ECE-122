from Bank import BankAccount

print("Welcome to App1\n===============")

salary,check_initial,save_initial = input("Enter salary and initial balances for Checking and Saving accounts: ").split() #set values for salary and initial balances
print("Checking balance " + str(check_initial)) #print initial checking balance
print("Saving balance " + str(save_initial)) #print initial saving balance
print("Month--salary-expense--saving")

check_bal=0 #create variables for equations
save_bal=0
check_final=float(0)
checking_final=check_initial
save_final=save_initial

for i in range (1,13): #does the following 12 times (for 12 months in a year)
    check_bal=float(salary)*0.8 #80% goes to expenses
    save_bal=float(salary)*0.15 #15% goes to savings
    check=BankAccount("checking",check_bal)
    save=BankAccount("saving",save_bal)
    checking_final=float(checking_final)+(float(salary)-float(check.balance)-float(save.balance))
    print(str(i)+"--"+str(int(salary))+"--"+str(int(check.balance))+"--"+str(int(save.balance))) #prints Month, salary, expenses, and saving per month
    salary=float(salary)*1.002 #equation for salary raise each month
    save_final=float(save_final)+float(save_bal)

check_final=check_final+float(check_bal)    
print("Checking balance " + str(checking_final)) #print final checking balance
print("Saving balance " + str(save_final)) #print final saving balance