import math
import os
import random
def draw(x1, y1, z1, x2, y2, z2, lamda):
    delta = math.fabs(x1 - x2)
    vx = (x2 - x1) / delta
    vy = (y2 - y1) / delta
    vz = (z2 - z1) / delta
    t = 0
    while t < delta:
        function_name = str((int)(t + x1))
        fp = open(dirname + "\\" + str(function_name) + ".mcfunction", "w")
        i = 0
        while i < lamda:
            zi = z1 + vz * (t + i / lamda) + 0.5
            yi = y1 + vy * (t + i / lamda) + 0.5
            xi = x1 + vx * (t + i / lamda) + 0.5
            fp.write("particle dust {3:.2f} {4:.2f} {5:.2f} 10 {0:.10f} {1:.10f} {2:.10f} 0 0 0 0 1 force\n".format(xi, yi, zi, random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))
            i += 1
        fp.close()
        t += 1


dirname = "line"
if os.path.exists(dirname) == False:
    os.mkdir(dirname)

draw(64.0, -49.0, -86, 94, -35, -84, 10)


