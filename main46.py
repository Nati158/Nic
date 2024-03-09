class BankAccount:
    def init(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance for {self.name}: ${self.balance}")


# Example usage:
account1 = BankAccount("Alice", 100)
account1.check_balance()
account1.deposit(50)
account1.withdraw(30)
account1.check_balance()