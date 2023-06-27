"""38. Write a program that adds all the digits in an integer. If the resulting sum is more
than one digit, keep repeating until the sum is one digit. For example, 827 has the sum
8 + 2+7= 17 which has the sum 1 + 7 = 8, your final answer."""

n = int(input("Input an integer:"))
sum_int=0  
while float(n)/10 >= .1:   
    r= n%10
    sum_int += r
    n= n//10   
    if float(n)/10 > .1: print(r,  end= " + ") 
    else: print(r,"=",sum_int)