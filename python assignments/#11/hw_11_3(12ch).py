"""
3. The human body has many organs (heart, lungs, brain, and kidneys, to name a few).
We could think of the human body as a complex object made up of simpler objects
(organs).
"""


"""
(a) Create classes for heart and brain. Think about what the functions of the heart and
brain are in our body and map these functions into methods.
"""
class Organ(object):

    def __init_(self, organ_class='', size_float = 0.0):
        self.__organ_class = organ_class
        self.__size = size_float

    def get_size(self):
        return self.__size

    def __str__(self):
        print("in str")
        return "Organ: {}".format(self.__organ_class)


class Heart(Organ):
    def _init__(self, size_float=0.0):
        Organ.__init__(self, 'Heart', size_float)


    def pump(self):
        print("Pump blood through the entire human body.")

    def generate_heartbeat(self):
        print(" generate electrical signals that spread to the rest of the heart.")

    def regulate(self):
        print("rate of heart beats per minutes")



class Brain(Organ):

    def __init__(self, size_float = 0.0, hemishpere_str = ''):
        Organ.__init_(self, 'Brian', size_float)
        self.hemisphere = hemishpere_str

    def dominant_hemisphere(self):
        return self.hemisphere

    def reasoning(self):
        print("Recording information")
    
    def sense(self):
        print("React to sense")




"""
(b) Create an Organ class as the base class for the organs and derive the classes created
earlier from the base class.
"""

class Organ(object):
    def __init__(self, organ_class ='', size_float = 0.0):
        self.__organ_class = organ_class
        self.__size = size_float

class Heart(Organ):
    def __init__(self, size_float = 0.0):
        Organ.__init__(self, 'Heart', size_float)
