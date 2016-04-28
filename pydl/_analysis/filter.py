""" File is for various filtering functions """

# imports
from scipy import signal
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
import sys

# Uses fft and gaussian functions to filter low frequency noise out
def _lowFreqFilter(data, sigma, test_filter):
    size = len(data)
    if size % 2 != 0: # if size is odd, subtract one
        data = np.delete(data, -1)
        size -= 1

    gauss = signal.gaussian(size, std=sigma) # gen gaussian function

    # generate filter
    filt = np.zeros_like(data)
    filt[:int(size/2)] = gauss[int(size/2):]
    filt[int(size/2):] = gauss[:int(size/2)]

    # test filter
    if (test_filter):
        print("Testing filter with size: {} and sigma: {}".format(size, sigma))
        plt.plot(abs(fft(data)), 'y')
        plt.plot(filt*1000, 'r')
        plt.show()
        print("Exiting program")
        sys.exit(0)

    # return filtered data
    return np.real(ifft(filt * fft(data)))
