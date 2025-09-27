#!/usr/bin/python3

import sys
import pyperclip
import subprocess


def process(n,t,v):
    print('Im working on ', n)
    print('    type:',t[n])
    print('    val: \n',v[n])
    if t[n] == 'link'  or t[n] == 'txt':
        # Optional: Show notification that it worked
        subprocess.run(['notify-send', 'Copied to clipboard', v[n] ])
        pyperclip.copy(v[n])
        quit
    elif t[n] == 'txtfile':
        ifn = v[n]
        ifp = open(ifn,'r')
        res = ''
        for line in ifp:
            res += line
        pyperclip.copy(res)
        # Optional: Show notification that it worked
        subprocess.run(['notify-send', 'Copied to clipboard', res] , stderr=subprocess.DEVNULL )
        quit()



fn = '/home/blake/BH_Sync_New/Maintenance/ftip/ftipDB.txt'
fp = open(fn, 'r')

#
#  get setup from the database
#
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

#
#  look at command line
#
args = sys.argv
if len(args) == 2:
    if args[1] not in names:
        print(f"I don't understand {args[1]} - quitting")
        quit()
    else:
        #
        #  go ahead and load paste buff
        process(args[1], types, vals)
    quit()
elif len(args) == 1:
    #
    #  print menu for user
    #
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
else:
    print("I couldn't understand the command line: ", ' '.join(args))
    quit()
