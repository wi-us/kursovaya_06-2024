"""

a widget with array of photos
Photos are resing to widget size

"""

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class SlideshowWidget(QWidget):
    widgetWidth = 16*20
    widgetHeight = 9*20

    imagesArray = []
    imagesCurrent = 0
    class ButtonLeftRight():
        button = QPushButton()
        width = 300
        height = 200
        text = ""
        direction = "left"

        def __init__(self, posX : int, posY : int, objectName : str, direction : str, parent : QWidget = None, width : int = width, height : int = height, text : str = text) -> QPushButton:
            self.buttonWidth = width
            self.buttonHeight = height
            self.parent = parent
            self.posX = posX
            self.posY = posY
            self.text = text
            self.objectName = objectName

            self.button.setParent(parent)
            self.button.setGeometry(QtCore.QRect(posX, posY, width, height))
            self.button.setText(text)
            self.button.setObjectName(objectName)
            self.button.clicked.connect(self.doChangePage)
            return self.button
        
        def doChangePage(self):
            if self.direction == "left":
                if self.imagesCurrent != 0:
                    self.imagesCurrent -= 1
                else: 
                    self.imagesCurrent = len(self.imagesArray) - 1
            if self.direction == "right":
                if self.imagesCurrent < len(self.imagesArray) - 1:
                    self.imagesCurrent += 1
                else: 
                    self.imagesCurrent = 0
            
            self.parent.setStyleSheet(f"#{self.parent.objectName()}" + " {image: url(" + self.imagesArray[self.imagesCurrent] + ");}")
        
    widget_Slideshow = QWidget()
    widget_Slideshow.setGeometry(QtCore.QRect(30, 290, 701, 401))
    widget_Slideshow.setObjectName("widget_Slideshow")
    widget_Slideshow.setParent()
    widget_Slideshow.setBaseSize
    
    buttonRight = ButtonLeftRight(posX=(widgetWidth - ButtonLeftRight.buttonWidth),
                         posY=0,
                         parent=widget_Slideshow,
                         objectName="_right",
                         text="")
    
    buttonLeft = ButtonLeftRight(posX=0,
                         posY=0,
                         parent=widget_Slideshow,
                         objectName="_left",
                         text="")
    
    def __init__(self, objectName : str, parent : QWidget = None, posX : int = 0, posY : int = 0, width : int = widgetWidth, height : int = widgetHeight, images : list[str] = None) -> QWidget:
        self.widget_Slideshow.setParent(parent)
        self.widget_Slideshow.setGeometry(QtCore.QRect(posX, posY, width, height))
        self.widget_Slideshow.setStyleSheet(f"#{self.widget_Slideshow.objectName()}" + " {image: url(" + self.imagesArray[self.imagesCurrent] + ");}")
        self.widget_Slideshow.setObjectName(objectName)
        self.imagesArray = images

        return self.widget_Slideshow

    
    @property.setter
    def setSize(self, width : int = None, height : int = None):
        if width != None: 
            self.widgetWidth = width
            self.widget_Slideshow.setFixedWidth(width)
        if height != None: 
            self.widgetHeight = height
            self.widget_Slideshow.setFixedHeight(height)
        
    
    