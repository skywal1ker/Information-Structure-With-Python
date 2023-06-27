"""
15. Write a function that takes a person’s first and last names as input and
(a) uses lists to return a list of the common letters in the first and last names (the intersection).
(b) uses sets to return a set that is the intersection of the characters in the first and last
names.
(c) uses sets to return the set that is the symmetric difference between the first and last
names.

"""


def func_b(fname,lname):
    fname_set = set(fname)
    lname_set = set(lname)
    common_char_inter = fname_set.intersection(lname_set)
    return common_char_inter

func_b('alan','Salline')


