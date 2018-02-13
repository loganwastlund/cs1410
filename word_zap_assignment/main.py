from player import Player
import sys


def instructions():
    return '''
Welcome! Time to play! Try to use all of your letters.
The first player that uses all of their letters wins!
'''


def getUserInt(prompt):
    keepLooping = True
    while keepLooping:
        response = input(prompt)
        try:
            intResponse = int(response)
            if intResponse <= 0:
                print("Please enter a number greater than zero.")
            else:
                keepLooping = False
        except ValueError:
            print("Please enter a number.")
            continue
    return intResponse


def getUserString(prompt):
    response = input(prompt)
    while len(response) < 0:
        response = input(prompt)
        response = response.strip()
    return response


def getPlayers():
    num_of_players = getUserInt("How many players will be playing? ")
    players = []
    for player in range(num_of_players):
        players.append(player)
    for i in range(len(players)):
        playerinst = Player(getUserString(f"Enter the name for player #{i + 1}: "))
        players[i] = playerinst
    return players


def convertToLower(word):
    word = word.lower


def main():
    print(instructions())
    players = getPlayers()
    print()
    print("Great! Now we can play!")
    game = True
    while game:
        for player in players:
            turn = True
            while turn:
                print(f'''
{player.name}, it is your turn!
Your letters are: {player.printLetters()}''')
                word = getUserString("Enter a word to play (or press enter to pass) ")
                if len(word) == 0:
                    print(f'You get another letter, "{player.drawLetter()}"')
                    turn = False
                else:
                    if player.checkWord(word):
                        print("Great job!")
                        print()
                        turn = False
                    else:
                        turn = True
            if len(player.getLetters()) == 0:
                print(f"{player.name} wins!!")
                game = False
                sys.exit()


if __name__ == '__main__':
    main()
