#!/usr/bin/env python3
import time

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

dst = 'AAA'

n = 0
while dst != 'ZZZ':
    dst = nodes[dst][inst[n%len(inst)]]
    n += 1


ans = n
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))


