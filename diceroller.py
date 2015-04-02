#!/usr/bin/env python

#dice roller

import random
import sys

while 1:
    choice = input("Do you want the dice to roll a number? Enter y for yes or n for no: ")

    if choice == "n":
        sys.exit()

    else:
        number = random.randint(1,6)
        print(number)
        
