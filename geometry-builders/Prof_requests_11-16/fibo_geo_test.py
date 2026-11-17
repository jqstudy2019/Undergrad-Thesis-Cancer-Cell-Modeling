import math


points = []
phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

for i in range(10):
    y = 1 - (i / float(10 - 1)) * 2  # y goes from 1 to -1
    radius = math.sqrt(1 - y * y)  # radius at y

    theta = phi * i  # golden angle increment

    x = math.cos(theta) * radius
    z = math.sin(theta) * radius

    points.append((x, y, z))

print(points)
