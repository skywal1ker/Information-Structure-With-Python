"""
19. In the earlier chapter on functions there was an exercise based on DNA searching to
make a multi find() function. That function had two constraints that we can now
remove: (i) it returned the indices in a string, and (ii) it couldn’t handle default arguments.
In this exercise we will fix both.


a) Write a string function multi find(some string, sub string [,start]
[,end]) where start and end are optional arguments with default values for the start
and end of some_string. The start and end are interpreted as they are in slicing, that
is:
0 = start ≤ index < end = len(some_string)
The function should return a list of indices of occurrences of sub_string in
some_string. If the substring is not found, return an empty list.


(b) Demonstrate that your string function works and that you can use it in a Boolean
expression.

"""
def multi_find(string, sub_string, start, end):
        flag = False

        for i in range(start, end-len(sub_string) + 1):
                if (string[i:i + len(sub_string)] == sub_string): 
                        flag = True
                        
        return flag
        


string = input("string: ") 
sub_string = input("sub_string: ")
start = int(input("Start Index: "))
end = int(input("Last Index: "))

multi_find(string, sub_string,start,end)


if (multi_find(string, sub_string,start,end)):
    print("Have Substring")
else:
    print("Have No Substring")


