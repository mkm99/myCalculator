from RandomGenerator.N_numbers_from_list_seed import PickNumbersSeed

from numpy.random import seed


class SimpleRandomSampling(PickNumbersSeed):
    @staticmethod
    def generateSampling(theSeed, aList, rangeNum):
        seed(theSeed)
        return PickNumbersSeed.pickNumbers(theSeed, aList, rangeNum)

