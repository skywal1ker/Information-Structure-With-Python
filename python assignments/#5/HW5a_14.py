"""
14. You buy an international calling card to India. The calling card company has some spe-
cial offers.
(a) If you charge your card with $5 or $10, you don't get any thing extra.
(b) For a $25 charge, you get $3 of extra phone time.
(c) For a $50 charge, you get $8 of extra phone time.
(d) For a $100 charge, you get $20 of extra phone time.

Write a function that asks the user for the amount he/she wants on the card, and returns
the total charge that the user gets. Note: Values other than those mentioned earlier are
not allowed.
"""

def check_ph(rech):
    if rech == 5 or rech == 10:
        return 0
    elif rech == 25:
        return 3
    elif rech == 50:
        return 8
    elif rech == 100:
        return 20
    else:
        return -1
        
def pay():
    rech = int(input("Enter recharge amount in the denomination of $5, $10, $25, $50, $100: "))
    extra_time = check_ph(rech)
    if extra_time >= 0:
        phone = extra_time + rech
        print("you've got $" + str(phone) + " of your amout $"+ str(rech))
    else:
        print("Cannot process your order please try again")
        rech = pay()
    return rech
rech = pay()

