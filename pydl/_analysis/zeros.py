""" Find zeros of given data """

# imports
import numpy as np

def _zeros(data):
    zeros = [] # return array

    for i in range(1, len(data)):
        if (_isPositive(data[i]) != _isPositive(data[i-1])):
            if (abs(data[i]) < abs(data[i-1])):
                zeros.append(i)
            else:
                zeros.append(i-1)

    return zeros

def _extrema(data):
    data = np.diff(data)
    zeros = _zeros(data)
    i = 0
    for x in zeros:
        if not _isPositive(data[x-1]): # if previous value is negative, then rel min
            zeros[i] = -x

        i += 1

    return zeros


# private
def _isPositive(val):
    if (val > 0): # if positive
        return True # return True
    return False # else return False

# private
def _isMinimum(data, index, extra=0):
    if not _isPositive(data[index-1]): # if previous is negative
        return -(index - extra)

    return index - extra
