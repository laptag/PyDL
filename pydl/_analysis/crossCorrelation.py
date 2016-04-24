""" Docstring """

def _staticCrossCorrelation(data_a, data_b):
    # check conditions
    if (len(data_a) != len(data_b)):
        print("Both input arrays need to have the same length!")
        return

    return sum(data_a * data_b)/sum(data_a * data_a)
