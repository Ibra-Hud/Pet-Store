'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Animal Class
'''

# Importing has a relationship class
from Inventory import Inventory
# Creating class Animal
class Animal(Inventory):
    # Setting attributes
    multiCellular: bool
    sexualReproduction: bool
    heterotroph: bool
    fourLimbs: bool
    inventory: Inventory
    backBone: bool
    TYPE: str

    def __init__(self):
        super().__init__()
        self.multiCellular = True
        self.sexualReproduction = True
        self.heterotroph = True
        self.fourLimbs = True
        self.inventory = Inventory
        self.backbone = True
        self.TYPE = 'Animal'
        self.name = ''

    # Def all the required methods
    def isMultiCellular(self):
        return self.multiCellular

    def hasSexualReproduction(self):
        return self.sexualReproduction

    def isHeterotroph(self):
        return self.heterotroph

    def hasFourLimbs(self):
        return self.fourLimbs

    def setFourLimbs(self, hasFourLimbs):
        self.fourLimbs = hasFourLimbs

    def hasBackbone(self):
        return self.backbone

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name



if __name__ == '__Main__':
    test = Animal()
