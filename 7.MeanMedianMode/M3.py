__author__ = 'Shane Yang'
class MeanMedianMode():
    def mean(numbers, size):
        #find mean for loop to add all numbers in list then divide by len(numbers)
        n = 0
        for i in range(int(size)):
            n +=numbers[i]
        return n/int(size)
    def median(numbers, size):
        #find median loop to order all numbers and find middle of array
        numbers.sort()
        middleind = int(size)/2-1
        remainder = int(size)%2
        if remainder==0:
            return (float((numbers[middleind]) + float(numbers[middleind+1]))/2)
        else:
            return numbers[middleind+1]
    def mode(numbers, size):
        #loop the list and find multiple occurences of a number and store the number. If there are multiple store that too
        numbers.sort()
        return numbers[int(size)-1] - numbers[0]
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
    print "Hello, I am the Mean, Median, Mode finder."
    again = True
    sizeCheck = True
    numberCheck = True
    functionCheck = True
    #accept numbers for sample
    while again:
        num_array = list()
        while sizeCheck:
            size = raw_input("Please enter the size of the sample: ")
            if size.isdigit():
                break
            else:
                print "Thats not a number! Try again!"
        print 'Enter numbers (Enter one number per line): '
        for i in range(int(size)):
            while numberCheck:
                n = raw_input("num: ")
                if n.isdigit():
                    num_array.append(int(n))
                    break
                else:
                    print "That's not a number! Try again!"
        while functionCheck:
            function = raw_input("What functionality would you like to use?(Enter Mean, Median, or Mode): ")
            if function.lower() == "mean":
                print mean(num_array, size)
                break
            elif function.lower() == "median":
                print median(num_array, size)
                break
            elif function.lower() == "mode":
                print mode(num_array,size)
                break
            else:
                print "Incorrect Input! Try again."
        a = raw_input("Try another set of numbers?(Y/N)?")
        again = checkYN(a)
