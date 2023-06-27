"""29. Create a program that prompts for a positive number greater than 2 (check this condition),
then keeps taking the square root of this number until the square root is less than
2. Print the value each time the square root is taken, along with the number of times
the operation has been completed. For example:
Enter an integer greater than 2: 20
1: 4.472
2: 2.115
3: 1.454
Extra: Look ahead to string formatting (Section 4.4) to print the values to only
3 decimal places as shown."""

import math

def sqrt(n):
    sqrt = n
    counter = 0
    while sqrt > 2:
        sqrt = math.sqrt(sqrt)
        counter += 1
        print("Number of steps:", counter, ", square value:", '{0:.2f}'.format(sqrt))

while True:
    n = int(input("Enter a number more than 2: "))
    if n <= 2:
        print("Enter a number > 2!")
        continue

    else:
        sqrt(n)
        break


    
