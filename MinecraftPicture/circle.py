from PIL import Image, ImageFilter, ImageEnhance
import os
import math
print(math.cos(-90))
sep = math.pi / 45
def circle(x, y, z, r, R):
    global count
    global i
    global fp
    yi = y + R * math.sin(i)
    yv = R * math.sin(i)
    if r == 0:
        y1 = y + R * math.sin(i)
        fp.write("particle firework {0:.10f} {1:.10f} {2:.10f} 0 {3:.10f} 0 0.4 0 force\n".format(x, y1, z, yv))
    else:
        j = 0
        while j < 2 * math.pi:
            xi = x + r * math.cos(j)
            zi = z + r * math.sin(j)
            xv = r * math.cos(j)
            zv = r * math.sin(j)
            fp.write("particle firework {0:.10f} {1:.10f} {2:.10f} {3:.10f} {4:.10f} {5:.10f} 0.4 0 force\n".format(xi, yi, zi, xv, yv, zv))
            j += sep

x = 89
y = -36
z = -61
count = 1000
R = 2
dirname = "sphere"
if os.path.exists(dirname) == False:
    os.mkdir(dirname)

fp = open(dirname + "\\" + str(count) + ".mcfunction", "w")
i = -math.pi / 2
while i < math.pi / 2:
    r = R * math.cos(i)
    circle(x, y, z, r, R)
    i += sep
fp.close()