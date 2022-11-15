#!/usr/bin/python
import sys
from collections import defaultdict
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
count = {}
count = defaultdict(lambda:0, count)
def output(id):
    for i in range(7):
        if count[week[i]] == 0:
            continue
        else:
            print( id + ', '+ week[i] + ', ' + str(count[week[i]]) )

prev_id = None

for line in sys.stdin:
    #split the line with \t
    b_id, weekday, value = line.split('\t')

    #check if there is a same key as the previous one
    if b_id != prev_id:
        if prev_id is not None:
            output(prev_id)
        prev_id = b_id
        count = {}
        count = defaultdict(lambda:0, count)
    count[weekday] = count[weekday] + int(value)

output(prev_id)