# Set a seed and randomly.select the same value from a list

class PickSeed():
    @staticmethod
    def pickSeed(theSeed, aList):
        listLen = len(aList)
        position = random.randint(0, listLen - 1)
        return aList[position]