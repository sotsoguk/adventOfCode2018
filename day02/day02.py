from collections import Counter
import itertools as it
with open('input.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]
numOfDoubles = numOfTriples= 0
# numOfTriples = 0

for word in lines:
    
    a = Counter(word)
    # for char, freq in a.items():
    #     if freq == 2:
    #         dbl = True
    #     elif freq == 3:
    #         trpl = True
    
    if 2 in a.values():
        numOfDoubles = numOfDoubles + 1
    if 3 in a.values():
        numOfTriples = numOfTriples +1


print(numOfDoubles*numOfTriples)

def compareWords(x,y):
    diffs = 0
    for i in range(0,min(len(x),len(y))):
        if x[i] != y[i]:
            diffs = diffs + 1
            # print(x[i],y[i])
    return diffs

def commonChars(x,y):
    commonWord=""
    for i in range(0,min(len(x),len(y))):
        if x[i] == y[i]:
            commonWord = commonWord + x[i]
            # print(x[i],y[i])
    return commonWord

for x,y in it.combinations(lines,2):
    numDiff = compareWords(x,y)
    if numDiff == 1:
        print(x,y)
        print(commonChars(x,y))