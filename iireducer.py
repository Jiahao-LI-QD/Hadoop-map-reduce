#!/usr/bin/python
import sys
import re
from collections import defaultdict

ids = ''
prev_key = None

def output():
    allid = ids.split(', ')
    allid.sort()
    bids = allid[0]
    for id in allid[1:]:
        bids = bids + ', ' + id
    print( prev_key + '\t' + bids)

for line in sys.stdin:
    line = re.sub(r'\n', '', line)
    key, value = line.split('\t')

    #check if there is a same key as the previous one
    if key != prev_key:
        if prev_key is not None:
            output()
        prev_key = key
        ids = ''
    if ids == '':
        ids = value
    else:
        ids = ids + ", " + value
output()