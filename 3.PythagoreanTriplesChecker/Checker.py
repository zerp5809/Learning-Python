__author__ = 'Shane Yang'
class PyTriChecker():
    def check(first, second, third):
        #a^2 + b^2 = c^2
        #ask for sides in any order 1. user can enter wahtever and code will check what side is what or 2. user has to enter what side they are plugging in before entring sides
        #1. compare each of them c will be largest
        if first > second and first > third:
            a = second
            b = third
            c = first
            #print a, ", ", b, " ,", c, ", ", a**2 + b**2, ", ", c**2
        elif second > first and second > third:
            a = first
            b = third
            c = second
            #print a, ", ", b, " ,", c, ", ", a**2 + b**2, ", ", c**2
        else:
            a = first
            b = second
            c = third
            #print a, ", ", b, " ,", c, ", ", a**2 + b**2, ", ", c**2
        if a**2 + b**2 == c**2:
            print "Yes, this is a Pythagorean triple"
        else:
            print "No, this is not a Pythagorean triple"
    again = True
    print("Hello, I am the PyTriChecker, I check if the 3 numbers you will enter will form a Pythagorean Triple")
    while again:
        first = input("Please enter the first number: ")
        second = input("Please enter the second number: ")
        third = input("Please enter the third number: ")
        check(first, second, third)
        a = raw_input("Try another set of numbers?(Y/N)?")
        while a != "Y" or a != "y" or a != "N" or a != "n":
            if (a == 'N' or a == "n" or a == "Y" or a == "y"):
                break
            else:
                a = raw_input("I didn\'t get that. Try another set of numbers?(Y/N)?")
        if (a == 'N' or a == "n"):
            again = False
        elif (a == "Y" or a == "y"):
            again = True
