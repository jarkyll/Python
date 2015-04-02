#!/usr/bin/envpython

import sys

def factorial(n):
    if n > 1:
        return n *factorial(n-1)
    else:
        return 1

num = int(input("Enter a number: "))
print( str(num),"! =",factorial(num))
