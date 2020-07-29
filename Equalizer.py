from matplotlib.image import imread
import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw
import numpy as np
import scipy.misc as smp

RGB_MAX = 255

class Equalizer:
    def __init__(self,imgName):
        self.imgFolder = "images/"
        self.imgName = imgName
        self.file = self.imgFolder + self.imgName
    
    def imgNormalizer(self):
        img = imread(self.file)
        r = img[:,:,0]
        g = img[:,:,1]
        b = img[:,:,2]
        n = np.shape(img)[0] * np.shape(img)[1]


        # print(np.shape(r))
        # exit()

        normR = np.zeros(RGB_MAX + 1)
        normG = np.zeros(RGB_MAX + 1)
        normB = np.zeros(RGB_MAX + 1)
        for i in range(np.shape(img)[0]):
            for j in range(np.shape(img)[1]):
                normR[r[i,j]] = normR[r[i,j]] + 1
                normG[g[i,j]] = normG[g[i,j]] + 1
                normB[b[i,j]] = normB[b[i,j]] + 1

        # print(normR)
        # print(np.shape(normR))
        plt.hist(normG, bins = RGB_MAX)
        plt.show()


        # print(r)
        # print(np.shape(r))
        # print("Number of pixels: " + str(n))
        # print(np.shape(r))

