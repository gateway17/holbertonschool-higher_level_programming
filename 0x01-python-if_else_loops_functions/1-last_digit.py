#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    number1 = number % 10
else:
    number1 = number % -10

if number1 > 5:
    txt = "and is greater than 5"
elif number1 < 6 and number1 != 0:
    txt = "and is less than 6 and not 0"
elif number1 == 0:
    txt = "and is 0"
print("Last digit of {:d} is {:d} {:s}".format(number,number1,txt))
