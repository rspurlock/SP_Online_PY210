#!/usr/bin/env python3

import os
import re
import sys
import random


# Global variables
maxWidth = 50                   # Maximum line width value (Characters)
ending = '.?!'                  # Sentence ending characters
punctuation = ';:,'             # Punctuation characters
closing = '\'\"’”)]}'           # Closing group characters
invalid = '-,;:\'"‘’“”()[]{}'   # Invalid sentence starting characters

# Grouping dictionary for word groups (Key is start group character, Value is matching end group character)
grouping = {"'":"'", '"':'"', '‘':'’', '“':'”', '(':')', '[':']', '{':'}'}


def findStart(text):
    """
    Function to find the start of the book text file (Begins with *** START OF THIS PROJECT GUTENBURG EBOOK)

    Positional Parameters
    :param text:        Open book text file

    :return:            Returns when the start of the book text is found (Can continue to read contents)
    """
    # Initialize line so we always try to read at least one line
    line = ' '

    # Loop reading the lines from the text file
    while (len(line) != 0):

        # Read the next line from the file (Striping leading/trailing whitespace)
        line = text.readline()

        # Check to see if we have found the start of the ebook
        if ('*** START OF THIS PROJECT GUTENBERG EBOOK' in line):

            # Stop searching for start of book (Since we have found it)
            break


def readContents(text):
    """
    Function to find and read the actual contents of the given book text file

    Positional Parameters
    :param text:        Open book text file

    :return:            Returns the valid contents of the given ebook
    """
    # Initialize the contents as an empty list and the line count as zero
    contents = []

    # Find the start of the Project Gutenburg eBook
    findStart(text)

    # Loop reading the lines from the text file (Looking for valid contents)
    line = ' '
    while (len(line) != 0):

        # Read next line from the book text
        line = text.readline()

        # First check for end of book contents (Should be a blank line before/after start/end of book)
        if ('*** END OF THIS PROJECT GUTENBERG EBOOK' in line):
            break

        # Strip off leading/trailing whitespace for checking for valid line contents
        stripped = line.strip()

        # Check for valid line contents (Not a blank line, all caps line, etc)
        if ((len(stripped) != 0) and (stripped != stripped.upper())):
            contents.append(stripped)

    # Join all the contents together as a single string
    contents = ' '.join(contents)

    # Return the contents of the ebook
    return contents


def buildTrigrams(contents):
    """
    Function to build trigrams dictionary from ebook contents

    Positional Parameters
    :param contents:    Contents of the ebook

    :return:            Returns the trigram dictionary
    """
    # Initialize the trigrams dictionary
    trigrams = dict();

    # Generate the tokens for the ebook contents
    tokens = re.findall(r"\w+(?:[-'’]\w+)*|['\"‘“]|[-.(\[{?!]+|\S\w*", contents)

    # Loop processing each triplet of tokens (Adding them to the trigrams dictionary)
    for index in range(len(tokens) - 2):

        # Get the next key/value pair that belongs in the trigrams dictionary
        key = tuple(tokens[index : index + 2])
        value = tokens[index + 2]

        # Try to add this key into the trigrams dictionary (Which is a dictionary with values and counts)
        dictionary = trigrams.setdefault(key, {value : 0})

        # Check to see if this value already in the dictionary (Increment count if so, add if not)
        if (value in dictionary):
            dictionary[value] += 1
        else:
            dictionary[value] = 1

    # Return the trigrams dictionary
    return trigrams


def normalizeDictionary(dictionary):
    """
    Function to "normalize" a given dictionary entry

    Positional Parameters
    :param dictionary:  Dictionary entry to "normalize"

    :return:            On return the dictionary entry is "normalized"
    """
    # Initialize the sum of the dictionary values
    total = 0

    # Loop thru all the dictionary values and compute the total
    for value in dictionary.values():
        total += value

    # Initialize the current sum value
    current = 0;

    # Now that we have the total loop thru "normalizing" the dictionary values
    for key, value in dictionary.items():

        # Update the current sum and normalize the dictionary value (Based on computed total)
        current += value
        dictionary[key] = current / total


def normalizeTrigrams(trigrams):
    """
    Function to "normalize" trigrams dictionary entries (Before using it to generate output)

    Positional Parameters
    :param trigrams:    Trigrams dictionary to "normalize" the entries for

    :return:            On return the trigram dictionary is "normalized"
    """
    # Loop thru all the dictionaries in the trigram dictionary
    for key, dictionary in trigrams.items():

        # Call routine to "normalize" this dictionary entry
        normalizeDictionary(dictionary)


def parseBook(book):
    """
    Function to parse the given book text file and generate trigrams dictionary

    Positional Parameters
    :param book:        Name of book text file

    :return:            Returns generated trigrams dictionary
    """
    # Open the book text file to read
    with open(book, 'r', encoding='utf-8') as text:

        # Read the contents of the ebook
        contents = readContents(text)

        # Generate trigrams from the ebook contents
        trigrams = buildTrigrams(contents)

        # Call function to "normalize" the trigram dictionary entries
        normalizeTrigrams(trigrams)

    # Close the book text file
    text.close()

    # Return the book trigrams
    return trigrams


def selectFollow(dictionary):
    """
    Function to randomly select the "following" word from the dictionary entry

    Positional Parameters
    :param dictionray:  Dictionary entry to select the following word from

    :return:            Randomly selected following word
    """
    # Select a random value for choosing the following word
    value = random.random()

    # Loop thru the dictionary key/values to find the desired following word
    for key, probability in dictionary.items():

        # Check to see if the next key is the desired following word (Should always find one)
        if (value <= probability):
            return key


def findInitial(trigrams):
    """
    Function to find an initial trigram key to start with

    Positional Parameters
    :param trigrams:    Trigrams dictionary to use for finding initial key

    :return:            Returns the initial trigram key to use (Following should be new sentence)
    """
    # Initialize initial trigram to none
    initial = None

    # Loop looking for an initial trigram to start with (Sentence end trigram)
    while not initial:

        # Initialize the current trigram dictionary key to a random entry
        key = list(trigrams.keys())[random.randint(0, len(trigrams) - 1)]

        # Try to follow this trigram chain until the end of the sentence
        while (key[1] not in ending):

            # Get the trigram dictionary entry for the current key
            dictionary = trigrams.get(key)

            # Make sure we found a dictionary entry for this key
            if dictionary:

                # Randomly select a following word from this dictionary entry
                following = selectFollow(dictionary)

                # Generate new key from current key and following word
                key = (key[1], following)

            else:       # End of trigram chain (Didn't find sentence ending)

                # No sentence ending, exit search loop to try another random trigram entry
                break

        # Check to see if we found the end of the sentence
        if (key[1] in ending):

            # Use the current key as the initial trigram
            initial = key

    # Return the initial key
    return initial


def getGroup(trigrams, key, following):
    """
    Function to return the entire grouping specified by the start group character following

    Positional Parameters
    :param trigrams:    Trigrams dictionary to use when building the group
    :param key:         Current trigram key for start of grouping
    :param following:   Following word that was the start grouping character

    :return:            Returns the updated key and the entire group (As list)
    """
    # Save the group start character
    start = following

    # Initialize the group to list with just the start character in it
    group = [start]

    # Clear following in case start and end grouping characters are the same
    following = ''

    # Loop until the closing group character is found
    while following != grouping[start]:

        # Get the trigram dictionary entry for the current key
        dictionary = trigrams.get(key)

        # Make sure we found a dictionary entry for this key
        if dictionary:

            # Randomly select a following word from this dictionary entry (May be punctuation)
            following = selectFollow(dictionary)

            # Generate new key from current key and following word
            key = (key[1], following)

            # Make sure we're not at the closing character
            if following != grouping[start]:

                # Make sure we don't have overlapping groups (Closing character without a start)
                if ((following in closing) or (following == start)):

                    # Just skip this trigram entry and continue on
                    continue

                # Check for another sub-grouping
                if (following in grouping):

                    # Call routine to get the entire sub-grouping
                    key, sub = getGroup(trigrams, key, following)

                    # Check for a valid sub-group (Must be longer than just the start/end group)
                    if (len(sub) > 2):

                        # Extend the group to contain this sub-group as well
                        group.extend(sub)

                else:       # Not a sub-group

                    # Add the following word to the group (Could be sentence end)
                    group.append(following)

                    # Check for sentence end, close the group if found
                    if (following in ending):

                        # Clear the key since we reached the end of a sentence
                        key = None

                        # Append closing group character to the group
                        group.append(grouping[start])

                        # Break out of the loop since we reached the end of a sentence
                        break

            else:       # End of group found

                # Append closing group character to the group
                group.append(following)

        else:       # End of trigram chain (Closing group character not found)

            # Clear the key since we reached the end of the chain
            key = None

            # Append closing group character to the group
            group.append(grouping[start])

            # Break out of the loop since we reached the chain end
            break

    # Return the updated key and the group list
    return (key, group)


def addWord(text, line, word, start = None):
    """
    Function to add a word to the line and optionally to the text

    Positional Parameters
    :param text:        Text list to add the word to (If line width exceeded)
    :param line:        Text line to add the word to
    :param word:        Word to add to the line
    :param start:       Grouping start character if in a group (Empty otherwise)

    :return:            Returns with updated line (Text list is updated if necessary)
    """
    # Check to see if time to add this line to the text (Exceeds text width)
    if (len(line) > maxWidth):

        # Add this line to the text list
        text.append(line)

        # Reset line to empty
        line = ''

    # Check for adding initial word to line (no space required)
    if (len(line) == 0):

        # Check for punctuation character (Punctuation, ending, or closing)
        if ((word in punctuation) or (word in ending) or ((word in closing) and (word == start))):

            # Add punctuation to last text line (Don't update line yet)
            text[-1] = text[-1] + word

        else:       # Not punctuation

            # Adding initial word, don't use space
            line = word

    else:       # Adding to current line (May need space)

        # Check for punctuation character (Punctuation or ending)
        if ((word in punctuation) or (word in ending)):

            # Add punctuation character with no space
            line = line + word

        else:       # Word not punctuation (Might still be a group character)

            # Check for adding in a group (Start is group start character)
            if start:

                # Check for ending group character
                if (word == grouping[start]):

                    # Add ending group character with no space
                    line = line + word

                else:       # Not end of grouping

                    # Check for first word after grouping start
                    if (line[-1] == start):

                        # Add new word after grouping character with no space
                        line = line + word

                    else:       # Not first word after grouping start

                        # Add new word to the line (with space)
                        line = line + ' ' + word

            else:       # Not adding within a group

                # Add new word to the line (with space)
                line = line + ' ' + word

    # Return the updated line
    return line


def generateText(trigrams, words):
    """
    Function to generate text output from trigrams dictionary (Generate the requested number of words)

    Positional Parameters
    :param trigrams:    Trigrams dictionary to use when generating output text
    :param words:       Number of words to generate in the output text

    :return:            Returns the generated output text
    """
    # Indicate we are at the start of a sentence (For checking for a valid sentence start)
    atStart = True

    # Initialize current key to none and word count to 0
    key = None
    count = 0

    # Initialize the output line and text to empty
    line = ''
    text = []

    # Loop until the requested word count is reached (May be exceeded)
    while count < words:

        # Check to see if we need a new trigram key (Start or end of trigram chain)
        if not key:

            # Try to final new initial trigram key to start with (Start of a sentence)
            key = findInitial(trigrams)

        # Try to follow this trigram chain to the end
        while key:

            # Get the trigram dictionary entry for the current key
            dictionary = trigrams.get(key)

            # Make sure we found a dictionary entry for this key
            if dictionary:

                # Randomly select a following word from this dictionary entry (May be punctuation)
                following = selectFollow(dictionary)

                # Check to see if we are at the start of a sentence
                if atStart:

                    # Check for an invalid sentence start
                    if (following in invalid):

                        # Clear key to try and select a new sentence start
                        key = None

                        # Skip this invalid sentence start
                        continue

                # Generate new key from current key and following word
                key = (key[1], following)

                # Check for end of sentence (Time to check word count)
                if (following in ending):

                    # Clear key to force a new sentence start
                    key = None

                    # Add end of sentence to the line
                    line = addWord(text, line, following)

                    # Indicate we are now once again at the start of a sentence
                    atStart = True

                    # Break out of while loop so word count will be checked
                    break

                # Check for start of a grouping (Need to collect the entire grouping)
                if (following in grouping):

                    # Call routine to get the entire grouping
                    key, group = getGroup(trigrams, key, following)

                    # Check for a valid group (Must be more than just the start/end group characters)
                    if (len(group) > 2):

                        # Clear indication we are in a group
                        start = ''

                        # Initialize a stack in case we have nested groups
                        stack = [start]

                        # Loop adding the grouping to the text
                        for word in group:

                            # Add this word to the current line/text
                            line = addWord(text, line, word, start)

                            # Check to see if currently in a group
                            if start:

                                # Check to see if this is the end of a group
                                if (word == grouping[start]):

                                    # Pop start character from stack in case of nested groups
                                    start = stack.pop()

                                    # Just continue if end of group (Not a new word)
                                    continue

                                # Check for a nested group
                                if (word in grouping):

                                    # Push current group character onto the stack
                                    stack.append(start)

                                    # Change to the new group character
                                    start = word

                                    # Just continue if nested group start (Also not a new word)
                                    continue

                            else:       # Not currently in a group

                                # Check to see if this is the start of a new group
                                if (word in grouping):

                                    # Indicate we are now in a group
                                    start = word

                                    # Just continue if group start (Also not a new word)
                                    continue

                            # Check for an actual word vs. punctuation (Don't count punctuation in word count)
                            if ((word not in punctuation) and (word not in ending)):

                                # Increment the current word count
                                count += 1

                    # Just continue after the group is completed
                    continue

                # Check for closing group (Invalid since no start group present)
                if (following in closing):

                    # Just skip this trigram entry and continue on
                    continue

                # Add this word to the current line/text
                line = addWord(text, line, following)

                # Indicate we are no longer at the start of a sentence
                atStart = False

                # Check for an actual word vs. punctuation (Don't count punctuation in word count)
                if (following not in punctuation):

                    # Increment the current word count (Sin
                    count += 1

            else:   # Reached the end of our trigram chain

                # Just end this sentence for now
                line = addWord(text, line, '.')

                # Reset key so we'll select a new trigram to start with
                key = None

                # Break out of while loop so new trigram can be selected (And word count checked)
                break

    # Check for any remaining lines to add to the text
    if line:

        # Add last line to the text
        text.append(line)

    # Return the generated text
    return text


def main(argc, argv):
    """
    Function to run trigrams program

    Positional Parameters
    :param argc:        Count of arguments
    :param argv:        List of passed arguments

    :return:            Generates a story of the desired length based on the trigrams of the given book
    """
    # Initialize to no random number seed (Can change to a constant seed value if needed)
    seed = None

    # Check for interactive usage (No arguments)
    if (len(argv) == 1):

        # Prompt user for the book source and number of text words to generate
        book = input('Enter book file name: ')
        words = int(input('Enter number of words to generate: '))

        # Uncomment the following line to request a user seed value
        #seed = int(input('Seed: '))

    else:   # Not interactive usage (Check for command line arguments)

        # Check for correct script usage (2 args required, book and words, optional seed as 3rd argument)
        if (argc >= 3):

            # Get the entered book filename and word count
            book = argv[1]
            words = int(argv[2])

            # Check for a seed argument present
            if (argc == 4):
                seed = int(argv[3])

        else:

            print('Usage: trigrams book words [seed]')
            exit()

    # Parse the given book to generate the trigrams
    trigrams = parseBook(book)

    # Check to see if a random number seed was given
    if seed:
        random.seed(seed)

    # Call routine to generate the requested text (From the trigrams)
    text = generateText(trigrams, words)

    # Print the generated text
    for line in text:
        print(line)

    print()

# Guard against running this code if imported
if __name__ == "__main__":
    main(len(sys.argv), sys.argv)

    # Uncomment the following code to process all the books in the books folder
#    words = 25
#    for path, dirs, files in os.walk('.\\books'):
#        for file in files:
#            print(os.path.join(path, file))
#            print()
#            args = ['trigrams.py', os.path.join(path, file), words]
#            main(len(args), args)
#        break
