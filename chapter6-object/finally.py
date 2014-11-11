#! /usr/bin/python
# Filename : finally.py

import time
import sys

print sys.argv[0]

try:
    f = file('poem.txt')
    while True: # ourd usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed the file'
