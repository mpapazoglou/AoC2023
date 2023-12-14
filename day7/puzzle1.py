#!/usr/bin/env python3
import time
import numpy as np

print('------------------')
print('day 7, part 1')
start_time = time.time()

with open('input.txt','rt') as f:
    lines = f.readlines()

t = np.zeros(len(lines),dtype=int)
bids = np.zeros(len(lines))

# table to convert card to ranking:
vdict = {v: n for n,v in enumerate(['2','3','4','5','6','7','8','9','T','J','Q','K','A'])}

hands = np.zeros((len(lines),5),dtype=int)
for n,l in enumerate(lines):
    h_str,bid_str = l.rstrip().split()
    bids[n] = int(bid_str)
    hands[n] = [vdict[h_] for h_ in h_str]

    u,count = np.unique(hands[n],return_counts=True)
    # assign a rank per hand:
    if len(count)==5: # high card
        t[n] = 1
    elif (len(count)==4): # one pair
        t[n] = 2
    elif (len(count)==3) and (max(count)==2): # two pair
        t[n] = 3
    elif (len(count)==3) and (max(count)==3): # three of a kind
        t[n] = 4
    elif (len(count)==2) and (max(count)==3): # full house
        t[n] = 5
    elif (len(count)==2) and (max(count)==4): # four of a kind
        t[n] = 6
    else: # five of a kind
        t[n] = 7

# for hands with the same rank, apply the tie-breaker
ix1 = np.argsort(t)
t = t[ix1]
bids = bids[ix1]
hands = hands[ix1]

for t_ in np.unique(t):
    i1 = np.where(t==t_)[0]
    if len(i1)>1:
        i2 = np.lexsort(hands[i1].T[::-1])
        hands[i1] = hands[i1[i2]]
        bids[i1] = bids[i1[i2]]


ans = sum((np.arange(len(bids))+1)*bids)
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))


    
    
    

