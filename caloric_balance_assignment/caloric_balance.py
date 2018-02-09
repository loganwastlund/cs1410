

class CaloricBalance:

    def __init__(self, gender, age, height, weight):
        self.weight = weight
        bmr = self.getBMR(gender, age, height, weight)
        self.balance = bmr - (bmr * 2)

    def getBMR(self, gender, age, height, weight):
        bmr = 0.0
        if gender == 'm':
            bmr = 66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
        if gender == 'f':
            bmr = 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
        return bmr

    def getBalance(self):
        return self.balance

    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        calories_burned_per_minute = caloric_burn_per_pound_per_minute * self.weight
        calories_burned = float(calories_burned_per_minute) * float(minutes)
        self.balance -= calories_burned

    def eatFood(self, calories):
        self.balance += calories
