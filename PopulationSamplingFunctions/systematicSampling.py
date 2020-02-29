from RandomGenerator.random_seed import RandomSeed


class SystSampling():
    @staticmethod
    def systSampling(aList):
        listSize = len(aList)
        NthNUM = round((RandomSeed.randomInt(listSize, 2, listSize))/4)

        if NthNUM == 1:
            NthNUM = 3

        newSamplingList = []
        temp = NthNUM - 1

        while temp <= listSize-1:
            value = aList[temp]
            newSamplingList.append(value)
            temp+= NthNUM

        return newSamplingList


