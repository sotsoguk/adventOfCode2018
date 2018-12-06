import numpy as np
import itertools
import re
from operator import itemgetter

with open('input.txt') as f:
    lines = f.readlines()

lines = [list(map(int,re.findall(r'\d+',line))) for line in lines]

points = {}
for i, p in enumerate(lines,1):
    points[i] = (p[0],p[1])
    # grid[points[i]] = i
maxDim = max(max(points.items(), key=itemgetter(1))[1][1],max(points.items(), key=itemgetter(1))[1][0])
print(maxDim)
grid = np.zeros((maxDim+3,maxDim+3))
print(points)
for k,v in points.items():

    grid[v] = k
#    print(p.value())

numPoints = len(points)
def closestPoint(p,points):
    dists = np.zeros(numPoints)
    for k,v in points.items():
        dists[k-1] = abs(p[0]-v[0]) + abs(p[1]-v[1])
    minDist = min(dists)
    minPoint = np.argmin(dists)
    #print(dists)
    #print(str(minDist)+"@"+str(minPoint+1))
    #print(np.where(dists==minDist)[0])
    if (len(np.where(dists==minDist)[0])==1):
        return int(minPoint + 1)
    else:
        return int(-1)

for ix,iy in np.ndindex(grid.shape):
    grid[(ix,iy)] = closestPoint((ix,iy),points)

print(grid)
    
areas=[]
for k,v in points.items():
    subGrid = np.where(grid==k)

    if np.any(subGrid[0]==0)  or np.any(subGrid[1] == 0) or np.any(subGrid[0]==maxDim+2)  or np.any(subGrid[1] == maxDim+2):
        print(str(k)+" Infite")
    else:
        print(str(k)+":"+ str(len(np.where(grid == k)[0])))
        areas.append(len(np.where(grid == k)[0]))
    
print(max(areas))
grid = np.zeros((maxDim+3,maxDim+3))

for ix,iy in np.ndindex(grid.shape):
    for k,v in points.items():
        grid[(ix,iy)] += abs(ix-v[0]) + abs(iy-v[1])
                           
print(len(np.where(grid<10000)[0]))