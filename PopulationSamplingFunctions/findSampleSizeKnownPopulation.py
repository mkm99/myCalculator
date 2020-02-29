'''
To find the sample size of unknown population, the z-value
is a value that is obtain using the z-score looked in a table
for now the z-score will be use for now
'''

from StatisticsFunctions.z_score import Z_score
from PopulationSamplingFunctions.marginOfError import MarginOfError
from StatisticsFunctions.standardDeviation import StandardDeviation
from Calculator.Exponentiation import exponentiation

class SampleSizeKnown():
    @staticmethod
    def sampleSize(theSeed, data):
        '''
        z = z-score
        e = margin of error
        s = standard deviation
        '''

        z = Z_score.z_score(theSeed, data)
        e = MarginOfError.margin(theSeed, data)
        stdDev = StandardDeviation.standardDeviation(data)
        val = (z * stdDev) / e
        sample = exponentiation(val, 2)

        return sample
