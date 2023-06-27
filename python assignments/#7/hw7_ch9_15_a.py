"""
15. Write a function that takes a person’s first and last names as input and
(a) uses lists to return a list of the common letters in the first and last names (the intersection).
(b) uses sets to return a set that is the intersection of the characters in the first and last
names.
(c) uses sets to return the set that is the symmetric difference between the first and last
names.

"""

def func_a(fname,lname):
    lst = []
    for ch in fname:
        if ch in lname and ch not in lst:
            lst.append(ch)
        return lst
func_a('alan','Salline')


