#!/usr/bin/python

#!/usr/bin/env python
import sys
import re
import csv

def output(l):
    if (len(l) < 4):
        exit
    b_id, weekday, hour, chechins = l
    print(b_id + '\t' + weekday + '\t' + chechins)

p = csv.reader(sys.stdin)
fir = next(p)
if fir[0] != "business_id":
    output(fir)

for line in p:
    output(line)



