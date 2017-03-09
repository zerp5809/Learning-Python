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
        elif second > first and second > third:
            a = first
            b = third
            c = second
        else:
            a = first
            b = second
            c = third
        if a**2 + b**2 == c**2:
            print "Yes, this is a Pythagorean Triple"
        else:
            print "No, this is not a Pythagorean triple"
    again = True
        first = input("Please enter the first number: ")
        second = input("Please enter the second number: ")
        third = input("Please enter the third number: ")
        check(first, second, third)
        while a != "Y" or a != "y" or a != "N" or a != "n":
            if (a == 'N' or a == "n" or a == "Y" or a == "y"):
                break
            else:
        if (a == 'N' or a == "n"):
            again = False
        elif (a == "Y" or a == "y"):
            again = True
