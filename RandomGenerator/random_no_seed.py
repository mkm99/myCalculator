import random


# Generate a random number without a seed between a range of two numbers - Both Integer and Decimal

class RandomNoSeed():
    @staticmethod
    def randomInt(num1, num2):
        if isinstance(num1, float):
            return RandomNoSeed.randomFloat(num1, num2)
        return random.randint(num1, num2)

    @staticmethod
    def randomFloat(num1, num2):
        return random.uniform(num1, num2)
        # return round(random.uniform(num1, num2), 5)

# print("This is random_no_seed")
# print(RandomNoSeed.randomInt(3.2,5.4))
