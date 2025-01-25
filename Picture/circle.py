import random

from PIL import Image, ImageFilter, ImageEnhance
import os
import math
print(math.cos(-90))
sep = math.pi / 30
def circle(x, y, z, r, R, red, gre, yel):
    green = 0
    global count
    global i
    global fp
    yi = y + R * math.sin(i)
    yv = R * math.sin(i)
    if r == 0:
        y1 = y + R * math.sin(i)
        fp.write("particle dust {4} {5} {6} 10 {0:.10f} {1:.10f} {2:.10f} 0 {3:.10f} 0 0.4 0 force\n".format(x, y1, z, yv, red, gre, yel))
    else:
        j = 0
        while j < 2 * math.pi:
            xi = x + r * math.cos(j)
            zi = z + r * math.sin(j)
            xi = xi + ((random.random() - random.random()) * 0.5)
            zi = zi + ((random.random() - random.random()) * 0.5)
            xv = r * math.cos(j)
            zv = r * math.sin(j)
            fp.write("particle dust {6} {7} {8} 10 {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force\n".format(xi, yi, zi, xv, yv, zv, red, gre, yel))
            fp.write("particle flash {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force\n".format(xi, yi, zi, xv, yv, zv))
            j += sep
            # green += 1
            # if(green % 2 == 0):
                # fp.write("summon minecraft:firework_rocket {0:.10f} {1:.10f} {2:.10f} {{Motion:[{3:.10f}d,{4:.10f}d,{5:.10f}d]".format(xi, yi, zi, xv * 3, yv * 3, zv * 3))
                # fp.write(",ShotAtAngle:1b,FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Explosions:[{Colors:[I;627721,318724,4438339],Type:4b,Flicker:0b,Trail:0b}]}}}}\n")
                # fp.write("summon minecraft:firework_rocket {0:.10f} {1:.10f} {2:.10f} {{Tags:[\"fire_2_2\"],Motion:[{3:.10f}d,{4:.10f}d,{5:.10f}d],".format(xi, yi, zi, xv, yv, zv) + "ShotAtAngle:1b,LifeTime:5,FireworksItem:{id:\"firework_rocket\",Count:1b,tag:{Fireworks:{Explosions:[{Colors:[I;627721,318724,4438339],Type:4b,Flicker:1b,Trail:1b}]}}}}")
x = 89
y = -36
z = -61
count = 1000
R = 4
dirname = "sphere"
if os.path.exists(dirname) == False:
    os.mkdir(dirname)

fp = open(dirname + "\\" + str(count) + ".mcfunction", "w")
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R, 1, 0, 0)
    i += sep
R = 8
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R, 1, 1, 0)
    i += sep
R = 12
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R, 0, 0, 1)
    i += sep
R = 16
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R, 1, 0, 1)
    i += sep
R = 20
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R, 1, 1, 1)
    i += sep
R = 24
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R, 0, 1, 1)
    i += sep
fp.close()