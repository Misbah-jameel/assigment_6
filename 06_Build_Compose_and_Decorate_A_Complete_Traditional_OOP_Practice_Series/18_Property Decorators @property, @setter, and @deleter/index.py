class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Invalid price. Must be non-negative.")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

#  Object banate waqt price dena zaroori hai
p = Product(100)   # yahan 100 price diya
print(p.price)     # output: 100

p.price = 150      # price update kiya
print(p.price)     # output: 150

del p.price        # price delete kar diya
