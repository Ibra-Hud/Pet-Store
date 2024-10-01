'''
Ibrahim Hudson
4/2/2024
Comp 163 - 001
Creating Lizard Class
'''

# Importing is a relationship class
from Reptile import Reptile
# Creating class Lizard
class Lizard(Reptile):
    # Setting attributes
    name: str
    size: str
    weight: float
    def __init__(self):
        super().__init__()
        self.name = ''
        self.size = ''
        self.weight = 0.00
        self.color = ''
        self.habitat = ''
        self.frill = False
        self.spikes = False

    # Def all the required methods
    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getSize(self) -> str:
        return self.__size

    def setSize(self, size: str):
        self.__size = size

    def getWeight(self) -> float:
        return self.__weight

    def setWeight(self, weight: float):
        self.__weight = weight

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str):
        self.__color = color

    def getHabitat(self) -> str:
        return self.__habitat

    def setHabitat(self, habitat: str):
        self.__habitat = habitat

    def hasFrill(self) -> bool:
        return self.__frill

    def setFrill(self, frill: bool):
        self.__frill = frill

    def hasSpikes(self) -> bool:
        return self.__spikes

    def setSpikes(self, spikes: bool)   :
        self.__spikes = spikes

if __name__ == '__Main__':
    test = Lizard()

