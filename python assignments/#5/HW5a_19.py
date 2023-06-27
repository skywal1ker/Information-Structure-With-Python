"""
19. Write a function that takes as input a string that stores date and time (24-hour clock) in
the following format:
"MM/DD/YYYY HR:MIN:SEC" and prints the following:
• DD/MM/YYYY
• HR:MIN:SEC
• MM/ YYYY
• Whether the time is "AM' or "PM"'.
"""

from datetime import datetime


def to_datetime(date_s):
    try:
        date_time = datetime.strptime(date_s, '%m/%d/%Y %H:%M:%S') 
        date = date_time.strftime('%d/%m/%Y')
        print("DD/MM/YYY :", date)
        hour_min_sec = date_time.strftime('%H:%M:%S')
        print("HR:MIN:SEC :", hour_min_sec)
        m_year = date_time.strftime('%m/%Y')
        print("MM/YYYY :",m_year)
        print("AM or PM  : ", date_time.strftime('%p'))

    except:
        print('Invalid date format')


to_datetime('12/01/2020 13:30:45')

