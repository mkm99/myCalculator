import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from StatisticsFunctions.mean import Mean



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 50, 20)
        pprint(self.testData)

    def test_mean(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 26.4)


if __name__ == '__main__':
    unittest.main()


