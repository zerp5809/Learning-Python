__author__ = 'Shane Yang'
class ChangeCalc():
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
    def calculate(cost, amount):
        #calculate Change
        if cost > amount:
            print("The amount given isn't enough please try again.")
        else:
            total = amount - cost
            quarters = 0
            dimes = 0
            nickels =0
            pennies = 0
            while total > 0:
                if total > .25:
                    quarters=total/.25
                    total = total - (int(quarters)*.25)
                elif total > .10:
                    dimes = total/.10
                    total = total - (int(dimes)*.10)
                elif total > .05:
                    nickels = total/.05
                    total = total - (nickels*.05)
                elif total < .05 and total > 0:
                    pennies = total/.01
                    total = total - (pennies*.01)

            print"You will need to give the customer:", int(quarters), " Quarter(s) ",  int(dimes), " Dime(s) ", int(nickels), " Nickle(s) and ", int(pennies),  " Penny(ies): "
    again = True
    print("Hello, I will calculate the change in coins based on your entry.")
    while again:
        cost = float(input("Please enter the total cost of the items: "))
        amount = float(input("Please enter the total amount from customer: "))
        calculate(cost, amount)
        a = raw_input("Calculate change of another transaction?(Y/N)?")
        again = checkYN(a)
