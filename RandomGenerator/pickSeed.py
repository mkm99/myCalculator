# Set a seed and randomly.select the same value from a list
import random
from RandomGenerator.pickRandom import PickRandomly

class PickSeed():
    @staticmethod
    def pickSeed(theSeed, aList):
        random.seed(theSeed)

        return PickRandomly.pick(aList)

