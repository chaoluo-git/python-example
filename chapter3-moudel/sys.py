__author__ = 'lch'
import sys as ss

print 'The command line arguments are:'
for i in ss.argv:
    print i

print '\n\nThe PYTHONPATH is', ss.path, '\n'
print dir()
