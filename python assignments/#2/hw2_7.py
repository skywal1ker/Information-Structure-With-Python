"""35. Consider a triangle with sides of length 3, 7, and 9. The law of cosines states that
given three sides of a triangle (a, b, and c) and the angle C between sides a and b:
ALpha **2 = a2 + b2 − 2*a*b*cos(C ). Write Python code to calculate the three angles in the
triangle."""

import math
a = 3
b = 7
c = 9
cos_c = 1

tr = a**2 + b**2 - 2 * a * b * cos_c

tra = math.sqrt(tr)


print(tra)


