#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

dictionary = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(", ")

    words[0] = words[0].strip("[")
    words[0] = words[0].strip("\"")

    words[1] = words[1].strip("]")
    words[1] = words[1].strip("\"")
    
    if words[0] not in dictionary.keys():
        dictionary[words[0]] = words[1][0:-10]

# print genes
key_list = list(dictionary.keys())
val_list = list(dictionary.values())

updated_val = set(val_list)
for i in updated_val:
    print "\""+i+"\""


