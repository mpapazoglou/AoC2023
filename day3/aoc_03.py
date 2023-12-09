#!/bin/env python3
import re
import time
import numpy as np

not_symbols = '0123456789.'

print('------------------')
print('day 3, part 1')
start_time = time.time()

ans = 0
# mask will be a mask of where symbols are
mask = []

num_map = []
num = []
with open('input.txt','rt') as f:
    # generate a mask of where symbols are: 
    for line in f:
        l = line.rstrip()
        mask.append([s not in not_symbols for s in l])
        num.append(re.findall('\d+',l))
        num_map.append([(max(0,m.start()-1), min(len(l),m.end()+1)) for m in re.finditer('\d+',l)])

for n,m1 in enumerate(num_map):
    for m, m2 in enumerate(m1):
        ix = []
        if n>0:
            ix += [mask[n-1][i] for i in range(*m2)]
        ix += [mask[n][i] for i in range(*m2)]
        if n<(len(mask)-1):
            ix += [mask[n+1][i] for i in range(*m2)]
        if any(ix):
            ans += int(num[n][m])
                
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))

    
print('------------------')
print('day 3, part 2')
start_time = time.time()

ans = 0
# mask will be a mask of where * are
mask = []

num_map = []
num = []
with open('input.txt','rt') as f:
    # generate a mask of where symbols are: 
    for line in f:
        l = line.rstrip()
        mask.append([s=='*' for s in l])
        num.append(re.findall('\d+',l))
        num_map.append([(max(0,m.start()-1), min(len(l),m.end()+1)) for m in re.finditer('\d+',l)])

#  give each * a unique label above 0:
mask_label = (np.cumsum(mask)*np.array(mask).flatten()).reshape((len(mask),-1))

# X will contain a list of list with the number and the * label it's next to:
X = []

for n,m1 in enumerate(num_map):
    for m, m2 in enumerate(m1):
        ix = []
        l1 = []
        if n>0:
            ix += [mask[n-1][i] for i in range(*m2)]
            l1 += [mask_label[n-1][i] for i in range(*m2)]

        ix += [mask[n][i] for i in range(*m2)]
        l1 += [mask_label[n][i] for i in range(*m2)]

        if n<(len(mask)-1):
            ix += [mask[n+1][i] for i in range(*m2)]
            l1 += [mask_label[n+1][i] for i in range(*m2)]

        for i in np.where(ix)[0]:
            X.append([int(num[n][m]), l1[i]])

# find cases where more than one number is next to a *:
X = np.array(X)
for l in range(mask_label.max()):
    i1 = np.where(X[:,1]==l+1)[0]
    if len(i1)>1:
        ans += X[i1,0].prod()
    
                
etime = time.time() - start_time
print('answer is %d, elapsed time: %.3f msec'%(ans,1000*etime))

