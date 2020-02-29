'''
Conchran Sample size utilizes z-value, which is obtained from looking at a table using the z-score
 for calculation purposes I used z-score just to get the formula done
 until I find out how to obtain the z-value
'''


from StatisticsFunctions.z_score import Z_score
from PopulationSamplingFunctions.marginOfError import MarginOfError
from StatisticsFunctions.populationProportion import PopulationProportion
from Calculator.Exponentiation import exponentiation
from Calculator.Division import division

class Cochran():
    @staticmethod
    def cochran(theSeed, data, rangeNumber):
        # z = z-score
        # p = proportion population
        # e = margin of error

        z = Z_score.z_score(theSeed, data)
        p = PopulationProportion.proportion(theSeed, data, rangeNumber)
        e = MarginOfError.margin(theSeed, data)
        q = 1 - p

        cochran = (exponentiation(z,2) * p * q)/exponentiation(e,2)

        return cochran

