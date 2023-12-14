#!/usr/bin/env python3
import re
import time
import math

totals = {'red': 12,
          'green': 13,
          'blue': 14}

print('------------------')
print('day 2, part 1')
start_time = time.time()

ans = 0
with open('input.txt','rt') as f:
    for line in f:
        g,r = line.rstrip().split(':')
        ok = True
        for s in r.split(';'):
            for t in s.split(','):
                u = t.split()
                if int(u[0])>totals[u[1]]:
                    ok = False
                    break
                
        if ok:
            ans += int(g.split()[1])
                

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))


print('------------------')
print('day 2, part 2')
start_time = time.time()
ans = 0
colors = ('red','green','blue')
with open('input.txt','rt') as f:
    for line in f:
        g,r = line.rstrip().split(':')
        count = {k: 0 for k in colors}
        for s in r.split(';'):
            for t in s.split(','):
                u = t.split()
                count[u[1]] = max(count[u[1]],int(u[0]))
        ans += math.prod(count.values())

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))
    
