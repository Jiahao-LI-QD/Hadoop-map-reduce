#!/usr/bin/python

#!/usr/bin/env python
import sys
import re
import csv

def output(l):
    next = re.sub( r',|\.$|\. |\: |\!|\，|\。|\！|\：|\？|\?|\"'," ", l[0])
    words = next.split()
    for word in words:
        print( word.lower() + "\t1")

p = csv.reader(sys.stdin)
fir = next(p)
if fir[0] != "text":
    output(fir)

for line in p:
    output(line)


