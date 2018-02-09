# dictionaries

d = {'key': 'value', 'name': 'Logan', 'id': 123, 'backpack': ['pencil', 'pen', 'pen', 'paper']}
d['name'] = 'John'
# how to update a key ^
d['dob'] = '01-17-18'
d['dob'] = '01-18-18'

# keys can be integers, strings, variables, but not lists. The value can be anything

print(d['backpack'][2])

# prints second pen ^
# if key in dictionary:
# how to check if key is in dictionary


# for key in dictionary:
# value = dictionary[key]
# if value == 'value':
# how to find a value in a dictionary
# del d['key']
# how to delete a key ^




# classes

# Classes:
# have abilities
# and traits

# a marker has:
# color
# erasable
# capacity
# tip size
# write

# use "class {name}:"
# Pascal Case
# StudlyCaps


class Marker:

    def __init__(self):
        self.color = (0, 0, 255)
        self.erasable = True
        self.capacity = 5
        self.tipsize = 0.001

    def write(self, length):
        self.capacity -= self.tipsize * abs(length)

    def show(self):
        print(self.color, self.erasable, self.capacity, self.tipsize)


redexpo1 = Marker()
redexpo1.color = (255, 0, 0)

blueexpo1 = Marker()
blueexpo2 = Marker()

bluesharpie1 = Marker()
bluesharpie1.erasable = False
bluesharpie1.tipsize = 0.001/5
bluesharpie1.capacity = 5/2

print(redexpo1.color)
print(blueexpo1.color)
print(bluesharpie1.erasable)

print(blueexpo1.capacity)
blueexpo1.write(1000)
print(blueexpo1.capacity)


print(blueexpo2.capacity)
blueexpo2.write(75.8)
print(blueexpo2.capacity)
redexpo1.show()
blueexpo1.show()
blueexpo2.show()
bluesharpie1.write(1000)
bluesharpie1.show()


# copy

# import copy
# copy.copy()
# used to copy anything from objects to lists and dictionaries

# class Nothing:
#
#       def __init__(self, something):
#           self.something = something
#                   OR
#           self.__something = something
#                   This makes it private so that you can't change it through self.__something = updated_value
#                                   It would have to be through a function


# TODO: surprise Logan, remember this, it is cool!!!!!!!!!!!!!!!!!!!!!!!
TODO: surprise Logan, remember this, it is cool!!!!!!!!!!!!!!!!!!!!!!!


# collapse code -> Command + -
