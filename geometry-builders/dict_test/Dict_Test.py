########################################################################################################################
#   Obj_Test_V3.py ----- A code to build the .data file for a LAMMPS Simulation
#
#   General Description - Testing a getting a better way of writing data working
#
#
########################################################################################################################

# Import Extra Modules / Tools

import numpy as np  # Numpy is used for Array Creation and Manipulation Mainly
from copy import deepcopy  # DeepCopy Is used to Copy Arrays

########################################################################################################################

###      Set Variables Used For Later       ###


#   Output File Options #

filename = input("Enter a name for the Output File (remember .data at the end!) :")  # String Name of File to be Created

#   Simulation Box Settings   #

sim_box_side_length = 100  # Each Side of the Simulation Box Will have sides of these lengths

SIM_SPACE = np.zeros((sim_box_side_length, sim_box_side_length, sim_box_side_length))
# Creates an Array Called SIM_SPACE (is a 3-D array (x,y,z of each simulation space position)

SIM_SPACE_PUREcopy = deepcopy(SIM_SPACE)  # Extra Copy of the Sim Space kept because its "pure"

x0 = int(np.floor(SIM_SPACE.shape[2] / 2))  # Finds the Center of the Sim Space ( x0, y0, z0 )
y0 = int(np.floor(SIM_SPACE.shape[1] / 2))
z0 = int(np.floor(SIM_SPACE.shape[0] / 2))

#   Molecule Geometry Creation Settings #

molecule_ids = 1     # LAMMPS Track molecules by their ID number ; this is the number of molecules created

molecule_1_thickness = 15   # The thickness is an extra range past the radius to include in the molecules

molecule_1_radius = 10  # Radius of each molecule

num_atoms_molecule_1 = 0    # Placeholder for total number of atoms created as part of the molecule

molecule_1_bond_length = 3  #Functions Similar to molecule radius but on the bond scale: sets how far apart the bonds go

molecule_1 = {} # initializes the dictionary for molecule 1

#   LAMMPS Data Inserts #

atom_types = 1  # LAMMPS Data Field ; Number of different types of Atoms

bond_types = 1  # LAMMPS Data Field ; Number of different types of Bonds

#   Program Performance Tracking

positions_checked = 0   #Keeps Count of How many points are iterated through ; easy way to check it iterating correctly

########################################################################################################################

###     Creates 3-D Set of Points      ###

# Iterates Each Position of the sim (x,y,z

for x in range(0, sim_box_side_length):
    for y in range(0, sim_box_side_length):
        for z in range(0, sim_box_side_length):

            # This section measures the distance from the Center (x0,y0,z0) to each point and
            # deb: measures how far a coordinate in A is far from the center.
            # deb>=0: inside the sphere.
            # deb<0: outside the sphere

            deb = (molecule_1_radius ** 2) - ((x0 - x) ** 2) - ((y0 - y) ** 2) - ((z0 - z) ** 2)
            positions_checked = positions_checked + 1

            # if statement for deciding which points will be in MOLECULE 1

            if (deb >= 0) and (deb <= molecule_1_thickness):
                num_atoms_molecule_1 = num_atoms_molecule_1 + 1
                molecule_1[num_atoms_molecule_1] = {'Positions': '{} {} {}'.format(x, y, z)}


########################################################################################################################

###     Prints Sim Info To Make Sure Its Running Correct        ###

print("Number of atoms placed in Molecule 1: {} \n".format(num_atoms_molecule_1))

print("Number of Points in Simulation Space Iterated thorough: {} \n".format(positions_checked))

########################################################################################################################

###     Write LAMMPS Data File      ###

with open(filename, 'w+') as fdata:  # opens a text file named a for the 'filename' variable
    fdata.write('{}\n\n'.format(filename))  # First line is a comment line

    ##     Header of Data File     ##

    fdata.write('{} atoms\n'.format(num_atoms_molecule_1))  # Specify number of atoms
    fdata.write('{} atom types\n'.format(atom_types))

    #   specify box dimensions      #

    fdata.write('{} {} xlo xhi\n'.format(0.0, sim_box_side_length))  # Writes X Position
    fdata.write('{} {} ylo yhi\n'.format(0.0, sim_box_side_length))  # Writes Y Position
    fdata.write('{} {} zlo zhi\n'.format(0.0, sim_box_side_length))  # Writes Z Position
    fdata.write('\n')  # Skips the Next line for Formatting

    ##      Data File Body      ##

    #       Atoms section       #
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(molecule_1):
        fdata.write('{} {} {} {} \n'.format(i, molecule_ids, atom_types, molecule_1[pos].get('Positions')))

########################################################################################################################

###         Finished!!!     ###

print('Data File Created Successfully; File name => {}  '.format(filename))

########################################################################################################################
