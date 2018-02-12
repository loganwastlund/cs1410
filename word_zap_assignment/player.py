from random import choice
from copy import copy


class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        letter = choice(letters)
        self.letters.append(letter)
        return letter

    def printLetters(self):
        string = ""
        for letter in self.letters:
            string += (letter + " ")
        return string.strip()

    def checkWord(self, word):
        letters = copy(self.letters)
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        self.letters = letters
        return True


# luke = Player("Luke")
# for i in range(20):
#     luke.drawLetter()
# print(luke.getLetters())
# print(luke.checkWord("jade"))
# print(luke.getLetters())
