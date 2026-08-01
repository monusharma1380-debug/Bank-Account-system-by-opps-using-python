import random
from abc import ABC, abstractmethod


class Bank_Account(ABC):
    def __init__(self, account_holder, branch, balance):
        self.acc_holder = account_holder
        self.branch = branch
        self.__account_number = random.randint(10000000000, 99999999999)
        self.__balance = balance
        self.transactions = []

    @property
    def balance(self):
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.__balance += amount
            self.transactions.append(f"Deposited: {amount}, balance: {self.__balance}")
            print(f"Dear customer,\nYour account has been credited with {amount}.\nYour balance is {self.__balance}.\nThank you.")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.__balance:
                raise ValueError("Insufficient funds for this withdrawal.")
            self.__balance -= amount
            self.transactions.append(f"Withdrew: {amount}, balance: {self.__balance}")
            print(f"Dear customer,\nYour account has been debited with {amount}.\nYour balance is {self.__balance}.\nThank you.")
        except ValueError as e:
            print(e)

    def transaction_history(self):
        print("=" * 50 + "Transaction History for Account Holder" + "=" * 50)
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction}")
        print(f"\nCurrent balance: {self.__balance}")
        self.extra_info()
        print("=" * 50 + "THANK YOU" + "=" * 50)

    def extra_info(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass


class Savings_Account(Bank_Account):
    def __init__(self, account_holder, branch, balance):
        super().__init__(account_holder, branch, balance)
        self.__interest_rate = 0.04

    def calculate_interest(self):
        interest = self.balance * self.__interest_rate
        self._Bank_Account__balance += interest
        self.transactions.append(f"Interest added: {interest}, balance: {self.balance}")
        print(f"Dear customer,\nInterest has been added to your account.\nYour new balance is {self.balance}.\nThank you.")

    def minimum_balance(self):
        if self.balance < 1000:
            penalty = self.balance * 0.05
            self._Bank_Account__balance -= penalty
            self.transactions.append(f"Minimum balance penalty applied: {penalty}, balance: {self.balance}")
            print(f"Dear customer,\nA minimum balance penalty has been applied to your account.\nYour new balance is {self.balance}.\nThank you.")
        print(f"Dear customer,\nYour current balance is {self.balance}.\nThank you.")

    def extra_info(self):
        print(f"Interest rate: {self.__interest_rate}")


class Current_Account(Bank_Account):
    def __init__(self, account_holder, branch, balance):
        super().__init__(account_holder, branch, balance)
        self.__overdraft_limit = 5000

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > (self.balance + self.__overdraft_limit):
                raise ValueError("Insufficient funds for this withdrawal, including overdraft limit.")
            self._Bank_Account__balance -= amount
            self.transactions.append(f"Withdrew: {amount}, balance: {self.balance}")
            print(f"Dear customer,\nYour account has been debited with {amount}.\nYour balance is {self.balance}.\nThank you.")
        except ValueError as e:
            print(e)




    def extra_info(self):
        print(f"Overdraft limit: {self.__overdraft_limit}")


def savings_menu(account):
    while True:
        print("=" * 50 + "BANK ACCOUNT MANAGEMENT SYSTEM" + "=" * 50)
        print("select option to continue:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Calculate Interest")
        print("5. Check minimum Balance Penalty")
        print("6. Transaction History")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            amount = int(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = int(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Your current balance is: {account.balance}")
        elif choice == "4":
            account.calculate_interest()
        elif choice == "5":
            account.minimum_balance()
        elif choice == "6":
            account.transaction_history()
        elif choice == "7":
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def current_menu(account):
    while True:
        print("=" * 50 + "BANK ACCOUNT MANAGEMENT SYSTEM" + "=" * 50)
        print("select option to continue:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            amount = int(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = int(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            print(f"Your current balance is: {account.balance}")
        elif choice == "4":
            account.transaction_history()
        elif choice == "5":
            print("Thank you for using the Bank Account Management System. Goodbye!\nHave a Nice Day!")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    print("Welcome to the Bank Account Management System made by Monu")
    print("Kindly select the type of account you want to create:")
    print("1. Savings Account")
    print("2. Current Account")

    acc_type = input("Enter your choice (1 / 2): ")

    if acc_type == "1":
        account_holder = input("Enter your name: ")
        branch = input("Enter your branch: ")
        balance = 1000
        savings_account = Savings_Account(account_holder, branch, balance)
        print(f"\nDear {account_holder}, your Savings Account has been created ({savings_account.account_number}) with an initial balance of {balance}.")
        savings_menu(savings_account)

    elif acc_type == "2":
        account_holder = input("Enter your name: ")
        branch = input("Enter your branch: ")
        balance = 0
        current_account = Current_Account(account_holder, branch, balance)
        print(f"Dear {account_holder}, your Current Account has been created ({current_account.account_number}) with an initial balance of {balance}.")
        current_menu(current_account)

    else:
        print("Invalid choice. Please restart and select 1 or 2.")


if __name__ == "__main__":
    main()
