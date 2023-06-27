"""
52. Write a program that prompts the user to enter a three-digit number such that the digits
are in order, for example, 123789. The program loops until a correct value is entered.
"""
def checking_number(summ):
    if(summ[0]<summ[1] and summ[1] < summ[2]):
        return 1
    else:
        return 0
while True:
    if(checking_number(str(input("Type a three digital number: "))) == 0):
        print("not correctly input, add the numbers in order please ")
    else:
        print("This is correct")
        break

