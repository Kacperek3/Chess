import sys

class Pieces:
    def __init__(self, coordinates, currenPosition):
        self.coordinates = coordinates
        self.currenPosition = currenPosition

    def moving(self, releasedPosition):
        for punkt in self.coordinates:
            if punkt[:2] == releasedPosition[:2]:
                if punkt[2] == False:
                    return True
        return False

class Pawn(Pieces):
    print("test")