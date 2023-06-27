"""
3. Given a string S with even length:
(a) Write an expression to print out the first half of the string.
(b) Write an expression to print out the second half of the string.
"""
full_name = "12345678" 
half_str_num = int(len(full_name) / 2)
print("(a) Write an expression to print out the first half of the string:",full_name[0:half_str_num])
print()
print("(b) Write an expression to print out the second half of the string:",full_name[half_str_num:int(len(full_name))])

