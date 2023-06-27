
"""
42. Write a program that prompts for two strings and then compares them, printing the
smaller string.
"""
str_1 = input("Please enter the first string: ")
str_2 = input("Please enter the second string: ")
less_than = str_1
bigger = str_2

if len(str_1) > len(str_2) :
    bigger = str_1
    less_than = str_2
print("The smaller string is:",less_than)

