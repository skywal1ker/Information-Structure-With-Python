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
#A
def palin(x,y):
    lst1 = list(x)
    lst2 = list(y)
    if(len(lst1)!=len(lst2)):
        return False
  
    i=0
    j=len(lst2)-1
    c=0
    while(i<len(lst1) and j>=0):
        if(x[i]!=y[j]):
            return False
        else:
            c=1
            i+=1
            j-=1
        return True

def main():
    x='leo'
    y='oel'
    print (palin(x,y))

