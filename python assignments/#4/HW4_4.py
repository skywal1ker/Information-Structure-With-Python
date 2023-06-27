"""
4. Given a string S with odd length:
(a) Write an expression to print the middle character.
(b) Write an expression to print the string up to but not including the middle character
(i.e., the first half of the string).
(c) Write an expression to print the string from the middle character to the end (not
including the middle character).
"""
full_name = "123456789"
len_str = int(len(full_name))
middle_letter = int((len_str / 2) - 0.5)
first_half = middle_letter
second_half = middle_letter + 1

print("The full string:",full_name)
print("The length of the string value:",len_str)
print("(a) Write an expression to print the middle character:",full_name[middle_letter])
print("(b) Write an expression to print the string up to but not including the middle character:",full_name[0:first_half])
print("(b) Write an expression to print the string from the middle character to the end:",full_name[second_half:len_str])

