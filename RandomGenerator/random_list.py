# Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
from numpy.random import seed
import random


class RandomList():
    @staticmethod
    def list_Of_Ints(num1, num2, length, theSeed):
        if isinstance(num1, float):
            return list_Of_Floats(num1, num2, length, theSeed)

        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.randint(num1, num2)
            aList.append(number)

        return aList

    @staticmethod
    def list_Of_Floats(num1, num2, length, theSeed):
        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.uniform(num1, num2)
            aList.append(number)

        return aList

#print(RandomList.list_Of_Floats(20,9,2.1,36.50))