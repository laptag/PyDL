""" Docstring """

import sys

def _staticCorrelation(data_a, data_b):
    # check conditions
    if (len(data_a) != len(data_b)):
        print("Static Correlation: '{} != {}' Both arrays need to be the same size!".format(len(data_a), len(data_b)))
        sys.exit(1)
        return

    tot = 0
    for i in range(len(data_a)):
        val = abs(data_a[i] - data_b[i])
        tot += val

    # return sum(data_a * data_b)/sum(data_a * data_a)
    return tot/len(data_a)
