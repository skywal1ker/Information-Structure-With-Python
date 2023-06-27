"""
15. Palindromes. A palindrome is a word that is the same backwards as forwards. The word
“rotor” is an example of a palindrome.
(a) Write a function which returns True, if two strings are palindromes. (Hints: You can
create a list from a string using the list() function. Lists are handy because there
is a reverse() method.)
(b) Write a program that uses your function. The program should prompt for the two
strings, call the function, and then print results (something other than “True” or
“False”).
(c) Some palindrome rules ignore spaces and capitalization so “Never odd or even”
is an acceptable palindrome. Improve your function to ignore spaces and capitalization.
(Hints: Lists have a remove() method, and strings have a lower()
method.)

"""

def palin(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    str1="".join(str1.split())
    str2="".join(str2.split())
    str1=str1[len(str1)::-1]
    if(str1==str2):
        return True
    else:
        return False

print("Please type two string to check whether they are palindrome or not.")
str1=input("Please type the first string: ")
str2=input("Please type the second string: ")
print("This strings are palindrome: ",palin(str1,str2))
