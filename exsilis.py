import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import time

class StockImage(object):
    image = img.imread(r"preview_image/stock/object_stock.png")    

class InputPath():   #TODO:Rename
        lag = (1 / 60)
        object_num = 0 

        while True:
            path = 'preview_image/object_' + str(object_num) + '.png' 
            object_num += 1 
            time.sleep(lag)   
            
            if object_num > 6:  #TODO:Off
                break
            
            #print(path)            
            camera_img = img.imread(path)
            print(camera_img) 

if __name__ == "__main__":
    InputPath()
   