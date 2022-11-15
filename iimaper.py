#!/usr/bin/python

#!/usr/bin/env python
import sys
import re
import csv

dict = {}
from collections import defaultdict
dict = defaultdict(lambda:"", dict)

def record(l):
    if (len(l) < 13):
        exit
    b_id = l[0]
    cats = l[12].split(';')
    for cat in cats:
        if dict[cat] == "":
            dict[cat] = b_id
        else:
            dict[cat] = dict[cat] + ", " + b_id

p = csv.reader(sys.stdin)
fir = next(p)
if fir[0] != "business_id":
    record(fir)

for line in p:
    record(line)
    
for k, v in dict.items():
    print(k + '\t' + v)

