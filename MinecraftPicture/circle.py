from PIL import Image, ImageFilter, ImageEnhance
import os
def bw_judge(R, G, B):
    Gray_Scale = (int)(0.229 * R + 0.587 * G + 0.114 * B)
    #这是灰度的计算公式来着，虽然有误差，但是好像问题不大？
    if(Gray_Scale < 132):
        color = "black"
    else:
        color = "white"
    return color


