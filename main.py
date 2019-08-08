#encoding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Lib.mainWindow import Ui_MainWindow
from Lib.readSequence import ReadSequence
from Lib.ImageProccess import Loader
from Lib.ImageDrawer import Drawer
from Lib.ImageSave import Saver
from skimage import io
import numpy as np
class mainWindow(Ui_MainWindow):
    """docstring for mainWindow. the main of the program"""

    def __init__(self,MainWindow):
        super(mainWindow, self).__init__()
        super(mainWindow,self).setupUi(MainWindow)
        self.viewer_init()
        self.connect_init()
        self.slider_init()
        self.drawFlag = 1
        self.eraseFlag = 0
        self.pointFlag = 1
        self.rectFlag = 0
        self.pointR = 1
        self.Flag = 0
    def slider_init(self):
        """
        init the slider widget
        """
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider.valueChanged.connect(self.CricleRChange)

    def viewer_init(self):
        """
        init the image viewer for widget
        """
        self.imageviewer.aspectRatioMode = Qt.KeepAspectRatio
        self.imageviewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.imageviewer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.imageviewer.canZoom = True
        self.imageviewer.canPan = True

    def setupUi(self,MainWindow):
        """
        set up the ui of the mainWindow
        """
        super(mainWindow,self).setupUi(MainWindow)

    def connect_init(self):
        """
        init the connect between widget and the function
        """
        self.Point_2.clicked.connect(self.opendir)
        self.Save.clicked.connect(self.saveOp)
        self.Point.clicked.connect(self.pointOp)
        self.Rect.clicked.connect(self.rectOp)
        self.Draw.clicked.connect(self.drawOp)
        self.Erase.clicked.connect(self.eraseOp)
        # self.pushButton.clicked.connect(self.printout)
    def pointOp(self):
        """
        set the point operation, then you can use the point to draw
        """
        self.printout('Set the state: Point!')
        self.rectFlag = 0
        self.pointFlag = 1
    def rectOp(self):
        """
        set the rect operation, then you can use the left of mouse to draw a rect.
        """
        self.printout('Set the state: Rect!')
        self.rectFlag = 1
        self.pointFlag = 0
    def drawOp(self):
        """
        set the state to draw
        """
        self.printout('Set the state: Draw!')
        self.eraseFlag = 0
        self.drawFlag  = 1

    def eraseOp(self):
        """
        set the state to erase
        """
        self.printout('Set the state: Erase!')
        self.eraseFlag = 1
        self.drawFlag = 0
    def detect_state(self):
        rectF = self.rectFlag
        pointF = self.pointFlag
        eraseF = self.eraseFlag
        drawF = self.drawFlag
        if rectF+pointF==0 or eraseF+drawF==0:
            return False,'There is nothing you set for the operation named LABEL'
        else:
            return True,'Set the state for LABEL Successful!'

    def printout(self,strVar):
        """
        print the strVar in the text browse.
        """
        self.textBrowser.append(strVar)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
    def saveOp(self):
        """
        save the label
        """
        save_dir = QFileDialog.getExistingDirectory(None,'Choose the directory to save','.')
        self.printout('Init the save path: ' + save_dir)
        if save_dir != '' and self.saveFlag :
            try:
                self.save = Saver(self.readSequence.data_list,save_dir,self.drawer.labelm,self.recon.img.shape)
                self.save.trigger.connect(self.saveFinish)
            except Exception as e:
                self.printout('There is some thing wrong in the Save Init Operation!')
            else:
                self.printout('Save init Successful! ')
            self.save.start()
    def saveFinish(self):
        self.printout(self.save.log[1])

    def opendir(self):
        """
        init the readSequence and get the path list
        """
        open_dir = QFileDialog.getExistingDirectory(None,'Import a sequence data','.')
        readSequence = ReadSequence(open_dir)
        log = readSequence.boollog()
        self.printout(log[1])
        if log[0]:
            self.path_list = readSequence.read()
            self.printout(readSequence.log[1])
            if readSequence.log[0]:
                self.printout(readSequence.datalog())
                self.loadim()
                self.readSequence = readSequence
    def loadim(self):
        """
        load the data and run the operation of reconstruct
        """
        self.recon = Loader(self.path_list)
        self.recon.trigger.connect(self.picshow)
        self.printout('Loader is init')
        log = self.recon.imgLog()
        self.printout(log[1])
        if(log[0]):
            self.printout('Computing and reconstruct the sequence to 2d!')
            self.printout('This proccess may need a few minutes...')
            self.printout('The caffee time~')
            self.recon.start()

    def picshow(self):
        """
        show the picture of the reconstruction
        """
        self.printout(self.recon.log[1])
        if(self.recon.log[0]):
            self.imageviewer.leftMouseButtonPressed.connect(self.handleLeftClick)
            self.imageviewer.leftMouseButtonReleased.connect(self.leftMouseReleased)
            self.img = self.recon.img_recon
            self.drawer = Drawer(self.img)
            self.frame = QImage(self.img,self.img.shape[1],self.img.shape[0],QImage.Format_Indexed8)
            self.imageviewer.setImage(self.frame)

    def handleLeftClick(self, x, y):
        """
        label the point and rect
        """
        self.row = int(y)
        self.column = int(x)
        if self.drawFlag*self.pointFlag == 1:
            self.img = self.drawer.drawPoint(self.row, self.column, self.pointR)
        if self.eraseFlag * self.pointFlag == 1:
            self.img = self.drawer.erasePoint(self.row, self.column, self.pointR)
        self.frame=QImage(self.img,self.img.shape[1],self.img.shape[0],QImage.Format_Indexed8)
        self.imageviewer.setImage(self.frame)
        self.saveFlag = 1
    def leftMouseReleased(self,x,y):
        """
        label the rect
        """
        row = int(y)
        column = int(x)
        if self.drawFlag*self.rectFlag == 1:
            self.img = self.drawer.drawRect(self.row, self.column, row, column)
        if self.eraseFlag*self.rectFlag == 1:
            self.img = self.drawer.eraseRect(self.row, self.column, row, column)
        self.frame=QImage(self.img,self.img.shape[1],self.img.shape[0],QImage.Format_Indexed8)
        self.imageviewer.setImage(self.frame)
    def CricleRChange(self):
        """
        set the r of the point, circle i.e.
        """
        self.pointR = self.horizontalSlider.value()
        self.printout('Set the Radius of Cricle: ' + str(self.pointR))
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('./logo.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
