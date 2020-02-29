import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from StatisticsFunctions.mean import Mean
from StatisticsFunctions.median import Median
from StatisticsFunctions.meanDeviation import MeanDeviation
from StatisticsFunctions.mode import Mode
#from StatisticsFunctions.populationCorrelation import PopulationCorrelation
from StatisticsFunctions.quartiles import Quartile
#from StatisticsFunctions.sampleCorrelation import SampleCorrelation
from StatisticsFunctions.skewness import Skewness
from StatisticsFunctions.standardDeviation import StandardDeviation
from StatisticsFunctions.variance import Variance
from StatisticsFunctions.z_score import Z_score




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 50, 15)
        #pprint(self.testData)

    def test_mean(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 25.466666666666665)

    def test_median(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 27.0)

    def test_standardDeviation(self):
        standardDeviation = StandardDeviation.standardDeviation(self.testData)
        self.assertEqual(standardDeviation, 14.01364414498321)

    def test_variance(self):
        variance = Variance.variance(self.testData)
        self.assertEqual(variance, 196.3822222222222)

    def test_mode(self):
        mode = Mode.mode(self.testData)
        self.assertEqual(mode, 16)

    def test_meanDeviation(self):
        meanDeviation = MeanDeviation.meanDeviation(self.testData)
        self.assertEqual(meanDeviation, 12.835555555555555)

    def test_quartiles(self):
        quartiles = Quartile.quartile(self.testData)
        self.assertEqual(quartiles, (13.0, 27.0, 37.0))

    def test_skewness(self):
        skewness = Skewness.skewness(self.testData)
        self.assertEqual(skewness, 0.15182604770872699)

    def test_z_score(self):
        z_score = Z_score.z_score(self.testData)
        self._getAssertEqualityFunc(z_score, [ 0.68028938, -0.81825017,  1.5365977 ,  0.89436646, -0.67553211,
       -1.1750453 , -1.24640432,  0.75164841,  0.96572549,  0.10941717,
        1.60795672,  0.32349425, -0.67553211, -1.31776335, -0.96096822])



if __name__ == '__main__':
    unittest.main()


