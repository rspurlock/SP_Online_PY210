#!/usr/bin/env python3

import os
import pathlib

# Display files using OS module walk method (Need to break to only do current directory)
print('Files using the OS module walk method')
for path, dirs, files in os.walk(os.getcwd()):
    for file in files:
        print(os.path.join(path, file))
    break
print()

# Display files using OS module listdir method (Must check each entry for a file vs dir)
print('Files using the OS module listdir method')
path = os.getcwd()
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print(os.path.join(path, entry))
print()

# Display files using Path module iterdir method (Must check each entry for a file vs dir)
print('Files using the Path module iterdir method')
path = pathlib.Path('./')
for entry in path.iterdir():
    if (entry.is_file()):
        print(entry.absolute())

