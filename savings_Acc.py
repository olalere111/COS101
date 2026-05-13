from Account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.withdraw_limit = 100

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal denied! Limit is ${self.withdraw_limit}")
        else:
            super().withdraw(amount)


print("--- Savings Account ---")

savings = SavingsAccount("Alice", 1000)

savings.withdraw(50)
savings.withdraw(150)

print("Current Balance:", savings.get_balance())