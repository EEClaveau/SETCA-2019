#This is geometry analysis code
import numpy
import os
import sys
file_location = os.path.join('data','water.xyz')
xyz_file=numpy.genfromtxt(fname=file_location,skip_header=2,dtype='unicode')
def open_xyz(filename):
    xyz_file=numpy.genfromtxt(fname=filename,skip_header=2,dtype='unicode')
    symbols=xyz_file[:,0]
    coordinates=xyz_file[:,1:]
    coordinates=coordinates.astype(numpy.float)
    return symbols,coordinates

if __name__=='__main__':
     if len(sys.argv)<2:
        raise IndexError('No file name given. Script requires and xyz file')
     xyzfilename=sys.argv[1]
     symbols,coordinates=open_xyz(xyzfilename)

def calculate_distance (atom1, atom2):
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atom1: list
        A list of coordinates [x,y,z]
    atom2: list
        A list of coordinates [x,y,z]

    Returns
    -------
    bond_length: bond_length
            The distance between atoms.

    Examples
    --------
    >>>calculate_distance([0, 0, 0],[0, 0, 1])
    1.0
    """
    x_distance = atom1[0]-atom2[0]
    y_distance = atom1[1]-atom2[1]
    z_distance = atom1[2]-atom2[2]
    distance = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
    return distance
def bond_check(bond_distance):
    """
    Check if distance is a bond.

    Parameters
    ----------
    atom_distance: float
        The distance between atoms.
    minimum_length: float
        The minimum distance for a bond.
    maximum_length: float
        The maximum distance for a bond.

    Returns
    -------
    True if bond
    False if not a bond
    """

    #Check that atom_distance is a float
    if not isinstance(bond_distance,float):
        raise TypeError(F'bond_distance must be type float. {bond_distance}')
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
