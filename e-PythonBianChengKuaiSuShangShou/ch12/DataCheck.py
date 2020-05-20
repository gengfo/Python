import collections
import os

import openpyxl
import ConfigParser
import StringIO


#key-file_name,value 

myprops = {}
with open('reportLLP.properties', 'r') as f:
    for line in f:
        line = line.rstrip() #removes trailing whitespace and '\n' chars
        if "=" not in line: continue #skips blanks and comments w/o =
        if line.startswith("#"): continue #skips comments which contain =

        k, v = line.split("=", 1)
        myprops[k] = v

for x in myprops.keys():
    print x +" => " + myprops[x]


