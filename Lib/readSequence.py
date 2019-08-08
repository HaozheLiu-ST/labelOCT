#encoding:utf-8
import os
import re
class Path(object):
    def __init__(self,keyValue,path):
        self.keyValue = int(keyValue)
        self.path = path

class ReadSequence(object):
    """docstring for ReadSequence. read the data"""
    def __init__(self, opendir):
        """
        this is the dir path of the sequence data
        """
        super(ReadSequence, self).__init__()
        self.dirname = opendir
    def read(self):
        """
        read the data path and sort the path list
        """
        self.data_list = []
        try:
            list_name = os.listdir(self.dirname)
            for i in range(0,len(list_name)):
                path = os.path.join(self.dirname, list_name[i])
                if os.path.isfile(path):
                    if self.filelog(list_name[i]):
                        keyValue = re.findall(r'\d*', list_name[i], flags=0)
                        path = Path(keyValue[0], path)
                        self.data_list.append(path)
            def keyfind(path):
                return path.keyValue
            self.data_list.sort(key=keyfind)
            self.log = (True,'Read the path list Successful')
            return self.data_list
        except Exception as e:
            self.log = (False,'There is something wrong in the operation to init the path list')
            return self.data_list
    def testout(self):
        """
        print out the result
        """
        for i in self.data_list:
            print(i.path)
    def boollog(self):
        """
        dir and detection
        """
        if os.path.isdir(self.dirname):
            return True,'this is a dir,init the operator...'
        else:
            return False,'something is wrong,please try again...'
    def filelog(self,str1):
        if '.bmp' in str1:
            return True
        if '.jpg' in str1:
            return True
        if '.png' in str1:
            return True
        return False
    def datalog(self):
        """
        data log
        """
        return 'The Number of data is '+str(len(self.data_list))

if __name__ == '__main__':
    readSequence = ReadSequence('/Users/wangsir/Desktop/project/OCTFingerPrint/data/性别/女/1-yt')
    readSequence.boollog()
    readSequence.read()
    readSequence.datalog()
