import random
from random import seed

# Generate a random number without a seed between a range of two numbers - Both Integer and Decimal

class RandomSeed():
    @staticmethod
    def randomInt(theSeed, num1, num2):
        #seed(theSeed)
        #ranNum = random.randint(num1,num2)
        if isinstance(num1, float):
            return RandomSeed.randomFloat(num1, num2)

        #return ranNum
        return random.randint(num1,num2)

    @staticmethod
    def randomFloat(theSeed, num1, num2):
        #seed(theSeed)
        ranNum = random.uniform(num1, num2)

        return ranNum


'''
    seed(5)
    self.testData = randint(0, 10, 20)
    pprint.pprint(self.testData)
    self.statistics = Statistics()
'''
#print(RandomSeed.randomInt(1, 20))
#print(RandomSeed.randomInt(2.3, 9.9))
