import numpy as np
import argparse
import os

# Write all functions definitions 
def calculate_distance(coords1, coords2):
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords2[2]
    
    distance = np.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return distance

def bond_check(atom_distance, minimum_length = 0, maximum_length = 1.5):
    """
    Checks if a distance is a bond based on a minimum and a maximum
    Inputs : distance, minimum length for bond, maximum length for bond
    Default: minimum : 0, maximum : 0
    
    
    """
   
    if atom_distance > minimum_length and atom_distance < maximum_length:
        return True
    else:
        return False
    
def open_pdb(filename):
    """
    This function opens a standard pdb file.
    It returns the symbols as strings, and the coordinates as floats

    Args:
        filename (type: file) : standard file
    """
    x = []
    y = []
    z = []
    symbols = []
    with open(filename, 'r') as f:
        for line in f:
            if (line.startswith('ATOM')):
                x.append(float(line.split()[6]))
                y.append(float(line.split()[7]))
                z.append(float(line.split()[8]))
                symbols.append(line.split()[2])
            if (line.startswith('TER')):
                break
    coordinates = np.empty([len(x), 3])
    for i in range(len(x)):
        coordinates[i,0] = x[i]
        coordinates[i,1] = y[i]
        coordinates[i,2] = z[i]
        
    return symbols, coordinates

if __name__ == '__main__':    
    
    #Now, write coordinates
    parser = argparse.ArgumentParser(description= "This script analyzes a user given pdb file and outputs the lengths of all the bonds") # turn on parser
    parser.add_argument("path", help = "The filepath of the pdb file to analyze", nargs='*')
    #Tells parser what arguments going to be
    args = parser.parse_args() # Now collect the argument, go get arguments from the command line
    filenames = args.path
    
    for filename in filenames:        
        symbols, coordinates = open_pdb(filename)

        num_atoms = len(symbols)
        print(f'{os.path.basename(filename)}')

        for num1 in range(num_atoms):
            for num2 in range(num_atoms):
                if num1 < num2:
                        distance = calculate_distance(coordinates[num1], coordinates[num2])
                        if bond_check(distance) is True:
                            
                            print(f'{symbols[num1]} to {symbols[num2]} : {distance:.3f}')
        print()

