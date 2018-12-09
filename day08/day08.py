with open('input.txt') as f:
    input = f.readline()

#input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
data = [int(x) for x in input.split()]

def recursiveParseTree(data):
    children, meta = data[:2]
    data = data[2:]
    values = []
    sumMeta = 0
    for _ in range(children):
        subSum, subValue, data = recursiveParseTree(data)
        sumMeta += subSum
        values.append(subValue)
    
    sumMeta += sum(data[:meta])
    if children == 0:
        return (sumMeta, sumMeta, data[meta:])
    else:
        return (sumMeta, sum(values[k-1] for k in data[:meta] if k>0 and k<= len(values)) , data[meta:])

print(recursiveParseTree(data))