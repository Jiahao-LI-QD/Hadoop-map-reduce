#!/usr/bin/python

#!/usr/bin/env python

import sys
import re
import csv

def output(l):
    #remove some tail symbols
    next = re.sub( r'\.$|\!$|\。$|\！$|\？$|\?$|\"'," ", l[0])
    
    #seperate it into sentence level
    sens = re.split('\.|\,|\。|\，|\n|\!|\！|\!|\！|\： |\: ', next)
    for s in sens:
        words = s.split()
        if len(words) <= 2:
            return
        for i in range(len(words) - 2) :
            print( words[i].lower()  + " " + words[i + 1].lower() + " " + words[i + 2].lower()  + "\t1")

p = csv.reader(sys.stdin)
fir = next(p)
if fir[0] != "text":
    output(fir)

for line in p:
    output(line)
