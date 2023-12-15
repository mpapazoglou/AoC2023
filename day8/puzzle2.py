#!/usr/bin/env python3
import time
import math

print('------------------')
print('day 8, part 1')
start_time = time.time()

with open('input.txt','rt') as f:
    lines = f.readlines()

inst = [l_ for l_ in lines[0].rstrip()]

nodes = {}

for l in lines:
    if '=' in l:
        s1 = l.strip().split('=')
        s2 = s1[1].split(',')
        nodes[s1[0].strip()] = {'L': s2[0][2:], 'R': s2[1][1:-1]}

dst = [k for k in nodes.keys() if k.endswith('A')]
n = [0 for d in dst]

for i,d in enumerate(dst):
    while not(d[-1]=='Z'):
        s = d
        d = nodes[s][inst[n[i]%len(inst)]]
        n[i] += 1
        

ans = math.lcm(*n)
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))


