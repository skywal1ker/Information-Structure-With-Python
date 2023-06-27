"""18. Sum of consecutive integers
(a) Write a program that prompts for an integer—let’s call it X—and then finds the
sum of X consecutive integers starting at 1. That is, if X = 5, you will find the sum
of 1 + 2 + 3 + 4 + 5 = 15.
(b) Modify your program by enclosing your loop in another loop so that you can find
consecutive sums. For example, if 5 is entered, you will find five sums of consecutive
numbers:
1 = 1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
Print only each sum, not the arithmetic expression.
(c) Modify your program again to only print sums if the sum is divisible by the number
of operands. For example, with the sum 1 + 2 + 3 + 4 + 5 = 15, there are
five operands and the sum, 15, is divisble by 5 so that sum will be printed. (Do you
notice a pattern?)"""

N = 5
count = N
x = range(1, N +1)
for i in x:
    N = i + N   
print(N - count)
    
    