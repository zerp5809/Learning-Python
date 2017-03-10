__author__ = 'Shane Yang'
class CoinEstimator():
    again = True
    def math(units, coinType, weight):
        #method should determine what units is being used
        #could return array of weights based off of coin weight
        print (units, coinType, weight)
    #units used lbs = 1 g = 0
    #ask for units, type of coin, then weight, and the finally calculate
    print("Hello, I am the coin estimator. I estimate the total amount of coins based on weight")
    while again:
        u = raw_input("Please enter units you are using (G/LBS): ")
        coinType = raw_input("Please enter the type of coin: ")
        weight = input("Please enter the total weight of coins: ")
        math(u, coinType, weight)
        a = raw_input("Estimate the amount of another set of coins?(Y/N)?")
        while a != "Y" or a != "y" or a != "N" or a != "n":
            if (a == 'N' or a == "n" or a == "Y" or a == "y"):
                break
            else:
                a = raw_input("I didn\'t get that. Estimate the amount of another set of coins?(Y/N)?")
        if (a == 'N' or a == "n"):
            again = False
        elif (a == "Y" or a == "y"):
            again = True
