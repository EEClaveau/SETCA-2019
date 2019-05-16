#This is geometry analysis code
import numpy
import os
file_location = os.path.join('data','water.xyz')
xyz_file=numpy.genfromtxt(fname=file_location,skip_header=2,dtype='unicode')
symbols=xyz_file[:,0]
coordinates=xyz_file[:,1:]
coordinates=coordinates.astype(numpy.float)
def calculate_distance (atom1, atom2):
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance
def bond_check(bond_distance):
    if bond_distance < 1.5 and bond_distance > 0:
        return True
    else:
        return False
for numA, atomA in enumerate(coordinates):
    for numB, atomB in enumerate(coordinates):
        if numB<numA:
            distance_AB=calculate_distance(atomA, atomB)
            if bond_check(distance_AB) is True:
                print(F'{symbols[numA]} to {symbols[numB]} : {distance_AB:.3f}')
