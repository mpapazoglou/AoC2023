import numpy as np
import matplotlib.pyplot as plt

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
next_step = {'|': ('N','S'),
             '-': ('E','W'),
             '7': ('W','S'),
             'F': ('E','S'),
             'L': ('E','N'),
             'J': ('W','N')}



class GridPath():

    def __init__(self,input_file,doplot=False):

        self.grid = []
        with open(input_file,'rt') as f:
            for n,l in enumerate(f):    
                self.grid.append([l_ for l_ in l.rstrip()])

                if 'S' in self.grid[-1]: 
                    self.start_pos = (n,self.grid[-1].index('S'))

        self.Nrow = len(self.grid)
        self.Ncol = len(self.grid[1])
        self.doplot = doplot

        # init forward and reverse paths
        self.path = {0: [self.start_pos], 1: [self.start_pos]}
        self.val = {0: [0], 1: [0]}
        n = 0

        if self.doplot:
            self.ax = plt.subplot(1,1,1)
            self.ax.set_xlim((0,self.Ncol)) 
            self.ax.set_ylim((self.Nrow,0)) 
            self.ax.text(self.start_pos[1],self.start_pos[0],'S',
                         horizontalalignment='center',
                         verticalalignment='center')
            

        for k,s in step.items():
            p1 = (self.start_pos[0]+s[0],self.start_pos[1]+s[1])
            if (p1[0]>=0) and (p1[0]<self.Nrow) and (p1[1]>=0) and (p1[1]<self.Ncol):
                if (self.grid[p1[0]][p1[1]] in key[k]):
                    self.path[n].append(p1)
                    self.val[n].append(1)
                    n += 1
                    if self.doplot:
                        self.ax.text(p1[1],p1[0],self.grid[p1[0]][p1[1]],
                                     horizontalalignment='center',
                                     verticalalignment='center')

        self.n = 1


    def step(self):
        for n in (0,1):
            p0 = (self.path[n][-1][0],self.path[n][-1][1])
            c0 = self.grid[p0[0]][p0[1]]
            for k in next_step[c0]:
                s = step[k]
                p1 = (p0[0]+s[0],p0[1]+s[1])
                if (p1[0]>=0) and (p1[0]<self.Nrow) and (p1[1]>=0) and (p1[1]<self.Ncol):
                    if (p1 not in self.path[n]) and (self.grid[p1[0]][p1[1]] in key[k]):
                        self.path[n].append(p1)
                        self.val[n].append(len(self.val[n])) 
                        if self.doplot:
                            self.ax.text(p1[1],p1[0],self.grid[p1[0]][p1[1]],
                                         horizontalalignment='center',
                                         verticalalignment='center')
        self.n += 1
        return self.path[0][-1]==self.path[1][-1]

g = GridPath('input_test2.txt')

r = False
while not r:
    r = g.step()

print('day 10, puzzle 1, answer is %d'%(g.n))

# find tiles inside loop:
T = np.zeros((g.Nrow,g.Ncol))

for p in g.path.values():
    for p_ in p:
        T[p_[0],p_[1]] = 1

Ninside = 0
for t in T:
    ix = np.where(t)[0]
    if len(ix)>0:
        n1 = ix[1::2]-ix[::2] 
        Ninside += n1.sum()

print('day 10, puzzle 2, answer is %d'%(Ninside))
        
    


