import random

from PIL import Image, ImageFilter, ImageEnhance
import os
import math

x = 89
y = -36
z = -61
count = 1000
R = 20

def circle(theta, fai, R, red, gre, blu):
    green = 0
    global count
    global i
    global fp
    xi = x + R * math.cos(fai) * math.sin(theta)
    zi = z + R * math.sin(fai) * math.sin(theta)
    yi = y + R * math.cos(theta)
    print(xi, yi, zi)
    yv = R * math.cos(theta)
    j = 0
    while j <= R:
        x1 = ((j / R) * (xi - x)) + x
        z1 = ((j / R) * (zi - z)) + z
        y1 = ((j / R) * (yi - y)) + y
        x1 = x1 + ((random.random() - random.random()) * 0.5)
        z1 = z1 + ((random.random() - random.random()) * 0.5)
        xv =  math.cos(j)
        zv =  math.sin(j)
        fp.write("particle dust {6} {7} {8} 10 {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force\n".format(x1, y1, z1, xv, yv, zv, red, gre, blu))
        fp.write("particle flash {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force\n".format(x1, y1, z1, xv, yv, zv))
        j += R / 20
            # green += 1
            # if(green % 2 == 0):
                # fp.write("summon minecraft:firework_rocket {0:.10f} {1:.10f} {2:.10f} {{Motion:[{3:.10f}d,{4:.10f}d,{5:.10f}d]".format(xi, yi, zi, xv * 3, yv * 3, zv * 3))
                # fp.write(",ShotAtAngle:1b,FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Explosions:[{Colors:[I;627721,318724,4438339],Type:4b,Flicker:0b,Trail:0b}]}}}}\n")
                # fp.write("summon minecraft:firework_rocket {0:.10f} {1:.10f} {2:.10f} {{Tags:[\"fire_2_2\"],Motion:[{3:.10f}d,{4:.10f}d,{5:.10f}d],".format(xi, yi, zi, xv, yv, zv) + "ShotAtAngle:1b,LifeTime:5,FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Explosions:[{Colors:[I;627721,318724,4438339],Type:4b,Flicker:1b,Trail:1b}]}}}}")


theta = []
fai = []
for i in range(30):
    theta.append(random.uniform(-math.pi, math.pi))
    fai.append(random.uniform(-math.pi, math.pi))
dirname = "sphere"
if os.path.exists(dirname) == False:
    os.mkdir(dirname)

fp = open(dirname + "\\" + str(count) + ".mcfunction", "w")
k = 0
for k in range(0, 30):
    print(theta[k], fai[k])
    circle(theta[k], fai[k], R, 0, 1, 0)
fp.close()