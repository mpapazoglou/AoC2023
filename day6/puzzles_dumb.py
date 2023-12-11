#!/bin/env python3
import time
from collections import OrderedDict
import math
import numpy as np


print('------------------')
print('day 6, part 1')
start_time = time.time()

with open('input.txt','rt') as f:
    lines = f.readlines()

times = [int(s) for s in lines[0].rstrip().split()[1:]]
dists = [int(s) for s in lines[1].rstrip().split()[1:]]

# loop over races
ans = 1
for n in range(len(times)):
    t = np.arange(times[n]+1)
    d = t*(times[n]-t)
    ix = np.where(d>dists[n])[0]
    ans = len(ix)*ans
    print(len(ix))

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))

print('------------------')
print('day 6, part 2')
start_time = time.time()

T = int(''.join([s for s in lines[0].rstrip().split()[1:]]))
D = int(''.join([s for s in lines[1].rstrip().split()[1:]]))

go = False
ans = 0
for t in range(T):
    d = t*(T-t)
    if d>D:
        ans+=1
        go = True
    elif go:
        break

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f sec'%(ans,etime))
