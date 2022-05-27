low_num = int(input("Enter the lowest number:"))    #Stores user input as the lowest number value.
high_num = int(input("Enter the highest number:"))  #Stores user input as the highest number value.

print("The prime numbers between" ,low_num, "and", high_num, "are:") #Prints as a preface to the prime values.

#"for loop" finds the prime numbers between two user inputted values.

for num in range(low_num, high_num): #Starts a loop that cycles through the lowest number to the highest.
    if num < 1:                      #Prevents users getting output when inputting numbers that are too small.
        print("You must have entered a value lower than 1. Goodbye!")
        break                        #Terminates the loop if the user enters a value lower than 1.
    elif num > 1:                    #Checks if the value of num is greater than 1. Which it should/needs to be as all primes are greater than 1.
        for i in range(2, num):      #Nested loop moving from 2 to the current value of num.
            if(num % i) == 0:        #Checks if the value of "num" modulo the value of "i" is equivalent to 0. If it is, the value of "num" is not prime.
                break                #Terminates loop if the value is not prime.
        else:                        #Otherwise the value of "num" must be prime and is printed.
            print(num)               #Prints the values of "num".

