class BankAccount:
    def __init__(self, person, balacne):
        self.owner = person
        self.balance = float(balacne)

    def get_balance(self):
        return '$' + str(self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return str(self.owner) + f', Balance: ${str(round(self.get_balance(), 2))}'
