import sys
import math
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtGui import QCursor
from Pieces import Pieces, Pawn, Horse, Bishop, Rock, Queen, King



#-------------------------------
#   numberFigure

# rock      - 1
# horse     - 2
# bishop    - 3
# queen     - 4
# king      - 5
# pawn      - 6
#-------------------------------


coordinates = [[45, 40, True], [145, 40, True], [245, 40, True], [345, 40, True], [445, 40, True],
                            [545, 40, True], [645, 40, True], [745, 40, True],
                            [45, 140, True], [145, 140, True], [245, 140, True], [345, 140, True], [445, 140, True],
                            [545, 140, True], [645, 140, True], [745, 140, True],
                            [45, 240, False, None], [145, 240, False, None], [245, 240, False, None], [345, 240, False, None],
                            [445, 240, False, None],
                            [545, 240, False, None], [645, 240, False, None], [745, 240, False, None],
                            [45, 340, False, None], [145, 340, False, None], [245, 340, False, None], [345, 340, False, None],
                            [445, 340, False, None],
                            [545, 340, False, None], [645, 340, False, None], [745, 340, False, None],
                            [45, 440, False, None], [145, 440, False, None], [245, 440, False, None], [345, 440, False, None],
                            [445, 440, False, None],
                            [545, 440, False, None], [645, 440, False, None], [745, 440, False, None],
                            [45, 540, False, None], [145, 540, False, None], [245, 540, False, None], [345, 540, False, None],
                            [445, 540, False, None],
                            [545, 540, False, None], [645, 540, False, None], [745, 540, False, None],
                            [45, 640, True], [145, 640, True], [245, 640, True], [345, 640, True], [445, 640, True],
                            [545, 640, True], [645, 640, True], [745, 640, True],
                            [45, 740, True], [145, 740, True], [245, 740, True], [345, 740, True], [445, 740, True],
                            [545, 740, True], [645, 740, True], [745, 740, True]]

def find_nearest_coordinate(x, y):
    def distance(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

    nearest_coord = coordinates[0]
    min_distance = distance((x, y), nearest_coord)

    for coord in coordinates:
        dist = distance((x, y), coord)
        if dist < min_distance:
            min_distance = dist
            nearest_coord = coord
    return nearest_coord

class DraggableSvgItem(QGraphicsSvgItem):
    i = 0
    def __init__(self, svg_file, numberFigure, color, mainScene):
        # new
        if DraggableSvgItem.i == 16:
            DraggableSvgItem.i = 48
        coordinates[DraggableSvgItem.i].append(self)
        DraggableSvgItem.i += 1
        #

        self.scene = mainScene
        self.numberFigure = numberFigure
        self.positionBeforeDrag = None
        self.color = color
        super().__init__(svg_file)
        self.setFlag(QGraphicsSvgItem.ItemIsMovable)
        self.red_square = None

        self.figure_classes = {
            1: Rock,
            2: Horse,
            3: Bishop,
            4: Queen,
            5: King,
            6: Pawn
        }
    def mousePressEvent(self, event):
        self.setFlag(QGraphicsSvgItem.ItemIsMovable, True)
        self.positionBeforeDrag = self.pos()

        self.current_figure = self.figure_classes.get(self.numberFigure)(self.positionBeforeDrag, self.color, self.scene)

        # adding a red square to program
        self.red_square = QGraphicsSvgItem("C:\\Users\\kapis\\OneDrive - Politechnika Gdańska\\Pulpit\\Python\\Pycharm\\chess\\Include\\images\\czerwony_kwadrat.svg")
        self.red_square.setPos(self.positionBeforeDrag.x() - 18, self.positionBeforeDrag.y() - 13)
        self.scene.addItem(self.red_square)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        position = self.pos()
        if 9 <= position.x() <= 785 and 9 <= position.y() <= 785:
            super().mouseMoveEvent(event)
        else:
            self.setPos(self.positionBeforeDrag)
            self.setFlag(QGraphicsSvgItem.ItemIsMovable, False)

    def mouseReleaseEvent(self, event):
        position = self.pos()

        nearest_coordinate = find_nearest_coordinate(position.x(),position.y())

        if self.current_figure.validate_move(nearest_coordinate):
            self.setPos(nearest_coordinate[0], nearest_coordinate[1])
        else:
            self.setPos(self.positionBeforeDrag)

        self.positionBeforeDrag = None

        self.scene.removeItem(self.red_square)
        super().mouseReleaseEvent(event)
