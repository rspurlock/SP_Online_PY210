#!/usr/bin/env python3

import os
import sys
import pathlib

# Declare the fileCopy buffer size
bufferSize = 4096

# Check for interactive usage (No arguments)
if (len(sys.argv) == 1):

    # Prompt user for the source and destination files
    source = input('Enter source file name: ')
    destination = input('Enter destination file name: ')

else:   # Not interactive usage (Check for command line arguments)

    # Check for correct script usage (2 args required, source and destination)
    if (len(sys.argv) == 3):

        # Get the entered source and destination file names
        source = sys.argv[1]
        destination = sys.argv[2]

    else:
        print('Usage: copyfile source destination')
        exit()

# Open the source and destination files as binary
with open(source, 'rb') as src, open(destination, 'wb') as dest:

    # Initialize buffer so we always try to read at least one block
    buffer = ' '

    # Loop reading and writing 'bufferSize' chunks of the files
    while (len(buffer) != 0):

        # Read and write the next buffer size chunk
        buffer = src.read(bufferSize)
        dest.write(buffer)

# Close the source and destination files
src.close()
dest.close()
