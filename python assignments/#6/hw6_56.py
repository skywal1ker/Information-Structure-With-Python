"""
56. Given a list of N numbers, write a function to shift the numbers circularly by some
integer & (where 4 < N). The function should take a list and & as a arguments and
return the shifted list.
(a) Write a function that assumes shifting is to the left.
(b) Write a function that takes a third argument that specifies shifting left or right.
"""


def rotate(lists, k, direction):
    direction = input("Type left for left rotate or anything for right rotate: ")
    if direction == "left":
        output_list = []
        for item in range(k - 1, len(lists)):
            output_list.append(lists[item])
        for item in range(0, k - 1):
            output_list.append(lists[item])
        return output_list
    else:
        direction == "right"
        output_list = []
        for item in range(len(lists) - k - 1, len(lists)):
            output_list.append(lists[item])
        for item in range(0, len(lists) - k - 1):
            output_list.append(lists[item])
        return output_list


k = int(input("Input the k number: "))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Direction to the left: ", rotate(lst, k, "left"))
print("Direction to the right: ", rotate(lst, k, "right"))
