from RandomGenerator.N_numbers_from_list_seed import PickNumbersSeed

class PopulationProportion():
    @staticmethod
    def proportion(theSeed, data, rangeNumber):
        subData = PickNumbersSeed.pickNumbers(theSeed, data, rangeNumber)
        proportion = len(subData)/len(data)
        return proportion

