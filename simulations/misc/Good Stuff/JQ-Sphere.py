import numpy as np
from copy import deepcopy

''' size : size of original 3D numpy matrix A.
    radius : radius of circle inside A which will be filled with ones.
'''
size, radius = 320, 4

sphere_coords = []

num_atoms_sphere = 0

''' A : numpy.ndarray of shape size*size*size. '''
A = np.zeros((size, size, size))

''' AA : copy of A (you don't want the original copy of A to be overwritten.) '''
AA = deepcopy(A)

''' (x0, y0, z0) : coordinates of center of circle inside A. '''
x0, y0, z0 = int(np.floor(A.shape[0] / 2)), \
             int(np.floor(A.shape[1] / 2)), \
             int(np.floor(A.shape[2] / 2))

for x in range(x0 - radius, x0 + radius + 1):
    for y in range(y0 - radius, y0 + radius + 1):
        for z in range(z0 - radius, z0 + radius + 1):
            ''' deb: measures how far a coordinate in A is far from the center.
                    deb>=0: inside the sphere.
                    deb<0: outside the sphere.'''
            deb = radius - abs(x0 - x) - abs(y0 - y) - abs(z0 - z)
            if deb >= 0:
                AA[x, y, z] = 1
                sphere_coords.append((x, y, z))
                num_atoms_sphere = num_atoms_sphere + 1

print("Number of atoms in Sphere: {} \n".format(num_atoms_sphere))

# 3. Write LAMMPS Data File

with open('JQ-Sphere.data', 'w') as fdata:
    # First line is a comment line
    fdata.write('Random Atoms - Written For JQ-Random - An exmaple made by: John Quinn\n\n')

    # --- Header ---#

    # Specify number of atoms and atom types
    fdata.write('{} atoms\n'.format(num_atoms_sphere))
    fdata.write('{} atom types\n'.format(1))

    # Specify box dimensions
    fdata.write('{} {} xlo xhi\n'.format(0.0, size))
    fdata.write('{} {} ylo yhi\n'.format(0.0, size))
    fdata.write('{} {} zlo zhi\n'.format(0.0, size))
    fdata.write('\n')

    # Atoms section
    fdata.write('Atoms\n\n')

    # Write each position
    for i, pos in enumerate(sphere_coords):
        fdata.write('{} 1 {} {} {}\n'.format(i + 1, *pos))

print('Data File Created Successfully; Fine name => JQ-Sphere.data  ')

