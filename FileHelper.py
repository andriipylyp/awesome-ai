from IFileHelper import IFileHelper
import matplotlib.image as img
import os.path as p
class FileHelper(IFileHelper):
    def __init__(self):
        pass

    def LoadImage(self, file_name):
        return img.imread(file_name)

    def SaveMatrix(self, file_name, matrix):
        File = open(file_name, "w+")
        File.write(matrix)
        File.close()
        if p.exists(file_name):
            return 0
        raise Exception(PermissionError)