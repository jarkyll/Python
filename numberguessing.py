#!/usr/bin/env python


import random

found = False


number = random.randint(1,21)

choice = int(input("Guess what the number is? It is between 1 and 21 inclusive: "))

if number == choice:
    found = True
    
else:
    while not found:
        choice = int(input("Guess again: "))
        if choice == number:
            found = True
print("Congrats, you got the number")
