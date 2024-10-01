'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Mammal Class
'''

# Importing is a relationship class
from Animal import Animal
# Creating class Mammal
class Mammal(Animal):
    # Setting attributes
    warmBlooded: bool
    fur: bool

    def __init__(self):
        super().__init__()
        self.fur = True
        self.warmBlooded = True

    # Def all the required methods
    def isWarmBlooded(self):
        return self.warmBlooded

    def setWarmBlooded(self, warmBlood):
        self.warmBlooded = bool(warmBlood)

    def hasFur(self):
        return self.fur

    def setFur(self, fur):
        self.fur = fur

if __name__ == '__main__':

    mammal = Mammal()

