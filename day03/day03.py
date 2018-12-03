import numpy as np
import re

with open('input.txt') as f:
    lines = f.readlines()

inp = []
rect = np.zeros((1000,1000))
inpm = map(lambda s:map(int, re.findall(r'-?\d+',s)),lines) 
for (idd, x, y, dx,dy) in inpm:
    inp.append([idd,x,y,dx,dy])
# for line in lines:
#     tmp = line.split()
#     idd = int(tmp[0].strip('#'))
#     x,y = map(int,(tmp[2].strip(":").split(",")))
#     xr,yr = map(int,tmp[3].split("x"))
#     inp.append([idd,x,y,xr,yr])

def part1():
    for _,x,y,dx,dy in inp:
        rect[x:x+dx,y:y+dy] += 1
    return np.sum(rect>1)

def part2():
    for idd,x,y,dx,dy in inp:
        if np.all(rect[x:x+dx, y:y+dy]==1):
            return idd

print(part1())
print(part2())