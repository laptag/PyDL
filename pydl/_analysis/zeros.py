""" Find zeros of given data """

def _zeros(data, extrema):
    zeros = [] # return array

    for i in range(1, len(data)):
        if (_isPositive(data[i]) != _isPositive(data[i-1])):
            if (abs(data[i]) < abs(data[i-1])):
                if extrema:
                    zeros.append(_isMinimum(data, i))
                else:
                    zeros.append(i)
            else:
                if extrema:
                    zeros.append(_isMinimum(data, i, extra=-1))
                else:
                    zeros.append(i-1)

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
