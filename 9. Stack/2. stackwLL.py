# Implement a Stack using Linked List.
# Step 1: Create a node class with value and next.
# Step 2: Create a Stack class with top.
# Step 3: For push: Create a new node from user value. Point new Node's next to top and update top.
# Step 4: For Pop: return value of top and move top ahead.

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top is None:
            raise Exception("Stack Underflow")
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data
    
    def print(self):
        temp = self.top
        while(temp is not None):
            print(temp.data)
            temp = temp.next


stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.pop()
stk.pop()
stk.pop()
stk.print()
