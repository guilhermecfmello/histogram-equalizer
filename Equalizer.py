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
        
        n = np.shape(img)[0] * np.shape(img)[1]

        normR, normG, normB = self.__countColors(img)
        normR, normG, normB = self.__normalizeColors(normR, normG, normB, n)
        

        print(normR)
        print(normG)
        print(normB)

        print("normRSum: " + str(np.sum(normR)))
        print("normGSum: " + str(np.sum(normG)))
        print("normBSum: " + str(np.sum(normB)))

    def __countColors(self, img):
        normR = np.zeros(RGB_MAX + 1)
        normG = np.zeros(RGB_MAX + 1)
        normB = np.zeros(RGB_MAX + 1)
        
        r = img[:,:,0]
        g = img[:,:,1]
        b = img[:,:,2]

        for i in range(np.shape(img)[0]):
            for j in range(np.shape(img)[1]):
                normR[r[i,j]] = normR[r[i,j]] + 1
                normG[g[i,j]] = normG[g[i,j]] + 1
                normB[b[i,j]] = normB[b[i,j]] + 1

        return normR, normG, normB
    
    def __normalizeColors(self, normR, normG, normB, n):
        for i in range(RGB_MAX + 1):
            normR[i] = normR[i] / n
            normG[i] = normG[i] / n
            normB[i] = normB[i] / n
        return normR, normG, normB