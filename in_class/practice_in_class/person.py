class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def get_name(self):
        return self.name

    def get_ssn(self):
        return self.ssn

    def __str__(self):
        return f'Name: {self.name}, SSN: {self.ssn}'


p = Person('Joe', '222-22-2222')
p2 = Person('Jane', '111-11-1111')
