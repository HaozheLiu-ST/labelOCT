# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from QtImageViewer import QtImageViewer
import sys

class Ui_MainWindow(object):
    """
    This class is used to instantiate a window
    that contains several different components:
    pushbutton graghicView and textbrowser.
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 452)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageviewer = QtImageViewer(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.imageviewer.sizePolicy().hasHeightForWidth())

        self.imageviewer.setSizePolicy(sizePolicy)
        self.imageviewer.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.imageviewer)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Point_2 = QtWidgets.QPushButton(self.centralWidget)
        self.Point_2.setObjectName("Point_2")
        self.verticalLayout.addWidget(self.Point_2)

        self.Draw = QtWidgets.QPushButton(self.centralWidget)
        self.Draw.setObjectName("Draw")
        self.verticalLayout.addWidget(self.Draw)

        self.Erase = QtWidgets.QPushButton(self.centralWidget)
        self.Erase.setObjectName("Erase")
        self.verticalLayout.addWidget(self.Erase)

        self.Point = QtWidgets.QPushButton(self.centralWidget)
        self.Point.setObjectName("Point")
        self.verticalLayout.addWidget(self.Point)

        self.horizontalSlider = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)

        self.Rect = QtWidgets.QPushButton(self.centralWidget)
        self.Rect.setObjectName("Rect")
        self.verticalLayout.addWidget(self.Rect)

        self.Save = QtWidgets.QPushButton(self.centralWidget)
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setAutoFillBackground(True)

        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 664, 22))

        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)

        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)

        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LabelOCT"))
        self.Draw.setText(_translate("MainWindow", "Draw"))
        self.Erase.setText(_translate("MainWindow", "Erase"))
        self.Point_2.setText(_translate("MainWindow", "Load"))
        self.Point.setText(_translate("MainWindow", "Point"))
        self.Rect.setText(_translate("MainWindow", "Rect"))
        self.Save.setText(_translate("MainWindow", "Save"))
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
