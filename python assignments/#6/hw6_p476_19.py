"""
19. Create a dictionary for the months in the calendar. Keys are the names of the months
and the values are the number of days in the month.
"""

# 1 option
import calendar

key_by_month = dict(zip(calendar.month_name[1:], [(-calendar.monthrange(2019, i)[1], i) for i in range(1, 13)]))
print(key_by_month)

# 2 option
dict = {}
ch = 'y'
while ch == 'y' or ch == 'Y':
    month = input("Enter name of month : ")
    days = eval(input("Enter no. of days of month : "))
    dict[month] = days
    ch = input("Want to add more months (Y/N) : ")
print(dict)
