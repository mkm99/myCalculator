from StatisticsFunctions.covariance import Covariance
from StatisticsFunctions.standardDeviation import StandardDeviation


class PopCorrelation():
    @staticmethod
    def correlation(dataA, dataB):
        cov = Covariance.covariance(dataA, dataB)
        stdDevA = StandardDeviation.standardDeviation(dataA)
        stdDevB = StandardDeviation.standardDeviation(dataB)
        return cov/(stdDevA*stdDevB)
