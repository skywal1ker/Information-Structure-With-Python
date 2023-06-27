"""
17. Remove Odds or Evens:
(a) Write a function that takes a list of integers as an argument, removes even numbers
from the list, and returns the modified list.
(b) Write a function that takes a list of integers as an argument, removes odd numbers
from the list, and returns the modified list.
(c) Write a function that takes a list of integers and a Boolean as arguments. If the
Boolean is True the function removes odd numbers from the list; otherwise, evens
are removed. The function returns the modified list.

"""



def removeOdd(l):
    for i in l[:]:
        if i % 2 != 0:
            l.remove(i)
    return l



l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(removeOdd(l))

