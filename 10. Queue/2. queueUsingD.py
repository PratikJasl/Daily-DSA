# The problem with standard python implementation of a queue is the deletion operation
# takes O(n) time. Because the pop() method removes and shifts elements.

#Solution:
# To make deletion and insertion in O(1), we use the double ended queue provided by python.

from collections import deque

class Queue:
    def __init__(self):
        # Initialize a deque instead of a standard list
        self.items = deque() 
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, value):
        self.items.append(value) # Still O(1)
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is Empty'
        else:
            # The Magic Method! Removes from the front in O(1) time
            return self.items.popleft() 

    def print(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            for item in self.items:
                print(item)