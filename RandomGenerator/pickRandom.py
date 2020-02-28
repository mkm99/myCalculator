# Select a random item from a list
import random


class PickRandomly():
    @staticmethod
    def pick(aList):
        listLen = len(aList)
        position = random.randint(0, listLen-1)
        return aList[position]



#print(PickRandomly.pick([1,22,83,47,65,644,71,18,9]))

