"""
28. Write a program that reads a word list and prints out all the anagrams in the word list. In
earlier exercises you saw how to read a word list. Also, in earlier examples we saw how
the sorted characters of a word are a useful canonical representation of an anagram
(Hint: Therefore, useful as a key).

"""


def anagrams(el):
    if len(el) <=1:
        yield el
    else:
        for perm in anagrams(el[1:]):
            for i in range(len(el)):
                yield perm[:i] + el[0:1] + perm[i:]


lst=["One",'no',"Leo"]
lst.sort()
for i in lst:
    word = i
    print(list(anagrams(word)))


