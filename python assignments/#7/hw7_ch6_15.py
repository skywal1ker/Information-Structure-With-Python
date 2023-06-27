"""
15. Write a program that prompts the user for an equation of a line and a circle and
calculates the point(s) of intersection between the two. If the two do not intersect,
return The two do not intersect. Be careful of the case where the discriminant is
negative—try-except is handy here. [Hint: First calculate the points on paper by
setting the general equations of a line and of a circle equal and solve for x.]
"""

import math

def intersection_checker(a, b, c, x, y, rad):
        try:
            distance = ((abs(a * x + b * y + c)) /
            math.sqrt(a * a + b * b))
            if (rad >= distance):
                print("Intersect")
            else:
                print("Don't intersect")

        except:
            print("Distance is negative")

print("Type the circle radius :-")
radius = int(input())
print("Type the centre of circle (in line with space (x y)) :-")
x,y = input().split()
x = int(x)
y = int(y)
print("Type the line coefficients a,b,c in a line with space between")
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
intersection_checker(a, b, c, x, y, radius)