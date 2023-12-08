#!/bin/env python3
import re
import time

print('------------------')
print('day 1, part 1')
start_time = time.time()
n = []
with open('input_01.txt','rt') as f:
    for line in f:
        s = re.findall('\d',line)
        n.append(int(s[0]+s[-1]))
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(sum(n),1000*etime))


print('------------------')
print('day 1, part 2')
start_time = time.time()
n = []
snum_set = ('one','two','three','four','five','six','seven','eight','nine')
with open('input_01.txt','rt') as f:
    for line in f:
        for m,s in enumerate(snum_set):
            line = line.replace(s,'%s%d%s'%(s,m+1,s))
        s = re.findall('\d',line)
        n.append(int(s[0]+s[-1]))
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msecs'%(sum(n),1000*etime))

    
