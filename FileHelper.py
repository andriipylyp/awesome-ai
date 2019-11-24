from include.IFileHelper import IFileHelper
import matplotlib.image as img
from PIL import Image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
import os.path as p
import numpy
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