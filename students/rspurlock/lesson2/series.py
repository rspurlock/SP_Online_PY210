def fibonacci(n):
    """
    Function to compute the Nth fibonacci series value

    Positional Parameters
    :param n:   Desired fibonacci series value (which Nth value)

    :return:    Requested Nth fibonacci value
    """
    if (n > 1):
        return fibonacci(n - 2) + fibonacci(n - 1)
    elif (n == 1):
        return 1
    else:
        return 0


# Test cases for fibonacci function
print("fibonacci(0) → ", fibonacci(0))
print("fibonacci(1) → ", fibonacci(1))
print("fibonacci(7) → ", fibonacci(7))
print()


def lucas(n):
    """
    Function to compute the Nth lucas series value

    Positional Parameters
    :param n:   Desired lucas series value (which Nth value)

    :return:    Requested Nth lucas value
    """
    if (n > 1):
        return lucas(n - 2) + lucas(n - 1)
    elif (n == 1):
        return 1
    else:
        return 2


# Test cases for lucas function
print("lucas(0) → ", lucas(0))
print("lucas(1) → ", lucas(1))
print("lucas(7) → ", lucas(7))
print()


# Print fibonacci series
print('Fibonacci series:', end=' ')
for i in range(9):
    print(fibonacci(i), end=', ')
print(fibonacci(9))


# Print lucas series
print('Lucas series:', end=' ')
for i in range(9):
    print(lucas(i), end=', ')
print(lucas(9))
print()


def sumSeries(n, first = 0, second = 1):
    """
    Function to compute the Nth general series value

    Positional Parameters
    :param n:       Desired series value (which Nth value)
    :param first:   Series first starting value (Defaults to 0 for fibonacci series)
    :param second:  Series second starting value (Defaults to 1 for fibonacci series)

    :return:    Requested Nth series value
    """
    if (n > 1):
        return sumSeries((n - 2), first, second) + sumSeries((n - 1), first, second)
    elif (n == 1):
        return second
    else:
        return first


# Test cases for sumSeries function
print("sumSeries(0) → ", sumSeries(0), " fibonacci(0) → ", fibonacci(0))
print("sumSeries(1) → ", sumSeries(1), " fibonacci(1) → ", fibonacci(1))
print("sumSeries(7) → ", sumSeries(7), " fibonacci(7) → ", fibonacci(7))
print("sumSeries(0, 0, 1) → ", sumSeries(0, 0, 1), " fibonacci(0) → ", fibonacci(0))
print("sumSeries(1, 0, 1) → ", sumSeries(1, 0, 1), " fibonacci(1) → ", fibonacci(1))
print("sumSeries(7, 0, 1) → ", sumSeries(7, 0, 1), " fibonacci(7) → ", fibonacci(7))
print("sumSeries(0, 2, 1) → ", sumSeries(0, 2, 1), " lucas(0) → ", lucas(0))
print("sumSeries(1, 2, 1) → ", sumSeries(1, 2, 1), " lucas(1) → ", lucas(1))
print("sumSeries(7, 2, 1) → ", sumSeries(7, 2, 1), " lucas(7) → ", lucas(7))
print()
