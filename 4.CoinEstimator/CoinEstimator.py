__author__ = 'Shane Yang'
class CoinEstimator():
    again = True
    more = True
    total = 0
    def math(units, coinType, weight):
        subtotal = 0
        if units.lower()=="g":
            p = 1.555
            n = 5
            d = 2.268
            q = 5.870
        elif units.lower()=="lbs":
            p = 0.003
            n = 0.011
            d = 0.005
            q = 0.013
        else:
            print("I don\'t understand ", units, " try again.")
            return 0
        if coinType.lower()=="quarters" or coinType.lower() == "quarter":
            amount = int((weight/q))*0.25
            return amount
        elif coinType.lower()=="dimes" or coinType.lower == "dime":
            amount = int((weight/d))*0.10
            return amount
        elif coinType.lower()=="nickels" or coinType.lower == "nickel":
            amount = int((weight/n))*0.05
            return amount
        elif coinType.lower()=="pennies" or coinType.lower == "penny":
            amount = int((weight/p))*0.01
            return amount
        else:
            print ("I don\'t understand" )
        #method should determine what units is being used
        #could return array of weights based off of coin weight
        print (units, coinType, weight)
        return subtotal
    def checkYN(input):
        a = input
        while a != "Y" or a != "y" or a != "N" or a != "n":
            if (a == 'N' or a == "n" or a == "Y" or a == "y"):
                break
            else:
                a = raw_input("I didn\'t get that. Estimate the amount of another set of coins?(Y/N)?")
        if (a == 'N' or a == "n"):
            return False
        elif (a == "Y" or a == "y"):
            return True
    #units used lbs = 1 g = 0
    #ask for units, type of coin, then weight, and the finally calculate
    print("Hello, I am the coin estimator. I estimate the total amount of coins based on weight")
    while again:
            while more:
                u = raw_input("Please enter units you are using (G/LBS): ")
                coinType = raw_input("Please enter the type of coin: ")
                try:
                    weight = float(input("Please enter the total weight of coins: "))
                except NameError as ev:
                    print('Invalid input. Try again.')
                    print(total)
                    continue
                total += math(u, coinType, weight)
                print (total)
                moreCoins = raw_input("Another coin type(Y/N)?")
                more = checkYN(moreCoins)
            a = raw_input("Estimate the amount of another set of coins(Y/N)?")
            again = checkYN(a)
