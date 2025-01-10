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
#他竟然不会算作临时变量吗，不愧是python

im = Image.open("newYear2.jpg")
function_dir = "zimu"
if (os.path.exists(function_dir) == False):
    os.mkdir(function_dir)
    #这一步是创建一个新文件夹
    #那我为何不创建完了把他删掉呢
    #有道理，因为要是在别处运行不一定有
count = 0
#接下来是起始坐标（话说我有没有办法获取玩家坐标）
zuobiao = "29.36 -56.67 -56.97"
zuobiaoList = zuobiao.split()
x = eval(zuobiaoList[0])
y = eval(zuobiaoList[1]) + 70
z = eval(zuobiaoList[2])


# 将字符串按空格分割


im.save("sduF.jpg")
pict = im.load()
width = im.size[0]
height = im.size[1]

name = str(count)
fp = open(function_dir + "/" + name + ".mcfunction", "w")
#虽然他叫open，但是他也能写（
total = 0
num = 0
for i in range(width):
    num = num + 1
    for j in range(height):
            xi = x + i / 4
            #哦，要让i除以16，这样x就不会挪的太快，那我很好奇如果直接整体除以16会怎么样
            R, G, B = pict[i, j]
            if(bw_judge(R, G, B) == "black"):
                total = total + 1
                yi = y - j / 4
                #所以x从左到右，y从上到下是吧
                fp.write("particle end_rod {0:.5f} {1:.5f} {2:.5f} 0 10 0 0 0 force\n".format(xi, yi, z))
                #0 1 0 0.4 force
                #这是命令方块里的指令, format里是代替大括号里数字的内容。吧？
                #particle end_rod x y z vx vy vz r 0 force
fp.close()
print(total)