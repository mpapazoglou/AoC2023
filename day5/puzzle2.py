#!/bin/env python3
import time
from collections import OrderedDict
import math
import multiprocessing as mp

print('------------------')
print('day 4, part 2')
start_time = time.time()
maps = []
with open('input.txt','rt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('seeds:'):
            s = [int(s) for s in line.split(':')[-1].split()]
            seed_list = [range(s[i],s[i]+s[i+1]) for i in range(0,len(s),2)]

        elif line.endswith('map:'):
            slist = line.split(':')[0].split(' ')[0].split('-')
            maps.append({'src': [], 'offset': []})

        elif len(line)>0:
            x = [int(s_) for s_ in line.split()]
            maps[-1]['src'].append(range(x[1],x[1]+x[2]))
            maps[-1]['offset'].append(x[0]-x[1])

def seed_location_fun(seed,maps,index,ret):
    print('seed_location_fun, start seed is %d'%(seed[0]))
    loc = math.inf
    for s in seed:
        src = s
        for m in maps:
            dst = src
            for i, s_ in enumerate(m['src']):
                if src in s_:
                    dst = src + m['offset'][i]
                    break
            src = dst
        loc = min(dst,loc)
    print('loc: %d'%(loc))
    ret[index] = loc

manager = mp.Manager()
ret = manager.dict()
jobs = [mp.Process(target=seed_location_fun,args=(s,maps,i,ret)) for i,s in enumerate(seed_list)]   
for j in jobs:
    j.start()

for j in jobs:
    j.join()

loc = min(ret.values())
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f minutes'%(loc,etime/60))








            
            

            
