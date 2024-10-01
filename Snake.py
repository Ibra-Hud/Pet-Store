'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Snake Class
'''
# Importing is a relationship class
from Reptile import Reptile
# Creating class Snake
class Snake(Reptile):
    # Setting attributes
    size: str
    weight: float
    color: str
    constrictor: bool
    food: str

    def __init__(self):
        super().__init__()
        self.size = ''
        self.weight = 0.00
        self.color = ''
        self.constrictor = True
        self.food = ''
    # Def all the required methods
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

    def getFood(self):
        return self.food
    def setFood(self, food):
        self.food = food

    def isConstrictor(self):
        return self.constrictor
    def setConstrictor(self, constrictor):
        self.Constrictor = constrictor

if __name__ == '__Main__':

    test = Snake()
