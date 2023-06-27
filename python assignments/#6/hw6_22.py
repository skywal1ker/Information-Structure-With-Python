"""
22. Given a list of integers, write Python code to create a new list with same number of
clements as the original list such that each integer in the new list is the sum of its neigh-
bors and itself in the original list. For example, if 
listA = [10, 20, 30, 40, 50],
listB = [30, 60, 90, 120, 90].
"""


# listA = [10, 20, 30, 40, 50]
# print("This is ListA: ", listA)
# listA = [0, *listA, 0]
# listB = [listA[i] + listA[i+1] + listA[i+2] for i, v in enumerate(listA[:-2])]

# print()
# print("This is ListB: ", listB)

listA = [10, 20, 30, 40, 50]
listB = list()

for i in range(len(listA)):
    if i == 0: listB.append(listA[i] + listA[i+1])
    elif i == len(listA) - 1: listB.append(listA[i] + listA[i-1])
    else: listB.append(listA[i] + listA[i-1] + listA[i+1])

print(listB)