#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint


class Point(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(400, 150, 500, 500)
        self.setWindowTitle('Game of Life')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):

        qp.setPen(Qt.blue)
        size = self.size()
        x = random.randint(1, size.width()-1)
        y = random.randint(1, size.height()-1)
        qp.drawPoint(x, y)
        
     def pointNeighbours(self, x, y)
    
        life = 0
       
        if x-1 and y-1:
            life += 1
        if x-1 and j:
            life += 1
        if x-1 and y+1:
            life += 1
        
        if y-1 and x:
            ctr += 1
        if y+1 and x:
            life += 1
        
        if x+1 and y-1:
            life += 1
        if x+1 and y:
            life += 1
        if x+1 and y+1:
            life += 1

        return life
   #set()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Point()
    sys.exit(app.exec_())
