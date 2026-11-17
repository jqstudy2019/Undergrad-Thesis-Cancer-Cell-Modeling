from __future__ import division
from math import sin, cos, pi

SAMPLES = 20

def to_x(r, theta, phi):
    return r*sin(theta)*cos(phi)

def to_y(r, theta, phi):
    return r*sin(theta)*sin(phi)

def to_z(r, theta, phi):
    return r*cos(theta)

xrange = range(1,10)

samples_r = [r for r in xrange]
samples_theta = [theta * pi / SAMPLES for theta in xrange]
samples_phi = [phi * 2*pi / SAMPLES for phi in xrange]

coords = []
num_atoms = 0
sys_size = 10

for r in samples_r:
    for theta in samples_theta:
        for phi in samples_phi:
            num_atoms= num_atoms + 1
            coords.append((to_x(r, theta, phi),
                           to_y(r, theta, phi),
                           to_z(r, theta, phi)))

for coord in coords:
   out = open("sphere.xyz", "a")
   print (coord)
   out.write( "Ar"  " " " " "%2.5s %2.5s %2.5s \n" %(coord))
   out.close()



# 3. Write LAMMPS Data File

with open('JQ-sphere1.data', 'w') as fdata:
    # First line is a comment line
    fdata.write('Random Atoms - Written For JQ-Random - An exmaple made by: John Quinn\n\n')

    # --- Header ---#

    # Specify number of atoms and atom types
    fdata.write('{} atoms\n'.format(num_atoms))
    fdata.write('{} atom types\n'.format(1))

    # Specify box dimensions
    fdata.write('{} {} xlo xhi\n'.format(0.0, sys_size))
    fdata.write('{} {} ylo yhi\n'.format(0.0, sys_size))
    fdata.write('{} {} zlo zhi\n'.format(0.0, sys_size))
    fdata.write('\n')

    # Atoms section
    fdata.write('Atoms\n\n')

    # Write each position
    for i, pos in enumerate(coords):
        fdata.write('{} 1 {} {} {}\n'.format(i + 1, *pos))
