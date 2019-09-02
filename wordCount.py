#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
import string

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

#first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print ("wordCount.py doesn't exist! Exiting")
    exit()

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()
    
#master dictionary and list
masterSet = set()   # create new empty set
masterList = []     # create new empty list

# attempt to open input file
with open(textFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        word = re.split('[ \t]', line)

        # add word to master set and list
        for key in word:
            s = key.lower()
            s = s.translate(None, string.punctuation)
            masterSet.add(s)
            masterList.append(s)

masterSet.remove('')
masterSet = dict.fromkeys(masterSet, 0)

for key in masterSet:
    for word in masterList:
        if key == word:
            masterSet[key] += 1

f = open(str(outputFname), "w+")
for key in sorted(masterSet):
    f.write("%s %d\n" %(key, masterSet.get(key)))

f.close()
