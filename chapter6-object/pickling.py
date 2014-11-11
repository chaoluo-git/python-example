#!/usr/bin/python
# Filename : pickling.py
import cPickle as p
import time as t

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
start = t.time()
print t.time()
p.dump(shoplist, f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist