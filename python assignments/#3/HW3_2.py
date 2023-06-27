"""5. Control:
if my_var % 2:
if my_var**3 != 27:
my_var = my_var + 4 # Assignment 1
else:
my_var /= 1.5 # Assignment 2
else:
if my_var <= 10:
my_var *= 2 # Assignment 3
else:
my_var -= 2 # Assignment 4
print(my_var)
(a) Find four values of my var so each of the four assignment statements will be executed:
each value should cause one assignment statement to be executed.
(b) Find four ranges of my var values that will cause each of the four assignment
statements to be executed."""

ass1=[]
ass2=[]
ass3=[]
ass4=[]
def var(my_var):
    
    if my_var % 2:
        if my_var**3 != 27:
            print('Assignment 1: ', my_var)
            ass1.append(my_var)
            my_var = my_var + 4 # Assignment 1
            
        else:
            print('Assignment 2: ', my_var)
            ass2.append(my_var)
            my_var /= 1.5 # Assignment 2
            
    else:
        if my_var <= 10:
            print('Assignment 3: ', my_var)
            ass3.append(my_var)
            my_var *= 2 # Assignment 3
            
        else:
            print('Assignment 4: ', my_var)
            ass4.append(my_var)
            my_var -= 2 # Assignment 4
            

for x in range(100):
    var(x)

    
print(ass1)
print(ass2)
print(ass3)
print(ass4)


