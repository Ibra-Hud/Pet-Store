'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Inventory Class
'''

# Creating class Inventory
class Inventory:
    # Setting attributes
    location: str
    quantity: int
    price: float

    def __init__(self):
        self.location = ''
        self.quantity = 0
        self.price = 0.00

    # Def all the required methods
    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getLocation(self):
        return self.location

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setPrice(self, price):
        self.price = price

    def setLocation(self, location):
        self.location = location

if __name__ == '__Main__':
    test = Inventory()
