import numpy as np


class Covariance():
    @staticmethod
    def covariance(dataA, dataB):
        return np.cov(dataA, dataB)