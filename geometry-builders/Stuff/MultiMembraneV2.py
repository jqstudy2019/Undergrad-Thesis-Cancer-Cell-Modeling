import numpy as np
from copy import deepcopy

''' size : size of original 3D numpy matrix A.
    radius : radius of circle inside A which will be filled with ones.
'''
filename = "MultiMembraneV2"

size = 100

radius = 10

sphere_thickness = 15

X_seperation = 20

Y_seperation = 20

Z_seperation = 20

sphere_1_coords = []

sphere_2_coords = []

num_atoms_sphere_1 = 0

num_atoms_sphere_2 = 0

num_of_excluded_atoms =0

''' A : numpy.ndarray of shape size*size*size. '''
A = np.zeros((size, size, size))

''' AA : copy of A (you don't want the original copy of A to be overwritten.) '''
AA = deepcopy(A)

''' (x0, y0, z0) : coordinates of center of circle inside A. '''
x0, y0, z0 = int(np.floor(A.shape[0] / 2)), \
             int(np.floor(A.shape[1] / 2)), \
             int(np.floor(A.shape[2] / 2))

for x in range(0,size):
    for y in range(0,size):
        for z in range(0,size):
            ''' deb: measures how far a coordinate in A is far from the center.
                    deb>=0: inside the sphere.
                    deb<0: outside the sphere.'''
            deb = (radius ** 2) - ((x0 - x)**2) - ((y0 - y)**2) - ((z0 - z)**2)
            if (deb >= 0) and (deb <= sphere_thickness):
                sphere_1_coords.append((x, y, z))
                num_atoms_sphere_1 = num_atoms_sphere_1 + 1
                x_2 = x + X_seperation
                y_2 = y + Y_seperation
                z_2 = z + Z_seperation
                sphere_2_coords.append((x_2, y_2, z_2))
                num_atoms_sphere_2 = num_atoms_sphere_2 + 1

print("Number of atoms in Sphere: {} \n".format(num_atoms_sphere_1 + num_atoms_sphere_2))

# 3. Write LAMMPS Data File

with open('MultiMembraneV2.data', 'w'.format('filename')) as fdata:
    # First line is a comment line
    fdata.write('MultiMembraneV2.data\n\n'.format('filename'))

    # --- Header ---#

    # Specify number of atoms and atom types
    fdata.write('{} atoms\n'.format(num_atoms_sphere_1 + num_atoms_sphere_2))
    fdata.write('{} atom types\n'.format(2))

    # Specify box dimensions
    fdata.write('{} {} xlo xhi\n'.format(0.0, size))
    fdata.write('{} {} ylo yhi\n'.format(0.0, size))
    fdata.write('{} {} zlo zhi\n'.format(0.0, size))
    fdata.write('\n')

    # Atoms section
    fdata.write('Atoms\n\n')

    # Write each position
    for i, pos in enumerate(sphere_1_coords):
        fdata.write('{} 1 0.5 1.0 {} {} {}\n'.format(i + 1, *pos))
    for i, pos in enumerate(sphere_2_coords):
        fdata.write('{} 1 0.5 1.0 {} {} {}\n'.format(i + num_atoms_sphere_1 + 1, *pos))

print('Data File Created Successfully; Fine name => {}.data  '.format(filename))