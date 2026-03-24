# LeetCode: 155. Min Stack
# Design a stack which can return the minimum element in O(1), 
# and also perform all standard operations.

class minStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if(not self.min_stack or val <= self.min_stack[-1]):
            self.min_stack.append(val)
    
    def pop(self):
        if(self.stack[-1] == self.min_stack[-1]):
            self.stack.pop()
            self.min_stack.pop()
        else:
            self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

