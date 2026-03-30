import random
class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self._balance = balance 
        self._acc_number = random.randint(1000000000, 9999999999)
        self.transactions = []

    # deposit part 
    def deposit(self, amount):
        if amount <= 0:
            return "Amount should be positive."
        else:
            self._balance += amount
            self.transactions.append(f"+{amount} credited, balance is {self._balance}/-")
            return f"{amount} /- credited  to your account no. {self._acc_number}.(total balance is {self._balance})\nThank you !"
           
    # withdrawal part 
    def withdraw(self, amount):
        if amount <= 0:
            return "invalid"
        if amount > self._balance:
            return "Insufficient balance."
        else:
            self._balance -= amount
            self.transactions.append(f"-{amount} debited, balance is {self._balance}/-")
            return f"{amount} debited from your account no. {self._acc_number}.(total balance is {self._balance}/-).\nThank you!"
        
    # balance
    @property 
    def balance(self):
        return self._balance
    
    def transaction(self):
        print("----------------Transition history----------------\n")
        for i, items in enumerate(self.transactions, 1):
            print(f"{i}: {items}")
        print("--------------------------------------------------")

class SavingsAccount(BankAccount):
    def __init__(self, acc_holder, balance, interest_rate):
        super().__init__(acc_holder, balance)
        self.interest_rate = interest_rate

    @property
    def interest(self):
        return self._balance * (self.interest_rate / 100) # here interesst rate is of a year which is 5% 
    
    def interest_deposit(self):
        interest_amount = self.interest
        self._balance += interest_amount
        self.transactions.append(f"+{interest_amount} interest credited as interest of {self.interest_rate}% per year, balance is {self._balance}/-")
        return f"{interest_amount} credited as interest of {self.interest_rate}% per year to your account no. {self._acc_number}.(total balance is {self._balance}/-).\nThank you!"



        
# loop included in CLI part 


print("Welcome to the Bank made by Monu\n")
print("======Select your Account Type======")
print("1.Savings Account\n2.current Account\n")

acc_type = int(input("Enter your choice: "))
try:
    if acc_type == 1:
        acc = SavingsAccount("Monu",1000,5)
    elif acc_type == 2:
        acc = BankAccount("Monu", 1000)
    else:
        print("invalid input")
except:
    print("invalid input")

while True:
    print("====== BANK MENU ======")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Transaction History")
    print("5.Calculate Interest (Only for Savings Account)")
    print("6.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = int(input("enter amount: "))
        if amt <= 0:
            print("amount should be greater than 0")
        else:
            print(acc.deposit(amt))
    elif choice == 2:
        amt = int(input("enter amount: "))
        if amt <= 0:
            print("amount should be greater than 0")
        else:
            print(acc.withdraw(amt))
    elif choice == 3:
        print(f"Your current balance is: {acc.balance}/-")
    
    elif choice == 4:
        acc.transaction()
        
    elif choice == "5" and isinstance(acc, SavingsAccount):
        print(acc.interest_deposit())
    
    elif choice == 6:
        print("Thank you for using our services!")
        break
    
        
    

    

    

    





