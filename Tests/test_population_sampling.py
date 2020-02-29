import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from PopulationSamplingFunctions.simpleRandomSampling import SimpleRandomSampling
from RandomGenerator.random_list import RandomList


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(3)
        self.testData = randint(0, 50, 15)
        #pprint(self.testData)


    def test_generate_sample(self):
        sample = SimpleRandomSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(sample, [8, 41, 43, 3, 21])



if __name__ == '__main__':
    unittest.main()
