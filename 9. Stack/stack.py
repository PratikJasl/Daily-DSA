# Implementing a stck using list.
# This implementation considers index-0 to be top of the stack.
# Operations: Length, push, pop, peek

class stack:
    def __init__(self):
        self.container = []
        self.top = 0
    
    # Function to return length of stack
    def length(self):
        return len(self.container)

    # Function to push an element to the top of stack.
    def push(self, value):
        self.container.insert(0, value)
    
    # Function to return the top element.
    def peek(self):
        if(len(self.container) == 0):
            return "Empty List"
        else:
            return (self.container[0])
    
    #Function to remove top element from stack.
    def pop(self):
        if(len(self.container) == 0):
            return "Empty List"
        else:
            return (self.container.pop(0))


stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.pop()
print(stk.peek())
