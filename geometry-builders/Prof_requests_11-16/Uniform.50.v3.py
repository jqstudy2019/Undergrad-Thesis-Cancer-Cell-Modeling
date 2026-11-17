########################################################################################################################
#   REGION_TEST_V1.py ----- A code to build the .data file for a LAMMPS Simulation
#
#       8/28/2020
#
########################################################################################################################
##      Import Extra Modules / Tools        ##

import numpy as np  # Numpy is used for Array Creation and Manipulation Mainly

import math

##--------------------------------------------------------------------------------------------------------------------##
########################################################################################################################
##      Set Constants and Variables Needed      ##
##--------------------------------------------------------------------------------------------------------------------##
#   Output File Options   #

Filename = input("Enter a name for the Output File (remember .data is now included at the end automatically) :")
# String Name of File to be Created

Filename = Filename + ".data"  # adds .data file extension

Set_Num_Particles = int(input("Enter Number of particles on membrane:"))

##--------------------------------------------------------------------------------------------------------------------##
#   Sim Box Settings    #
Sim_Box_Side_Length = 100  # Each Side of the Simulation Box Will have sides of these lengths

SIM_SPACE = np.zeros((Sim_Box_Side_Length, Sim_Box_Side_Length, Sim_Box_Side_Length))
# Creates an Array Called SIM_SPACE (is a 3-D array (x,y,z of each simulation space position)

x0 = int(np.floor(SIM_SPACE.shape[2] / 2))  # Finds the Center of the Sim Space ( x0, y0, z0 )
y0 = int(np.floor(SIM_SPACE.shape[1] / 2))
z0 = int(np.floor(SIM_SPACE.shape[0] / 2))

Atom_Place_Limit = 90  # limits where atoms maybe placed based on box dimensions

##--------------------------------------------------------------------------------------------------------------------##
#   Membrane Settings   #
Membrane_Atom_Type = 1

Membrane_Molecule_Type = 1

Membrane_Thickness = 1

Membrane_Radius = 4

Membrane_Diameter = Membrane_Radius * 2

Membrane_Number_Atoms = 0

Membrane_points_xyz = {}

##--------------------------------------------------------------------------------------------------------------------##
#   Total / Aggregate Variables     #

Total_Number_Atoms = 0

Total_xyz = {}

Total_Atom_Types = 1

Total_Molecule_Type = 1

Total_Bond_Types = 1

Total_Angle_Types = 1

Total_Dihedral_Types = 1

##--------------------------------------------------------------------------------------------------------------------##
#   Uniformity Calculations   #

Gold_Ratio = (math.sqrt(5) + 1) / 2
Gold_Angle = (2 - Gold_Ratio) * (2 + np.pi)

Set_Num_Particles_algo = Set_Num_Particles + 1  # Accounts for Algorithm Starting at 1 thus losing 1 particle

Expansion_Factor = 10   # Algorithm computes for a unit circle so use this to increase the size of the sphere

for i in range(Set_Num_Particles_algo):
    latitude = np.arcsin(-1 + 2 * i / (Set_Num_Particles_algo + 1))
    longitude = Gold_Angle * i

    temp_x = ((np.cos(longitude) * np.cos(latitude)) * Expansion_Factor) + x0
    # These Calculate the x,yz pointsCenter the membrane in the sim cell
    temp_y = ((np.sin(longitude) * np.cos(latitude)) * Expansion_Factor) + y0
    # and centers the membrane in the sim cell
    temp_z = ((np.sin(latitude)) * Expansion_Factor) + z0

    if (temp_x and temp_y and temp_z) <= Atom_Place_Limit:
        Total_Number_Atoms = Total_Number_Atoms + 1

        Total_xyz[Total_Number_Atoms] = {'Atom_ID': Total_Number_Atoms,
                                         'Molecule_ID': Membrane_Molecule_Type,
                                         'Atom_Type': Membrane_Atom_Type,
                                         'X': temp_x,
                                         'Y': temp_y,
                                         'Z': temp_z,
                                         'Positions String': '{} {} {}'.format(temp_x,
                                                                               temp_y,
                                                                               temp_z)}

########################################################################################################################
###     Write LAMMPS Data File      ###
with open(Filename, 'w+') as fdata:  # opens a text file named a for the 'filename' variable
    fdata.write('{}\n\n'.format(Filename))  # First line is a comment line

    ##     Header of Data File     ##

    #   Atoms Header #

    fdata.write('{} atoms\n'.format(Total_Number_Atoms))  # Specify number of atoms
    fdata.write('{} atom types\n'.format(Total_Atom_Types))

    # fdata.write('{} bonds per atom\n'.format(bonds_per_atom_limit))

    # Bonds Header  #
    # fdata.write('{} bonds\n'.format(num_molecule_1_bonds))  # Specify number of atoms

    fdata.write('{} bond types\n'.format(Total_Bond_Types))
    fdata.write('{} angle types\n'.format(Total_Angle_Types))
    fdata.write('{} dihedral types\n'.format(Total_Dihedral_Types))

    #   specify box dimensions      #

    fdata.write('{} {} xlo xhi\n'.format(0.0, Sim_Box_Side_Length))  # Writes X Position
    fdata.write('{} {} ylo yhi\n'.format(0.0, Sim_Box_Side_Length))  # Writes Y Position
    fdata.write('{} {} zlo zhi\n'.format(0.0, Sim_Box_Side_Length))  # Writes Z Position

    fdata.write('\n')  # Skips the Next line for Formatting

    ##      Data File Body      ##

    #       Atoms section       #
    fdata.write('Atoms\n\n')
    for i, pos in enumerate(Total_xyz):
        fdata.write('{} {} {} {} \n'.format(Total_xyz[pos].get('Atom_ID'),
                                            Total_xyz[pos].get('Molecule_ID'),
                                            Total_xyz[pos].get('Atom_Type'),
                                            Total_xyz[pos].get('Positions String')))
    fdata.write('\n')

########################################################################################################################
###         Finished!!!     ###
print(' Data File Created Successfully!!! ; File name => {} '.format(Filename))
