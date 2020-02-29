from RandomGenerator.pickSeed import PickSeed
from StatisticsFunctions.standardDeviation import StandardDeviation
from StatisticsFunctions.mean import Mean

class Z_score():
    @staticmethod
    def z_score(theSeed, data):
        X = PickSeed.pickSeed(theSeed, data)
        mean = Mean.mean(data)
        stdDev = StandardDeviation.standardDeviation(data)
        return (X-mean)/stdDev
