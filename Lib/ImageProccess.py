# -*- coding: utf-8 -*-

import numpy as np
from skimage import io,color
from readSequence import ReadSequence
from PyQt5.QtCore import *
class Loader(QThread):
    """docstring for Reconstruct.
    load the image,
    provides the start() interface to run the load and reconstruct
    self.img_recon is the result of the reconstrution of the sequence data
    self.img is the example of the sequence data
    self.imgLog() is the test of the loading
    """
    trigger = pyqtSignal()
    def __init__(self, PathList):
        """
        Pathlist is the path list of the data,the element is a class which has two attribution:path and key.
        """
        super(Loader, self).__init__()
        self.PathList = PathList
        self.img_recon = []
        print self.trigger
    def run(self):
        self.log = self.load()
        self.trigger.emit()
    def imgLog(self):
        try:
            self.img = self.readImage(self.PathList[0].path)
            self.img = np.array(self.img)
        except Exception,e:
            return False,'There is something wrong in the proccess of load image!'
        else:
            return True,'Image shape is ' + str(self.img.shape)
    def load(self):
        """
        this is the core of this class
        """
        try:
            for path in self.PathList:
                self.img = self.readImage(path.path)
                img = self.add_sum(self.img)
                self.reconstruct(img)
        except Exception as e:
            return False,'There is something wrong in the proccess of reconstrution!'
        else:
            self.recons_procc()
            return True,'Reconstruction successful!'
    def readImage(self, path):
        img = io.imread(path)
        if(len(img.shape)<3):
            return img
        else:
            return color.rgb2gray(img)
    def reconstruct(self,img):
        self.img_recon.append(img)
    def add_sum(self,img):
        return np.sum(img,axis=0)
    def recons_procc(self):
        """
        do some image algorithm to strengthen the image.
        """
        img_recon = np.array(self.img_recon)
        img_recon = img_recon.astype(np.float32)
        max_ = np.max(self.img_recon)
        min_ = np.min(self.img_recon)
        img_recon = (img_recon - min_) / (max_ - min_)
        img_recon = img_recon * 255

        self.img_recon = img_recon.astype(np.uint8)
if __name__ == '__main__':
    readSequence = ReadSequence('/Users/wangsir/Desktop/recent/wangsir/sweatGland/predict/B37left-1-male-2/original_L')
    readSequence.boollog()
    readSequence.read()
    readSequence.datalog()
    recon = Loader(readSequence.data_list)
    recon.load()
    print recon.imgLog
    import matplotlib.pyplot as plt
#    print np.max(recon.img_recon),np.min(recon.img_recon),recon.img_recon.shape
    plt.imshow(recon.img_recon)
    print('run successful')
    print(recon.img_recon.shape)
    plt.show()
