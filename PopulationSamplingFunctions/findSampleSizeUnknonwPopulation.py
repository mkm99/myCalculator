'''
To find the sample size of unknown population, the z-value
is a value that is obtain using the z-score looked in a table
for now the z-score will be use for now
'''


from StatisticsFunctions.z_score import Z_score
from PopulationSamplingFunctions.marginOfError import MarginOfError
from Calculator.Exponentiation import exponentiation

class SampleSizeUnkPopul():
    @staticmethod
    def sampleSize(theSeed, data, percentage):
        '''
        z = z-score
        e = margin of error
        p = percentage
        q = 1 -p
        '''

        z = Z_score.z_score(theSeed, data)
        e = MarginOfError.margin(theSeed, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = exponentiation(val, 2) * p * q

        return sample