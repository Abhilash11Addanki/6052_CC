#!/usr/bin/env python

import sys
import json
words = []
dictionary = {}
for line in sys.stdin:
	words = line.strip().split(" ",1)
	
	if (words[0] in dictionary):
		dictionary[words[0]].append(words[1])
	else:
		dictionary[words[0]] = []
		dictionary[words[0]].append(words[1])

jenc = json.JSONEncoder()

for item in dictionary:
	print(item), (dictionary[item])
