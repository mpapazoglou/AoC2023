#!/bin/env python3
import time

print('------------------')
print('day 4, part 1')
start_time = time.time()

ans = 0

with open('input.txt','rt') as f:
    for line in f:
        label, data = line.rstrip().split(':')
        winners, mine = data.split('|')

        common = set(winners.split()).intersection(mine.split())
        num_matches = len(common)

        if num_matches>0:
            ans += 2**(num_matches-1)

etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))


print('------------------')
print('day 4, part 2')
start_time = time.time()

# first get a count of the number of winners on each card:
card_data = []
with open('input.txt','rt') as f:
    for line in f:
        label, data = line.rstrip().split(':')
        winners, mine = data.split('|')

        common = set(winners.split()).intersection(mine.split())
        card_data.append({'Nmatch': len(common),
                          'Ncard': 1})

# now figure out how many copies of each card there will be:
total = len(card_data)
for n,c in enumerate(card_data):
    N1 = min(n+c['Nmatch']+1,total)
    for i in range(n+1,N1):
        card_data[i]['Ncard'] += c['Ncard']*1

ans = sum([c['Ncard'] for c in card_data])
    
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))
