'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Canine class
'''

# Importing is a relationship class
from Mammal import Mammal
# Creating class Canine
class Canine(Mammal):

    # Setting attributes
    size: str
    weight: float
    color: str

    def __init__(self):
        super().__init__()
        self.size = ''
        self.weight = 0.00
        self.color = ''

    # Def all the required methods

    def bark(self, count):
        while int(count) > 0:
            print('Bark')
            count -= 1

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

if __name__ == '__Main__':
    test = Canine()
