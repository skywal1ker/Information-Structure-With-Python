"""
16. Create a dictionary that maps countries to their capitals. You may start with an empty
dictionary. Ask the user to input the name of the country and its capital and add them
to the dictionary.
For example, Capitals = { ‘Argentina’:‘Buenos Aires’, ‘France’:‘Paris’, ‘US’:‘Washington
D.C.’}
Once the dictionary is created, print the capitals in alphabetical order.

"""

import collections
dictionary = {}
while(1):
   data = input("Enter a country and a capital comma separated (Q,Q to quit): ")
   if(data == ("Q,Q" or "Q, Q")):
       break
   else:
       data = data.split(',')
       dictionary[data[0]] = data[1]

for capital,country in sorted((v, k) for k, v in dictionary.items()):
    print("%s: %s" % (country,capital))

