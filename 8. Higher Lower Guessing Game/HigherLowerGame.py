__author__ = 'Shane Yang'

from random import randint

class HigherLowerGame():
    def checkYN(input):
         a = input
         while a.lower()!= "y" or a.lower()!="n":
            if (a.lower() == "n" or a.lower() == "y"):
                break
            else:
                a = raw_input("I didn\'t get that. Estimate the amount of another set of coins?(Y/N)?")
         if (a.lower() == "n"):
            return False
         elif (a.lower() == "y"):
            return True

    print "Hello, I am the Higher Lower Game. I will select a number and you will guess what it is."
    again = True
    incorrect = True
    while again:
        count = 0
        selectedNumber = randint(0, 100)
        print "I have selected a number."
        while incorrect:
            count += 1
            guess = raw_input("Enter your guess or type q to roll a new number: ")
            if guess == 'q':
                break
            elif not guess.isdigit():
                print "Thats not a number! Try again"
            elif int(guess) == selectedNumber:
                print "You got it! Congratulations!"
                print "You tried ", count, " times."
                break
            elif int(guess) > selectedNumber:
                print "The number I've selected is smaller than what you guessed. Try again!"
            elif int(guess) < selectedNumber:
                print "The number I've selected is larger than what you guessed. Try again!"
        a = raw_input("Try to guess another number?(Y/N)?")
        again = checkYN(a)
