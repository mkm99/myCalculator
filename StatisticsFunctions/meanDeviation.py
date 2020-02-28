import numpy as np

class MeanDeviation():
    @staticmethod
    def meanDeviation(data):
        return np.mean(np.absolute(data - np.mean(data)))



#mean(absolute(data - mean(data)))