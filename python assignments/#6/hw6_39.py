"""
39. Given a list of integers L, use list comprehension to:
(a) find the sum of the even integers in list L
b) find the sum of the odd integers in list I.
"""


def even_sum(lst):
    even_sum = sum([i for i in lst if i % 2 == 0])
    print("\nSum of even numbers are:", even_sum)


lst = [1, 5, 9, 6, 8, 6, 4]
print("\nList values are:", lst)
even_sum(lst)


def odd_sum(lst):
    odd_sum = sum([i for i in lst if i % 2 == 1])
    print("\nSum of odd numbers are:", odd_sum)


lst = [1, 5, 9, 6, 8, 6, 4]
print("\nList values are:", lst)
odd_sum(lst)