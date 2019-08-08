#encoding:utf-8

import numpy as np
from skimage import io,color
from PyQt5.QtCore import *


from readSequence import ReadSequence
from ImageProccess import Loader
from ImageDrawer import Drawer

class Saver(QThread):
    """
    docstring for Saver.
    Saver is used to save the annotated image
    and provides the start() interface to the outside.
    You can use this function to run a new thread to save the image.
    """
    trigger = pyqtSignal()
    def __init__(self,PathList,targetPath,label,shape):
        """
        PathList is the dir path of the original cross section of the data
        targetPath is the dir path of the labeled image.
        shape is the shape of original cross section
        """
        super(Saver, self).__init__()
        self.pathList = PathList
        self.targetPath = targetPath
        self.label = label
        self.shape = shape
    def run(self):
        self.allProc()
        self.trigger.emit()
    def allProc(self):
        try:
            for i in range(self.label.shape[0]):
                var_ind = np.where(self.label[i]==0)[0]
                self.save(i,var_ind)
        except Exception as e:
            self.log = (False,'There is some thing wrong in the proccess of Save!')
        else:
            self.log = (True,'Save successful!')
    def save(self,path_ind,label_ind):
        """
        save two kinds of label one is the real label and the other one is the fusion of label and original data.
        """
        label__ = np.zeros(self.shape)
        label__[:,label_ind] = 1
        img = io.imread(self.pathList[path_ind].path)
        label_ = label__ * 255
        label_ = label_.astype(np.uint8)
        io.imsave(self.targetPath+'/'+'_label_'+str(path_ind+1)+'.png', label_)
        img = img.astype(np.float32)
        if(len(img.shape)>2):
            for i in range(3):
                img[:,:,i] = 0.5 * label_ + 0.5*img[:,:,i]
                maxx = np.max(img[:,:,i])
                minn = np.min(img[:,:,i])
                img[:,:,i] = (img[:,:,i]-minn)/(maxx-minn)
                img[:,:,i] = img[:,:,i]*255
        else:
            img = 0.99 * label_ + 0.01*img
            maxx = np.max(img)
            minn = np.min(img)
            img = (img-minn)/(maxx-minn)
            img = img * 255
        img = img.astype(np.uint8)
        io.imsave(self.targetPath+'/'+'_view_'+str(path_ind+1)+'.png', img)



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    readSequence = ReadSequence('/Users/wangsir/Desktop/recent/wangsir/sweatGland/predict/B37left-1-male-2/original_L')
    readSequence.boollog()
    readSequence.read()
    readSequence.datalog()
    recon = Loader(readSequence.data_list)
    recon.load()
    img = np.ones(recon.img_recon.shape)
    drawer = Drawer(img)
    drawer.drawPoint(40,40,50)
    plt.imshow(drawer.labelm)
    save = Saver(readSequence.data_list,'./',drawer.labelm,recon.img.shape)
    save.allProc()
    plt.show()
