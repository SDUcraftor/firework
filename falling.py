from PIL import Image, ImageFilter, ImageEnhance
import os
import matplotlib as plt
import numpy as np
def bw_judge(R, G, B):
    Gray_Scale = (int)(0.229 * R + 0.587 * G + 0.114 * B)
    if(Gray_Scale < 132):
        color = "black"
    else:
        color = "white"
    return color

start = [103, -1, -61]
R = 10

fp = open("zimu" + "/" + "falling" + ".mcfunction", "w")
total = 0
num = 0
seg = 16
perDe = 360 / seg
for i in range(seg):
    l = 0
    while(l < R):
        y = -(l * l) / 5.0
        x = l * np.cos(perDe * (i + 1))
        z = l * np.sin(perDe * (i + 1))
        fp.write("particle firework {0:.5f} {1:.5f} {2:.5f} 0 10 0 0 0 force\n".format(start[0] + x, start[1] + y, start[2] + z))
        l += 0.05
        #好丑···