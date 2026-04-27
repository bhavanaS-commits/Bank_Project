'''
print("Welcome to SBI Bank")
print("1 : Check Your Balance")
print("2 : Deposit")
print("3 : Withdraw")
print("4 : Exit")
acc=5000
while True:
    ch=int(input("Enter What you want to do:"))
    if ch==1:
        print(f"The Balance in Your Account is {acc}")
    elif ch==2:
        damt=float(input("Enter the ammount to be Deposit:"))
        acc+=damt
        print(f"The Current Ammount in Your Account is {acc}")
    elif ch==3:
        wamt=float(input("Enter the ammount to be Withdraw:"))
        if acc>=5000:
            acc-=wamt
            print(f"The Current Ammount in Your Account is {acc}")
        else:
            print("Sorry! Unable to Withdraw as minimum Amount is Not Sufficient")
    elif ch==4:
        break
    else:
        print("Invalid Choice")
print("Thank You for visiting our Bank")
'''    

class Bank:
    def __init__(self):
        print("\n=====Welcome to SBI Bank=====")
        print("1 : Create Account")
        print("2 : Check Your Balance")
        print("3 : Deposit")
        print("4 : Withdraw")
        print("5 : Delete Account")
        print("6 : Exit")
    def create_Account(self,acc):
        global l
        self.acc=acc
        if self.acc not in l:
            l.append(self.acc)
            global amt
            while True:
                amt=float(input("Enter the Amount to Deposit in Account:"))
                if amt>=5000:
                    print("Account created Successful!!")
                    break
                else:
                    print("Insufficient Amount")
        else:
            print("Account Number is already Created")
    def check_Balance(self,acc):
        global amt
        self.acc=acc
        if self.acc in l:
            print(f"The Balance in Your Account is {amt}")
        else:
            print("Account Number Doesn't Exist")
    def deposit(self,acc,damt):
        global amt
        self.acc=acc
        self.damt=damt
        if self.acc in l:
            amt=amt+self.damt
            print(f"The Current Ammount in Your Account is {amt}")
        else:
            print("Account Number Doesn't Exist")
    def withdraw(self,acc,wamt):
        global amt
        self.acc=acc
        self.wamt=wamt
        if self.acc in l:
            if amt>5000:
                amt=amt-wamt
                print(f"The Current Ammount in Your Account is {amt}")
            else:
                print("Sorry! Unable to Withdraw as minimum Amount (Rs.5000) is Not Sufficient")
        else:
            print("Account Number Doesn't Exist")
    def delete(self,acc):
        self.acc=acc
        if self.acc in l:
            l.remove(self.acc)
            print("Account Deleted Successfully!!")
        else:
            print("Account Number Doesn't Exist")
l=[]
bank=Bank()
while True:
    ch=int(input("Enter What you want to do:"))
    if ch==1:
        acc=int(input("Enter Account Number to be Created:"))
        bank.create_Account(acc)
        continue
    if ch==2:
        acc=int(input("Enter Account Number to be Created:"))
        bank.check_Balance(acc)
        continue
    elif ch==3:
        acc=int(input("Enter Account Number to be Created:"))
        damt=float(input("Enter the ammount to be Deposit:"))
        bank.deposit(acc,damt)
        continue
    elif ch==4:
        acc=int(input("Enter Account Number to be Created:"))
        wamt=float(input("Enter the ammount to be Withdraw:"))
        bank.withdraw(acc,wamt)
        continue
    elif ch==5:
        acc=int(input("Enter Account Number to be Created:"))
        bank.delete(acc)
        continue
    elif ch==6:
        break
    else:
        print("Invalid Choice")
print("Thank You for visiting our Bank")
