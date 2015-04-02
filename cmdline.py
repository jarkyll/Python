#!/usr/bin/env python

from urllib.request import urlopen
#fetches urls
import base64
# binary to text
import json
#javascript
import os
import sys
import re



os.system("Clear")
print("-" * 80)
print("Command Line Searching Tool")
print("-" * 80)


def banner(input):
    print("*" * 70)
    print(input)
    print("*" * 70)

def sorting():
    banner("Sorting By Votes")
    url ="http://www.commandlinefu.com/commands/browse/sort-by-votes/json"
    request = urlopen(url)
    print(url)
    print(request)
sorting()
