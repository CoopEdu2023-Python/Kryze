class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def deposit(self):
        self.balance += self.interest_rate


