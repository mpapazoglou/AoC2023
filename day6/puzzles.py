#!/usr/bin/env python3
import time
from collections import OrderedDict
import math
import numpy as np

def time_dist_fun(T,D):
    # quadratic formula, A = 1, B = -T, C = D
    t1 = (T - np.sqrt(T**2 - 4*D))/2
    t2 = (T + np.sqrt(T**2 - 4*D))/2

    return (np.ceil(t2)-np.floor(t1)-1).prod()

print('------------------')
print('day 6, part 1')
start_time = time.time()

with open('input.txt','rt') as f:
    lines = f.readlines()

T = np.array([int(s) for s in lines[0].rstrip().split()[1:]])
D = np.array([int(s) for s in lines[1].rstrip().split()[1:]])

ans = time_dist_fun(T,D)

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))

print('------------------')
print('day 6, part 2')
start_time = time.time()

T = int(''.join([s for s in lines[0].rstrip().split()[1:]]))
D = int(''.join([s for s in lines[1].rstrip().split()[1:]]))

ans = time_dist_fun(T,D)
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))
