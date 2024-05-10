import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtGui, QtCore
from gui.qt.main_ui import Ui_windowMain

import gui.pages as pages
import gui.restaraunts as restaraunts


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_windowMain()
        self.ui.setupUi(self)

        self.ui.widget_Photos.setFixedHeight(401)
        self.ui.widget_Photos.setFixedWidth(701)
        self.ui.pushButton_NextImage.setFixedHeight(401)
        self.ui.pushButton_PrevImage.setFixedHeight(401)
        self.currentPhotoIndex = 0
        self.ui.widget_Photos.setStyleSheet("#widget_Photos {image: url(" + restaraunts.RESTARAUNTS_PHOTOS_ARRAY[self.currentPhotoIndex] + ");}")
        self.ui.pushButton_NextImage.clicked.connect(self.doChangePage)
        self.ui.pushButton_PrevImage.clicked.connect(self.doChangePage)

    def doChangePage(self):
        button = self.sender()
        if button == self.ui.pushButton_NextImage:
            if self.currentPhotoIndex < len(restaraunts.RESTARAUNTS_PHOTOS_ARRAY) - 1:
                self.currentPhotoIndex += 1
            else: 
                self.currentPhotoIndex = 0
        if button == self.ui.pushButton_PrevImage:
            if self.currentPhotoIndex != 0:
                self.currentPhotoIndex -= 1
            else: 
                self.currentPhotoIndex = len(restaraunts.RESTARAUNTS_PHOTOS_ARRAY) - 1

        self.ui.widget_Photos.setStyleSheet("#widget_Photos {image: url(" + restaraunts.RESTARAUNTS_PHOTOS_ARRAY[self.currentPhotoIndex] + ");}")
 
if __name__ == "__main__":
    with open("NtiWorks/Kursovaya/Application/gui/qt/style.qss","r") as f:
        style_str = f.read()

    app = QApplication(sys.argv)

    window = MainWindow()
    #window.ui.pushButton_NextImage.setIcon(QtGui.QIcon("NtiWorks/Kursovaya/resources/icons/white-arrow-3_right.png"))
    #window.ui.pushButton_PrevImage.setIcon(QtGui.QIcon("NtiWorks/Kursovaya/resources/icons/white-arrow-3_left.png"))
    #window.ui.widget_Photos.setStyleSheet("#widget_Photos {image: url(NtiWorks/Kursovaya/resources/photos/jungle_1-1.png);}")
    window.setStyleSheet(style_str)
    window.show()

    sys.exit(app.exec())