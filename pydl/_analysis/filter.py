""" File is for various filtering functions """

# imports
from scipy import signal
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import numpy as np

# Uses fft and gaussian functions to filter low frequency noise out
def _lowFreqFilter(data, sigma, test_filter):
    size = len(data)
    gauss = signal.gaussian(size, std=sigma) # gen gaussian function

    # generate filter
    filt = np.zeros_like(data)
    filt[:int(size/2)] = gauss[int(size/2):]
    filt[int(size/2):] = gauss[:int(size/2)]

    # test filter
    if (test_filter):
        plt.plot(abs(fft(data)), 'y')
        plt.plot(filt*1000, 'r')
        plt.show()

    # return filtered data
    return ifft(filt * fft(data))
