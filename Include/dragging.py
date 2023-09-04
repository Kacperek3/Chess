import sys
import math
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtGui import QCursor


#-------------------------------
#   numberFigure

# rock      - 1
# horse     - 2
# bishop    - 3
# queen     - 4
# king      - 5
# pawn      - 6
#-------------------------------


def find_nearest_coordinate(x, y, coordinates):
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

coordinates = [(45,40), (145,40),(245,40),(345,40), (445,40), (545,40),(645,40), (745,40),
               (45,140), (145,140),(245,140),(345,140), (445,140), (545,140),(645,140), (745,140),
               (45,240), (145,240),(245,240),(345,240), (445,240), (545,240),(645,240), (745,240),
               (45,340), (145,340),(245,340),(345,340), (445,340), (545,340),(645,340), (745,340),
               (45,440), (145,440),(245,440),(345,440), (445,440), (545,440),(645,440), (745,440),
               (45,540), (145,540),(245,540),(345,540), (445,540), (545,540),(645,540), (745,540),
               (45,640), (145,640),(245,640),(345,640), (445,640), (545,640),(645,640), (745,640),
               (45,740), (145,740),(245,740),(345,740), (445,740), (545,740),(645,740), (745,740)]


class DraggableSvgItem(QGraphicsSvgItem):

    def __init__(self, svg_file, numberFigure = 6):
        self.numberFigure = numberFigure
        self.positionBeforeDrag = None
        super().__init__(svg_file)
        self.setFlag(QGraphicsSvgItem.ItemIsMovable)

    def mousePressEvent(self, event):
        self.positionBeforeDrag = self.pos()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):

        position = self.pos()
        if position.x() < 0 or position.x() > 800 or position.y() < 0 or position.y() > 800:
            self.setPos(self.positionBeforeDrag)
        else:
            nearest_coordinate = find_nearest_coordinate(position.x(),position.y(),coordinates)
            self.setPos(nearest_coordinate[0], nearest_coordinate[1])

            self.positionBeforeDrag = None
        super().mouseReleaseEvent(event)

