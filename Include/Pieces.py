import sys
import dragging

class Pieces:
    def __init__(self, currenPosition):
        self.currenPosition = currenPosition

    def friendlyFire(self, targetIndex):
        return self.color == dragging.coordinates[targetIndex][3].color

class Pawn(Pieces):
    def __init__(self, currenPosition, color, scene):
        self.currenPosition = currenPosition
        self.color = color
        self.scene = scene

    def validate_move(self, releasedPosition):
        index = None
        targetIndex = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i

        if self.color == "black":
            if index == 8 or index == 9 or index == 10 or index == 11 or index == 12 or index == 13 or index == 14 or index == 15:
                if ((releasedPosition[2] == False and index + 8 == targetIndex)
                    or (releasedPosition[2] == False and index + 16 == targetIndex)):
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    return True

                elif ((releasedPosition[2] == True and index + 7 == targetIndex)
                    or (releasedPosition[2] == True and index + 9 == targetIndex)):
                    if self.friendlyFire(targetIndex):
                        return False

                    self.scene.removeItem(dragging.coordinates[targetIndex][3])
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    return True
            else:
                if releasedPosition[2] == False and index + 8 == targetIndex:
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    return True
                elif ((releasedPosition[2] == True and index + 7 == targetIndex)
                    or (releasedPosition[2] == True and index + 9 == targetIndex)):
                    if self.friendlyFire(targetIndex):
                        return False

                    self.scene.removeItem(dragging.coordinates[targetIndex][3])
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    return True

        else:
            if index == 48 or index == 49 or index == 50 or index == 51 or index == 52 or index == 53 or index == 54 or index == 55:
                if ((releasedPosition[2] == False and index - 8 == targetIndex)
                        or (releasedPosition[2] == False and index - 16 == targetIndex)):
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    return True

                elif ((releasedPosition[2] == True and index - 7 == targetIndex)
                      or (releasedPosition[2] == True and index - 9 == targetIndex)):
                    if self.friendlyFire(targetIndex):
                        return False

                    self.scene.removeItem(dragging.coordinates[targetIndex][3])
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    return True
            else:
                if releasedPosition[2] == False and index - 8 == targetIndex:
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    return True
                elif ((releasedPosition[2] == True and index - 7 == targetIndex)
                      or (releasedPosition[2] == True and index - 9 == targetIndex)):
                    if self.friendlyFire(targetIndex):
                        return False

                    self.scene.removeItem(dragging.coordinates[targetIndex][3])
                    dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
                    dragging.coordinates[index][3] = None
                    dragging.coordinates[targetIndex][2] = True
                    dragging.coordinates[index][2] = False
                    return True
        return False


class Horse(Pieces):
    def __init__(self, currenPosition, color, scene):
        self.currenPosition = currenPosition
        self.color = color
        self.scene = scene

    def validate_move(self, releasedPosition):
        index = None
        targetIndex = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i

        if ((releasedPosition[2] == False and index + 15 == targetIndex)
                or(releasedPosition[2] == False and index - 15 == targetIndex)
                or(releasedPosition[2] == False and index + 17 == targetIndex)
                or(releasedPosition[2] == False and index - 17 == targetIndex)
                or(releasedPosition[2] == False and index + 10 == targetIndex)
                or(releasedPosition[2] == False and index - 10 == targetIndex)
                or(releasedPosition[2] == False and index + 6  == targetIndex)
                or(releasedPosition[2] == False and index - 6  == targetIndex)):
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[index][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
            dragging.coordinates[index][3] = None
            return True

        elif ((releasedPosition[2] == True and index + 15 == targetIndex)
                or (releasedPosition[2] == True and index - 15 == targetIndex)
                or (releasedPosition[2] == True and index + 17 == targetIndex)
                or (releasedPosition[2] == True and index - 17 == targetIndex)
                or (releasedPosition[2] == True and index + 10 == targetIndex)
                or (releasedPosition[2] == True and index - 10 == targetIndex)
                or (releasedPosition[2] == True and index + 6 == targetIndex)
                or (releasedPosition[2] == True and index - 6 == targetIndex)):

            if self.friendlyFire(targetIndex):
                return False

            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
            dragging.coordinates[index][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[index][2] = False
            return True

        return False


class King(Pieces):
    def __init__(self, currenPosition, color, scene):
        self.currenPosition = currenPosition
        self.color = color
        self.scene = scene

    def validate_move(self, releasedPosition):
        index = None
        targetIndex = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i

        if ((releasedPosition[2] == False and index - 8 == targetIndex)
                or(releasedPosition[2] == False and index - 7 == targetIndex)
                or(releasedPosition[2] == False and index - 9 == targetIndex)
                or(releasedPosition[2] == False and index + 1 == targetIndex)
                or(releasedPosition[2] == False and index - 1 == targetIndex)
                or(releasedPosition[2] == False and index + 7 == targetIndex)
                or(releasedPosition[2] == False and index + 8 == targetIndex)
                or(releasedPosition[2] == False and index + 9 == targetIndex)):
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[index][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
            dragging.coordinates[index][3] = None
            return True

        elif ((releasedPosition[2] == True and index - 8 == targetIndex)
                or (releasedPosition[2] == True and index - 7 == targetIndex)
                or (releasedPosition[2] == True and index - 9 == targetIndex)
                or (releasedPosition[2] == True and index + 1 == targetIndex)
                or (releasedPosition[2] == True and index - 1 == targetIndex)
                or (releasedPosition[2] == True and index + 7 == targetIndex)
                or (releasedPosition[2] == True and index + 8 == targetIndex)
                or (releasedPosition[2] == True and index + 9 == targetIndex)):

            if self.friendlyFire(targetIndex):
                return False

            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[index][3]
            dragging.coordinates[index][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[index][2] = False
            return True
        return False

class Bishop(Pieces):
    def __init__(self, currenPosition, color, scene):
        self.currenPosition = currenPosition
        self.color = color
        self.scene = scene

    def validate_move(self, releasedPosition):
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
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
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

        elif dragging.coordinates[index - 7][2] == True and index - 7 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False
            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True

        return False

    def recursionLeftUp(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
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

        elif dragging.coordinates[index - 9][2] == True and index - 9 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False
            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True

        return False

    def recursionRightDown(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
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

        elif dragging.coordinates[index + 9][2] == True and index + 9 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False
            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        return False

    def recursionLeftDown(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
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

        elif dragging.coordinates[index + 7][2] == True and index + 7 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False
            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True

        return False


class Rock(Pieces):
    def __init__(self, currenPosition, color, scene):
        self.currenPosition = currenPosition
        self.color = color
        self.scene = scene
    def validate_move(self, releasedPosition):
        index = None
        targetIndex = None
        memory = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
                memory = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i

        if (self.recursionUp(index, targetIndex, memory)
                or self.recursionLeft(index,targetIndex,memory)
                or self.recursionDown(index,targetIndex,memory)
                or self.recursionRight(index,targetIndex,memory)):
            return True
        else:
            return False

    def recursionUp(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            return True
        if dragging.coordinates[index - 8][2] == False:
            return self.recursionUp(index - 8, targetIndex, memory)

        elif dragging.coordinates[index - 8][2] == True and index - 8 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False

            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True

        return False

    def recursionLeft(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            return True
        if (dragging.coordinates[index - 1][2] == False
                and index != 0
                and index != 8
                and index != 16
                and index != 24
                and index != 32
                and index != 40
                and index != 48
                and index != 56):
            return self.recursionLeft(index - 1, targetIndex, memory)
        elif dragging.coordinates[index - 1][2] == True and index - 1 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False

            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        return False

    def recursionDown(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            return True
        if index + 8 > 63:
            return False
        if dragging.coordinates[index + 8][2] == False:
            return self.recursionDown(index + 8, targetIndex, memory)
        elif dragging.coordinates[index + 8][2] == True and index + 8 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False

            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        return False

    def recursionRight(self, index, targetIndex, memory):
        if index == targetIndex:
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            return True
        if index == 63:
            return False
        if (dragging.coordinates[index + 1][2] == False
                and index != 7
                and index != 15
                and index != 23
                and index != 31
                and index != 39
                and index != 47
                and index != 55
                and index != 63):
            return self.recursionRight(index + 1, targetIndex, memory)
        elif dragging.coordinates[index + 1][2] == True and index + 1 == targetIndex:
            if self.friendlyFire(targetIndex):
                return False

            self.scene.removeItem(dragging.coordinates[targetIndex][3])
            dragging.coordinates[targetIndex][3] = dragging.coordinates[memory][3]
            dragging.coordinates[memory][3] = None
            dragging.coordinates[targetIndex][2] = True
            dragging.coordinates[memory][2] = False
            return True
        return False

class Queen(Rock,Bishop):
    def __init__(self, currenPosition, color, scene):
        self.currenPosition = currenPosition
        self.color = color
        self.scene = scene

    def validate_move(self, releasedPosition):
        index = None
        targetIndex = None
        memory = None

        for i, point in enumerate(dragging.coordinates):
            if point[0] == self.currenPosition.x() and point[1] == self.currenPosition.y():
                index = i
                memory = i
            if point[0] == releasedPosition[0] and point[1] == releasedPosition[1]:
                targetIndex = i

        if (self.recursionUp(index, targetIndex, memory)
                or self.recursionLeft(index, targetIndex, memory)
                or self.recursionDown(index, targetIndex, memory)
                or self.recursionRight(index, targetIndex, memory)
                or self.recursionLeftUp(index, targetIndex, memory)
                or self.recursionRightUp(index, targetIndex, memory)
                or self.recursionLeftDown(index, targetIndex, memory)
                or self.recursionRightDown(index, targetIndex, memory)):
            return True
        else:
            return False

