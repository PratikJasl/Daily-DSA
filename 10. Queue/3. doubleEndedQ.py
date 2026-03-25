# A double ended queue allows insertion and deletion from both ends. Its created using doubly linked list.
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None

    # 1. INSERT FRONT (appendleft)
    def insert_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front # Point new node to current front
            self.front.prev = new_node # Point current front back to new node
            self.front = new_node      # Officially move the Front pointer

    # 2. INSERT REAR (append)
    def insert_rear(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear  # Point new node back to current rear
            self.rear.next = new_node  # Point current rear to new node
            self.rear = new_node       # Officially move the Rear pointer

    # 3. DELETE FRONT (popleft)
    def delete_front(self):
        if self.is_empty():
            return "Deque is empty"
            
        popped_val = self.front.val
        
        # If there is only one element
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next # Move front pointer to the right
            self.front.prev = None       # Sever the tie to the old node
            
        return popped_val

    # 4. DELETE REAR (pop)
    def delete_rear(self):
        if self.is_empty():
            return "Deque is empty"
            
        popped_val = self.rear.val
        
        # If there is only one element
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev   # Move rear pointer to the left
            self.rear.next = None        # Sever the tie to the old node
            
        return popped_val
