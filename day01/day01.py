with open('input.txt') as f:
    lines = f.readlines()

lines = [int(x.strip()) for x in lines]
oneRound = sum(lines)
print("First Star:"+str(oneRound))

seen = set()
twice = False
partSums = [sum(lines[0:i]) for i,_ in enumerate(lines,1)]

while not twice:
    for x in partSums:
        if x not in seen:
            seen.add(x)
        else:
            print("Second Star:" +str(x))
            twice = True
            break
    
    partSums = list(map(lambda x:x+oneRound, partSums))
