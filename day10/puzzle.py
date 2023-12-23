#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import shapely 
from tqdm import tqdm

input_file = 'input.txt'

doplot = False

# key gives possble characters if you move N,S,E, or W:
key = {'N': ('|','7','F'),
       'S': ('|','L','J'),
       'E': ('-','J','7'),
       'W': ('-','L','F')}

# step gives the step coordinates for each move
step = {'N': (-1,0),
        'S': (1,0),
        'E': (0,1),
        'W': (0,-1)}

# next step gives possible next steps given the character:
next_step = {'S': ('N','S','E','W'),
             '|': ('N','S'),
             '-': ('E','W'),
             '7': ('W','S'),
             'F': ('E','S'),
             'L': ('E','N'),
             'J': ('W','N')}



grid = []

with open(input_file,'rt') as f:
    for n,l in enumerate(f):    
        grid.append([l_ for l_ in l.rstrip()])

        if 'S' in grid[-1]: 
            start_pos = (n,grid[-1].index('S'))

Nrow = len(grid)
Ncol = len(grid[1])

path = [start_pos]

if doplot:
    plt.ion()
    plt.clf()
    ax = plt.subplot(1,1,1)
    ax.set_xlim((-.5,Ncol-.5)) 
    ax.set_ylim((Nrow-.5,-0.5)) 
    ax.text(start_pos[1],start_pos[0],'S',
                 horizontalalignment='center',
                 verticalalignment='center')

goflag = True
while goflag:
    p0 = (path[-1][0],path[-1][1])
    c0 = grid[p0[0]][p0[1]]

    goflag = False

    for k in next_step[c0]:
        s = step[k]
        p1 = (p0[0]+s[0],p0[1]+s[1])

        if (p1[0]>=0) and (p1[0]<Nrow) and (p1[1]>=0) and (p1[1]<Ncol) and \
           (p1 not in path) and (grid[p1[0]][p1[1]] in key[k]):

            path.append(p1)
            
            goflag = True
            if doplot:
                ax.text(p1[1],p1[0],grid[p1[0]][p1[1]],
                        horizontalalignment='center',
                        verticalalignment='center')

print('day 10, puzzle 1, answer is %d'%(len(path)/2))

# getting the area:
poly = shapely.geometry.polygon.Polygon(path)

# get all points that are not along the path:
p1 = [[n,m] for n in range(Nrow) for m in range(Ncol) if [n,m] not in path]

# check if inside:
T = [poly.contains(shapely.geometry.Point(p[0],p[1])) for p in tqdm(p1,ncols=0)]

print('day 10, puzzle 2, answer is %d'%(sum(T)))





        
    


