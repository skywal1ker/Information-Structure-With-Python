class Item:
    def __init__(self, product_id, type, manufacturer, product_name, amount):
        self.product_id = product_id
        self.type = type
        self.manufacturer = manufacturer
        self.product_name = product_name
        self.amount = amount

    def getId(self):
        return self.product_id

    def category(self):
        return self.type

    def manufacturer(self):
        return self.manufacturer

    def product_name(self):
        return self.product_name

    def getAmount(self):
        return self.amount


class ShoppingCart:
    def __init__(self):
        self.content = []

    def addItem(self, item):
        self.content.append(item)

    def removeItem(self, item):
        self.content.remove(item)

    def getItemCount(self):
        return len(self.content)

    def getTotal(self):
        total = 0.0
        for item in self.content:
            total = total + item.getAmount()
        return total

item1 = Item(1, "Music Player", "Apple", "IPod", 200)
item2 = Item(2, "Camera", "Fujiflim", "Fujiflim instamax", 150)
item3 = Item(3, "TV", "Sony", "66 inch Smart TV", 1500)
item4 = Item(4, "Laptop", "ASUS", "ASUS ZenBook", 1100)
userCart = ShoppingCart()
userCart.addItem(item1)
print("IPod added to the cart")
userCart.addItem(item2)
print("Fujiflim instamax added to the cart")
userCart.addItem(item3)
print("Sony 66 inch Smart TV added to the cart")
userCart.addItem(item4)
print("ASUS ZenBook added to the cart")

print("Total no. of items in your cart are " + str(userCart.getItemCount()))

print("The cost for all these items are " + str(userCart.getTotal()))

userCart.removeItem(item3)

print("You removed one item from the cart")

print("Total no. of items in your cart are " + str(userCart.getItemCount()))

print("The cost for all the items in your cart are " + str(userCart.getTotal()))
