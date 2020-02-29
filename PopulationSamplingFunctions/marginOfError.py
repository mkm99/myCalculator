from StatisticsFunctions.standardDeviation import StandardDeviation
from StatisticsFunctions.z_score import Z_score


class MarginOfError():
    @staticmethod
    def margin(theSeed, data):
        z_score = Z_score.z_score(theSeed, data)
        stdDev = StandardDeviation.standardDeviation(data)
        return z_score * stdDev
