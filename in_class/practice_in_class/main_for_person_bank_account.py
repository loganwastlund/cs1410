import person
from bank_account import BankAccount

joe = person.Person('Joe', '222-22-2222')
print(joe)
account = BankAccount(joe, 1200)
print(account.get_balance())
print(account)
