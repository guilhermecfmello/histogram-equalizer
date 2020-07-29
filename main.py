from matplotlib.image import imread
from Equalizer import Equalizer
import matplotlib.pyplot as plt
# from PIL import Image, ImageDraw
import numpy as np
import scipy.misc as smp
import sys


# Arguments tratment function
def getArgs(args, param):
    try:
        argValue = False
        for a in args:
            if(a == '-h'):
                print('============= Help Menu =============')
                print("Exec format: python main.py [args] | python main.py -h for help")
                print("\n\nCommands:")
                print('-i "imageName"')
                print('-f format of image output, can be: "cmyk" or "hsi')
                return False
        for i in range(1, len(args)):
            # print("args len: " + str(len(args)))
            # print("i: " + str(i))
            if(args[i] == param):
                argValue = args[i+1]
        if(argValue == False): raise Exception("Param " + str(param) + " couldn't be found")
        return argValue
    except Exception as e:
        print("Exec format: python main.py [args] | python main.py -h for help.\nError: " + str(e))
        exit()    


# Todo: Normalize, Accumulation, equalizer

if __name__ == '__main__':
    imgName = getArgs(sys.argv, "-i")
    eq = Equalizer(imgName)
    eq.imgNormalizer()


