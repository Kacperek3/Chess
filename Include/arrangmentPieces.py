import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QVBoxLayout
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QCursor
from dragging import DraggableSvgItem
class arrangment(QGraphicsScene):
    def __init__(self, mainScene):
        self.scene = mainScene

    def fullfil(self):

        board = QGraphicsSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\board.svg')
        self.scene.addItem(board)

        #black figure
        #--------------------------------------------------
        BlackRock1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bR.svg')
        BlackRock1.setPos(45, 40)
        self.scene.addItem(BlackRock1)

        BlackHorse1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bN.svg')
        BlackHorse1.setPos(145, 40)
        self.scene.addItem(BlackHorse1)

        BlackBishop1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bB.svg')
        BlackBishop1.setPos(245, 40)
        self.scene.addItem(BlackBishop1)

        BlackQueen = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bQ.svg')
        BlackQueen.setPos(345, 40)
        self.scene.addItem(BlackQueen)

        BlackKing = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bK.svg')
        BlackKing.setPos(445, 40)
        self.scene.addItem(BlackKing)

        BlackBishop2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bB.svg')
        BlackBishop2.setPos(545, 40)
        self.scene.addItem(BlackBishop2)

        BlackHorse2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bN.svg')
        BlackHorse2.setPos(645, 40)
        self.scene.addItem(BlackHorse2)

        BlackRock2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bR.svg')
        BlackRock2.setPos(745, 40)
        self.scene.addItem(BlackRock2)

        BlackPawn1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn1.setPos(45, 140)
        self.scene.addItem(BlackPawn1)

        BlackPawn2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn2.setPos(145, 140)
        self.scene.addItem(BlackPawn2)

        BlackPawn3 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn3.setPos(245, 140)
        self.scene.addItem(BlackPawn3)

        BlackPawn4 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn4.setPos(345, 140)
        self.scene.addItem(BlackPawn4)

        BlackPawn5 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn5.setPos(445, 140)
        self.scene.addItem(BlackPawn5)

        BlackPawn6 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn6.setPos(545, 140)
        self.scene.addItem(BlackPawn6)

        BlackPawn7 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn7.setPos(645, 140)
        self.scene.addItem(BlackPawn7)

        BlackPawn8 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\bP.svg')
        BlackPawn8.setPos(745, 140)
        self.scene.addItem(BlackPawn8)

        #white figure
        #--------------------------------------------------------

        WhiteRock1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wR.svg')
        WhiteRock1.setPos(45, 740)
        self.scene.addItem(WhiteRock1)

        WhiteHorse1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wN.svg')
        WhiteHorse1.setPos(145, 740)
        self.scene.addItem(WhiteHorse1)

        WhiteBishop1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wB.svg')
        WhiteBishop1.setPos(245, 740)
        self.scene.addItem(WhiteBishop1)

        WhiteQueen = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wQ.svg')
        WhiteQueen.setPos(345, 740)
        self.scene.addItem(WhiteQueen)

        WhiteKing = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wK.svg')
        WhiteKing.setPos(445, 740)
        self.scene.addItem(WhiteKing)

        WhiteBishop2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wB.svg')
        WhiteBishop2.setPos(545, 740)
        self.scene.addItem(WhiteBishop2)

        WhiteHorse2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wN.svg')
        WhiteHorse2.setPos(645, 740)
        self.scene.addItem(WhiteHorse2)

        WhiteRock2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wR.svg')
        WhiteRock2.setPos(745, 740)
        self.scene.addItem(WhiteRock2)

        WhitePawn1 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn1.setPos(45, 640)
        self.scene.addItem(WhitePawn1)

        WhitePawn2 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn2.setPos(145, 640)
        self.scene.addItem(WhitePawn2)

        WhitePawn3 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn3.setPos(245, 640)
        self.scene.addItem(WhitePawn3)

        WhitePawn4 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn4.setPos(345, 640)
        self.scene.addItem(WhitePawn4)

        WhitePawn5 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn5.setPos(445, 640)
        self.scene.addItem(WhitePawn5)

        WhitePawn6 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn6.setPos(545, 640)
        self.scene.addItem(WhitePawn6)

        WhitePawn7= DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn7.setPos(645, 640)
        self.scene.addItem(WhitePawn7)

        WhitePawn8 = DraggableSvgItem('C:\\Users\\kapis\\Desktop\\Python\\Pycharm\\chess\\Include\\images\\wP.svg')
        WhitePawn8.setPos(745, 640)
        self.scene.addItem(WhitePawn8)
