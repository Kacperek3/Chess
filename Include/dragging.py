import sys
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtGui import QCursor

class DraggableSvgItem(QGraphicsSvgItem):
    def __init__(self, svg_file):
        super().__init__(svg_file)
        self.setFlag(QGraphicsSvgItem.ItemIsMovable)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)