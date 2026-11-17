###############################################################################################################################
# GENERAL CODE FORMAT (DELETE THIS LINE AND ONE BELOW)
#
# (CODE TITLE.EXTENSION) - (DISCRPITION OF CODE GOAL/OBJECTIVE)
#
# By: John Quinn
#
# Date: ##/##/2020
#
# Summary of Code: (General Steps of code)
#   0. Import Packages
#
#   1. Specify Parameters
#       1a. Set Initial Values
#       1b. Calculations based on  Initial Values
#
#	2. Generate Random Atom Positons
#       2a. Creates the Initial Configuration of RBC membrane with spectrin network
#
#   3. Write LAMMPS Data file
#
#
# Apendix of Commands:
#	Command -> commands function ; format( Command arg1 arg 2 . . .) ; more notes
#
# Version List:
#
# Possible Future Improvments:
#
# Refrences:
#   JQ-Random.py
#
#   create_rbc_with_water.m (https://data.mendeley.com/datasets/4v53nkv5hc/1)
#
###############################################################################################################################

# 0. Import Packages
from typing import List

import numpy as np

# 1. Specify Parameters
#   1.a. Set Initial Values

pi = 3.14159265359                                                                                  # Defines Pi

num_atoms = 1000                                                                                    # Number of Atoms to Write/Generate

sys_size = 100                                                                                      # Size of the Simulation Box (Will be set size in x,y,and z)

d0_water = 2.7                                                                                      # distance between water particles in the initial configuration

d0_vesicle  = 0.97                                                                                  # particle distance

D_vesicle=50                                                                                        # distance between the bilayer membrane particles

gap = 2                                                                                             # gap between bilayer and spectrin network in initial configuration

b = 10                                                                                              # extra space between box boundary and vesicle

n_bead = 11                                                                                         # Number of beads between nodes of spectrin network, *needs to be an odd number

d0_network  = 9                                                                                     # Distance between the nodes in the initial configuration or A-A distance

shape = [ 1 1 1]                                                                                  # Shape of bilayer particles, * No need to change this



#   1.b. Calculations based on  Initial Values

R_vesicle = D_vesicle/2                                                                             # Diameter of the vesicle in initial configuration

D_network = D_vesicle - (gap * 2)                                                                   # Diameter of Spectrin Network in initial configuration

volume_vesicle = 4/3 * pi * (0.5 ** 3) * shape(1) * shape(2) * shape(3)

volume_network = 4/3*pi*0.5^3

volume_water=4/3*pi*(d0_water/2)^3



# 2. Generate Atom Positions
#   2a. Creates the Initial Configuration of RBC membrane with spectrin network

[natoms_vesicle,xyz_vesicle]=points_on_sphere(D_vesicle,d0_vesicle)

[natoms_anchor,xyz_network]=points_on_sphere(D_network,d0_network)

tri = convhulln(xyz_network)

[bond,~]=find_bond(tri,xyz_network);

n_tri = size(tri, 1);
n_bond = n_tri * 3 / 2;

new_n_bond = n_bond * (n_bead + 1) + natoms_anchor + n_bond;
new_bond = zeros(new_n_bond, 2);

for i=1:n_bond
atom_i = bond(i, 1);
atom_j = bond(i, 2);
r_i = xyz_network(atom_i,:);
r_j = xyz_network(atom_j,:);

j = 1;
new_atom_id = natoms_anchor + j + (i - 1) * n_bead;
new_bond_id = j + (i - 1) * (n_bead + 1);
new_bond(new_bond_id, 1: 2) = [atom_i, new_atom_id];
xyz_network(new_atom_id, 1: 3) = r_i + j * (r_j - r_i) / (n_bead + 1);

for j=2:n_bead
new_atom_id = natoms_anchor + j + (i - 1) * n_bead;
new_bond_id = j + (i - 1) * (n_bead + 1);
new_bond(new_bond_id, 1: 2) = [new_atom_id - 1, new_atom_id];
xyz_network(new_atom_id, 1: 3) = r_i + j * (r_j - r_i) / (n_bead + 1);
end

new_bond_id = new_bond_id + 1;
new_bond(new_bond_id, 1: 2) = [new_atom_id, atom_j];
end

vesicle_atom_type = ones(1, natoms_vesicle);

for i=1:natoms_anchor
r = xyz_vesicle - ones(natoms_vesicle, 1) * xyz_network(i,:);
r = sum(r. * r, 2);
[~, ind] = sort(r);

new_bond(n_bond * (n_bead + 1) + i,:) = [ind(1), i + natoms_vesicle];

vesicle_atom_type(ind(1)) = 2;
end

for i=natoms_anchor+1:natoms_anchor + n_bond
k = (i - natoms_anchor - 1) * n_bead + (n_bead + 1) / 2;
r = xyz_vesicle - ones(natoms_vesicle, 1) * xyz_network(natoms_anchor + k,:);
r = sum(r. * r, 2);
[~, ind] = sort(r);

new_bond(n_bond * (n_bead + 1) + i,:) = [ind(1), natoms_anchor + k + natoms_vesicle];

vesicle_atom_type(ind(1)) = 2;
end

natoms_network = natoms_anchor + n_bond * n_bead;

n_point = natoms_vesicle + natoms_network;

density_vesicle = 1 / (4 / 3 * pi * shape(1) * shape(2) * shape(3));
density_network = 1 / (4 / 3 * pi);
density_water = 1 / (4 / 3 * pi);






# 3. Write LAMMPS Data File

with open('JQ-random.data', 'w') as fdata:
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
    for i, pos in enumerate(positions):
        fdata.write('{} 1 {} {} {}\n'.format(i + 1, *pos))
