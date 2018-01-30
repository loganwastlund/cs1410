import sys


def createIndex():
    return {}


def recordBook(index, isbn, title):
    index[isbn] = title


def findBook(index, isbn):
    if isbn in index:
        return index[isbn]
    else:
        return ""


def listBooks(index):
    list_index = []
    number = 1
    for key in index:
        item = f"{number}) {key}: {index[key]}"
        list_index.append(item)
        number += 1
    return list_index


def formatMenu():
    return ['What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit']


def formatMenuPrompt():
    return "Enter an option: "


def getUserChoice(prompt):
    choice = input(prompt)
    choice = choice.strip()
    while choice == "":
        choice = input(prompt)
        choice = choice.strip()
    return choice


def getISBN():
    choice = getUserChoice("Enter an ISBN: ")
    return choice


def getTitle():
    choice = getUserChoice("Enter a book title: ")
    return choice


def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    recordBook(index, isbn, title)
    print("Book saved!")


def findBookAction(index):
    isbn = getISBN()
    title = findBook(index, isbn)
    if len(title) > 0:
        print("Book found: {0}".format(title))
    else:
        print("Sorry, book not found. ")


def listBooksAction(index):
    list = listBooks(index)
    if len(list) > 0:
        for item in list:
            print(item)
    else:
        print("Sorry, no books in library. ")


def quitAction(index):
    print("Bye! See you next time! ")
    index_keys = open("isbn_keys.txt", 'a')
    index_values = open("isbn_values.txt", 'a')
    for key in index:
        index_keys.write(key + '\n')
    for value in index:
        index_values.write(index[value] + '\n')
    index_keys.close()
    index_values.close()
    sys.exit(0)


def applyAction(index, action):
    if action == 'r':
        recordBookAction(index)
    elif action == 'f':
        findBookAction(index)
    elif action == 'l':
        listBooksAction(index)
    elif action == 'q':
        quitAction(index)
    else:
        print("Sorry, that option is invalid. ")


def main():
    index_keys = open("isbn_keys.txt", 'r')
    index_values = open("isbn_values.txt", 'r')
    values = []
    for valueline in index_values:
        valueline = valueline.strip()
        values.append(valueline)

    index = createIndex()
    i = 0
    for keyline in index_keys:
        keyline = keyline.strip()
        index[keyline] = values[i]
        i += 1

    index_keys.close()
    index_values.close()

    useroption = "hehe"
    while useroption != 'q':
        menu = formatMenu()
        for option in menu:
            print(option)
        useroption = input(formatMenuPrompt())
        applyAction(index, useroption)
        print()


if __name__ == '__main__':
    main()
