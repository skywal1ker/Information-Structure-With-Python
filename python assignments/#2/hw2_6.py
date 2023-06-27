
#6 TASK

"""33. If the lengths of the two parallel sides of a trapezoid are X meters and Y meters,
respectively, and the height isH meters, what is the area of the trapezoid?Write Python
code to output the area"""

x = int(input("Enter X side: "))
y = int(input("Enter Y side: "))
H = int(input("Enter H height: "))

area = (x + y) / 2 * H

print("Area will be", area)