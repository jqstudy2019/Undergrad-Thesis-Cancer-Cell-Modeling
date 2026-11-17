import numpy as np

d0 = 2.7

d = .97


temp_x_points = []
temp_y_points = []
temp_z_points = []

rr1 = d / 2

nn = 1

temp_x_points[nn] = d0
temp_y_points[nn] = d0
temp_z_points[nn] = r1

nn = 2

temp_x_points[nn] = d0
temp_y_points[nn] = d0
temp_z_points[nn] = -rr1

for ii in range(2, round(np.pi / 2.0 / np.arcsin(d0 / 2.0 / rr1))):
    ti = (ii - 1) * np.pi / round(np.pi / 2.0 / np.arcsin(d0 / 2.0 / rr1))
    for jj in range(1, round(np.pi * np.sin(ti) / np.arcsin(d0 / 2.0 / rr1))):
        nn = nn + 1
        fj = (jj - 1) * 2.0 * np.pi / round(np.pi * np.sin(ti) / np.arcsin(d0 / 2.0 / rr1))
        temp_x_points[nn] = rr1 * np.sin(ti) * np.cos(fj)
        temp_y_points[nn] = rr1 * np.sin(ti) * np.sin(fj)
        temp_z_points[nn] = rr1 * np.cos(ti)

natoms = temp_x_points.shape

xyz = [temp_x_points, temp_y_points, temp_z_points]

xyz = xyz + np.rand((xyz.shape[0], xyz.shape[1]), 3) / 100

print (natoms, xyz)