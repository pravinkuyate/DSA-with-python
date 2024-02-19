from collections import deque

class stack:

    def __init__(self):
        self.container=deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    

stack1=stack()
stack1.push(10)


print(stack1.size())
