def division(dividend, divisor):
    try:
        return float(dividend) / float(divisor)
    except ZeroDivisionError:
        return "Trying to divide by zero"