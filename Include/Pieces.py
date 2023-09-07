import sys
import dragging

class Pieces:
    def __init__(self, currenPosition):
        self.currenPosition = currenPosition

    def moving(self, releasedPosition):
        released_x, released_y = releasedPosition[:2]
        drag_x, drag_y = self.currenPosition.x(), self.currenPosition.y()

        released_punkt = None
        drag_punkt = None

        for i, point in enumerate(dragging.coordinates):
            if point[:2] == releasedPosition[:2]:
                released_punkt = point
            elif point[0] == drag_x and point[1] == drag_y:
                drag_punkt = point

        if released_punkt and not released_punkt[2]:
            released_punkt[2] = True
            if drag_punkt and drag_punkt[2]:
                drag_punkt[2] = False
            return True

        return False


class Pawn(Pieces):
    def __init__(self, currenPosition):
        self.currenPosition = currenPosition

    def legalPawnMove(self,releasedPosition):
        index = None
        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                print("ala")
                index = i
                break
        print(index)
        if releasedPosition[:2] == dragging.coordinates[index + 8][:2] and not dragging.coordinates[index + 8][2]:
            dragging.coordinates[i+8][2] = True
            return True
        return False

