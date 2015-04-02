#! /usr/bin/env python

#Years till 100 again using optparse

import sys
import optparse


parser = optparse.OptionParser()
parser.add_option("-n", "--name", dest="name", help="Your Name")
parser.add_option("-a", "--age", dest="age", help="Your Age", type = int)

(options, args) = parser.parse_args()

if options.name is None:
    options.name = input("Your name please: ")

if options.age is None:
    options.age = int(input("Your age please: "))

hello = "Hello, " + options.name

if options.age == 100:
    sayAge = 'You are already 100 years old!'
elif options.age < 100:
    sayAge = 'You will be 100 in ' + str(100 - options.age) + ' years!'
else:
    sayAge = 'You turned 100 ' + str(options.age - 100) + ' years ago!'

print (hello, sayAge)
