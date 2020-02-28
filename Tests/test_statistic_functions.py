import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from StatisticsFunctions.mean import Mean
from StatisticsFunctions.median import Median
#from StatisticsFunctions.meanDeviation import MeanDeviation
#from StatisticsFunctions.mode import Mode
#from StatisticsFunctions.populationCorrelation import PopulationCorrelation
#from StatisticsFunctions.quartiles import Quartiles
#from StatisticsFunctions.sampleCorrelation import SampleCorrelation
#from StatisticsFunctions.skewness import Skewness
from StatisticsFunctions.standardDeviation import StandardDeviation
#from StatisticsFunctions.variance import Variance
#from StatisticsFunctions.z_score import Z_score




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 50, 20)
        #pprint(self.testData)

    def test_mean(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 26.4)

    def test_median(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 27.0)

    def test_standardDeviation(self):
        standardDeviation = StandardDeviation.standardDeviation(self.testData)
        self.assertEqual(standardDeviation, 13.904675472660266)


if __name__ == '__main__':
    unittest.main()


