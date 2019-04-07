#!/usr/bin/env python
import sys
 
dictionary = {}
for line in sys.stdin:
	value = line.strip().split()
	if (value[0] in dictionary): 
		dictionary[value[0]].append(value[1])
	else:
		dictionary[value[0]] = [value[1]]

for keys in dictionary:
	print keys, len(dictionary[keys])

