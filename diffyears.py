#! /usr/bin/env python
# more years till you are 100

import sys
#gets the command line arguments
script= sys.argv[0]
name = sys.argv[1]
age = int(sys.argv[2])
diff = 100 - age

print("Hello", name , " you will be 100 in ", diff, " years")
print("Script name is ", script)

      
