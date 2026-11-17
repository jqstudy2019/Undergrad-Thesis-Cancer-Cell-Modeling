import numpy as np
from copy import deepcopy


class Membrane:
    def __init__(self, part_id, x, y, z):
        self.part_id = part_id
        self.x = x
        self.y = y
        self.z = z

    def sqwak(self):
        print(" Test: Blah bLah {} \n".format(m1.part_id))


m1 = Membrane(1, 30, 30, 30)

print("\n Test: Particle_ID = {} ; X = {} ; Y = {} : Z = {} \n".format(m1.part_id, m1.x, m1.y, m1.z))

m1.sqwak()

