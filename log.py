#!/usr/bin/env python

import sys




if len(sys.argv) < 2:
    logLevel = int(input("Loglevel please: "))


else:
    logLevel = int( sys.argv[1] )
                   
def logit(level, message):
    if level >= logLevel:
        print(" Msg " , str(level) , ":", message)

def getUser():
    logit(2, "Entering Function getUser()")
    user = input("Enter name: ")
    logit(1, "Leaving Function getUser()")
    return user

logit(3, 'Starting Script...')
logit(3, 'User Entered: ' + getUser())
logit(3, 'Ending Script.')
