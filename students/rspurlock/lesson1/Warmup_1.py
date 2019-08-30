# Function to return True to sleep in if not a weekday or we're on vacation
def sleep_in(weekday, vacation):
    return (not(weekday) or vacation)


# Test cases for sleep_in function
print('sleep_in')
print("sleep_in(False, False) → ", sleep_in(False, False))
print("sleep_in(True, False) → ", sleep_in(True, False))
print("sleep_in(False, True) → ", sleep_in(False, True))
print()


# Function to return True if either both monkeys are smiling or neither monkey is smiling
#   In either case we are in monkey trouble
def monkey_trouble(a_smile, b_smile):
    return (a_smile == b_smile)


# Test cases for monkey_trouble function
print('monkey_trouble')
print("monkey_trouble(True, True) → ", monkey_trouble(True, True))
print("monkey_trouble(False, False) → ", monkey_trouble(False, False))
print("monkey_trouble(True, False) → ", monkey_trouble(True, False))
print()


# Function to return the sum of two values
#   Unless the values are the same and in that case return double the sum
def sum_double(a, b):
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


# Function to return the absolute difference between the value and 21
#   Unless the absolute difference is greater than 21, in that case return double the absolute difference
def diff21(n):
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


# Function to return True if the parrot is talking outside the hours of 7 - 20
#   In which case our parrot is just causing trouble
def parrot_trouble(talking, hour):
    return (talking and ((hour < 7) or (hour > 20)))


# Test cases for parrot_trouble function
print('parrot_trouble')
print("parrot_trouble(True, 6) → ", parrot_trouble(True, 6))
print("parrot_trouble(True, 7) → ", parrot_trouble(True, 7))
print("parrot_trouble(False, 6) → ", parrot_trouble(False, 6))
print()


# Function to return True if either value is 10 or the sum of the values is 10
def makes10(a, b):
    return ((a == 10) or (b == 10) or ((a + b) == 10))


# Test cases for makes10 function
print('makes10')
print("makes10(9, 10) → ", makes10(9, 10))
print("makes10(9, 9) → ", makes10(9, 9))
print("makes10(1, 9) → ", makes10(1, 9))
print()


# Function to return True if the given value is within 10 of either 100 or 200
def near_hundred(n):
    return ((abs(n - 100) <= 10) or (abs(n - 200) <= 10))


# Test cases for near_hundred function
print('near_hundred')
print("near_hundred(93) → ", near_hundred(93))
print("near_hundred(90) → ", near_hundred(90))
print("near_hundred(89) → ", near_hundred(89))
print()


# Function to return True if one value is negative and the other value is positive
#   Unless the negative parameter is True and then only returns True if both values negative
def pos_neg(a, b, negative):
    return ((a < 0) and (b < 0)) if negative else ((a < 0) and (b > 0)) or ((a > 0) and (b < 0))


# Test cases for pos_neg function
print('pos_neg')
print("pos_neg(1, -1, False) → ", pos_neg(1, -1, False))
print("pos_neg(-1, 1, False) → ", pos_neg(-1, 1, False))
print("pos_neg(-4, -5, True) → ", pos_neg(-4, -5, True))
print()

# Function to return a string with 'not' added to the front
#   Unless the string already starts with 'not'
def not_string(str):
    return str if (str[0:3] == "not") else ("not " + str)


# Test cases for not_string function
print('not_string')
print("not_string('candy') → ", not_string('candy'))
print("not_string('x') → ", not_string('x'))
print("not_string('not bad') → ", not_string('not bad'))
print()

# Function to return a string with the given character removed
def missing_char(str, n):
    return (str[1:len(str)]) if (n == 0) else (str[0:n] + str[n + 1:len(str)])


# Test cases for missing_char function
print('missing_char')
print("missing_char('kitten', 1) → ", missing_char('kitten', 1))
print("missing_char('kitten', 0) → ", missing_char('kitten', 0))
print("missing_char('kitten', 4) → ", missing_char('kitten', 4))
print()


# Function to return a string with the first and last characters swapped
def front_back(str):
    return str if (len(str) < 2) else str[len(str) - 1] + str[1:len(str) - 1] + str[0]


# Test cases for front_back function
print('front_back')
print("front_back('code') → ", front_back('code'))
print("front_back('a') → ", front_back('a'))
print("front_back('ab') → ", front_back('ab'))
print()


# Function to return 3 copies of the front 3 characters of a given string
#   If the string is less than 3 characters then the string is the front
def front3(str):
    return (str + str + str) if len(str) < 4 else (str[0:3] + str[0:3] + str[0:3])

# Test cases for front3 function
print('front3')
print("front3('Java') → ", front3('Java'))
print("front3('Chocolate') → ", front3('Chocolate'))
print("front3('abc') → ", front3('abc'))
print()
