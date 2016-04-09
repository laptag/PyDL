import numpy as np

def Step(data, width):
    # check variable types
    # if (type(data) is not np.ndarray) or (type(width) is not int):
    #     print("Error")
    #     return

    # create output array
    output = np.zeros_like(data)

    # loop through data
    for i in range(len(data)):
        if (i+width > len(data)-1):
            width -= (i+width - len(data)-1)
        bucket = data[i:i+width]
        output[i] = np.average(bucket)


    print(bucket)
# 1, 2, 3 4 5 6 7 8 9
# (1+2+3)/3, (2+3+4)/3,

    print("test")
