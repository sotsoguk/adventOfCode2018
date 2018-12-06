class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items ==[]
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
import operator

input=[]
#input = open("input.txt").read().splitlines()[0]
with open('input.txt') as f:
    input = f.readlines()

input = input[0].strip()
stack = Stack()
for c in input:
    if stack.isEmpty():
        stack.push(c)
    elif str.swapcase(c) == stack.peek():
          stack.pop()
    else:
          stack.push(c)

# speed up by using the collapsed polymer output of part1 as input for part2
input = stack.items
print('Part1:\t')
print(stack.size())

polyList = []
values = {}
for i in range(ord('a'),ord('z')+1):
    polyList.append(''.join([chr(i),chr(i).upper()]))
stack = Stack()
for deletePoly in polyList:
    stack = Stack()
    for c in input:
       # print(stack.items)
        if c in deletePoly:
            pass
        elif stack.isEmpty():
            stack.push(c)
        elif str.swapcase(c) == stack.peek():
              stack.pop()
        else:
              stack.push(c)
    #print(deletePoly + " " + str(stack.size()))
    values[deletePoly] = stack.size()

minLength = min(values.items(),key=operator.itemgetter(1))[1]
print("Part2:\t")
print(minLength)