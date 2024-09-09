"""A module that provides statistical functions like average, variance, and standard deviation."""

from math import sqrt


def average(data):
    """Calculate and return the average of a list of numeric values in data.

    :param data: List of numeric values.
    :returns: The average of the values in data.
    :raises ValueError: If the list is empty.
    """
    if len(data) == 0:
        raise ValueError("List must contain at least one value")
    return sum(data) / len(data)


def variance(data):
    """Calculate the population variance of a list of numbers in data.

    The variance is the sum of squared differences between data values
    and their mean, divided by the number of items in the list.
    This is different from the Python library function statistics.variance
    which returns the sample variance, where the sum is divided by (n-1).

    Example: variance([1,5]) is ((1-3)**2 + (5-3)**2)/2 = 4.

    :param data: List of numbers for which variance will be computed.
    :returns: Population variance of values in the data list.
    :raises ValueError: If the list is empty.

    >>> variance([1])
    0.0
    >>> variance([1, 1, 1, 1])
    0.0
    >>> variance([1, 2])
    0.25
    >>> variance([1000000, 1000004])
    4.0
    """
    n = len(data)
    if n == 0:
        raise ValueError("List must contain at least one value")
    avg = average(data)
    return sum((x - avg) ** 2 for x in data) / n


def stdev(data):
    """Calculate the standard deviation of a list of values.

    :param data: List of numbers for which standard deviation will be computed.
    :returns: Standard deviation of values in the data list.
    :raises ValueError: If the list is empty.
    """
    return sqrt(variance(data))
