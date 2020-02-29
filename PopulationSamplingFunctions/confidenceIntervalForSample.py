from scipy.stats import sem, t

from PopulationSamplingFunctions.confidenceIntervalForPopulation import ConfIntervalPopulation
from PopulationSamplingFunctions.simpleRandomSampling import SimpleRandomSampling


class ConfIntervalSample(ConfIntervalPopulation):
    @staticmethod
    def confidenceInterval(confidence, data, theSeed, higher):
        newSample = SimpleRandomSampling.generateSampling(theSeed, data, higher)
        return ConfIntervalPopulation.confidenceInterval(confidence, newSample)