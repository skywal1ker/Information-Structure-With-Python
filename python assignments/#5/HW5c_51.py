"""
51. Write your own versions of the Python built-in functions min and max. They should
take a list as an argument and return the minimum or maximum element. Hint: Pick
the first element as the minimum (maximum) and then loop through the elements to
find a smaller (arger) element. Each time you find a smaller larger) element, update
your minimum (maximum).
"""


def min(lst):
    m=lst[0]
    for element in range(1,len(lst)):
        if lst[element]<m:
            m=lst[element]
    return m

def max(lst):
    m=lst[0]
    for element in range(1,len(lst)):
        if lst[element]>m:
            m=lst[element]
    return m


print("Min = ",min([10,20,3,56]))
print("Max = ",max([10,20,3,56]))

