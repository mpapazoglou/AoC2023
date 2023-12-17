#!/usr/bin/env python3
import time
import numpy as np

print('------------------')
print('day 7, part 2')
start_time = time.time()


def score_hand(hand):
    u,count = np.unique(hand,return_counts=True)
    # assign a rank per hand:
    if len(count)==5: # high card
        t = 1
    elif (len(count)==4): # one pair
        t = 2
    elif (len(count)==3) and (max(count)==2): # two pair
        t = 3
    elif (len(count)==3) and (max(count)==3): # three of a kind
        t = 4
    elif (len(count)==2) and (max(count)==3): # full house
        t = 5
    elif (len(count)==2) and (max(count)==4): # four of a kind
        t = 6
    else: # five of a kind
        t = 7

    return t

def find_best_joker_hand(hand):
    ix = np.where(hand==0)[0]
    h1 = hand.copy()
    if len(ix)>0:
        t = np.zeros(13)
        for k in range(13):
            h1[ix] = k
            t[k] = score_hand(h1)
        kmax = np.argmax(t)
        h1[ix] = kmax
    return h1

with open('input.txt','rt') as f:
    lines = f.readlines()

t = np.zeros(len(lines),dtype=int)
bids = np.zeros(len(lines))

# table to convert card to ranking (jacks are the weakest now)
vdict = {v: n for n,v in enumerate(['J', '2','3','4','5','6','7','8','9','T','Q','K','A'])}

hands = np.zeros((len(lines),5),dtype=int)
for n,l in enumerate(lines):
    h_str,bid_str = l.rstrip().split()
    bids[n] = int(bid_str)
    hands[n] = [vdict[h_] for h_ in h_str]

    h1 = find_best_joker_hand(hands[n])
    t[n] = score_hand(h1) 

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


    
    
    

