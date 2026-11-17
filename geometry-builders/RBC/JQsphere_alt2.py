###############################################################################################################################
# JQsphere.py - python code to make a sphere geometry for a simple lammps simulation
#
# By: John Quinn
#
# Date: 4/23/2020
#
# Summary of Code: (General Steps of code)
#   0. Import Packages
#       -Numpy
#
#   1.
#
# Apendix of Commands:
#	Command -> commands function ; format( Command arg1 arg 2 . . .) ; more notes
#
# Version List:
#
# Possible Future Improvments:
#
# Refrences:
#       Google
#           https://datascienceplus.com/vectors-and-arrays-in-python/
#
#
###############################################################################################################################
# 0. Import Packages
#       - Numpy

import numpy as np

#

sradius = 100

boxlength = sradius * 2

boxvolume = boxlength ** 3

i = 0

for x in range(boxlength):
    for y in range(boxlength):
         for z in range(boxlength):
            i = i + 1
            M = np.empty([3,boxvolume])
            np.append(M, [i, x, y, z])


print(M)
