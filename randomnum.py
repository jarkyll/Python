#!/usr/bin/env python
#guess the number game
import random

answer = random.randint(1, 10)
num = 0

while num != answer:
    num = int(input('What number am I thinking of? '))

    if num != answer:
        print ('Wrong!')

print ('Correct!')
