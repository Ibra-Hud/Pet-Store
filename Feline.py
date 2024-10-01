'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Feline Class
'''
# Importing is a relationship class
from Mammal import Mammal
# Creating class Feline
class Feline(Mammal):
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

    def purr(self, count):
        while int(count) > 0:
            print('Bark')
            count -= 1

    def getSize(self):
        return self.size

    def setSize(self, string: str):
        self.size = string

    def getWeight(self):
        return self.weight

    def setWeight(self, weight: float):
        self.weight = weight

    def getColor(self):
        return self.weight

    def setColor(self, color: str):
        self.color = color

if __name__ == '__Main__':
    test = Feline()
