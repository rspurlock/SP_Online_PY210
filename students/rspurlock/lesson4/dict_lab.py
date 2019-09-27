#!/usr/bin/env python3

def printDictionary(dictionary):
    """
    Function to display a dictionary in a nice readable fashion

    Positional Parameters
    :param dictionary:  Dictionary to print key/value pairs for
    """

    # Loop thru all the dictionary items (key/value pairs) printing them
    for key, value in dictionary.items():
        print(f'{key} = {value}')

    # Print a blank line for readability
    print()

# Dictionaries 1
print('Dictionaries 1')

dictionary = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
printDictionary(dictionary)
del dictionary['cake']
printDictionary(dictionary)
dictionary['fruit'] = 'Mango'
printDictionary(dictionary)
print('Keys')
for key in dictionary.keys():
    print(f'{key}')
print()
print('Values')
for value in dictionary.values():
    print(f'{value}')
print()

# Dictionaries 2
print('Dictionaries 2')

# Create and print the original dictionary
dictionary = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'Chocolate'}
printDictionary(dictionary)

# Copy original dictionary and update values to number of letter t's
newDictionary = dictionary.copy()
for key, value in newDictionary.items():
    newDictionary[key] = value.lower().count('t')

# Print the updated dictionary
printDictionary(newDictionary)

# Sets 1
print('Sets 1')

# Create the 'empty' sets to build
s2 = set()
s3 = set()
s4 = set()

# Loop through the number 0 - 20 building the sets
for n in range(0, 21):
    if ((n % 2) == 0):
        s2.add(n)
    if ((n % 3) == 0):
        s3.add(n)
    if ((n % 4) == 0):
        s4.add(n)

# Print all of the created sets
print('s2 = ' + str(s2))
print('s3 = ' + str(s3))
print('s4 = ' + str(s4))
print()

# Check for subsets
print('Is s3 a subset of s2? ' + str(s3.issubset(s2)))
print('Is s4 a subset of s2? ' + str(s4.issubset(s2)))
print()

# Sets 2
print('Sets 2')

# Create the python and marathon sets
pythonSet = set('Python')
marathonSet = frozenset('marathon')

# Display these two sets
print('Python set - ' + str(pythonSet))
print('marathon set - ' + str(marathonSet))
print()

# Display the union and intersection of these sets
print("Python union marathon is " + str(pythonSet.union(marathonSet)))
print("Python intersect marathon is " + str(pythonSet.intersection(marathonSet)))
print()
