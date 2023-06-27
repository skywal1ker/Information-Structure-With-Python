"""
5. Design a class called Bill that has fields to store the list of items, their prices per unit,
quantity of each item in the bill, and the grand total of the items. Create an overloaded
add operator so that when you add two bills, you get a new bill with all the items in the
two bills (there may be duplicates in the final bill) and a new grand total.
Would you have multiply and divide overloaded operators in this case? 'Think!
For example, a McDonald's bill might include: 2 burgers @$4.00 each, 4 strawberry
milkshakes @$2.50 each.
"""
class Bill: 
    def __init__(self,list_of_items=[],prices=[],quantity=[]):  
        self.list_of_items = list_of_items 
        self.prices = prices
        self.quantity = quantity
    def getGrandTotal(self):  
        total = 0  
        for i in range(len(self.prices)): 
            total+= (self.quantity[i]*self.prices[i]) 
        return total 
    def __add__(self, other):  
        new_list =  self.list_of_items + other.list_of_items  
        new_prices =  self.prices + other.prices
        new_quantity = self.quantity + other.quantity
        return Bill(new_list,new_prices,new_quantity) 

mcd = Bill(['burgers','strawberry milkshakes'],[4.00,2.50],[2,4]) 
mcd2 = Bill(['maggi','pizza'],[5.00,12.50],[5,3])

print("Grand total: $",mcd.getGrandTotal())
result = mcd.__add__(mcd2)
print(result.getGrandTotal())

