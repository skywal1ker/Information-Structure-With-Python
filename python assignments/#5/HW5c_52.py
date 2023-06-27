
"""
52. Create a program that uses the Gettysburg Address as input and outputs a list
of tuples for every two words. For example: ( ('Four', 'score'), ('and'
'seven'), …].
"""


inp_str=input("Enter Gettysburg Address: ")
lst=inp_str.split()
my_list=[]

for element in range(0,len(lst),2):
    my_list.append((lst[element],lst[element+1]))

print(my_list)