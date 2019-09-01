def string_times(str, n):
    """
    Function to return the given string duplicated the given number of times

    :param str: The string to duplicate
    :param n:   The number of times to duplicate the string

    :return:    New string that is the original string duplicated the requested number of times
    """
    result = ''
    for x in range(n):
        result += str
    return result


# Test cases for string_times function
print('string_times')
print("string_times('Hi', 2) → ", string_times('Hi', 2))
print("string_times('Hi', 3) → ", string_times('Hi', 3))
print("string_times('Hi', 1) → ", string_times('Hi', 1))
print()


def front_times(str, n):
    """
    Function to return the front 3 characters of the given string the requested number of times
        If the given string is less than 3 characters then the string is the front

    :param str: String to get the front 3 characters from
    :param n:   The number of times to duplicate the front 3 characters

    :return:    New string that is the front 3 characters duplicated the requested number of times
    """
    result = ''
    if (len(str) < 4):
        for x in range(n):
            result += str
    else:
        for x in range(n):
            result += str[0:3]
    return result


# Test cases for front_times function
print('front_times')
print("front_times('Chocolate', 2) → ", front_times('Chocolate', 2))
print("front_times('Chocolate', 3) → ", front_times('Chocolate', 3))
print("front_times('Abc', 3) → ", front_times('Abc', 3))
print()


def string_bits(str):
    """
    Function to return a new string made up of every other character of the given string

    :param str: String to extract every other character from

    :return:    New string that is made up of every other character from the original string
    """
    pos = 0
    result = ''
    for x in range((len(str) + 1) // 2):
        result += str[pos:pos + 1]
        pos += 2
    return result


# Test cases for string_bits function
print('string_bits')
print("string_bits('Hello') → ", string_bits('Hello'))
print("string_bits('Hi') → ", string_bits('Hi'))
print("string_bits('Heeololeo') → ", string_bits('Heeololeo'))
print()


def string_splosion(str):
    """
    Function to retuen a string "splosion", i.e. a new string made up of a combination of each substring of the given string

    :param str: Original string to generate the "splosion" string from

    :return:    New string made up of a combination of each substring of the given string
    """
    result = ''
    for x in range(len(str)):
        result += str[0:x + 1]
    return result


# Test cases for string_splosion function
print('string_splosion')
print("string_splosion('Code') → ", string_splosion('Code'))
print("string_splosion('abc') → ", string_splosion('abc'))
print("string_splosion('ab') → ", string_splosion('ab'))
print()


def last2(str):
    """
    Function to return a count of the number of times a substring of the last 2 characters appears in the given string
        Not counting the actual last 2 character substring itself

    :param str: String to count the number of times the substring of the last 2 characters occurs

    :return:    Number of times the substring of the last 2 characters appears in the original string
                    Not counting the actual last 2 character substring itself
    """
    count = 0
    if (len(str[-2:]) == 2):
        for x in range(len(str) - 2):
            if (str[x:x + 2] == str[-2:]):
                count += 1
    return count


# Test cases for last2 function
print('last2')
print("last2('hixxhi') → ", last2('hixxhi'))
print("last2('xaxxaxaxx') → ", last2('xaxxaxaxx'))
print("last2('axxxaaxx') → ", last2('axxxaaxx'))
print()


def array_count9(nums):
    """
    Function to count the number of 9's in an array

    :param nums:    Array containing the numbers to check

    :return:        The number of 9's in the given array
    """
    count = 0
    for x in nums:
        if (x == 9):
            count += 1
    return count


# Test cases for array_count9 function
print('array_count9')
print("array_count9([1, 2, 9]) → ", array_count9([1, 2, 9]))
print("array_count9([1, 9, 9]) → ", array_count9([1, 9, 9]))
print("array_count9([1, 9, 9, 3, 9]) → ", array_count9([1, 9, 9, 3, 9]))
print()


def array_front9(nums):
    """
    Function to return True if one of the first four elements of the array is 9
        The array length may be less than four

    :param nums:    Array of numbers to check (the length may be less than four)

    :return:        True if one of the first four elements of the array is 9
    """
    count = min(4, len(nums))
    result = False
    for x in range(count):
        if (nums[x] == 9):
            result = True
    return result


# Test cases for array_front9 function
print('array_front9')
print("array_front9([1, 2, 9, 3, 4]) → ", array_front9([1, 2, 9, 3, 4]))
print("array_front9([1, 2, 3, 4, 9]) → ", array_front9([1, 2, 3, 4, 9]))
print("array_front9([1, 2, 3, 4, 5]) → ", array_front9([1, 2, 3, 4, 5]))
print()


def array123(nums):
    """
    Function to return True if the sequence 1, 2, 3 appears in the given array

    :param nums:    Array to check for the sequence 1, 2, 3

    :return:        True is the given array contains the sequence 1, 2, 3
    """
    result = False
    for x in range(len(nums) - 2):
        if ((nums[x] == 1) and (nums[x + 1] == 2) and (nums[x + 2] == 3)):
            result = True
    return result


# Test cases for array123 function
print('array123')
print("array123([1, 1, 2, 3, 1]) → ", array123([1, 1, 2, 3, 1]))
print("array123([1, 1, 2, 4, 1]) → ", array123([1, 1, 2, 4, 1]))
print("array123([1, 1, 2, 1, 2, 3]) → ", array123([1, 1, 2, 1, 2, 3]))
print()


def string_match(a, b):
    """
    Function to return the number of positions where two strings have the same 2 character substring

    :param a:   First string sequence to check
    :param b:   Second string sequence to check

    :return:    The number of positions where the two strings have the same 2 character substring
    """
    num = min(len(a), len(b)) - 1
    count = 0
    for x in range(num):
        if (a[x:x + 2] == b[x:x + 2]):
            count += 1
    return count


# Test cases for string_match function
print('string_match')
print("string_match('xxcaazz', 'xxbaaz') → ", string_match('xxcaazz', 'xxbaaz'))
print("string_match('abc', 'abc') → ", string_match('abc', 'abc'))
print("string_match('abc', 'axc') → ", string_match('abc', 'axc'))
print()
