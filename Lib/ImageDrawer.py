#encoding:utf-8
from skimage import io
from skimage import draw
import numpy as np
class Drawer(object):
    """docstring for Drawer."""

    def __init__(self,img):
        super(Drawer, self).__init__()
        self.img = img
        self.labelm = np.ones(img.shape)
    def _draw(self,index):
        self.labelm[index[0],index[1]] = 0
        self.result = self.img * self.labelm
    def _erase(self,index):
        self.labelm[index[0],index[1]] = 1
        self.result = self.labelm * self.img


    def drawPoint(self,x,y,r):
        xx, yy = draw.circle(x,y,r)
        self._draw([xx,yy])
        return self.result.astype(np.uint8)
    def drawRect(self,x1,y1,x2,y2):
        xx = [x1,x1,x2,x2]
        yy = [y1,y2,y2,y1]
        rr,cc = draw.polygon(xx, yy)
        self._draw([rr,cc])
        return self.result.astype(np.uint8)
    def erasePoint(self,x,y,r):
        xx, yy = draw.circle(x,y,r)
        self._erase([xx,yy])
        return self.result.astype(np.uint8)
    def erasePoint(self,x,y,r):
        xx, yy = draw.circle(x,y,r)
        self._erase([xx,yy])
        return self.result.astype(np.uint8)
    def eraseRect(self,x1,y1,x2,y2):
        xx = [x1,x1,x2,x2]
        yy = [y1,y2,y2,y1]
        rr,cc = draw.polygon(xx, yy)
        self._erase([rr,cc])
        return self.result.astype(np.uint8)
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    img = np.ones([100,200])
    drawer = Drawer(img)
    drawer.drawPoint(10,10, 10)
#    drawer.eraseRect(10, 10, 100, 100)
    plt.imshow(drawer.result)
    plt.show()
