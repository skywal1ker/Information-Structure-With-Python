"""
6. If you had 2 lists, one of first names and one of last names [Jane', John', Jack'] and
(Doe', 'Deer', 'Black'], use zip to create a dictionary with the keys as the first names
and the values as the last names.
"""
keys = ['Jane', 'John', 'Jack']
values = ['Doe', 'Deer', 'Black']
dictionary = dict(zip(keys, values))
print(dictionary)

