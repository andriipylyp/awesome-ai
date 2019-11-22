import os
import matplotlib.pyplot as plt
import matplotlib.image as img

class StockImage(object):
    image = img.imread(r"preview _image/stock/object_stock.png")
    plt.imshow(image)
    plt.show()

    print(image)
    

if __name__ == "__main__":
    StockImage()