"""
26. Use a dictionary to create a program that prompts for an integer and prints out the
integer using words. For example: 138 will print "one three eight.”
"""

number_dictionary = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
                     '7': 'seven', '8': 'eight', '9': 'nine'}
number_string = input("Enter the value of integer to convert to words: ")
print()
for number in number_string:
    print(number_dictionary[number], end=' ')
