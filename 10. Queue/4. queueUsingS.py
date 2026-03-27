# Leetcode: 232. Implement Queue using Stacks.

# Approach:
# We will be using two lists, one to track insertion and other to track Pop and peek.
# The idea here is we can only use the operations on a stack that means remove from top.(FILO)
# But a Queue requires remove from First as well. (FIFO)
# To create a queue using stack we must keep push the first value to top.
# [10] -> [20, 10] -> [30,20,10] Now if we remove form top we will remove first element.
# To achieve this we store the elements in reverse order in our stack_out.
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.move_elements()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.move_elements()
        return self.stack_out[-1]
        
    def empty(self) -> bool:
        return len(self.stack_in) == 0 and len(self.stack_out == 0)
    
    def move_elements(self):
        if not self.stack_out:
                while(self.stack_in):
                     self.stack_out.append(self.stack_in.pop())
        
