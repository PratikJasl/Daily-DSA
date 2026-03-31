# Queue Implementation using List
# In python, since lists are dynamic we do not need to maintain front and rear pointers.
# Step1: Create a queue class and initialize a list.
# Step2: Create an isEmpty function, and enqueue function.
# Step3: Create dequeue funciton, check empty before deleting.

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self): #O(n) complexity since pop(0) shifts elements front
        if(self.isEmpty()):
            return 'Queue is Empty'
        else:
            return self.items.pop(0)

    def print(self):
        if(self.isEmpty()):
            return 'Queue is Empty'
        else:
            for item in self.items:
                print(item)

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.dequeue()
q1.dequeue()
q1.print()