import numpy as np

class Quantile():
    @staticmethod
    def quantile(data):
        q1 = np.quantile(data, .25)
        q2 = np.quantile(data, .50)
        q3 = np.quantile(data, .75)
        return q1, q2, q3
