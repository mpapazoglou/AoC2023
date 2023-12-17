#!/usr/bin/env python3
import time
from collections import OrderedDict
import math

print('------------------')
print('day 5, part 1')
start_time = time.time()
maps = []
with open('input.txt','rt') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('seeds:'):
            seed_list = [int(s) for s in line.split(':')[-1].split()]

        elif line.endswith('map:'):
            slist = line.split(':')[0].split(' ')[0].split('-')
            maps.append({'src': [], 'offset': []})

        elif len(line)>0:
            x = [int(s_) for s_ in line.split()]
            maps[-1]['src'].append(range(x[1],x[1]+x[2]))
            maps[-1]['offset'].append(x[0]-x[1])

loc = math.inf
for s in seed_list:
    src = s
    for m in maps:
        dst = src
        for i, s_ in enumerate(m['src']):
            if src in s_:
                dst = src + m['offset'][i]
                break
        src = dst
    loc = min(dst,loc)

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(loc,1000*etime))





            
            

            
