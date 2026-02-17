# Doubly Linked List
class Node:
    def __init__(self, data, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class doubly_linked_list():
    def __init__(self, head = None):
        self.head = head

    def insert_at_end(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node
    
    def insert_at_begining(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_specific(self, data, position):
        new_node = Node(data)
        temp = self.head
        while(temp.next != None):
            if(temp.data == position):
                break
            else:
                temp = temp.next
        
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        
    def deletion(self, data):
        if(self.head == None):
            print("empty linked list")
            return 
        temp = self.head
        if(temp.data == data):
            self.head = temp.next
            self.head.prev = None
            return
        while(temp.next != None):
            if(temp.data == data):
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            else:
                temp = temp.next
        
        if(temp.data == data):
            temp.prev.next = None

    def print_ll(self):
        temp = self.head
        while(temp.next != None):
            print(temp.data, end="<-->")
            temp = temp.next
        print(temp.data)
            
    
obj = doubly_linked_list()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_begining(1)
obj.insert_at_specific(15, 20)
obj.insert_at_begining(0)
obj.insert_at_specific(5, 10)
obj.insert_at_specific(25, 30)
obj.insert_at_specific(0.1, 0)
obj.deletion(0.1)
obj.deletion(5)
obj.print_ll()

