########################################################################################################################
# SphereSimV2.py - builds the .data file
#
# By: John Quinn
#
# Date: 4/29/2020
#
# Summary of Code: (General Steps of code)
#	0. Import Functions
#       __future__ - https://docs.python.org/3/library/__future__.html
#           # Imports the division ( / ) function
#
#       math - https://docs.python.org/3/library/math.html
#           # Imports Math Functions
#               ## Trig Functions - Sine (sin) ; Cosine (cos) ; the # Pi (pi)
#	1. Define Initial Variables
#
#
#   2. Define Internal Functions
#
#   3. Generate Coordinates
#
#   4. Write LAMMPS Data File
#
# Appendix of Commands:
#	#((Command -> commands function ; format( Command arg1 arg 2 . . .) ; more notes))
#
# Version List:
#
# Possible Future Improvements:
#
# References:
#   https://stackoverflow.com/questions/29398875/how-can-i-obtain-the-coordinates-for-a-sphere-using-python
#
########################################################################################################################
# 0. Import Functions

from __future__ import division
from math import sin, cos, pi

########################################################################################################################
# 1. Define Initial Variables

SAMPLES = 20

xrange = range(1, 10)

coords = []

num_atoms = 0

sys_size = 10


########################################################################################################################
# 2. Define Internal Functions

def to_x(r, theta, phi):
    return r * sin(theta) * cos(phi)


def to_y(r, theta, phi):
    return r * sin(theta) * sin(phi)


def to_z(r, theta, phi):
    return r * cos(theta)


########################################################################################################################
# 3. Generate Coordinates ( coords )

samples_r = [r for r in xrange]
samples_theta = [theta * 4 * pi / SAMPLES for theta in xrange]
samples_phi = [phi * 4 * pi / SAMPLES for phi in xrange]

for r in samples_r:
    for theta in samples_theta:
        for phi in samples_phi:
            num_atoms = num_atoms + 1
            coords.append((to_x(r, theta, phi),
                           to_y(r, theta, phi),
                           to_z(r, theta, phi)))

for coord in coords:
    out = open("sphere.xyz", "a")
    print(coord)
    out.write("Ar"  " " " " "%2.5s %2.5s %2.5s \n" % coord)
    out.close()

########################################################################################################################
    # 4. Write LAMMPS Data File

    # Creates and Opens the file to be made
    with open('SphereSimV2.data', 'w') as fdata:
        # First line is a comment line
        fdata.write('Random Atoms - Written For JQ-Random - An exmaple made by: John Quinn\n\n')

    # Header
    # Specify number of atoms and atom types
        fdata.write(f'{num_atoms} atoms\n')
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
