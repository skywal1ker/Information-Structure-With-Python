"""
63. Using only list comprehensions (no loops) how would you change a List of positive
integers such as [2, 3, 4, 5] and [9, 2, 1, 9] into their actual numbers 2345 and 9919?
"""

my_lst1 = [2, 3, 4, 5]
my_lst2 = [9, 2, 1, 9]
my_lst_str1 = ''.join(map(str, my_lst1))
my_lst_str2 = ''.join(map(str, my_lst2))
print("This is List1: ", my_lst_str1)
print("This is List2:", my_lst_str2)

