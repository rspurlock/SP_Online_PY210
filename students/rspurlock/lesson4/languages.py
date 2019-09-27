#!/usr/bin/env python3

import os
import sys
import pathlib

# Open the students.txt file to read the information from
with open('students.txt', 'r') as input:

    #  Read and skip the first line as that is just a header
    line = input.readline()

    # Initialize the language dictionary to empty
    languageDict = dict()

    # Loop reading all the lines of the file
    while line:

        # Get the next line from the file (May be none)
        line = input.readline()
        if line:

            # Split the line into Name and [Nickname], Languages
            items = line.split(':')

            # Extract the Name and [Nickname], Languages (Strip off leading and trailing whitespace from each)
            name = items[0].strip()
            items = items[1].strip()

            # Split the items out into [Nickname], Languages
            languages = [item.strip() for item in items.split(',') if len(item) > 0]

            # Check for languages remaining in the list (may be empty)
            if (len(languages) > 0):

                # Check for [Nickname] or languages present (and not equal to nothing)
                if (len(languages[0]) > 0) and (languages[0] != 'nothing'):

                    # Get the first letter of the first entry (Nickname or first language)
                    letter = languages[0][0]

                    # Check to see if this is a nickname (First letter is capitalized), if so remove it
                    if (letter == letter.upper()):
                        languages = languages[1:]

                else:   # No nickname or language (or nothing)

                    # Remove the empty or nothing entry
                    languages = languages[1:]

                # Update the languages dictionary which has a count for each entry
                for language in languages:
                    if language in languageDict:
                        languageDict[language] += 1
                    else:
                        languageDict[language] = 1

# Print the languages found
print(F'Found {len(languageDict)} languages used:')
for language in languageDict:
    print(f'{language:11} - {languageDict[language]}')

# Close the input file
input.close()
