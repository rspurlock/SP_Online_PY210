#!/usr/bin/env python3

# Task 1
print('Task 1')

data = ( 2, 123.4567, 10000, 12345.67)
print('file_{:03} : {:5.2f}, {:.2e}, {:.2e}'.format(data[0], data[1], data[2], data[3]))
print()

# Task 2
print('Task 2')

data = ( 2, 123.4567, 10000, 12345.67)
print('file_{d[0]:03} : {d[1]:5.2f}, {d[2]:.2e}, {d[3]:.2e}'.format(d=data))
print(f'file_{data[0]:03} : {data[1]:5.2f}, {data[2]:.2e}, {data[3]:.2e}')
print()

# Task 3
print('Task 3')

def formatter(tupleData):
    """
    Function to return a format string for outputting all the members of a given tuple

    Positional Parameters
    :param tupleData:   Tuple data to return the format string to print all the tuple members

    :return:            Format string to display all the given tuple members
    """
    formatString = 'the ' + str(len(tupleData)) + ' numbers are ' + ', '.join(tuple(('{:d} ' * len(tupleData)).split()))
    return formatString.format(*tupleData)


# Test cases for formatter function
print('formatter')
print(formatter((2, 3, 5)))
print(formatter((2, 3, 5, 7, 9)))
print()

# Task 4
print('Task 4')

data = ( 4, 30, 2017, 2, 27)
print('{d[3]:02d} {d[4]:02d} {d[2]:04d} {d[0]:02d} {d[1]:02d}'.format(d=data))
print(f'{data[3]:02d} {data[4]:02d} {data[2]:04d} {data[0]:02d} {data[1]:02d}')
print()

# Task 5
print('Task 5')

data = ['oranges', 1.3, 'lemons', 1.1]
print(f'The weight of an {data[0][:-1]} is {data[1]} and the weight of a {data[2][:-1]} is {data[3]}')
print(f'The weight of an {data[0].upper()[:-1]} is {data[1]*1.2} and the weight of a {data[2].upper()[:-1]} is {data[3]*1.2}')
print()

# Task 6
print('Task 6')

data1 = ['Apples', 3, 1.59]
data2 = ['Oranges', 5, 1.79]
data3 = ['Computers', 10, 799.99]
data4 = ['Cars', 30, 45237.59]
data5 = ['Houses', 180, 249954.33]
data = [data1, data2, data3, data4, data5]
for entry in data:
    print(f'{entry[0]:15}{entry[1]:5d}'+"{:>15}".format(f'${entry[2]:,.2f}'))

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(('{:5d}' * len(data)).format(*data))
