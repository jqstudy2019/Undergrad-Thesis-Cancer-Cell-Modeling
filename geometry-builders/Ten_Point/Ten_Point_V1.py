########################################################################################################################
#   Soft_Ball.py ----- A code to build the .data file for a LAMMPS Simulation
#
#       8/28/2020
########################################################################################################################
##      Import Extra Modules / Tools        ##

import numpy as np  # Numpy is used for Array Creation and Manipulation Mainly
import random as random


########################################################################################################################
###         User Defined Functions ###
def packing_roll(coeff):
    temp_roll = random.randint(1, 100)
    if temp_roll in range(0, coeff):
        return 'Place Atom'
    else:
        return 'Leave Empty'


########################################################################################################################
###      Set Variables Used For Later       ###

##--------------------------------------------------------------------------------------------------------------------##
##     Output File Options      ##
import sys  # output name may be given on the command line
filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter a name for the Output File (remember .data at the end!) :")  # String Name of File to be Created

##--------------------------------------------------------------------------------------------------------------------##
##      Simulation Box Settings     ##
sim_box_side_length = 100  # Each Side of the Simulation Box Will have sides of these lengths

SIM_SPACE = np.zeros((sim_box_side_length, sim_box_side_length, sim_box_side_length))
# Creates an Array Called SIM_SPACE (is a 3-D array (x,y,z of each simulation space position)

x0 = int(np.floor(SIM_SPACE.shape[2] / 2))  # Finds the Center of the Sim Space ( x0, y0, z0 )
y0 = int(np.floor(SIM_SPACE.shape[1] / 2))
z0 = int(np.floor(SIM_SPACE.shape[0] / 2))

##--------------------------------------------------------------------------------------------------------------------##
##      Molecule Geometry Creation Settings         ##

membrane_atom_type = 1  # LAMMPS Track molecules by their ID number ; this is the number of molecules created

membrane_molecule_type = 1

molecule_1_radius = 20  # Radius of each molecule

num_atoms_molecule_1 = 0  # Placeholder for total number of atoms created as part of the molecule

molecule_1 = {}  # initializes the dictionary for molecule 1

membrane_1_packing_density = 100  # Coeff Determining the density of the blob

Atom_Limit = 10

##--------------------------------------------------------------------------------------------------------------------##
##       LAMMPS Variables       ##

num_atoms_total = 0

total_atom_types = 1

##--------------------------------------------------------------------------------------------------------------------##
##         Program Performance Tracking         ##

positions_checked = 0  # Keeps Count of How many points are iterated through ; easy way to check it iterating correctly

##--------------------------------------------------------------------------------------------------------------------##
##        EXPERIMENTAL       ##

ATOMS = {}

########################################################################################################################

###     Creates 3-D Set of Points      ###

# Iterates Each Position of the sim (x,y,z

for x in range(0, sim_box_side_length):
    for y in range(0, sim_box_side_length):
        for z in range(0, sim_box_side_length):
            deb = (molecule_1_radius ** 2) - ((x0 - x) ** 2) - ((y0 - y) ** 2) - ((z0 - z) ** 2)
            positions_checked = positions_checked + 1
            if deb >= molecule_1_radius:
                pack_roll_temp = packing_roll(membrane_1_packing_density)
                if pack_roll_temp == 'Place Atom':
                    if num_atoms_total < Atom_Limit:
                        num_atoms_molecule_1 = num_atoms_molecule_1 + 1
                        SIM_SPACE[x, y, z] = membrane_atom_type
                        num_atoms_total = num_atoms_total + 1
                        ATOMS[num_atoms_total] = {'Atom_ID': num_atoms_total,
                                                  'Molecule_ID': membrane_molecule_type,
                                                  'Atom_Type': membrane_atom_type,
                                                  'X': x,
                                                  'Y': y,
                                                  'Z': z,
                                                  'Positions String': '{} {} {}'.format(x, y, z)}

########################################################################################################################

###     Prints Sim Info To Make Sure Its Running Correct        ###

print("Number of Points in Simulation Space Iterated thorough: {} \n".format(positions_checked))

########################################################################################################################

###     Write LAMMPS Data File      ###

with open(filename, 'w+') as fdata:  # opens a text file named a for the 'filename' variable
    fdata.write('{}\n\n'.format(filename))  # First line is a comment line

    ##     Header of Data File     ##

    #   Atoms Header #

    fdata.write('{} atoms\n'.format(num_atoms_total))  # Specify number of atoms
    fdata.write('{} atom types\n'.format(total_atom_types))

    fdata.write('1 bond types\n')
    fdata.write('1 angle types\n')
    fdata.write('1 dihedral types\n')

    #   specify box dimensions      #

    fdata.write('{} {} xlo xhi\n'.format(0.0, sim_box_side_length))  # Writes X Position
    fdata.write('{} {} ylo yhi\n'.format(0.0, sim_box_side_length))  # Writes Y Position
    fdata.write('{} {} zlo zhi\n'.format(0.0, sim_box_side_length))  # Writes Z Position

    fdata.write('\n')  # Skips the Next line for Formatting

    ##      Data File Body      ##

    #       Atoms section       #
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(ATOMS):
        fdata.write('{} {} {} {} \n'.format(ATOMS[pos].get('Atom_ID'),
                                            ATOMS[pos].get('Molecule_ID'),
                                            ATOMS[pos].get('Atom_Type'),
                                            ATOMS[pos].get('Positions String')))
    fdata.write('\n')

########################################################################################################################
###         Finished!!!     ###

print(' Data File Created Successfully!!! ; File name => {} '.format(filename))

########################################################################################################################
