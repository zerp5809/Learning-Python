__author__ = 'Shane Yang'
import random
again = True
while again:
    q = raw_input("Enter your question: ")
    print('Thinking')
    choice = random.randint(0,7)
    response = ["Yes", "No", "Maybe", "Try again", "Outcome not clear", "Go for it", "na", "Ask something else"]
    print(response[choice])
    a = raw_input("Again(Y/N)?")
    while a != "Y" or a != "y" or a != "N" or a != "n":
        if (a == 'N' or a == "n" or a == "Y" or a == "y"):
            break
        else:
            a = raw_input("I didn\'t get that. Again(Y/N)?")
    if (a == 'N' or a == "n"):
        again = False
    elif (a == "Y" or a == "y"):
        again = True
