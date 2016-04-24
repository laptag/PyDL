# Data Object
from enum import Enum
import numpy as np
import csv

class FileType(Enum):
    csv = 'csv'
    hdf5 = 'hdf5'

class Data(object):
    def __init__(self, filename, filetype=None):
        self.filename = filename
        self.filetype = filetype

        self.data = []
        self.time = []

        self.header = []
        self.variable_names = []

        self._read_data()

    def _read_data(self):
        if self.filetype == FileType.csv:
            print("Reading CSV File: {}".format(self.filename))
            self._get_info_csv()
            self._get_data_csv()
        elif self.filetype == FileType.hdf5:
            print('not yet implemented')
        else:
            print("got some work to do")

    def _get_data_csv(self):
        csvfile = open(self.filename)
        data = []
        time = []
        reader = csv.reader(csvfile)
        for line in reader:
            if len(line) != 0:
                if isfloat(line[0]):
                    if "Time" in self.variable_names:
                        time.append(line[0])
                        data.append(line[1])
                    else:
                        data.append(line)

        csvfile.close()
        self.data = np.array(data, dtype=float)
        self.time = np.array(time, dtype=float)

    def _get_info_csv(self):
        csvfile = open(self.filename)
        reader = csv.reader(csvfile)
        header = []

        while True:
            line = reader.__next__()
            if len(line) != 0:
                if not isfloat(line[0]):
                    self.header.append(line)
                else:
                    break

        csvfile.close()
        self.variable_names = self.header[-1]

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
