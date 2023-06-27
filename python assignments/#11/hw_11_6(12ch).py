"""
6. In Newtonian physics, we know that two velocities in the same direction add to each
other; in the opposite direction, they subtract from each other to give a net result in the
direction of the bigger velocity.
Design a simple class called Velocity that has a field for the speed in meters per
second. (Forget about the direction for now).
The default constructor would work with meters/sec metric.
Write a constructor that takes three parameters: (a) distance, (b) time, and (c)
whether the velocity is in meters/sec or feet/sec.
This constructor should accordingly convert the feet/sec into meters/sec. Create
overloaded unary, addition, and subtraction operators for velocity.
A more advanced version of this class would consider the directions other than
same or opposite directions.
"""

class Velocity(object):
    def __init__(self, d, sec, units = 'meter'):
        self.distance = float(d)
        self.time = float(sec)
        self.units = units.lower()
        if units == 'feet':
            self.distance = 0.3048*self.distance
        elif units != 'meter':
            print(("Error in units:", units))
        self.speed = self.distance/self.time

    def __add__(self, v):
        return self.speed + v.speed

    def __sub__(self, v):
        return self.speed - v.speed

v = Velocity(5, 10, "feet")
v1 = Velocity(10, 8, "meter")
print("Addition of velocity:",v + v1)
print("Subtraction of velocity:",v - v1)