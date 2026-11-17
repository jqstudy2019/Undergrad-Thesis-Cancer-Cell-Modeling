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

# Set Variables Used For Later

#   Simulation Variables

filename = "SimpV4"

sim_size = 100

atom_types = 1

bond_types = 1

num_molecules = 1

sphere_1_thickness = 15

sphere_1_radius = 10

sphere_1_coords = []

num_atoms_sphere_1 = 0

membrane_1 = {}

num_objects = 0

#   Program Performance Tracking

positions_checked = 0


# Used in multimembrane sims to set separation of membranes

# X_separation = 0
# Y_separation = 0
# Z_separation = 39

########################################################################################################################

# Molecular Atom Style Class Definition
# Class definition is used to set up the needed data structure

class Moleculule1:
    def __init__(self, atom_id, mol_id, atom_type, x_pos, y_pos, z_pos):
        self.self = atom_id
        self.mol_id = 1
        self.atom_type = 1
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos

    def sqwak_data(self):
        print(" Test: Blah bLah {} \n"
              .format(self.atom_id, self.mol_id, self.atom_type, self.x_pos, self.y_pos, self.z_pos))

def make_object(atom_id, mol_id, atom_type, x_pos, y_pos, z_pos, num_objects):
    num_objects = 1





########################################################################################################################

# Creates an Array Called SIM_SPACE ( is a 3-D array (x,y,z of each simulation space position )
SIM_SPACE = np.zeros((sim_size, sim_size, sim_size))

# Extra Copy of the Sim Space kept because its "pure"
SIM_SPACE_copy = deepcopy(SIM_SPACE)

########################################################################################################################

# Finds the Center of the Sim Space ( x0, y0, z0 )

x0 = int(np.floor(SIM_SPACE_copy.shape[2] / 2))
y0 = int(np.floor(SIM_SPACE_copy.shape[1] / 2))
z0 = int(np.floor(SIM_SPACE_copy.shape[0] / 2))

# Iterates Each Position of the sim and . . .
for x in range(0, sim_size):
    for y in range(0, sim_size):
        for z in range(0, sim_size):
            ''' # This section measures the distance from the Center (x0,y0,z0) to each point and . . .
                    # deb: measures how far a coordinate in A is far from the center.
                    # deb>=0: inside the sphere.
                    # deb<0: outside the sphere.'''

            deb = (sphere_1_radius ** 2) - ((x0 - x) ** 2) - ((y0 - y) ** 2) - ((z0 - z) ** 2)
            positions_checked = positions_checked + 1

            # if statement to execute code for saving sphere coords + info
            if (deb >= 0) and (deb <= sphere_1_thickness):

                temp = [x, y, z]




               # for num_atoms_sphere_1:
               # temp = Molecular(num_atoms_sphere_1, num_molecules, atom_types, x, y, z)
               # membrane_1 = membrane_1 + temp
              #  num_atoms_sphere_1 = num_atoms_sphere_1 + 1

            ''' sphere_1_coords.append((x, y, z)) # Used in code before python class was used '''

########################################################################################################################

# Prints Sim Info To Make Sure Its Running Correct

print("Number of atoms placed in Sphere 1: {} \n".format(num_atoms_sphere_1))
print("Number of Points in Simulation Space: {} \n".format(positions_checked))
print("List of Points (test): {} \n".format(membrane_1))

########################################################################################################################

# 3. Write LAMMPS Data File

#with open('SimpV4.data', 'w+'.format('filename')) as fdata:
    # First line is a comment line
   # fdata.write('{}.data\n\n'.format('filename'))

    # --- Header ---#

    # Specify number of atoms and atom types
   # fdata.write('{} atoms\n'.format(num_atoms_sphere_1))
    #fdata.write('{} bonds\n\n'.format(num_atoms_sphere_1 - 2))

  #  fdata.write('{} atom types\n'.format(atom_types))
   # fdata.write('{} bond types\n\n'.format(bond_types))

    # Specify box dimensions
   # fdata.write('{} {} xlo xhi\n'.format(0.0, sim_size))
   # fdata.write('{} {} ylo yhi\n'.format(0.0, sim_size))
    #fdata.write('{} {} zlo zhi\n'.format(0.0, sim_size))
    #fdata.write('\n')

    # Atoms section
    #fdata.write('Atoms\n\n')

    # Write each position
    #for i, pos in range(num_atoms_sphere_1):
        #fdata.write('{} \n'.format())

    # Writes bonds Section
    #fdata.write('\nBonds\n\n')

    #for i in range(1, 929):
       # fdata.write('{} 1 {} {}\n'.format(i, i, i + 1))

#print('Data File Created Successfully; File name => {}.data  '.format(filename))

########################################################################################################################
