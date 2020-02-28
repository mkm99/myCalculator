from scipy.stats import skew

class Skewness():
    @staticmethod
    def skewness(data):
        return skew(data)