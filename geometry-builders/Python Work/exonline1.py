x = list(range(-5,5))
y = list(range(-5,5))
z = list(range(-5,5))
r = [1,2,3,4,5,6,7,10]
xcoords = []
ycoords = []
zcoords = []
##"""functions used"""
def square(number):
    return number**2
##"""determines which values satisfies the equation for a sphere"""
for itemx in x:
    for itemy in y:
        for itemz in z:
            for itemr in r:
                if abs(itemx) == abs(itemy) and abs(itemy) == abs(itemz) and square(itemx) + square(itemy) +square(itemz) == itemr:
                    xcoords.append(itemx)
                    ycoords.append(itemy)
                    zcoords.append(itemz)
"""determines the number of atoms in the system"""
natoms = len(xcoords)
"""writes coords onto txt file"""
out = open("sphere.xyz", "a")
print (natoms)
out.write("%s \n \n" %(natoms))
out.close()
for item in zip(xcoords, ycoords,zcoords):
   out = open("sphere.xyz", "a")
   print (item)
   out.write( "Ar"  " " " " "%2.5s %2.5s %2.5s \n" %(item))
   out.close()