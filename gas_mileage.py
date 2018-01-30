import sys


def milesPerGallon(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons


def createNotebook():
    return list()


def recordTrip(notebook, date, miles, gallons):
    tripdata = dict()
    tripdata["date"] = date
    tripdata["miles"] = miles
    tripdata["gallons"] = gallons
    notebook.append(tripdata)
    return notebook


def listTrips(notebook):
    trips = []
    for note in notebook:
        trip = "On {0}: {1} miles traveled using {2} gallons. Gas mileage: {3} MPG"\
            .format(note["date"], note["miles"], note["gallons"], milesPerGallon(note["miles"], note["gallons"]))
        trips.append(trip)
    return trips


def calculateMPG(notebook):
    if len(notebook) == 0:
        return 0.0
    else:
        miles = 0
        gallons = 0
        for note in notebook:
            miles += note["miles"]
            gallons += note["gallons"]
    return milesPerGallon(miles, gallons)


def formatMenu():
    return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History',
            '[c] Calculate Gas Mileage', '[q] Quit']


def formatMenuPrompt():
    return 'Enter an option: '


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
            if floatResponse > 0:
                keepLooping = False
        except ValueError:
            continue
    # while float(response) <= 0:
    #     notyet = True
    #     while notyet:
    #         response = input(prompt)
    #         try:
    #             float(response)
    #             notyet = False
    #         except ValueError:
    #             notyet = True
    # return float(response)
    # my first attempt or second
    return floatResponse


def getDate():
    response = getUserString("What is the date? ")
    return response


def getMiles():
    response = getUserFloat("How many miles did you drive since last filling up? ")
    return response


def getGallons():
    response = getUserFloat("How many gallons of gas did you add to your tank? ")
    return response


def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print("Saved!")


def listTripsAction(notebook):
    trips = listTrips(notebook)
    if len(trips) == 0:
        print("You first need to record your gas consumption! ")
    else:
        for trip in trips:
            print(trip)


def calculateMPGAction(notebook):
    mpg = calculateMPG(notebook)
    if mpg == 0.0:
        print("You first need to record your gas consumption! ")
    else:
        print(f"Average gas mileage: {mpg} MPG")


def quitAction(notebook):
    print("Bye! See you next time! ")
    sys.exit(0)


def applyAction(notebook, action):
    if action == "r":
        recordTripAction(notebook)
    elif action == "l":
        listTripsAction(notebook)
    elif action == "c":
        calculateMPGAction(notebook)
    elif action == "q":
        quitAction(notebook)
    else:
        print("Sorry, that action is invalid. ")


def main():
    notebook = createNotebook()
    useroption = "hehe"
    while useroption != "q":
        menu = formatMenu()
        for option in menu:
            print(option)
        useroption = input(formatMenuPrompt())
        applyAction(notebook, useroption)
        print()


if __name__ == '__main__':
    main()
