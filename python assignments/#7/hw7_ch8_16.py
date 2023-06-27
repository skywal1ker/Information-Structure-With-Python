"""
16. Write a function that takes a list as an argument and verifies whether the list is sorted.
Return True if sorted; False if not.
"""

def sorted_lst(k):
    for value in range(len(k)-1):
        print(k[value],k[value+1])
        if k[value]>k[value+1]:
            return False
    return True
print(sorted_lst([8, 7, 3, 2, 1, 25, 5]))
print(sorted_lst([1, 0, 24, 34, 76, 119]))