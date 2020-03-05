import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from PopulationSamplingFunctions.simpleRandomSampling import SimpleRandomSampling
from PopulationSamplingFunctions.systematicSampling import SystSampling
from PopulationSamplingFunctions.confidenceIntervalForPopulation import ConfIntervalPopulation
from PopulationSamplingFunctions.confidenceIntervalForSample import ConfIntervalSample
from PopulationSamplingFunctions.marginOfError import MarginOfError
from PopulationSamplingFunctions.cochransSampleSize import Cochran
from PopulationSamplingFunctions.findSampleSizeUnknonwPopulation import SampleSizeUnkPopul
from PopulationSamplingFunctions.findSampleSizeKnownPopulation import SampleSizeKnown


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(3)
        self.testData = randint(0, 50, 15)

    def test_generate_sample(self):
        sample = SimpleRandomSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(sample, [8, 41, 43, 3, 21])

    def test_systematic_sampling(self):
        result = SystSampling.systSampling(self.testData)
        self.assertEqual(result, [3, 21, 43, 21, 20])

    def test_Confidence_Interval_Popul(self):
        result = ConfIntervalPopulation.confidenceInterval(0.90, self.testData)
        self.assertEqual(result, (15.581632402905116, 28.68503426376155))

    def test_Confidence_Interval_Sample(self):
        result = ConfIntervalSample.confidenceInterval(0.90, self.testData, 3, 5)
        self.assertEqual(result, (5.6669372302865675, 40.73306276971343))

    def test_Margin_Error(self):
        result = MarginOfError.margin(3, self.testData)
        self.assertEqual(result, -14.133333333333335)

    def test_Cochran(self):
        result = Cochran.cochran(3, self.testData, 4)
        self.assertEqual(result, 0.0010094984628091588)

    def test_sample_size_unkown(self):
        result = SampleSizeUnkPopul.sampleSize(3 , self.testData, 0.41)
        self.assertEqual(result, 0.0012487381269214882)

    def test_sample_size_known(self):
        result = SampleSizeKnown.sampleSize(3, self.testData)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()