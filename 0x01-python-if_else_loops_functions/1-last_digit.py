#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

if number > 0 :
    last_d = number % 10
else:
    last_d = number % -10

print("Last digit of  {}  is {} ".format(number,last_d),end='')

if last_d > 5 :
    print("and is greater than 5")
elif last_d == 0 :
    print ("and is 0")
elif last_d < 6 and last_d != 0 :
    print ("and is less than 6 and not 0")
