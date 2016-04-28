
""" Takes data array and reducer factor (int) """
from ._analysis.reduceResolution import _reduceResolution
def reduceResolution(data, reducer):
    return _reduceResolution(data, reducer)

""" Takes two time series and returns a value for how correlated they are """
from ._analysis.correlation import _staticCorrelation
def staticCorrelation(data_a, data_b):
    return _staticCorrelation(data_a, data_b)

""" Finds approximate zeros for given data """
from ._analysis.zeros import _zeros
def zeros(data):
    return _zeros(data)

""" Finds relative extrema from given data. Returns array of extrem. Rel mins are negative. """
from ._analysis.zeros import _extrema
def extrema(data, threshold=None):
    return _extrema(data, threshold)

""" Uses fft and gaussian functions to filter low frequency noise out """
from ._analysis.filter import _lowFreqFilter
def lowFreqFilter(data, sigma=40, test_filter=False):
    return _lowFreqFilter(data, sigma, test_filter)
