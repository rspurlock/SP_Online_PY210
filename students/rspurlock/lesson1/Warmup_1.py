def sleep_in(weekday, vacation):
    """
    Function to return True to sleep in if not a weekday or we're on vacation

    :param weekday:     True is this is a weekday, otherwise False
    :param vacation:    True if on vacation, otherwise False

    :return:            True is not a weekday or we're on vacation (Sleep in)
    """
    return (not(weekday) or vacation)


# Test cases for sleep_in function
print('sleep_in')
print("sleep_in(False, False) → ", sleep_in(False, False))
print("sleep_in(True, False) → ", sleep_in(True, False))
print("sleep_in(False, True) → ", sleep_in(False, True))
print()


def monkey_trouble(a_smile, b_smile):
    """
    Function to return True if either both monkeys are smiling or neither monkey is smilig
        In either case we are in "monkey trouble"

    :param a_smile: True if monkey a is smiling, otherwise False
    :param b_smile: True if monkey b is smiling, otherwise False

    :return:        True if either both monkeys are smiling or neither monkey is smiling (monkey trouble)
    """
    return (a_smile == b_smile)


# Test cases for monkey_trouble function
print('monkey_trouble')
print("monkey_trouble(True, True) → ", monkey_trouble(True, True))
print("monkey_trouble(False, False) → ", monkey_trouble(False, False))
print("monkey_trouble(True, False) → ", monkey_trouble(True, False))
print()


def sum_double(a, b):
    """
    Function to return the sum of two values
        Unless the values are the same and in that case return double the sum

    :param a:   First value to sum
    :param b:   Second value to sum

    :return:    The sum of a + b unless a == b and in that case it returns 2 * (a + b)
    """
    sum = a + b
    if (a == b):
        sum *= 2
    return sum


# Test cases for sum_double function
print('sum_double')
print("sum_double(1, 2) → ", sum_double(1, 2))
print("sum_double(3, 2) → ", sum_double(3, 2))
print("sum_double(2, 2) → ", sum_double(2, 2))
print()


def diff21(n):
    """
    Function to return the absolute difference between a given value and 21
        Unless the absolute difference is great than 21, in that case return double the absolute difference

    :param n:   Value to get absolute difference from 21 from

    :return:    Absolute difference between value and 21, unless difference is greater than 21, then return 2 * absolute difference
    """
    diff = abs(n - 21)
    if (n > 21):
        diff *= 2
    return diff


# Test cases for diff21 function
print('diff21')
print("diff21(19) → ", diff21(19))
print("diff21(10) → ", diff21(10))
print("diff21(21) → ", diff21(21))
print()


def parrot_trouble(talking, hour):
    """
    Function to return True if the parrot is talking outside the hours of 7 to 20
        In which case our parrot is just causing trouble (parrot trouble)

    :param talking: True if the parrot is talking, otherwise False
    :param hour:    The current time hour value (In a 24 hour format)

    :return:        True if the parrot is talking and the time is outside of 7 to 20 (parrot trouble)
    """
    return (talking and ((hour < 7) or (hour > 20)))


# Test cases for parrot_trouble function
print('parrot_trouble')
print("parrot_trouble(True, 6) → ", parrot_trouble(True, 6))
print("parrot_trouble(True, 7) → ", parrot_trouble(True, 7))
print("parrot_trouble(False, 6) → ", parrot_trouble(False, 6))
print()


def makes10(a, b):
    """
    Function to return True if either value is 10 or the sum of the values is 10

    :param a:   First value to check for 10
    :param b:   Second value to check for 10

    :return:    Return True if either value a or b is 10 or the sum of a + b is 10
    """
    return ((a == 10) or (b == 10) or ((a + b) == 10))


# Test cases for makes10 function
print('makes10')
print("makes10(9, 10) → ", makes10(9, 10))
print("makes10(9, 9) → ", makes10(9, 9))
print("makes10(1, 9) → ", makes10(1, 9))
print()


def near_hundred(n):
    """
    Function to return True if the given value is within 10 of either 100 or 200

    :param n:   Value to check against 100 or 200

    :return:    Returns True if the value is within 10 of either 100 or 200
    """
    return ((abs(n - 100) <= 10) or (abs(n - 200) <= 10))


# Test cases for near_hundred function
print('near_hundred')
print("near_hundred(93) → ", near_hundred(93))
print("near_hundred(90) → ", near_hundred(90))
print("near_hundred(89) → ", near_hundred(89))
print()


def pos_neg(a, b, negative):
    """
    Function to return True if one value is negative and the other value is positive
        Unless the negative parameter is True and then only return True if both values are negative

    :param a:           First value to check (positive/negative)
    :param b:           Second value to check (positive/negative)
    :param negative:    If True then both values must be negative to return True

    :return:            Returns True if one value is positive and the other value is negative
                            Unless the negative parameter is True and in that case both values must be negative to return True
    """
    return ((a < 0) and (b < 0)) if negative else ((a < 0) and (b > 0)) or ((a > 0) and (b < 0))


# Test cases for pos_neg function
print('pos_neg')
print("pos_neg(1, -1, False) → ", pos_neg(1, -1, False))
print("pos_neg(-1, 1, False) → ", pos_neg(-1, 1, False))
print("pos_neg(-4, -5, True) → ", pos_neg(-4, -5, True))
print()

def not_string(str):
    """
    Function to return a string with the 'not' prefix added to the front of it
        Unless the string already starts with the 'not' prefix

    :param str: String to add the 'not' prefix to (Unless already prefixed with 'not')

    :return:    New string prefixed with 'not' unless the given string was already prefixed with 'not'
    """
    return str if (str[0:3] == "not") else ("not " + str)


# Test cases for not_string function
print('not_string')
print("not_string('candy') → ", not_string('candy'))
print("not_string('x') → ", not_string('x'))
print("not_string('not bad') → ", not_string('not bad'))
print()

def missing_char(str, n):
    """
    Function to return a string with the given character removed

    :param str: String to remove the character from
    :param n:   Which character to remove from the string

    :return:    The string with the given character removed
    """
    return (str[1:len(str)]) if (n == 0) else (str[0:n] + str[n + 1:len(str)])


# Test cases for missing_char function
print('missing_char')
print("missing_char('kitten', 1) → ", missing_char('kitten', 1))
print("missing_char('kitten', 0) → ", missing_char('kitten', 0))
print("missing_char('kitten', 4) → ", missing_char('kitten', 4))
print()


def front_back(str):
    """
    Function to return a string with the first and last characters swapped

    :param str: String to swap the first and last characters of

    :return:    New string with the first and last characters swapped
    """
    return str if (len(str) < 2) else str[len(str) - 1] + str[1:len(str) - 1] + str[0]


# Test cases for front_back function
print('front_back')
print("front_back('code') → ", front_back('code'))
print("front_back('a') → ", front_back('a'))
print("front_back('ab') → ", front_back('ab'))
print()


def front3(str):
    """
    Function to return 3 copies of the front 3 characters of a given string
        If the string is less than 3 characters then the string is the "front"

    :param str: String to duplicate the front 3 characters of

    :return:    New string with 3 copies of the first 3 characters of the given string
                    Unless the original string is less than 3 characters, in which it returns 3 copies of the string
    """
    return (str + str + str) if len(str) < 4 else (str[0:3] + str[0:3] + str[0:3])

# Test cases for front3 function
print('front3')
print("front3('Java') → ", front3('Java'))
print("front3('Chocolate') → ", front3('Chocolate'))
print("front3('abc') → ", front3('abc'))
print()
