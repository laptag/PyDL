import numpy as np
""" Takes data array and reducer factor (int)"""

def _reduceResolution(data, reducer):
    if (reducer > len(data)):
        print("Reduce factor greater than the length of the array!")
        return

    red_data = []
    for i in range(0, len(data), reducer):
        try:
            red_data.append(data[i])
        except:
            break

    return np.array(red_data)
