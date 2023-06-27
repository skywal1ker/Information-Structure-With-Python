"""
12. A leap year in the Gregorian calendar system is a year that's divisible by 4 but not by
100, unless it is also divisible by 400. For example, 1896, 1904, and 2000 were leap years
but 1900 was not. Write a function that takes in a year as input and prints whether it's a
leap year (or not)
"""
def leap_year():
    leap = "Is a leap year" 
    leap_not = "Is not a leap year" 
    year = int(input("Enter year: ")) 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year,leap) 
            else:
                print(year,leap_not) 
        else:
            print(year,leap) 
    else:
        print (year,leap_not)
        return

leap_year()