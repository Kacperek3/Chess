import sys
import dragging

class Pieces:
    def __init__(self, currenPosition):
        self.currenPosition = currenPosition

    def moving(self, releasedPosition, positionBeforeDrag):
        released_x, released_y = releasedPosition[:2]
        drag_x, drag_y = positionBeforeDrag.x(), positionBeforeDrag.y()

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
    print("test")
