########################################################################################################################
#   Bonding_Test_V3.py ----- A code to build the .data file for a LAMMPS Simulation ; WIth new bonding Scheme
#
#   General Description - New and Improved Methods implemented and now\
#                           build new bonding scheme
#
#
########################################################################################################################

# Import Extra Modules / Tools

import numpy as np  # Numpy is used for Array Creation and Manipulation Mainly
from copy import deepcopy  # DeepCopy Is used to Copy Arrays


###     *** TEST: FIND ATOM ID FROM X Y Z FUNCTION ***  ###
# try using this fromat
#
# thisdict =	{
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# for x, y in thisdict.items():
# print(x, y)

# to sort and find the atom id of a given set of xyz points of the atom
# simple Steps:
# 0. Inputs(x y z)  outputs(Atom ID)
# 1. print the contents of molecule_1


def findatom_id(xfind, yfind, zfinds):
    for atoms in range(1, num_atoms_molecule_1):
        temp = molecule_1[atoms]
        if (temp['X'] == xfind) and (temp['Y'] == yfind) and (temp['Z'] == zfinds):
            temp_atom_id = temp['Atom_ID']
            return temp_atom_id
        else:
            return 'No Atom There'

        # def findbond(atom_id_1, atom_id_2)


########################################################################################################################


###      Set Variables Used For Later       ###


#   Output File Options #

import sys  # output name may be given on the command line
filename = sys.argv[1] if len(sys.argv) > 1 else input("Enter a name for the Output File (remember .data at the end!) :")  # String Name of File to be Created

#   Simulation Box Settings   #

sim_box_side_length = 100  # Each Side of the Simulation Box Will have sides of these lengths

SIM_SPACE = np.zeros((sim_box_side_length, sim_box_side_length, sim_box_side_length))
# Creates an Array Called SIM_SPACE (is a 3-D array (x,y,z of each simulation space position)

SIM_SPACE_PUREcopy = deepcopy(SIM_SPACE)  # Extra Copy of the Sim Space kept because its "pure"

x0 = int(np.floor(SIM_SPACE.shape[2] / 2))  # Finds the Center of the Sim Space ( x0, y0, z0 )
y0 = int(np.floor(SIM_SPACE.shape[1] / 2))
z0 = int(np.floor(SIM_SPACE.shape[0] / 2))

#   Molecule Geometry Creation Settings #

molecule_ids = 1  # LAMMPS Track molecules by their ID number ; this is the number of molecules created

molecule_1_thickness = 15  # The thickness is an extra range past the radius to include in the molecules

molecule_1_radius = 10  # Radius of each molecule

num_atoms_molecule_1 = 0  # Placeholder for total number of atoms created as part of the molecule

molecule_1_bond_length = 1  # Functions Similar to molecule radius but on the bond scale

molecule_1 = {}  # initializes the dictionary for molecule 1

molecule_1_COPY = {}  # Copy of Molecule dictionary

molecule_1_bonds = {}  # dictionary for bonds

num_molecule_1_bonds = 0

#   LAMMPS Data Inserts #

atom_types = 1  # LAMMPS Data Field ; Number of different types of Atoms

bond_types = 1  # LAMMPS Data Field ; Number of different types of Bonds

#   Program Performance Tracking

positions_checked = 0  # Keeps Count of How many points are iterated through ; easy way to check it iterating correctly

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
            SIM_SPACE[x, y, z] = molecule_ids
            # if statement for deciding which points will be in MOLECULE 1

            if (deb >= 0) and (deb <= molecule_1_thickness):
                num_atoms_molecule_1 = num_atoms_molecule_1 + 1
                molecule_1[num_atoms_molecule_1] = {'Atom_ID': num_atoms_molecule_1,
                                                    'Molecule_ID': molecule_ids,
                                                    'Atom_Type': atom_types,
                                                    'X': x,
                                                    'Y': y,
                                                    'Z': z,
                                                    'Positions String': '{} {} {}'.format(x, y, z)}

                for x1 in range(x - molecule_1_bond_length, x + molecule_1_bond_length):
                    for y1 in range(y - molecule_1_bond_length, y + molecule_1_bond_length):
                        for z1 in range(z - molecule_1_bond_length, z + molecule_1_bond_length):
                            if SIM_SPACE[x1, y1, z1] == molecule_ids:
                                Atom_ID_1 = findatom_id(x, y, z)
                                if Atom_ID_1 is int:
                                    Atom_ID_2 = findatom_id(x1, y1, z1)
                                    if Atom_ID_2 is int:
                                        num_molecule_1_bonds = num_molecule_1_bonds + 1
                                        molecule_1_bonds[num_molecule_1_bonds] = {'Bond_ID': num_molecule_1_bonds,
                                                                                  'Bond_Type': bond_types,
                                                                                  'atom1': Atom_ID_1,
                                                                                  'atom2': Atom_ID_2}

########################################################################################################################

###     Prints Sim Info To Make Sure Its Running Correct        ###

print("Number of atoms placed in Molecule 1: {} \n".format(num_atoms_molecule_1))

print("Number of Points in Simulation Space Iterated thorough: {} \n".format(positions_checked))

print("Number of Bonds Created: {} \n".format(molecule_1_bonds))

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

    #       Atoms Section       #
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(molecule_1):
        fdata.write('{} {} {} {} \n'.format(molecule_1[pos].get('Atom_ID'),
                                            molecule_1[pos].get('Molecule_ID'),
                                            molecule_1[pos].get('Atom_Type'),
                                            molecule_1[pos].get('Positions String')))
    fdata.write('\n')

    #       Bonds Section       #
    fdata.write('Bonds\n\n')
    for iV2, posV2 in enumerate(molecule_1):
        fdata.write('{} {} {} {} \n'.format(molecule_1[posV2].get('Bond_ID'),
                                            molecule_1[posV2].get('Bond_Type'),
                                            molecule_1[posV2].get('atom1'),
                                            molecule_1[posV2].get('atom2')))

########################################################################################################################

###         Finished!!!     ###

print(' Data File Created Successfully!!! ; File name => {} '.format(filename))

########################################################################################################################
