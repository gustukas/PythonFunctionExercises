class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"You have succesfully deposited {amount}, now your balance is {self.balance}.")
        else: print("Transaction failed.")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"You have succesfully withdrawn {amount}, now your balance is {self.balance}.")
        elif amount > self.balance:
            print("Not enough funds.")
        else: print("Transaction failed.")





account1 = Account("Jonas",500)

print(account1)
print(account1.owner)
print(account1.balance)
account1.withdraw()