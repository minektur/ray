#!/usr/bin/env python
import sys
with open(sys.argv[1], "r") as f:
    count = 0
    for line in f:
        if argv[2] in line:
            count +=1
            if count == 4:
                print line
                sys.exit()

#alternatively if file is small
#lines = [line for line in f.readline() if argv[2] in line]
#print lines[3]

