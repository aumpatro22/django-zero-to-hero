class UserAccount:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate_account(self):
        self.is_active = False
        return f"Account for {self.username} has been suspended"

class Product:
    def __init__(self,name:str,price:float,stock_qty:int):
        self.name=name
        self.price=price
        self.stock_qty=stock_qty

    def restock(self,amount):
        self.stock_qty+=amount 
        return self.stock_qty

class product_checkout:
    item_name = "Generic Item" # Intent: default name

    def __init__(self,name, price):
        self.name= name
        self.price = price
        
    def apply_discount(self, discount_pct):
        self.price = self.price - (self.price * discount_pct)
        return self.price

# Execution test
item = product_checkout("Mechanical Keyboard", 100)
print(item.apply_discount(0.10))
p1=Product("pen",5000,50)
p1.restock(400)
print(f"the product name is {p1.name} and the price of it is {p1.price} and the stocks quantity is {p1.stock_qty}")
print(f"the rectock number is {p1.stock_qty}")


# # Create an instance
# user_one = UserAccount("aum patro", None)

# # Print details
# print(f"The name is {user_one.username} and email is {user_one.email}")

# # Deactivate account
# print(user_one.deactivate_account())
# user_two=UserAccount(username="zero",email=None)
# print(user_two.username,user_two.email)

