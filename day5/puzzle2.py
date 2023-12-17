#!/usr/bin/env python3
import time
from collections import OrderedDict
import math
import multiprocessing as mp

print('------------------')
print('day 5, part 2')
start_time = time.time()
maps = []
with open('input.txt','rt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('seeds:'):
            s = [int(s) for s in line.split(':')[-1].split()]
            seed_ranges = [range(s[i],s[i]+s[i+1]) for i in range(0,len(s),2)]

        elif line.endswith('map:'):
            slist = line.split(':')[0].split(' ')[0].split('-')
            maps.append({'src': [], 'offset': []})

        elif len(line)>0:
            x = [int(s_) for s_ in line.split()]
            maps[-1]['src'].append(range(x[1],x[1]+x[2]))
            maps[-1]['offset'].append(x[0]-x[1])

def location2seed_fun(loc,maps):
    src = loc
    for m in maps[::-1]:
        dst = src
        for i, s_ in enumerate(m['src']):
            if src - m['offset'][i] in s_:
                src = dst - m['offset'][i]
                break
    return src

def check_seed(seed,seed_ranges):
    ret = False
    for s in seed_ranges:
        if seed in s:
            ret = True
            break
    return ret
        
# search over locations to find initial seed, and check if it's in any of the the
# seed ranges
ret = False
loc = -1
while not ret:
    loc += 1
    if math.remainder(loc,500000)==0:
        print('loc: %d'%(loc))
    s = location2seed_fun(loc,maps)
    ret = check_seed(s,seed_ranges)
    
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f minutes'%(loc,etime/60))








            
            

            
