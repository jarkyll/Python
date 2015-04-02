#! /usr/bin/env python
#years again
import sys
if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Please put your name: ")



if len(sys.argv) > 2:
    age = int( sys.argv[2] )
else:
    age = int( input("Please put your age: ") )



hello = "Hello " + name + ","

if age == 100:
    agestring = "You are already 100."
elif age < 100:
    agestring = "You will be 100 in " + str(100-age) + " years."
else:
    agestring = "You were 100 years old " + str(age-100) + " years ago."

print (hello, agestring) 
