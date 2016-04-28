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

# threshold = (a, b) => everything above a and below b
def _extrema(data, threshold):
    diffdata = np.diff(data)
    zeros = _zeros(diffdata)
    i = 0
    for x in zeros:
        if not _isPositive(diffdata[x-1]): # if previous value is negative, then rel min
            zeros[i] = -x

        if threshold != None and type(threshold) == tuple: # a threshold is provided and is tuple
            valid = False
            if threshold[0] != None: # upper limit
                if data[x] > threshold[0]: valid = True

            if threshold[1] != None: # lower limit
                if data[x] < threshold[1]: valid = True

            if not valid:
                zeros[i] = None

        i += 1

    return list(filter(lambda x: x is not None, zeros))


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
