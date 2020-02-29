import numpy as np


class Quartile():
    @staticmethod
    def quartile(data):
        q1 = np.quantile(data, .25)
        q2 = np.quantile(data, .50)
        q3 = np.quantile(data, .75)
        return q1, q2, q3
