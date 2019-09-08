def exchangeFirstLast(seq):
    """
    Function to exchange the first and last elements of a sequence

    Positional Parameters
    :param seq: Sequence to exchange the first and last elements of

    :return:    Sequence with the first and last elements exchanged
    """
    return seq[-1:] + seq[1:-1] + seq[:1]


# Test cases for exchangeFirstLast function
print('exchangeFirstLast')
print("exchangeFirstLast('this is a string') → ", exchangeFirstLast("this is a string"))
print("exchangeFirstLast((2, 54, 13, 12, 5, 32)) → ", exchangeFirstLast((2, 54, 13, 12, 5, 32)))
print()


def everyOtherItem(seq):
    """
    Function to return every other item from a given sequence

    Positional Parameters
    :param seq: Sequence to get every other item from

    :return:    Sequence with every other item removed
    """
    return seq[::2]


# Test cases for everyOtherItem function
print('everyOtherItem')
print("everyOtherItem('this is a string') → ", everyOtherItem("this is a string"))
print("everyOtherItem((2, 54, 13, 12, 5, 32)) → ", everyOtherItem((2, 54, 13, 12, 5, 32)))
print()


def removeFirstLastFour(seq):
    """
    Function to return a sequence by removing the first and last 4 elements and then return every other item

    Positional Parameters
    :param seq: Sequence to remove first and last four elements and then return every other item

    :return:    Sequence with first and last four elements removed and then every other item
    """
    return seq[4:-4:2]


# Test cases for removeFirstLastFour function
print('removeFirstLastFour')
print("removeFirstLastFour('this is a longer string') → ", removeFirstLastFour("this is a longer string"))
print("removeFirstLastFour((2, 54, 13, 12, 5, 32, 11, 15, 17, 19)) → ", removeFirstLastFour((2, 54, 13, 12, 5, 32, 11, 15, 17, 19)))
print()


def reverse(seq):
    """
    Function to reverse a sequence

    Positional Parameters
    :param seq: Sequence to reverse

    :return:    Sequence with the elements reversed
    """
    return seq[::-1]


# Test cases for reverse function
print('reverse')
print("reverse('this is a string') → ", reverse("this is a string"))
print("reverse((2, 54, 13, 12, 5, 32)) → ", reverse((2, 54, 13, 12, 5, 32)))
print()


def thirds(seq):
    """
    Function to exchange thirds of a sequence

    Positional Parameters
    :param seq: Sequence to exchange thirds of

    :return:    Sequence with the first third, followed by the last third, followed by the middle third
    """
    third = len(seq) // 3
    return seq[-third:] + seq[:third] + seq[third:-third]


# Test cases for thirds function
print('thirds')
print("thirds('this is a string') → ", thirds("this is a string"))
print("thirds((2, 54, 13, 12, 5, 32)) → ", thirds((2, 54, 13, 12, 5, 32)))
print()


