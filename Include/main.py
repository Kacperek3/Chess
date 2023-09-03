import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QVBoxLayout
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QCursor
from arrangmentPieces import arrangment

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Chess")
    window.showFullScreen()

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)

    instance = arrangment(scene)
    instance.fullfil()

    central_layout = QVBoxLayout(central_widget)
    central_layout.addWidget(view)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
