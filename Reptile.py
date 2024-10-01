'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Reptile Class
'''
# Importing is a relationship class
from Animal import Animal
# Creating class Reptile
class Reptile(Animal):
    # Setting attributes
    coldBlooded: bool
    food: str
    attribute: str

    def __init__(self):
        super().__init__()
        self.coldBlooded = True
        self.food = 'Live'
        self.attribute = 'Reptile'

    # Def all the required methods
    def isColdBlooded(self):
        return self.coldBlooded

    def getFood(self):
        return self.food

    def setFood(self, food):
        self.food = food

if __name__ == '__main__':
    test: Reptile = Reptile()

