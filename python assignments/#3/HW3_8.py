"""22. Write a program that checks to see if a number N is prime. A simple approach checks
all numbers from 2 up toN, but after some point numbers are checked that need not be
checked. For example, numbers greater than √ N need not be checked. Write a program
that checks for primality and avoids those unnecessary checks. Remember to import the
math module."""


prime_number_checker = int(input("Enter the number to check: "))
for element in range(2, prime_number_checker):
    if(element % 2 != 0):
        print(element)
        
