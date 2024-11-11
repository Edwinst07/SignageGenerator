import numpy as np
import math
class Series:
    def __init__(self, file):
        self._file = file
        self.rFile = open(self._file, 'r') 
        self.series = np.array(self.rFile.read().split('\n'))
        self.cantPages = math.ceil(self.series.size/2)
        self.series1 = []
        self.series2 = []
    
    def arraySeries1(self):
        for serie in self.series:
            if (self.series.tolist().index(serie)+1) % 2 == 1:
                self.series2.append(str(serie))
        return self.series2

    def arraySeries2(self):
        for serie in self.series:
            if (self.series.tolist().index(serie)+1) % 2 == 0:
                self.series1.append(str(serie))
        return self.series1
    