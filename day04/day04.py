import re
import numpy as np
import operator
with open('input.txt') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines.sort()
guards = {}

activeGuard = 0
startSet = False
startTime = 0
endTime = 0
for l in lines:
    nums = list(map(int,re.findall(r'\d+',l)))
    if len(nums) == 6:
        gnum = nums[5]
        activeGuard = gnum
        if gnum not in guards.keys():
            guards[gnum] = np.zeros(60)
    elif not startSet:
        startTime = nums[4]
        startSet = True
    else:
        startSet = False
        endTime = nums[4]
        guards[activeGuard][startTime:endTime]+=1
        

guardsTime={}
guardsMax = {}
guardsMaxMin = {}
for k,v in guards.items():
    guardsTime[k] = np.sum(v)
for k,v in guards.items():
    guardsMax[k] = max(guards[k])
    guardsMaxMin[k] = np.argmax(guards[k])

maxGuard =  max(guardsMax.items(), key=operator.itemgetter(1))[0]

# Part1
sleepyGuard = max(guardsTime.items(), key=operator.itemgetter(1))[0]
minute=np.argmax(guards[sleepyGuard])
print("Part1:\t" + str(sleepyGuard * minute))

# Part2
print("Part2:\t"+ str(maxGuard*guardsMaxMin[maxGuard]))