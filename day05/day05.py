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
    

input = "dabAcCaCBAcCcaDA"
input = "dabAaCBAcCcaDA"
input=[]
with open('input.txt') as f:
    input = f.readlines()


#input = open("input.txt").read().splitlines()[0]
input = input[0].strip()
a="hallo\n"
print(a)
print(a.strip())
#print(len(input))
stack = Stack()

for c in input:
    if stack.isEmpty():
        stack.push(c)
    
    elif (c.islower() and (c.upper() == stack.peek())) or (c.isupper() and (c.lower() == stack.peek())):
          stack.pop()
    else:
          stack.push(c)

print(''.join(stack.items))
print('Part1')
#polyToDelete = ['aA', 'bB','cC','dD','eE','fF','gG','hH','iI','jJ','kK','lL','mM','nN','oO','pP','qQ','rR','sS','tT','uU','vV','wW','xX','yY','zZ']
polyList = []
for i in range(ord('a'),ord('z')+1):
    polyList.append(''.join([chr(i),chr(i).upper()]))
stack = Stack()
#for c in input:
#    if c in polyToDelete:
#        print(c)
#part2
for deletePoly in polyList:
    stack = Stack()
    #print(deletePoly)
    for c in input:
       # print(stack.items)
        if c in deletePoly:
            pass
        elif stack.isEmpty():
            stack.push(c)

        
        elif (c.islower() and (c.upper() == stack.peek())) or (c.isupper() and (c.lower() == stack.peek())):
              stack.pop()
        else:
              stack.push(c)
    print(deletePoly + " " + str(stack.size()))

    
    


print(len(stack.items))
#while not stack.isEmpty():
#    print(stack.pop())