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
                index = i
                break
        if releasedPosition[:2] == dragging.coordinates[index + 8][:2] and not dragging.coordinates[index + 8][2]:
            dragging.coordinates[i+8][2] = True
            dragging.coordinates[index][2] = False
            return True
        return False


class Horse(Pieces):
    def __init__(self, currenPosition):
        self.currenPosition = currenPosition

    def minusoutOfRange(self, index, n):
        if index - n >0:
            return dragging.coordinates[index - n][:2]
        else:
            return False
    def plusoutOfRange(self, index, n):
        if index + n <64:
            return dragging.coordinates[index + n][:2]
        else:
            return False
    def isStandingMinus(self, index, n):
        if index - n >0:
            if not dragging.coordinates[index - n][2]:
                return True
            return False
        return False
    def isStandingPlus(self, index, n):
        if index + n < 64:
            if not dragging.coordinates[index + n][2]:
                return True
            return False
        return False

    def legalHorseMove(self, releasedPosition):
        index = None
        targetIndex = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i

        if ((releasedPosition[:2] == self.plusoutOfRange(index, 15) and self.isStandingPlus(index,15))
                or(releasedPosition[:2] == self.plusoutOfRange(index, 17) and self.isStandingPlus(index,17))
                or(releasedPosition[:2] == self.plusoutOfRange(index, 10) and self.isStandingPlus(index,10))
                or(releasedPosition[:2] == self.plusoutOfRange(index, 6) and self.isStandingPlus(index,6))
                or(releasedPosition[:2] == self.minusoutOfRange(index, 17) and self.isStandingMinus(index,17))
                or(releasedPosition[:2] == self.minusoutOfRange(index, 10) and self.isStandingMinus(index,10))
                or(releasedPosition[:2] == self.minusoutOfRange(index, 6) and self.isStandingMinus(index,6))
                or(releasedPosition[:2] == self.minusoutOfRange(index, 15) and self.isStandingMinus(index,15))):
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[index][2] = False
            return True
        return False

class Bishop(Pieces):
    def __init__(self, currenPosition):
        self.currenPosition = currenPosition

    def legalBishopMove(self, releasedPosition):
        index = None
        targetIndex = None
        memory = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
                memory = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i
        if (self.recursionRightUp(index, targetIndex, memory)
                or self.recursionLeftUp(index,targetIndex,memory)
                or self.recursionRightDown(index,targetIndex,memory)
                or self.recursionLeftDown(index,targetIndex,memory)):
            return True
        else:
            return False

    def recursionRightUp(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        if (dragging.coordinates[index - 7][2] == False
                and index != 7
                and index != 15
                and index != 23
                and index != 31
                and index != 39
                and index != 47
                and index != 55
                and index != 63):
            return self.recursionRightUp(index - 7, targetIndex, memory)
        return False

    def recursionLeftUp(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        if (dragging.coordinates[index - 9][2] == False
                and index != 0
                and index != 8
                and index != 16
                and index != 24
                and index != 32
                and index != 40
                and index != 48
                and index != 56):
            return self.recursionLeftUp(index - 9, targetIndex, memory)
        return False

    def recursionRightDown(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        if index + 9 > 63:
            return False
        if (dragging.coordinates[index + 9][2] == False
                and index != 7
                and index != 15
                and index != 23
                and index != 31
                and index != 39
                and index != 47
                and index != 55
                and index != 63):
            return self.recursionRightDown(index + 9, targetIndex, memory)
        return False

    def recursionLeftDown(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        if index + 7 > 63:
            return False
        if (dragging.coordinates[index + 7][2] == False
                and index != 0
                and index != 8
                and index != 16
                and index != 24
                and index != 32
                and index != 40
                and index != 48
                and index != 56):
            return self.recursionLeftDown(index + 7, targetIndex, memory)
        return False