class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        print(f"The total balance in the account is {self.balance}")
        self.balance = int(self.balance)+amount
        print(f"{self.account_holder} now has {self.balance}")

    def withdraw(self,amount):
        self.balance = int(self.balance)-amount
        print(f"{self.account_holder} now has {self.balance}")

bankaccount1 = BankAccount("Ruthwik",500)
bankaccount1.deposit(1000)

bankaccount2 = BankAccount("Ruthwik",500)
bankaccount2.withdraw(200)