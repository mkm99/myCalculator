# Select N number of items from a list without a seed
import random

class PickNumbersNoSeed():
    @staticmethod
    def pickNumbers(aList, rangeNum):
        newList =[]
        listSize = len(aList)

        for each in range(rangeNum):
            position = random.randint(0, listSize-1)
            newList.append(aList[position])

        return newList
