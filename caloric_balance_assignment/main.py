import sys
from caloric_balance import CaloricBalance


def formatMenu():
    return ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']


def formatMenuPrompt():
    return 'Enter an option: '


def formatActivityMenu():
    return ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']


def getUserString(prompt):
    response = ""
    while len(response) == 0:
        response = input(prompt)
        response = response.strip()
    return response


def getUserFloat(prompt):
    keepLooping = True
    while keepLooping:
        response = input(prompt)
        try:
            floatResponse = float(response)
            if floatResponse <= 0:
                print("Please enter a number greater than zero.")
            else:
                keepLooping = False
        except ValueError:
            print("Please enter a number.")
            continue
    return floatResponse


def createCaloricBalance():
    gender = getUserString('What is your gender (f or m)? ')
    age = getUserFloat('What is your age? ')
    height = getUserFloat('What is your height in inches? ')
    weight = getUserFloat('What is your weight in pounds? ')
    caloricbalance = CaloricBalance(gender, age, height, weight)
    return caloricbalance


def recordActivityAction(caloricbalance):
    for string in formatActivityMenu():
        print(string)
    activities = {'j': .074, 'r': .087, 's': .009, 'w': .036}
    activity = input(formatMenuPrompt())
    if activity in activities:
        minutes = getUserFloat("For how many minutes did you perform this activity? ")
        for key in activities:
            if activity == key:
                cpm = activities[key]
        caloricbalance.recordActivity(cpm, minutes)
        print(f"Awesome! Your caloric balance is now {caloricbalance.getBalance()}")
    else:
        print("Sorry, that option is invalid. ")


def eatFoodAction(caloricbalance):
    calories = getUserFloat("Okay! How many calories did you just eat? ")
    caloricbalance.eatFood(calories)
    print(f"Sweet! Your caloric balance is now {caloricbalance.getBalance()}")


def quitAction(caloricbalance):
    print("Leaving? You should do this again tomorrow. Stay healthy!")
    sys.exit(0)


def applyAction(caloricbalance, action):
    if action == 'f':
        eatFoodAction(caloricbalance)
    elif action == 'a':
        recordActivityAction(caloricbalance)
    elif action == 'q':
        quitAction(caloricbalance)
    else:
        print("Sorry, that option is invalid.")


def main():
    caloricbalance = createCaloricBalance()
    print()
    action = 'hello'
    while action != 'q':
        for string in formatMenu():
            print(string)
        action = input(formatMenuPrompt())
        applyAction(caloricbalance, action)
        print()


if __name__ == '__main__':
    main()
