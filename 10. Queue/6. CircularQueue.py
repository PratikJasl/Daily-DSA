# To create circular queue we set the array size to be fixed.
# Next we use the front and rear pointers for deletion and insertion operation.
# And for incrementing the front and rear pointers we use % operator.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1
    
    def isEmpty(self):
        return self.front == -1 and self.rear == -1
    
    def isFull(self):
        return ((self.rear + 1) % self.size == self.front)
    
    def insert(self, val):
        if(self.isFull()):
            print('Queue is Full')
            return
        elif(self.isEmpty()):
            self.front = self.rear = 0
            self.items[self.rear] = val
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = val
    
    def delete(self):
        if self.isEmpty():
            print('Queue is Empty')
            return 
        
        popped_val = self.items[self.front]
        self.items[self.front] = None
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
            
        return popped_val


cq = CircularQueue(3)
cq.insert(10)
cq.insert(20)
cq.insert(30)
print(cq.delete())
