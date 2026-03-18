# Implementing a stck using array.
# Step 1: Create a pointer Top = -1, and an empty list  in constructor.
# Step 2: For Push: increment the top and append a value to list.
# Step 3: For Pop: check if stack is empty, if not decrement top and pop a value.
# Step 4: For Peek: Check if stack is empty, if not return the top element.
# Step 5: For Length: Return length of stack.
# Step 6: For Print: Check is stack is empty, and run a for loop from top to -1 and print elements.
# Operations: Length, push, pop, peek, print

class stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, value): #O(1)
        self.top += 1
        self.stack.append(value)
    
    def pop(self): # O(1)
        if(self.top == -1):
            raise Exception("Index out of range")
        self.top -= 1
        return self.stack.pop()

    def peek(self): 
        if(self.top == -1):
            raise Exception("Index out of range")
        else:
            return self.stack[self.top]
    
    def length(self): 
        return len(self.stack)
    
    def print_stack(self):
        if(self.top == -1):
            print("Stack is empty")
        
        for i in range(self.top, -1, -1):
            if(i == self.top):
                print(self.stack[i], "<-- Top")
            else:
                print(self.stack[i])
        

stk = stack()
stk.push(10)
stk.push(20)
stk.push(50)
print(stk.peek())
print(stk.length())
stk.print_stack()

