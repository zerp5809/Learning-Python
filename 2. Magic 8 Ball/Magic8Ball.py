__author__ = 'Shane Yang'
import random
import time
again = True
while again:
    q = raw_input("Enter your question: ")
    print('Thinking')
    time.sleep(1)
    choice = random.randint(0,19)
    response = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    print(response[choice])
    a = raw_input("Again(Y/N)?")        
    while a.lower()!= "y" or a.lower()!="n":
        if (a.lower() == "n" or a.lower() == "y"):
            break
        else:
            a = raw_input("I didn\'t get that. Again(Y/N)?")
    if (a.lower() == "n"):
        again =  False
    elif (a.lower() == "y"):
        again =  True
