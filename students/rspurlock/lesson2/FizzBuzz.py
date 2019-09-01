def fizzBuzz():
    """
    Function to print the numbers from 1 to 100 inclusive

        Except if the number is a multiple of 3 print Fizz instead
        Except if the number is a multiple of 5 print Buzz instead
        Except if the number is a multiple of both 3 & 5 print FizzBuzz instead
    """
    for x in range(1, 101):
        if ((x % (3 * 5)) == 0):
            print('FizzBuzz')
        elif ((x % 5) == 0):
            print('Buzz')
        elif ((x % 3) == 0):
            print('Fizz')
        else:
            print(x)


# Test case for fizzBuzz function
fizzBuzz()
