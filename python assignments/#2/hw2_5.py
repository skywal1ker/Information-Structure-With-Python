#5 Task

"""28. (Integer operators) One way to determine whether an integer is even is to divide the
number by two and check the remainder. Write a three-line program that prompts for
a number, converts the input to an integer, and prints a zero if the number is even and
a one if the number is odd."""


a = int(input("Enter integer number:"))
if (a % 2) == 1:
    print("the number is odd")

    