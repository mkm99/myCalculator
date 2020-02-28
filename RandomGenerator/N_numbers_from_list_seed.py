# Select N number of items from a list with a seed

import random
from RandomGenerator.N_numbers_from_list import PickNumbersNoSeed

class PickNumbersSeed():
    @staticmethod
    def pickNumbers(theSeed, aList, rangeNum):
        random.seed(theSeed)

        newList = PickNumbersNoSeed.pickNumbers(aList, rangeNum)
        return newList

#print(Pick_with_seed.pickNumbers(3, [34,45,67,89,123,44], 4))