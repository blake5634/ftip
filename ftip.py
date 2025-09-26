#!/usr/bin/python3

# import os
# import re
# import subprocess as sub
# import sys
import argparse as ap
import pyperclip


def process(n,t,v):
    print('Im working on ', n)
    print('    type:',t[n])
    print('    val: \n',v[n])
    if t[n] == 'link'  or t[n] == 'txt':
        pyperclip.copy(v[n])
        quit
    elif t[n] == 'txtfile':
        ifn = v[n]
        ifp = open(ifn,'r')
        res = ''
        for line in ifp:
            res += line
        pyperclip.copy(res)
        quit()



fn = '/home/blake/BH_Sync_New/Maintenance/ftip/ftipDB.txt'
fp = open(fn, 'r')

names = []
types = {}
vals = {}
for line in fp:
    n,t,v = line.split(';')
    n = n.strip()
    t = t.strip()
    v = v.strip().replace('"', '').replace('\\n', '\n').replace('\\t', '\t')
    names.append(n)
    types[n] = t
    vals[n] = v

i = 1
print('\n      Select:')
for n in names:
    print(f'{i:2}  {n:15} ')
    i += 1

sel = input ('> ')
if sel=='':
    quit()
else:
    nn = int(sel)-1
    process(names[nn],types,vals)
