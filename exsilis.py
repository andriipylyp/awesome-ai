import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import time

class StockImage(object):
    image = img.imread(r"preview _image/stock/object_stock.png")

class InputPath(): 
        timer = (1 / 60)
        object_num = 0 

        while True:
            path = '\"' + 'preview_image/object_' + str(object_num) + '.png' + '\"'
            object_num += 1 
            time.sleep(timer)   
            
            if object_num > 3:
                break
            
            #print(path)            
            #camera_img = img.imread()
            #print(camera_img)  

if __name__ == "__main__":
    InputPath()
   