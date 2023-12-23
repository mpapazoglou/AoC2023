#!/usr/bin/env python3
import time
import numpy as np
from scipy.special import factorial

with open('input.txt','rt') as f:
    lines = f.readlines()

ans_1 = 0
ans_2 = 0

for n,line in enumerate(lines):
    d = np.array([int(l_) for l_ in line.strip().split()])

    y = []

    a = 0
    b = 0

    while any(d!=0):

        y.append(d)
        d = np.diff(d)

    for y_ in y[::-1]:
        a += y_[-1]
        b = y_[0]-b

    ans_1 += a
    ans_2 += b

print('day 9, puzzle 1, answer is %d'%(ans_1))
print('day 9, puzzle 2, answer is %d'%(ans_2))


