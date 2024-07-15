class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount should be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Withdrawal amount should be greater than zero and less than or equal to balance.")
    
    def get_balance(self):
        return self.balance

# Example usage:
# Creating an instance of BankAccount
accountno=int(input("enter the account no="))
name=input("enter the name of account holder=")
account1 = BankAccount(accountno,name)

# Depositing money
account1.deposit(1000.0)

# Withdrawing money
account1.withdraw(500.0)

# Getting the current balance
print(f"Current balance: ${account1.get_balance()}")
