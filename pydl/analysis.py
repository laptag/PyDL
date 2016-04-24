
""" Takes data array and reducer factor (int) """
from ._analysis.reduceResolution import _reduceResolution
def reduceResolution(data, reducer):
    return _reduceResolution(data, reducer)

""" Takes two time series and returns a value for how correlated they are """
from ._analysis.crossCorrelation import _staticCrossCorrelation
def staticCrossCorrelation(data_a, data_b):
    return _staticCrossCorrelation(data_a, data_b)

""" Finds approximate zeros for given data """
from ._analysis.zeros import _zeros
def zeros(data, extrema=False):
    return _zeros(data, extrema)
